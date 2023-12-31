# Projeto explorando corrotinas em Python 3.9

## O que é uma corrotina?

Corrotinas são rotinas que podem ser interrompidas e depois retornar ao ponto onde pararam. Elas são muito úteis para tarefas que envolvem I/O, como ler e escrever em arquivos, sockets, etc.

## Yield como controle de fluxo

O `yield` é uma palavra reservada do Python que permite que uma função seja interrompida e depois retorne ao ponto onde parou. Isso é muito útil para tarefas que envolvem I/O, como ler e escrever em arquivos, sockets, etc.

No exemplo abaixo, exemplo_00.py, importamos duas funções para nossa classe Scheduler: `add` e `run`. A função `add` recebe uma corrotina e a adiciona a uma lista de tarefas. A função `run` executa as tarefas adicionadas à lista.

Por trabalhar com Yield, temos um fluxo que executa a função, para, executa a função a outra função, para, executa a função, para, e assim por diante.

```python
from collections import deque


def contador(stop):
    cont = 1
    while cont <= stop:
        yield cont
        cont += 1


def contador_regressivo(start):
    while start >= 1:
        yield start
        start -= 1


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add_new(self, coro):
        self.queue.append(coro)

    def run(self):
        while self.queue:
            task = self.queue.popleft()
            try:
                result = next(task)
                print(f"{task=}: {result=}")

                self.queue.append(task)
            except StopIteration:
                ...

    def __repr__(self) -> str:
        return "Scheduler(" + str(self.queue) + ")"
```

## Yield vs Return

O `yield` funciona como um `return`, mas com a diferença de que ele não encerra a função, apenas retorna um valor e continua a execução da função. O `return` encerra a função e retorna um valor.

No exemplo abaixo, exemplo_01.py, temos uma função que retorna um valor e encerra a função. Diferente do exemplo anterior, onde a função não é encerrada, apenas retorna um valor e continua a execução. O yield torna a função um gerador.

O `yield` produz e o `next` consome. O `yield` é um produtor e o `next` é um consumidor. o `next` não consegue iterar sobre uma função que não seja um gerador.

## Yield trabalhando junto com Thread

No exemplo 02, colocamos nossas funções dentro de um Thread. Dessa forma conseguimos inserir novas funções entre a execução principal.

## Yield como corrotina

No exemplo 03, adicionamos os métodos `send`. O método `send` envia um valor para a corrotina. Ou seja, o yield é um produtor e o send é um consumidor.

## `send` vs `next`

O `send` é um `next` com um valor. O `next` não consegue enviar um valor para a corrotina, apenas o `send` consegue.

## Yield como produtor e consumidor ao mesmo tempo

No exemplo 04, temos o Yield atuando como produto e consumidor ao mesmo tempo.

```python
def média():
    total: int = 0
    contador = 0
    média = None
    while True:
        entrada = yield média
        total += entrada
        contador += 1
        média = total / contador


coro = média()
# next(coro)
# coro.send(10)
# coro.send(20)
```

### Corrotinas

Corrotinas são rotinas que podem ser interrompidas e depois retornar ao ponto onde pararam. Elas são muito úteis para tarefas que envolvem I/O, como ler e escrever em arquivos, sockets, etc. Na engenharia de dados, por exemplo, podemos usar corrotinas para ler arquivos grandes e processá-los em pequenos pedaços, sem precisar carregar o arquivo inteiro na memória. Outro exemplo, é o uso de corrotinas para fazer requisições HTTP em paralelo.

## Primer

O exemplo 05 é um primer de como usar corrotinas. Criarmos um decorador que realizar o next(coro) inicial, para que não seja necessário realizar o next(coro) toda vez que for executar uma corrotina.