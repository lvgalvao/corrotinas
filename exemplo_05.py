def corrotina(func):
    def preparação(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro

    return preparação


@corrotina
def média():
    total: int = 0
    contador = 0
    média = 0
    while True:
        entrada = yield média
        total += entrada
        contador += 1
        média = total / contador


coro = média()
