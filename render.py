#!/usr/bin/env python3
"""Genera una imagen 1080x1350 de EYFiber a partir de la plantilla.

Uso:
  python3 render.py --publico "Para tu casa" --titulo "..." --sub "..." \
      --semilla 12 --salida imagenes/2026-10-27-fibra.png
"""
import argparse
import base64
import json
import pathlib

from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent
PLANTILLA = RAIZ / "plantilla" / "post.html"
LOGO = RAIZ / "assets" / "logo.png"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--publico", required=True)
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--sub", default="")
    ap.add_argument("--semilla", type=int, default=7)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    datos = {"publico": a.publico, "titulo": a.titulo, "sub": a.sub, "semilla": a.semilla}
    if LOGO.exists():
        datos["logo"] = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()

    salida = pathlib.Path(a.salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page(viewport={"width": 1080, "height": 1350})
        pag.add_init_script(f"window.POST = {json.dumps(datos)};")
        pag.goto(PLANTILLA.as_uri())
        pag.wait_for_selector("body[data-listo='1']")
        pag.evaluate("document.fonts.ready")
        pag.screenshot(path=str(salida), type="png")
        nav.close()
    print(salida)


if __name__ == "__main__":
    main()
