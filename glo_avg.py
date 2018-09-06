import matplotlib.pyplot as plt
import numpy as np

# 1 -  Plotagem conforme os dias ao inves dá posição do array, para caso exista alguma falha no banco de dados.
# 2 -  Detectar se o mês tem 31 dias, ou menos.

<<<<<<< HEAD
dia= 1 # ~Dia Inicial
max_dia = 30# ~Dia Final or Max day

def printa():
    global dia
    lin_min = ((dia-1)*1439)
    lin_max = ((dia)*1439)
=======
dia= 0 # ~Dia Inicial
max_dia = 30 # ~Dia Final or Max day

def printa():
    global dia
    dia+= 1
    lin_min = ((dia-1)*1439)
    lin_max = (dia*1439)
<<<<<<< HEAD
>>>>>>> e1b96b72460c25bfa4808fd828e77f37f3c776ec
=======
>>>>>>> e1b96b72460c25bfa4808fd828e77f37f3c776ec
    x = data[lin_min:lin_max,3]
    y = data[lin_min:lin_max,4]
    plt.figure(dia)
    plt.plot(x,y, '-b') # b- é azul
    plt.title("Radiação Global Horizontal - Rede Sonda - Dia " + str(dia))
    plt.ylabel('Irradiância (Wm-2)')
    plt.xlabel('Minuto')

# Lê a planilha
with open('BRB1511ED.csv', 'r') as csvfile:
    data = np.genfromtxt(csvfile, delimiter=';')
    
# Gráfico dos 30 dias.
while(dia <= max_dia): 
    printa()

# Arruma o espaçamento entre gráficos, caso use o subplot.
plt.tight_layout()
plt.show()
