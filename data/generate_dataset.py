"""
Circular Economy Dataset Generator
Generates 2,000 synthetic company-level records with 24 variables.
Usage: python generate_dataset.py
"""
import csv, random
from datetime import date
random.seed(42)
countries=["México","España","Colombia","Argentina","Chile","Perú","Brasil","Uruguay","Ecuador","Paraguay"]
sectors=["Manufactura","Construcción","Agroindustria","Textil","Electrónica","Plásticos","Papel y Cartón","Metales","Químicos","Alimentos"]
strategies=["Reutilización","Reciclaje","Compostaje","Upcycling","Reparación","Remanufactura","Digestión Anaeróbica","Co-procesamiento","Economía de Producto como Servicio","Intercambio Industrial"]
company_sizes=["Micro (<10)","Pequeña (10-49)","Mediana (50-249)","Grande (250+)"]
certifications=["ISO 14001","ISO 50001","EMAS","Ninguna","Cradle to Cradle","B Corp","ISO 14001 + B Corp"]
waste_types=["Residuos Orgánicos","Plástico","Metal","Vidrio","Papel/Cartón","Electrónicos (RAEE)","Textil","Construcción","Químico Peligroso","Madera"]
rows=[]
for i in range(1,2001):
    size=random.choice(company_sizes)
    wg=round(random.uniform(5,5000),2); wr=round(wg*random.uniform(0.2,0.98),2)
    inv=round(random.uniform(1000,500000),2); rev=round(inv*random.uniform(0.5,3.5),2)
    rows.append([i,date(random.randint(2019,2024),random.randint(1,12),random.randint(1,28)).strftime("%Y-%m-%d"),
        random.choice(countries),random.choice(["Norte","Sur","Este","Oeste","Centro"]),
        random.choice(sectors),size,{"Micro (<10)":random.randint(1,9),"Pequeña (10-49)":random.randint(10,49),"Mediana (50-249)":random.randint(50,249),"Grande (250+)":random.randint(250,2000)}[size],
        random.choice(certifications),random.choice(waste_types),random.choice(strategies),
        wg,wr,round(wg-wr,2),round(wr/wg*100,2),round(wr*random.uniform(0.3,2.5),2),
        round(wr*random.uniform(1.5,15),2),round(wr*random.uniform(0.5,8),2),
        inv,rev,random.randint(0,50),round((rev-inv)/inv*100,2),round(random.uniform(1,10),1)])
with open("economia_circular_dataset.csv","w",newline="",encoding="utf-8") as f:
    csv.writer(f).writerows([["ID","Fecha","País","Región","Sector","Tamaño_Empresa","Empleados","Certificación","Tipo_Residuo","Estrategia_Circular","Residuos_Generados_Ton","Residuos_Recuperados_Ton","Residuos_Dispuestos_Ton","Tasa_Recuperación_Pct","CO2_Evitado_TonCO2eq","Agua_Ahorrada_m3","Energía_Ahorrada_MWh","Inversión_USD","Ingresos_Circular_USD","Empleos_Creados","ROI_Pct","Índice_Circularidad"]]+rows)
print("Done: 2000 rows")
