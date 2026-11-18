import csv


def celula(valor):
    """Mantém texto com aparência de fórmula como texto em planilhas."""
    if isinstance(valor, str) and valor.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + valor
    return valor


def linhas(relatorio):
    for detalhe in relatorio["matriz"]:
        for relato, presente in detalhe["presenca"].items():
            yield detalhe["item"], relato, relatorio["relatos"][relato], "sim" if presente else "não"


def escrever_csv(relatorio, destino):
    escritor = csv.writer(destino, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
    escritor.writerow(('detalhe', 'relato', 'referencia', 'presente'))
    for linha in linhas(relatorio):
        escritor.writerow([celula(valor) for valor in linha])
