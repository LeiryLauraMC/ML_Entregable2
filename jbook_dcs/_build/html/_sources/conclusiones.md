# Conclusiones

## Lo que encontramos

**Hay señal, pero con techo.** Las 14 variables permiten predecir la dificultad cognitiva subjetiva (DCS) bastante mejor que el azar:
una PR-AUC de 0,538 [0,517-0,561] frente a 0,206 del clasificador trivial, y un ROC-AUC de 0,804. Los dos modelos base, la regresión
logística y la SVM lineal, quedan empatados (diferencia de PR-AUC de unas milésimas, con un intervalo que incluye el cero), producen
probabilidades casi idénticas (correlación de 0,994) y coinciden en la clasificación del 97,8 % de las personas de prueba.
La curva de aprendizaje indica que el modelo no sobreajusta y que más filas del mismo tipo no lo mejorarían.

**La salud mental y los sentidos pesan más que los factores cardiometabólicos.** Los síntomas depresivos diarios (OR 4,9), el diagnóstico de
depresión (2,2) y las dificultades auditivas y visuales (2,1-2,6) son los factores con mayor asociación. El ACV tiene un OR de 1,69 y los factores
cardiometabólicos son modestos (colesterol 1,28, diabetes 1,17; la hipertensión deja de ser significativa al ajustar). La escolaridad protege con un
gradiente claro (OR de 0,53 con posgrado). La interacción entre ACV y edad que se ve en los datos crudos se debe a otras variables: ajustada, deja de ser significativa.

**La relación con la edad tiene forma de U.** La probabilidad predicha es de 0,245 a los 18 años, baja hasta 0,168 hacia los 51 y sube a 0,361 a los 85.
Esto justifica haber modelado la edad con splines.

**Las probabilidades son confiables, salvo en los extremos.** La calibración es buena en la mayor parte del rango y por subgrupos; el modelo
sobrestima el riesgo del grupo de menor probabilidad. La discriminación es peor en las personas de 65 años o más, en quienes ya tuvieron un ACV y en quienes tienen diagnóstico de depresión.

**El umbral es una decisión de uso.** Con 0,246 se recupera el 64 % de los casos con una precisión de 46 %; con 0,15 el recall sube a 0,805 y la precisión baja a 0,368.

## Limitaciones

- **Corte transversal.** Todo es asociación en un momento dado; el modelo no anticipa deterioro futuro.
- **La DCS es subjetiva.** Se mezcla con depresión, ansiedad, sueño y estrés, y no se puede separar de ellos con estos datos.
- **Cobertura parcial del marco Lancet.** Se miden 9 de los 14 factores en los dos años; faltan, sobre todo, la actividad física y el aislamiento social.
- **Sesgo de selección.** Se excluyeron los informantes sustitutos, que probablemente concentran los casos más severos.
- **Modelos lineales.** No capturan interacciones ni relaciones no lineales entre variables distintas de la edad.
- **Grupos pequeños.** Los resultados por raza o etnia en categorías con menos de 150 personas tienen intervalos muy amplios.
- **Población estadounidense.** No se garantiza que el modelo se transfiera a otros países.

## Próximos pasos

1. Probar modelos que capturen no linealidades e interacciones (árboles potenciados, bosques aleatorios) y compararlos con esta línea base.
2. Hacer un análisis de sensibilidad sin las variables que dejamos «en observación» en la auditoría de fuga.
3. Evaluar la equidad del desempeño por raza, sexo y edad con métricas específicas, no solo con los diagnósticos por subgrupo.
4. Incorporar los factores de un solo año (inactividad física, alcohol) en un análisis restringido a 2022.
5. Explorar la ponderación por el peso muestral para estimar efectos poblacionales.
