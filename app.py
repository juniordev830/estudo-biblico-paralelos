'Monte uma matriz para comparar detalhes que o leitor identificou em relatos paralelos.'


def texto(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Use texto não vazio.")
    return value.strip()


def textos(items):
    if not isinstance(items, list):
        raise ValueError("Use uma lista de textos.")
    return [texto(item) for item in items]


def run(data):
    if not isinstance(data, dict):
        raise ValueError("A entrada deve ser um objeto JSON.")
    if not isinstance(data["detalhes"], list) or any(not isinstance(item, dict) for item in data["detalhes"]):
        raise ValueError("O campo detalhes deve ser uma lista de objetos.")
    if not isinstance(data["relatos"], dict):
        raise ValueError("O campo relatos deve ser um objeto JSON.")
    relatos = {}
    for nome, referencia in data["relatos"].items():
        nome = texto(nome)
        if nome in relatos:
            raise ValueError("Nomes de relatos duplicados após remover espaços.")
        relatos[nome] = texto(referencia)
    if len(relatos) < 2:
        raise ValueError("Inclua pelo menos dois relatos.")
    matriz, comuns, exclusivos = [], [], {}
    for detalhe in data["detalhes"]:
        item = texto(detalhe["item"])
        em = set(textos(detalhe["em"]))
        if not em or em - relatos.keys():
            raise ValueError("Cada detalhe deve apontar para relatos registrados.")
        matriz.append({"item": item, "presenca": {nome: nome in em for nome in relatos}})
        if len(em) == len(relatos):
            comuns.append(item)
        if len(em) == 1:
            exclusivos.setdefault(next(iter(em)), []).append(item)
    return {"relatos": relatos, "matriz": matriz, "comuns": comuns, "exclusivos": exclusivos}


import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", type=Path, help="Arquivo JSON com os dados")
    args = parser.parse_args()

    try:
        with args.entrada.open(encoding="utf-8") as source:
            data = json.load(source)
        if not isinstance(data, dict):
            raise ValueError("A entrada deve ser um objeto JSON.")
        result = run(data)
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f"Erro nos dados ou na execução: {exc}\n")

    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()

