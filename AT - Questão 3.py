def impressao(tipo, calculo, porMaxima,renda,gasto):
    print(f'Seus gastos totais com {tipo} comprometem {calculo}% de sua renda mensal. O máximo recomendado é {porMaxima}%. {obterMsg(renda, porMaxima, gasto)}')

def calculo(gasto, renda):
    return gasto * 100 / renda

def obterMsg(aRenda, aPor, oGasto):
    msg = (f'Seus gastos estão dentro da margem recomendada.')
    if calculo(oGasto, aRenda) > aPor:
        msg = (f'Portanto, idealmente, o máximode sua renda comprometida com moradia deveria ser de R$ {aRenda * aPor / 100}')
    return msg

porMxMor=30
porMxEdu=20
porMxTrans=15

rendaMensal=float(input('Renda mensal total: R$ '))
gastoMoradia=float(input('Gastos totais com moradia: R$ '))
gastoEducacao=float(input('Gastos totais com educação: R$ '))
gastoTransportes=float(input('Gastos totais com transportes: R$ '))

impressao('moradia', calculo(gastoMoradia, rendaMensal), porMxMor, rendaMensal, gastoMoradia)
impressao('educação', calculo(gastoEducacao, rendaMensal), porMxEdu, rendaMensal, gastoEducacao)
impressao('transportes', calculo(gastoTransportes, rendaMensal), porMxTrans, rendaMensal, gastoTransportes)
