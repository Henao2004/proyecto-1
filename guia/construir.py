"""Genera la guía de uso diario para usar SIN internet en el computador de la asistente.

Entrada:
  guia/guia-artifact.html   Fuente de la página publicada en claude.ai (sin doctype ni <head>).
  guia/fuentes-google.css   Hoja de Google Fonts con las URL de las fuentes.

Salida:
  guia/guia-uso-diario.html  Archivo único que se abre con doble clic: fuentes incrustadas y
                             ninguna conexión externa.
  guia/guia-uso-diario.pdf   Versión PDF tamaño carta, de respaldo.

Uso:  python3 guia/construir.py
Requiere acceso a fonts.gstatic.com (solo para descargar las fuentes) y Node con Playwright
(solo para el PDF).
"""
import base64
import pathlib
import re
import sys
import urllib.request

AQUI = pathlib.Path(__file__).resolve().parent
FUENTE = AQUI / "guia-artifact.html"
CSS_FUENTES = AQUI / "fuentes-google.css"
SALIDA_HTML = AQUI / "guia-uso-diario.html"
SALIDA_PDF = AQUI / "guia-uso-diario.pdf"
SUBCONJUNTOS = {"latin"}  # incluye todas las letras del español (á, é, ñ, ü, ¿, ¡)

EXTRA_CSS = """
/* --- Ajustes de la versión sin internet --- */
body { margin: 0; -webkit-text-size-adjust: 100%; }
.solo-pdf { display: none; }
@media print {
  @page { size: letter; margin: 14mm 12mm; }
  :root { --bg: #FFFFFF; }
  html { font-size: 12.5px; }
  body { font-size: 1rem; }
  .page { max-width: none; gap: 22px; padding: 0; }
  .picker { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .cols { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 18px; }
  .m-row { grid-template-columns: 150px minmax(0, 1fr) 190px; gap: 12px; }
  .m-row.h { display: grid; }
  .agent, .moments, .rules, .picker li { break-inside: avoid; }
  .agent { padding: 16px; gap: 12px; }
  .solo-pantalla { display: none; }
  .solo-pdf { display: inline; }
  .phrase { border-style: solid; }
  .picker a { padding: 10px; }
}
"""


def incrustar_fuentes(css: str) -> str:
    """Devuelve solo los @font-face latinos, con cada woff2 como data: URI."""
    bloques = re.findall(r"/\* ([a-z-]+) \*/\s*(@font-face\s*\{.*?\})", css, re.S)
    salida = []
    for subconjunto, bloque in bloques:
        if subconjunto not in SUBCONJUNTOS:
            continue
        url = re.search(r"url\((https://[^)]+)\)", bloque).group(1)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        datos = urllib.request.urlopen(req, timeout=60).read()
        b64 = base64.b64encode(datos).decode("ascii")
        salida.append(bloque.replace(url, f"data:font/woff2;base64,{b64}"))
    if not salida:
        sys.exit("No se encontraron fuentes latinas en la hoja de Google Fonts.")
    return "\n".join(salida)


def construir_html() -> str:
    src = FUENTE.read_text(encoding="utf-8")
    titulo = re.search(r"<title>.*?</title>", src, re.S).group(0)
    # Quitar título, meta de claude y enlaces a Google Fonts: van en el <head> nuevo o se incrustan.
    cuerpo = re.sub(r"<title>.*?</title>\s*", "", src, count=1, flags=re.S)
    cuerpo = re.sub(r'<meta name="claude:[^>]*>\s*', "", cuerpo)
    cuerpo = re.sub(r'<link rel="(?:preconnect|stylesheet)"[^>]*>\s*', "", cuerpo)
    estilo, resto = re.match(r"\s*(<style>.*?</style>)\s*(.*)", cuerpo, re.S).groups()
    estilo = estilo.replace("</style>", EXTRA_CSS + "</style>")
    # Textos que solo tienen sentido en pantalla o en papel.
    resto = resto.replace(
        "Toque la situación para ir directo al agente.",
        '<span class="solo-pantalla">Toque la situación para ir directo al agente.</span>'
        '<span class="solo-pdf">Busque el número del agente en las páginas siguientes.</span>',
    )
    resto = resto.replace(
        "En cada uno: toque una frase para copiarla, péguela en el agente",
        '<span class="solo-pantalla">En cada uno: toque una frase para copiarla, péguela en el agente</span>'
        '<span class="solo-pdf">En cada uno: copie la frase, péguela en el agente</span>',
    )
    fuentes = incrustar_fuentes(CSS_FUENTES.read_text(encoding="utf-8"))
    return (
        "<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"{titulo}\n<style>\n{fuentes}\n</style>\n{estilo}\n</head>\n<body>\n{resto}\n</body>\n</html>\n"
    )


PDF_JS = r"""
const { chromium } = require('playwright');
(async () => {
  const [entrada, salida] = process.argv.slice(1);
  const nav = await chromium.launch();
  const pag = await nav.newPage();
  const externas = [];
  pag.on('request', r => { if (!/^(file|data):/.test(r.url())) externas.push(r.url()); });
  await pag.goto('file://' + entrada, { waitUntil: 'networkidle' });
  await pag.emulateMedia({ media: 'print', colorScheme: 'light' });
  await pag.pdf({ path: salida, format: 'Letter', printBackground: true,
                  margin: { top: '14mm', bottom: '14mm', left: '12mm', right: '12mm' } });
  await nav.close();
  if (externas.length) { console.error('Conexiones externas: ' + externas.join(', ')); process.exit(1); }
})();
"""


def construir_pdf() -> None:
    import subprocess

    subprocess.run(["node", "-e", PDF_JS, str(SALIDA_HTML), str(SALIDA_PDF)], check=True)


if __name__ == "__main__":
    SALIDA_HTML.write_text(construir_html(), encoding="utf-8")
    print(f"HTML: {SALIDA_HTML} ({SALIDA_HTML.stat().st_size // 1024} KB)")
    construir_pdf()
    print(f"PDF:  {SALIDA_PDF} ({SALIDA_PDF.stat().st_size // 1024} KB)")
