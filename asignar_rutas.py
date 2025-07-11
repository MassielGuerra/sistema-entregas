# asignar_rutas.py

def asignar_ruta(entrega):
    destino = entrega.get("destino")
    rutas = {
        "Lima": "Ruta 1",
        "Arequipa": "Ruta 2",
        "Cusco": "Ruta 3",
    }
    return rutas.get(destino, "Ruta Desconocida")

if __name__ == "__main__":
    entregas = [
        {"id": 1, "destino": "Lima"},
        {"id": 2, "destino": "Cusco"},
    ]

    for entrega in entregas:
        ruta = asignar_ruta(entrega)
        print(f"🚛 Entrega {entrega['id']} asignada a {ruta}")
