# Comparação de relatos bíblicos

**Navegação** · [Rodar](#rodar) · [Uso](#uso) · [Fontes e exemplos](#fontes-e-exemplos) · [Código e estudo](docs/ENGENHARIA_REVERSA.md)

Monte uma matriz para comparar detalhes que o leitor identificou em relatos paralelos.

## Rodar

Python 3.10 ou mais recente. Cada execução lê um JSON local e imprime outro JSON no terminal.

```bash
python app.py exemplo.json
python -m unittest -v
```

## Uso

Dê uma chave curta a cada passagem e registre os detalhes observados com a lista de chaves onde aparecem. O relatório mostra os detalhes comuns e os registrados em um só relato.

## Fontes e exemplos

Os exemplos incluem referências bíblicas, perguntas e anotações de demonstração. Consulte o texto e o contexto em uma [tradução publicada pela Sociedade Bíblica do Brasil](https://www.sbb.org.br/traducoes-da-biblia). Para aprofundar, o catálogo da [Nova Bíblia de Estudo Almeida](https://www.sbb.org.br/nova-almeida/biblias-de-estudo/biblia-de-estudo-almeida) e o do [Comentário Bíblico Pentecostal do Novo Testamento, CPAD](https://www.cpad.com.br/comentario-biblico-pentecostal-novo-testamento-/p) ajudam a identificar edições. Registre as páginas verificadas na sua própria consulta.

## Exportação para planilha

Use `python app.py exemplo.json --csv > relatorio.csv` para exportar a presença de cada detalhe nos relatos. O CSV usa ponto e vírgula, conserva a ordem do relatório e inclui o cabeçalho mesmo quando a seleção está vazia. O JSON continua sendo a saída padrão.

Também é possível encadear a ferramenta com outro comando usando `-` como entrada. Exemplo em um terminal Bash:

```bash
cat exemplo.json | python app.py -
```

## Código e roteiro de estudo

Como diferenciar na saída uma observação ausente de uma divergência explícita entre relatos? O [guia de engenharia reversa](docs/ENGENHARIA_REVERSA.md) reúne o mapa dos módulos e uma pergunta técnica baseada no projeto.

Mantido por [João Junior](https://github.com/juniordev830).
