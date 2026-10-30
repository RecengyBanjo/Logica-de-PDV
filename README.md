# PDV com Descontos (Python)

## O que o código faz

Este programa simula a lógica de um PDV (Ponto de Venda) que aplica descontos progressivos em compras. A partir do valor da compra e da idade do cliente, ele calcula o valor final com desconto por idade e por valor, permite registrar várias compras seguidas e, ao encerrar, mostra um resumo do dia com a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como ele faz

1. O código recebe o valor da compra (decimal) e a idade do cliente (inteiro) pelo console.
2. Se o valor ou a idade forem negativos, exibe uma mensagem de aviso e pede o dado novamente.
3. Verifica se a idade é maior ou igual a 65 para aplicar 20% de desconto.
4. Depois verifica se o valor já descontado pela idade é maior que 100 para aplicar mais 10% de desconto sobre esse valor.
5. Arredonda o resultado para duas casas decimais e exibe o valor final formatado em reais (exemplo: `R$ 144.00`).
6. Guarda cada compra em uma lista usando `.append()`.
7. Repete o processo para novas compras até o usuário digitar `0` no valor da compra.
8. Ao encerrar, percorre a lista, soma tudo e mostra o resumo do dia.

## Regras de negócio

| Regra | Condição | Desconto |
|-------|----------|----------|
| Desconto por idade | Idade >= 65 anos | 20% sobre o valor original |
| Desconto por valor | Valor (já com desconto de idade) > R$ 100,00 | 10% extra sobre esse valor |

## Como rodar

```bash
python pdv.py
```

Digite o valor da compra e a idade do cliente a cada rodada. Para encerrar e ver o resumo do dia, digite `0` no valor da compra.

## Tabela de exemplos (casos de teste)

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|-----------|-------|----------------|----------------|----------------------|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | _(preencher com o caso 6 da plataforma)_ | | | | |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | _(preencher com o caso 8 da plataforma)_ | | | | |
| 9 | _(preencher com o caso 9 da plataforma)_ | | | | |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

### Casos-limite

- **Caso 5 (125.00, idade 70):** 125 × 0.8 = 100. Como o valor não é maior que 100, os 10% não se aplicam. Resultado: R$ 100.00.
- **Caso 7 (101.00, idade 30):** 101 × 0.9 = 90.90. O resultado é arredondado para duas casas decimais.
- **Caso 10 (200.00, idade 64):** a idade é 64, então não há desconto por idade. Só o de valor (10%). Resultado: R$ 180.00.

## Exemplo do resumo do dia

```
=== RESUMO DO DIA ===
Quantidade de compras: 2
Total bruto: R$ 250.00
Total de descontos: R$ 46.00
Total final: R$ 204.00
```

## Estrutura de entrega

```
nivel_1/
├── pdv.py      <- código
└── README.md   <- documentação
```
