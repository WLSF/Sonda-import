import matplotlib.pyplot as plt
import csv

# http://sonda.ccst.inpe.br/infos/variaveis.html
# http://sonda.ccst.inpe.br/basedados/index.html

planilha = 'BRB1511ED.csv'
ano = int(planilha[3:5])
mes = int(planilha[5:7])

x=[]
y=[]

xmensal=[]
ymensal=[]

# Radiação Global Horizontal
# Ignore! ==== planilha[3:5]
# Passar de dia Juliano para dia conforme o mês == xmensal


def plot_sonda():
    with open(planilha, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=';')
        global dia, diainicial, media, soma, total, somamensal, totalmensal
        total = 0
        soma = 0
        somamensal = 0
        totalmensal = 0
        
        # Detecta a versao do cabecalho
        for row in plots:
            if(row[3].isdigit()): versao(1)
            else: versao(0)
            break
        
        # Pega o dia inicial
        for row in plots:
            dia = row[col_dia]
            diainicial = row[col_dia]
            break
        
        # Plotagem diaria
        for row in plots:
            if(dia != row[col_dia]):
                diaria();
                
            dia = row[col_dia]  
            x.append(horamin(int(row[col_min])))
            y.append(float(row[col_irrad]))
            soma += float(row[col_irrad])
            total += 1
            
        # Plotagem do ultimo dia,
        # pois não há um próximo dia para realizar a comparação.
        diaria();

        # Plotagem mensal 
        mensal();

# Plotagem diaria
def diaria():
    global dia, diainicial, media, soma, total, somamensal, totalmensal
    plt.figure(dia)
    plt.plot(x,y, 'b-') #b- é azul
    plt.title("Rede Sonda - " + planilha[:7] +  " - Dia [" + str(dia) + "]")
    plt.ylabel('Irradiância (Wm-2)')
    plt.xlabel('Tempo (Horas)')
    plt.ylim(0, 1600)

    # Media
    media = soma/total
    plt.text(0.35, 1400, 'Média: %5.2f' % media, bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})


    diaplot  = (int(dia)-(int(diainicial)-1))
    xmensal.append(diaplot)
    ymensal.append(media)

    # Media Mensal
    somamensal += media
    totalmensal += 1

    # Limpa as Variaveis
    x.clear()
    y.clear()   
    soma = 0
    total = 0


# Plotagem Mensal
def mensal():
    global media, soma, total, somamensal, totalmensal
    plt.figure(1000)
    plt.plot(xmensal,ymensal, 'b-') #b- é azul
    plt.title("Rede Sonda - " + planilha[:7] +  " - Média Mensal")
    plt.ylabel('Irradiância (Wm-2)')
    plt.xlabel('Dia')
    plt.ylim(0, 1600)
    plt.xlim(1,31)
    
    # Media
    mediamensal = somamensal/totalmensal
    plt.text(3, 1400, 'Média: %5.2f' % mediamensal, bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

    # Limpa as Variaveis
    xmensal.clear()
    ymensal.clear()   
    somamensal = 0
    totalmensal = 0    
    
# Cabecalhos
def versao(x):
    global col_dia, col_min, col_irrad, rede
    if x == 0: # Sonda Antigo 
       col_dia = 2
       col_min = 4
       col_irrad = 5
            
    elif(x == 1): # Sonda Novo
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
