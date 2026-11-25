# Comparação de relatos bíblicos

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


## Novo recurso

Com `diagnostico: true`, inclui totais, exclusivos e percentual de detalhes registrados por relato. São estatísticas das anotações do leitor, não prova de ausência de detalhes no texto bíblico.
