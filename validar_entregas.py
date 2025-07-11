# validar_entregas.py

def validar_entregas(entregas):
    print("✅ Validando entregas...")

    for entrega in entregas:
        if "id" not in entrega or "destino" not in entrega:
            print("❌ Entrega inválida:", entrega)
        else:
            print("✔️ Entrega válida:", entrega)

if __name__ == "__main__":
    entregas = [
        {"id": 1, "destino": "Arequipa"},
        {"destino": "Cusco"},
    ]
    validar_entregas(entregas)
