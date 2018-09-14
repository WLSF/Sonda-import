import matplotlib.pyplot as plt
import csv

# http://sonda.ccst.inpe.br/infos/variaveis.html
# http://sonda.ccst.inpe.br/basedados/index.html
            
def plot_sonda():
    with open('BRB1511ED.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=';')
        x=[]
        y=[]
        total = 0
        soma = 0

        # Detecta a versao do cabecalho
        for row in plots:
            if(row[3].isdigit()): versao(1)
            else: versao(0)
            break
        
        # Pega o dia inicial
        for row in plots:
            dia = row[col_dia]
            break
        
        # Faz a plotagem dos graficos 
        for row in plots:
            if(dia != row[col_dia]):

                plt.figure(dia)
                plt.plot(x,y, 'b-') #b- é azul
                plt.title("Radiação Global Horizontal - Rede " + rede + " - Dia " + str(dia))
                plt.ylabel('Irradiância (Wm-2)')
                plt.xlabel('Tempo (Horas)')
                plt.ylim(0, 1600)

                media = soma/total
                plt.text(0.35, 1400, 'Média: %5.2f' % media, bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

                x.clear()
                y.clear()   
                dia = row[col_dia]
                soma = 0
                total = 0
                
            x.append(horamin(int(row[col_min])))
            y.append(float(row[col_irrad]))
            soma += float(row[col_irrad])
            total += 1

# Cabecalhos
def versao(x):
        global col_dia, col_min, col_irrad, rede
        if x == 0: # Sonda Antigo 
            rede = 'Sonda'
            col_dia = 2
            col_min = 4
            col_irrad = 5
            
        elif(x == 1): # Sonda Novo
            rede = 'Sonda'
            col_dia = 2
            col_min = 3
            col_irrad = 4

# Converte minutos em horas
def horamin(x):
        hora = int(x/60)
        minuto = (x%60)/100
        return (hora + minuto) 

plot_sonda()
plt.show()
