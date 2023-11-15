def corrotina(func):
    def preparação(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro

    return preparação


@corrotina
def print_(formatação):
    while True:
        values = yield
        print(formatação.format(*values))


@corrotina
def média(target):
    total: int = 0
    contador = 0
    while True:
        contador += 1
        total += yield
        target.send((contador, total, total / contador))


formatação = print_("Contador: {}, - Total: {}, - Média: {}")
formatação02 = print_("A: {}, - B: {}, - C: {}")

coro = média(target=formatação)
coro2 = média(target=formatação)
