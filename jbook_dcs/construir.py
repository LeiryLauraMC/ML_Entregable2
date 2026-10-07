"""Ensambla los cuadernos del JBook a partir de cap_*.py, los ejecuta y construye el HTML.
Uso:  python construir.py [--sin-html]"""
import importlib, os, subprocess, sys
from pathlib import Path
import nbformat as nbf
from nbclient import NotebookClient

AQUI = Path(__file__).resolve().parent
os.chdir(AQUI); sys.path.insert(0, str(AQUI))
os.environ.setdefault("BROWSER_PATH", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
CAPS = {"01_contexto": "cap_contexto", "02_eda": "cap_eda", "03_modelos": "cap_modelos"}

for nb_name, mod in CAPS.items():
    celdas = importlib.import_module(mod).CELDAS
    nb = nbf.v4.new_notebook()
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nb.cells = [nbf.v4.new_markdown_cell(t.strip("\n")) if k == "md" else nbf.v4.new_code_cell(t.strip("\n")) for k, t in celdas]
    print("Ejecutando", nb_name, "...", flush=True)
    NotebookClient(nb, timeout=900, kernel_name="python3", resources={"metadata": {"path": str(AQUI)}}).execute()
    nbf.write(nb, AQUI / f"{nb_name}.ipynb")
if "--sin-html" not in sys.argv:
    subprocess.run(["jupyter-book", "build", "."], check=True)
