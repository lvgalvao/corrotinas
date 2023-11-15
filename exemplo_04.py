def média():
    total: int = 0
    contador = 0
    média = "Batata"
    while True:
        entrada = yield média
        total += entrada
        contador += 1
        média = total / contador


coro = média()
# next(coro)
# coro.send(10)
# coro.send(20)
