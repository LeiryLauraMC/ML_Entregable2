"""
informe.py · utilidades de los capítulos del JBook
==================================================
Los capítulos usan exactamente el mismo código de cálculo y las mismas funciones de
figuras que el dashboard (carpeta ../dashboard_dcs/src/dcs), de modo que cada gráfica
del informe es la misma que se ve en el dashboard, pero fija (imagen) para poder
leerse en papel o en HTML sin servidor.
"""
import os
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ.parent / "dashboard_dcs" / "src"))

# Kaleido necesita un navegador Chrome/Chromium para dibujar las figuras como imagen.
for _ruta in ["/opt/pw-browsers/chromium-1194/chrome-linux/chrome"]:
    if Path(_ruta).exists():
        os.environ.setdefault("BROWSER_PATH", _ruta)

import numpy as np                      # noqa: E402
import pandas as pd                     # noqa: E402
from IPython.display import Markdown, display   # noqa: E402

from dcs import figuras as F            # noqa: E402,F401
from dcs.calculos import ETIQUETAS, obtener_artefactos, prevalencia_por, wilson   # noqa: E402,F401
from dcs.utils import (CATEGORIAS, DICCIONARIO, OBJETIVO, ORDENES, PREDICTORAS,   # noqa: E402,F401
                       PREDICTORAS_CAT, cargar_particiones)

pd.set_option("display.max_columns", 60)
pd.set_option("display.width", 180)

A = obtener_artefactos()                 # modelos y resultados guardados por el dashboard
TRAIN, TEST = cargar_particiones()
DF = F.preparar(TRAIN)                   # entrenamiento con columnas de grupos de edad


def mostrar(fig, ancho=980, alto=None):
    """Dibuja una figura Plotly como imagen estática, con fondo blanco."""
    fig.update_layout(paper_bgcolor="white")
    fig.show(renderer="png", width=ancho, height=alto or fig.layout.height, scale=1.5)


def ver(df, formato=None, indice=False):
    """Muestra una tabla con el estilo del informe (formato: dict columna -> formato)."""
    sty = df.style
    if not indice:
        sty = sty.hide(axis="index")
    if formato:
        sty = sty.format(formato)
    display(sty.set_properties(**{"text-align": "left"}))
