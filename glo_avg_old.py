import matplotlib.pyplot as plt
import csv

x=[]
y=[]

vezes = 2 # Numero do dia, valor inicial = 0, a 30.
line_count = 0 # Variavel do contador de linhas.

# http://sonda.ccst.inpe.br/infos/variaveis.html
# http://sonda.ccst.inpe.br/basedados/index.html

# Conforme é chamado a função myrange o numero de vezes é incrementado.
# 1 vez ou 1 dia = 1439 minutos --- grafico do minuto 0 ao 1439.
# 2 vez ou 2 dia = 2878 minutos --- grafico do minuto 1439 ao 2878.

# Problema 1 : A partir do segundo dia o gráfico é plotado com as informações e cordenadas do primeiro dia/gráfico, como também ignora a area de plotagem.
# Problema 2 : A partir do segundo gráfico o mesmo imprime as cordenadas iguais ao primeiro, problema talvez relacionado ao array.

def myrange():
    with open('BRB1511ED.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=';')
        global line_count
        global vezes
        vezes += 1 
        for row in plots:
            line_min = ((vezes-1)*1439) # minuto inicial
            line_max = ((vezes*1439)+1) # minuto final   
            if  line_min < line_count & line_count < line_max:   # < Problema 2 possivelmente está aqui!
                x.append(int(row[3])+((vezes-1)*1439)) # Coluna minutos
                y.append(float(row[4])) # Coluna Irradiância
                
            line_count += 1  # Incremento ao contador de linhas, mesmo caso não entre no if.
		
# Gambiarra para ler uma celula especifica!
def read_cell(x, y):
       with open('BRB1511ED.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=';')
        y_count = 0
        for row in plots:
            if y_count == y:
                return row[x]
            y_count += 1

# Imprime os graficos
def print():
    global vezes
    myrange()
    plt.figure(vezes-1)  # Numero da figura a ser apresentada.
    plt.plot(x,y, 'b-') # b- é azul
    plt.title("Radiação Global Horizontal - Rede Sonda - Dia " + str(read_cell(2,((vezes)*1439))))
    plt.ylabel('Irradiância (Wm-2)')
    plt.xlabel('Minuto')

print() # dia 1
print() # dia 2
print() # dia 3

plt.tight_layout() # Arruma o espaçamento entre gráficos, caso use o subplot.
plt.show() # Imprime os gráficos
