# generar_reportes.py

import csv

def generar_reporte(entregas, archivo="reporte_entregas.csv"):
    with open(archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "destino", "estado"])
        writer.writeheader()
        for entrega in entregas:
            writer.writerow(entrega)
    print(f"📄 Reporte generado en {archivo}")

if __name__ == "__main__":
    entregas = [
        {"id": 1, "destino": "Lima", "estado": "Entregado"},
        {"id": 2, "destino": "Cusco", "estado": "En ruta"},
    ]
    generar_reporte(entregas)
