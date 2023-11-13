# Projeto explorando corrotinas em Python 3.9

## O que é uma corrotina?

Corrotinas são rotinas que podem ser interrompidas e depois retornar ao ponto onde pararam. Elas são muito úteis para tarefas que envolvem I/O, como ler e escrever em arquivos, sockets, etc.

## Como criar uma corrotina?

Para criar uma corrotina, basta usar a palavra reservada `async` antes da definição da função. Veja o exemplo abaixo:

```python
async def corrotina():
    print('Olá, mundo!')
```