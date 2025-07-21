import pandas as pd

def process_excel(file_path):
    df = pd.read_excel(file_path)
    resultados = []

    for i, row in df.iterrows():
        resultados.append({
            "tipo": row["Tipo"],
            "credito": float(row["Crédito"]),
            "entrada": float(row["Entrada"]),
            "parcelas": row["Parcelas"]
        })

    return resultados
