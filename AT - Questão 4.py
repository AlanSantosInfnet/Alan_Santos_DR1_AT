
def impressao(cont,valor,por,periodo):
    print(f'Após {cont} períodos(s), o montante será de R${calculo(valor,por,periodo):.2f}')

def calculo (valor,por,periodo):
    return (valor * por/100) + (valor+periodo)

valorInicial = float(input('Valor inicial: R$ '))
rendimentoPeriodo = float(input('Rendimento por período (%): '))
aportePeriodo = float(input('Aporte a cada período: R$ '))
totalPeriodo = int(input('Total de períodos: '))
print('')
contador = 1
while contador <= totalPeriodo:
    impressao(contador,valorInicial,rendimentoPeriodo,aportePeriodo)
    valorInicial = calculo(valorInicial,rendimentoPeriodo,aportePeriodo)
    contador = contador + 1


