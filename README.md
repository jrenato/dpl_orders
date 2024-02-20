# DPL Orders

## VSCode setup

Add the following to settings.json

```
{
    "pylint.args": [
        "--load-plugins=pylint_django",
        "--django-settings-module=dpl_orders.settings",
    ],
}
```

## Naming conventions

**Reserva (*Preorder*)**: a distribuidora não tem a mercadoria para pronta entrega. Fará o pedido para o fornecedor e repassará para os clientes.

**Pedido (*Order*)**: a distribuidora tem a mercadoria para pronta entrega. Atenderá o pedido imediatamente. O pedido pode ser resultado de uma reserva ou não.

## Preorder and Order

```mermaid
sequenceDiagram
    Clientes ->> Distribuidora: Fazem as reservas
    Distribuidora->>Fornecedor: Agrupa reservas e faz pedido
    Fornecedor->>Distribuidora: Entrega a mercadoria
    Distribuidora->>Clientes: Separa produtos e atende pedidos
```

## Order Sequence

```mermaid
  graph TD;
        id1(Início)-->id2(Pendente);
        id2-->|Liberado|id3(Em separação);
        id3-->|Conferido|id4(Aguardando confirmação);
        id4-->|Confirmado|id5(Faturado);
        id5-->|Coleta solicitada|id6(Aguardando transporte);
        id6-->|Coletado|id7(Finalizado);

        id3--->|Ajuste|id2
        id4--->|Ajuste|id2

        id2--->|Cancelado|id8(Cancelado);
        id3--->|Cancelado|id8;
        id4--->|Cancelado|id8;
```
