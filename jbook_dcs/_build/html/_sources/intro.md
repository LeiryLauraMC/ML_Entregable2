# Dificultad cognitiva subjetiva y factores de riesgo modificables de demencia

Segundo entregable del proyecto de investigación de Machine Learning
Maestría en Ingeniería Biomédica, Universidad del Norte · Santiago Díaz, Gina Huguet y Leiry Mares · Octubre de 2026

## De qué trata este informe

En el primer entregable construimos la base de datos, exploramos la información, revisamos que no
hubiera fuga de datos y entrenamos una regresión logística como modelo de referencia. Este segundo
entregable toma ese trabajo y lo vuelve algo que se puede recorrer con el ratón: un dashboard en
Dash Plotly con tres pestañas (contexto del problema, análisis exploratorio y modelos base) y este
informe, que acompaña cada pantalla del dashboard con la explicación de lo que se está viendo.

La pregunta de investigación no cambia. Queremos saber qué tan bien los factores de riesgo
modificables de demencia, junto con el antecedente de accidente cerebrovascular (ACV), permiten
predecir si un adulto reporta dificultad para recordar o concentrarse, usando 56.129 participantes de
la National Health Interview Survey (NHIS) 2022-2023 de los CDC. Con la regresión logística
obtenemos una PR-AUC de 0,538 [IC 95 %: 0,517-0,561] en el conjunto de prueba, frente a 0,206 de la
línea base trivial, y un ROC-AUC de 0,804 [0,794-0,814]. Una SVM lineal, que incorporamos como
segundo modelo base, llega prácticamente al mismo lugar (PR-AUC de 0,537).

## Cómo leer este informe junto con el dashboard

Cada capítulo corresponde a una pestaña del dashboard y sigue su mismo orden, así que se puede
tener el dashboard abierto y avanzar sección por sección. Las gráficas del informe se generan con las
mismas funciones del dashboard, pero aquí quedan fijas y con los filtros en su valor por defecto
(toda la población de entrenamiento). Cuando algo solo se aprecia moviendo los controles, lo
decimos en el texto y damos los valores que se obtienen con algunos filtros.

| Capítulo | Pestaña del dashboard | Qué contiene |
|---|---|---|
| 1. Contexto del problema | Pestaña 1 | El problema, los objetivos, el origen de los datos, el marco Lancet, el mapa de variables y el diccionario |
| 2. Análisis exploratorio | Pestaña 2 | Variable objetivo, edad, factores de riesgo, ACV, estructura multivariada, calidad de datos y auditoría de fuga |
| 3. Modelos base | Pestaña 3 | Regresión logística y SVM lineal: umbral, métricas, calibración, hiperparámetros, odds ratios, subgrupos y simulador |
| Conclusiones | | Hallazgos, limitaciones y próximos pasos |

Además de interpretar lo que aparece en el dashboard, cada capítulo incluye una sección de
**detalles que el dashboard no muestra**: las pruebas estadísticas detrás de las gráficas, las
decisiones de preprocesamiento, el análisis de faltantes, la comparación entre los dos modelos y
algunos cálculos adicionales, como la interacción entre ACV y edad.

## Cómo está construido el dashboard

El dashboard se generó con la herramienta `dash-tools` (`pip install dash-tools`), usando su
plantilla de pestañas como punto de partida, y se organizó así:

```text
entregable2/
├── dashboard_dcs/             proyecto creado con dashtools
│   ├── src/app.py             diseño de las tres pestañas y callbacks (comentado por secciones)
│   ├── src/assets/style.css   estilos (fondo claro, paleta de tierras)
│   ├── src/dcs/               cálculos y figuras compartidos con este informe
│   ├── data/                  train.csv, test.csv y la base completa del Entregable 1
│   └── cache/                 modelos y resultados guardados la primera vez que se ejecuta
└── jbook_dcs/                 este informe
```

Para abrirlo basta con `pip install -r requirements.txt` y `python src/app.py` dentro de
`dashboard_dcs`; el dashboard queda en <http://127.0.0.1:8050/>. La primera ejecución entrena los
modelos y tarda unos minutos, las siguientes abren en segundos porque leen la caché.

## Reproducibilidad

- Datos: los mismos archivos procesados del Entregable 1 (`train.csv`, `test.csv`), con la partición 80/20
  estratificada por objetivo y año hecha antes de cualquier decisión basada en los datos.
- Semilla aleatoria: `SEED = 42` en la partición, la validación cruzada, el bootstrap, los modelos
  y los métodos exploratorios con componente aleatorio.
- Dependencias: `requirements.txt` de cada carpeta. Los resultados de este informe se obtuvieron con
  scikit-learn 1.9.1, por lo que en versiones distintas las cifras pueden diferir en el cuarto decimal.
- Los capítulos se entregan ya ejecutados. Volver a ejecutarlos exige `kaleido` y un navegador
  Chrome o Chromium para dibujar las figuras como imagen.
