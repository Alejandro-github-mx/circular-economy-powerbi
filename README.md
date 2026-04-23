# Circular Economy Analytics Dashboard
### Power BI Portfolio Project — Doctoral Research

![Power BI](https://img.shields.io/badge/Power%20BI-Online-F2C811?style=flat&logo=powerbi&logoColor=black)
![Dataset](https://img.shields.io/badge/Dataset-2%2C000%20records-1D9E75?style=flat)
![Variables](https://img.shields.io/badge/Variables-24-0F6E56?style=flat)
![Period](https://img.shields.io/badge/Period-2019--2024-3C3489?style=flat)

---

## 📋 Project Overview

This project presents an interactive business intelligence dashboard built in **Power BI Service (online)** to analyze circular economy practices across 10 Latin American and European countries. The dataset covers 2,000 company-level observations spanning 2019–2024, with 24 variables measuring waste recovery, environmental impact, financial performance, and circular economy strategies.

This dashboard was developed as part of doctoral research in sustainability and circular economy at **Kozminski University**.

---

## 🎯 Research Questions

1. Which circular economy strategy is most commonly adopted across sectors?
2. Do certified companies (ISO 14001, EMAS, B Corp) achieve higher ROI than non-certified ones?
3. Is there a relationship between company size and the circular economy index?
4. Which economic sector generates the highest ROI through circular practices?
5. Is there a temporal trend of improvement in waste recovery rates (2019–2024)?

---

## 🔍 Key Findings

| # | Finding |
|---|---------|
| H1 | **Recycling** is the most common circular strategy across all sectors and countries |
| H2 | Companies with ISO 14001 certification show **higher average ROI** (9.66K) vs. non-certified (9.24K), suggesting a positive but moderate effect of environmental certification on financial performance |
| H3 | **Small companies** (10–49 employees) display a slightly higher circularity index than other size categories, though differences are not dramatic — suggesting size is not a strong predictor of circularity |
| H4 | **Manufacturing** leads in average ROI, followed by Agroindustry and Paper & Cardboard, then Plastics — indicating that capital-intensive sectors may capture more value from circular transitions |
| H5 | Waste recovery rates appear **relatively stable post-2021** with a slight but consistent downward trend, suggesting implementation plateaus that may require new policy or investment incentives |

---

## 📊 Dashboard Structure

```
┌─────────────────────────────────────────────────────────┐
│  KPI Cards: Recovery Rate · CO2 Avoided · ROI · CI Index│
├─────────────────────────────────────────────────────────┤
│          Line Chart: Recovery Rate Trend 2019–2024       │
├──────────────────────────┬──────────────────────────────┤
│  Bar Chart: ROI by Sector│  Donut: Circular Strategies  │
├─────────────────────────────────────────────────────────┤
│     Scatter: Investment vs Circular Revenue (bubble)     │
├─────────────────────────────────────────────────────────┤
│  Slicers: Year · Country · Sector · Company Size · Cert  │
└─────────────────────────────────────────────────────────┘
```

---

## 🗄️ Dataset Description

**File:** `data/economia_circular_dataset.csv`
**Rows:** 2,000 | **Columns:** 24 | **Period:** 2019–2024

| Column | Type | Description |
|--------|------|-------------|
| ID | Integer | Unique record identifier |
| Fecha | Date | Record date |
| Año / Mes | Integer | Year and month extracted |
| País | Text | Country (10 countries) |
| Región | Text | Geographic region within country |
| Sector | Text | Economic sector (10 sectors) |
| Tamaño_Empresa | Text | Company size category |
| Empleados | Integer | Number of employees |
| Certificación | Text | Environmental certification held |
| Tipo_Residuo | Text | Type of waste managed |
| Estrategia_Circular | Text | Circular economy strategy applied |
| Residuos_Generados_Ton | Decimal | Total waste generated (tonnes) |
| Residuos_Recuperados_Ton | Decimal | Waste recovered (tonnes) |
| Residuos_Dispuestos_Ton | Decimal | Waste sent to landfill (tonnes) |
| Tasa_Recuperación_Pct | Decimal | Recovery rate (%) |
| CO2_Evitado_TonCO2eq | Decimal | CO2 emissions avoided (tCO2eq) |
| Agua_Ahorrada_m3 | Decimal | Water saved (m³) |
| Energía_Ahorrada_MWh | Decimal | Energy saved (MWh) |
| Inversión_USD | Decimal | Investment in circular practices (USD) |
| Ingresos_Circular_USD | Decimal | Revenue from circular activities (USD) |
| Empleos_Creados | Integer | Jobs created |
| ROI_Pct | Decimal | Return on investment (%) |
| Índice_Circularidad | Decimal | Composite circularity index (1–10) |
| Trimestre | Text | Quarter (Q1–Q4) — calculated column |
| Rentabilidad | Decimal | Revenue/Investment ratio — calculated column |

---

## 🧮 DAX Measures

See full documentation in [`dax/medidas.dax`](dax/medidas.dax)

```dax
Tasa_Recuperación_Promedio = AVERAGE(economia_circular_dataset[Tasa_Recuperación_Pct])
CO2_Total_Evitado          = SUM(economia_circular_dataset[CO2_Evitado_TonCO2eq])
ROI_Promedio               = AVERAGE(economia_circular_dataset[ROI_Pct])
Índice_Circularidad_Medio  = AVERAGE(economia_circular_dataset[Índice_Circularidad])
Empresas_Con_Cert          = CALCULATE(COUNTROWS(economia_circular_dataset),
                               economia_circular_dataset[Certificación] <> "Ninguna")
```

---

## 🛠️ Tools & Technology

- **Power BI Service** (online) — Microsoft Fabric / Kozminski University license
- **Power Query (M language)** — data transformation and calculated columns
- **DAX** — KPI measures and dynamic calculations
- **Python** — synthetic dataset generation (`data/generate_dataset.py`)

---

## 📁 Repository Structure

```
circular-economy-powerbi/
├── README.md
├── data/
│   ├── economia_circular_dataset.csv   ← main dataset (2,000 rows)
│   └── generate_dataset.py             ← Python script used to generate it
├── dax/
│   └── medidas.dax                     ← all DAX measures documented
└── docs/
    └── guia_paso_a_paso.md             ← step-by-step Power BI guide (ES)
```

---

## 🔗 Academic Context

This project applies Business Intelligence methods to circular economy research, an emerging field at the intersection of industrial ecology, sustainability management, and data science. The dashboard enables exploratory analysis of:

- **Ellen MacArthur Foundation** circular economy principles (reduce, reuse, recycle)
- **SDG 12** (Responsible Consumption and Production) monitoring
- Financial viability of circular transitions by sector and company size

---

## 👤 Author

**Alejandro** | Doctoral Researcher  
Kozminski University, Warsaw  
*Sustainability · Circular Economy · Business Intelligence*

---

*Dataset is synthetic and generated for educational/research portfolio purposes.*
