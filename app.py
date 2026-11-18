'Monte uma matriz para comparar detalhes que o leitor identificou em relatos paralelos.'


def texto(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Use texto não vazio.")
    return value.strip()


def textos(items):
    if not isinstance(items, list):
        raise ValueError("Use uma lista de textos.")
    return [texto(item) for item in items]


def chave_relato(nome):
    normalizado = normalize("NFKD", texto(nome).casefold())
    return " ".join("".join(c for c in normalizado if not combining(c)).split())


def run(data):
    if not isinstance(data, dict):
        raise ValueError("A entrada deve ser um objeto JSON.")
    if not isinstance(data["detalhes"], list) or any(not isinstance(item, dict) for item in data["detalhes"]):
        raise ValueError("O campo detalhes deve ser uma lista de objetos.")
    if not isinstance(data["relatos"], dict):
        raise ValueError("O campo relatos deve ser um objeto JSON.")
    relatos = {}
    nomes_por_chave = {}
    for nome, referencia in data["relatos"].items():
        exibicao = texto(nome)
        chave = chave_relato(exibicao)
        if chave in nomes_por_chave:
            raise ValueError("Nomes de relatos duplicados após normalização.")
        nomes_por_chave[chave] = exibicao
        relatos[exibicao] = texto(referencia)
    if len(relatos) < 2:
        raise ValueError("Inclua pelo menos dois relatos.")
    matriz, comuns, exclusivos = [], [], {}
    for detalhe in data["detalhes"]:
        item = texto(detalhe["item"])
        chaves = {chave_relato(nome) for nome in textos(detalhe["em"])}
        if not chaves or chaves - nomes_por_chave.keys():
            raise ValueError("Cada detalhe deve apontar para relatos registrados.")
        em = {nomes_por_chave[chave] for chave in chaves}
        matriz.append({"item": item, "presenca": {nome: nome in em for nome in relatos}})
        if len(em) == len(relatos):
            comuns.append(item)
        if len(em) == 1:
            exclusivos.setdefault(next(iter(em)), []).append(item)
    return {"relatos": relatos, "matriz": matriz, "comuns": comuns, "exclusivos": exclusivos}


import argparse
import json
from pathlib import Path
from unicodedata import combining, normalize


def objeto_sem_campos_repetidos(pares):
    objeto = {}
    for chave, valor in pares:
        if chave in objeto:
            raise ValueError(f"Campo JSON repetido: {chave!r}.")
        objeto[chave] = valor
    return objeto


def rejeitar_constante_json(constante):
    raise ValueError(f"Constante numérica inválida em JSON: {constante}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", type=Path, help="Arquivo JSON com os dados")
    args = parser.parse_args()

    try:
        with args.entrada.open(encoding="utf-8-sig") as source:
            data = json.load(
                source,
                object_pairs_hook=objeto_sem_campos_repetidos,
                parse_constant=rejeitar_constante_json,
            )
        if not isinstance(data, dict):
            raise ValueError("A entrada deve ser um objeto JSON.")
        result = run(data)
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f"Erro nos dados ou na execução: {exc}\n")

    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()

