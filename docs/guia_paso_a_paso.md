# Guía paso a paso: Dashboard de Economía Circular en Power BI

**Plataforma:** Power BI Service (online)  
**Licencia:** Microsoft 365 universitaria (Kozminski University)  
**Duración estimada:** 2 horas  
**Nivel:** Doctorado / investigación aplicada

---

## Paso 1 — Cargar el dataset

1. En Power BI Service, haz clic en **"+ Nuevo informe"**
2. Selecciona **"Obtener datos"** → **Texto/CSV**
3. Sube el archivo `economia_circular_dataset.csv`
4. Haz clic en **"Transformar datos"** (no en Cargar directo)

**Configuración del origen:**

- Delimitador: coma
- Codificación: UTF-8 (65001)
- Columnas detectadas: 24

---

## Paso 2 — Transformar datos en Power Query

### Tipos de columna correctos

Aplica estos tipos en el Editor de Power Query:

| Columna                                                                                | Tipo           |
| -------------------------------------------------------------------------------------- | -------------- |
| ID, Año, Mes, Empleados, Empleos_Creados                                               | Número entero  |
| Fecha                                                                                  | Fecha          |
| Residuos_*, Tasa_*, CO2_*, Agua_*, Energía_*, Inversión_*, Ingresos_*, ROI_*, Índice_* | Número decimal |
| País, Región, Sector, Tamaño_Empresa, Certificación, Tipo_Residuo, Estrategia_Circular | Texto          |

### Columnas calculadas

**Trimestre:**

```
= "Q" & Text.From(Date.QuarterOfYear([Fecha]))
```

**Rentabilidad (ratio ingresos/inversión):**

```
= [Ingresos_Circular_USD] / [Inversión_USD]
```

### Script M completo (Editor avanzado)

```powerquery
section Section1;
shared economia_circular_dataset = let
  Origen = Csv.Document(Web.Contents("<TU_URL_AQUI>"),
    [Delimiter=",", Columns=24, Encoding=65001, QuoteStyle=QuoteStyle.None]),
  #"Encabezados promovidos" = Table.PromoteHeaders(Origen, [PromoteAllScalars=true]),
  #"Tipo de columna cambiado" = Table.TransformColumnTypes(
    #"Encabezados promovidos", {
      {"ID", Int64.Type}, {"Fecha", type date}, {"Año", Int64.Type}, {"Mes", Int64.Type},
      {"País", type text}, {"Región", type text}, {"Sector", type text},
      {"Tamaño_Empresa", type text}, {"Empleados", Int64.Type},
      {"Certificación", type text}, {"Tipo_Residuo", type text},
      {"Estrategia_Circular", type text},
      {"Residuos_Generados_Ton", type number}, {"Residuos_Recuperados_Ton", type number},
      {"Residuos_Dispuestos_Ton", type number}, {"Tasa_Recuperación_Pct", type number},
      {"CO2_Evitado_TonCO2eq", type number}, {"Agua_Ahorrada_m3", type number},
      {"Energía_Ahorrada_MWh", type number}, {"Inversión_USD", type number},
      {"Ingresos_Circular_USD", type number}, {"Empleos_Creados", Int64.Type},
      {"ROI_Pct", type number}, {"Índice_Circularidad", type number}
    }),
  #"Trimestre agregado" = Table.AddColumn(
    #"Tipo de columna cambiado", "Trimestre",
    each "Q" & Text.From(Date.QuarterOfYear([Fecha])), type text),
  #"Rentabilidad agregada" = Table.AddColumn(
    #"Trimestre agregado", "Rentabilidad",
    each [Ingresos_Circular_USD] / [Inversión_USD], type number)
in
  #"Rentabilidad agregada";
```

---

## Paso 3 — Crear medidas DAX

En la vista del modelo semántico, crear las siguientes medidas (ver archivo `dax/medidas.dax` para documentación completa):

```dax
Tasa_Recuperación_Promedio = AVERAGE(economia_circular_dataset[Tasa_Recuperación_Pct])
CO2_Total_Evitado = SUM(economia_circular_dataset[CO2_Evitado_TonCO2eq])
ROI_Promedio = AVERAGE(economia_circular_dataset[ROI_Pct])
Índice_Circularidad_Medio = AVERAGE(economia_circular_dataset[Índice_Circularidad])
Empresas_Con_Cert = CALCULATE(COUNTROWS(economia_circular_dataset),
    economia_circular_dataset[Certificación] <> "Ninguna")
```

Las medidas aparecen con ícono de calculadora (∑⚡) en el panel Datos.

---

## Paso 4 — Construir el dashboard (5 visualizaciones)

### Visual 1 — Gráfico de líneas: Tendencia temporal

- Eje X: `Fecha`
- Eje Y: `Tasa_Recuperación_Promedio`
- Título: *Tendencia de Recuperación 2019–2024*

### Visual 2 — Gráfico de barras: ROI por sector

- Eje Y: `Sector`
- Eje X: `ROI_Promedio`
- Ordenar: descendente por ROI_Promedio (menú "..." del visual)
- Título: *ROI Promedio por Sector Económico*

### Visual 3 — Gráfico de dona: Estrategias circulares

- Leyenda: `Estrategia_Circular`
- Valores: recuento de `ID`
- Título: *Distribución de Estrategias Circulares*

### Visual 4 — Gráfico de dispersión: Inversión vs ingresos

- Eje X: `Inversión_USD`
- Eje Y: `Ingresos_Circular_USD`
- Tamaño de burbuja: `CO2_Evitado_TonCO2eq`
- Leyenda: `Tamaño_Empresa`
- Título: *Inversión vs Ingresos Circulares*

### Visual 5 — Tarjetas KPI (4 tarjetas)

- Tarjeta 1: `Tasa_Recuperación_Promedio` → campo **Valor**
- Tarjeta 2: `CO2_Total_Evitado` → campo **Valor**
- Tarjeta 3: `ROI_Promedio` → campo **Valor**
- Tarjeta 4: `Índice_Circularidad_Medio` → campo **Valor**

**Nota:** El ícono de Tarjeta está en la fila 4, último ícono a la derecha del panel Visualizaciones.

---

## Paso 5 — Segmentadores interactivos

Insertar 5 segmentadores (ícono de embudo con líneas = "Segmentación de datos"):

| Segmentador       | Campo            | Estilo recomendado      |
| ----------------- | ---------------- | ----------------------- |
| Año               | `Año`            | Entre (slider de rango) |
| País              | `País`           | Lista                   |
| Sector            | `Sector`         | Lista                   |
| Tamaño de empresa | `Tamaño_Empresa` | Lista                   |
| Certificación     | `Certificación`  | Lista                   |

Para cambiar el estilo del segmentador de Año a slider:  
Seleccionar visual → "..." → **"Segmentación de datos"** → estilo **"Entre"**

---

## Paso 6 — Hallazgos e interpretación académica

### Preguntas de investigación y respuestas

| Pregunta                          | Hallazgo                                                                           |
| --------------------------------- | ---------------------------------------------------------------------------------- |
| ¿Estrategia más común?            | **Reciclaje** es la estrategia circular más frecuente en todos los sectores        |
| ¿Certificaciones y ROI?           | ISO 14001 → ROI promedio **9.66K** vs. sin certificación **9.24K** (+4.5%)         |
| ¿Tamaño e índice de circularidad? | Empresas **pequeñas** (10–49) tienen índice marginalmente mayor; sin patrón fuerte |
| ¿Sector con mayor ROI?            | **Manufactura** > Agroindustria > Papel y Cartón > Plásticos                       |
| ¿Tendencia temporal?              | Tasa de recuperación **estable post-2021** con ligero decrecimiento constante      |

### Implicaciones para la investigación doctoral

- La estabilidad post-2021 sugiere una **meseta de implementación** que requiere nuevos incentivos políticos o de inversión
- La diferencia ISO 14001 vs. sin certificación (+4.5% ROI) apoya la hipótesis de que la certificación ambiental genera valor financiero, aunque el efecto es moderado
- El liderazgo de empresas pequeñas en circularidad es consistente con la literatura sobre flexibilidad e innovación en PyMEs

---

*Proyecto desarrollado para portafolio doctoral — datos sintéticos generados con fines educativos.*
