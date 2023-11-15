def corrotina():
    print("corrotina iniciada")
    valor = yield
    print("corrotina recebeu:", valor)


c = corrotina()
next(c)
c.send(10)
c.close()
