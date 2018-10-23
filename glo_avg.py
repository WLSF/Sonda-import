import matplotlib.pyplot as plt
import csv

# Baixar dados BRB2017.
# Plotagem disperção.
# Formatar os dados a serem atualizados para duas casas.

# http://sonda.ccst.inpe.br/infos/variaveis.html
# http://sonda.ccst.inpe.br/basedados/index.html

planilha = 'BRB1511ED.csv'
listaunica = 'ListaUnicaCompleta_201606.txt'
estacoesin = './DADOS/GLESTACAO/2017/estacao_201701.txt'
estacoesout = './DADOS/OUTPUT/estacao_201701.txt'
dadosGL = './DADOS/GLGOES/2017/TabMGLGLB_Diar.201701.txt'

ano = int(planilha[3:5])
mes = int(planilha[5:7])
sigla = planilha[:3]

x=[]
y=[]

xmensal=[]
ymensal=[]

GLdia=[]
GLir=[]

# Inicio
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
            break;
        
        # Pega o dia inicial
        for row in plots:
            dia = row[col_dia]
            diainicial = row[col_dia]
            break;

        # Faz a leitura dos dados do Modelo GL
        GL();
        
        # Plotagem diaria
        for row in plots:
            if(dia != row[col_dia]):
                diaria();
                
            dia = row[col_dia]  
            x.append(horamin(int(row[col_min])))
            y.append(float(row[col_irrad]))
            soma += float(row[col_irrad])
            total += 1
            
        # Plotagem do ultimo dia, pois não há um próximo dia para realizar a comparação.
        diaria();

        # Plotagem mensal 
        mensal();

        # Atualiza Estacoes
        atualizar();
        
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
    plt.text(0.35, 1400, 'Média: %5.2f' % media, bbox={'facecolor':'blue', 'alpha':0.5, 'pad':10})

    xmensal.append(diajuliano(int(dia)))
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
    plt.figure(1000)
    plt.plot(xmensal,ymensal, 'b-') #b- é azul
    plt.plot(GLdia, GLir, 'r-') #r- é vermelho
    plt.title("Rede Sonda - " + planilha[:7] +  " - Média Mensal")
    plt.ylabel('Irradiância (Wm-2)')
    plt.xlabel('Dia')
    plt.ylim(0, 450)
    plt.xlim(1,numerodiasmes(mes))
    
    # Media
    mediamensal = somamensal/totalmensal
    plt.text(3, 400, 'Média Sonda: %5.2f' % mediamensal, bbox={'facecolor':'blue', 'alpha':0.5, 'pad':8})

    # Media GL
    mediagl = somararray(GLir)/len(GLir)
    plt.text(15, 400, 'Média GL: %5.2f' %mediagl, bbox={'facecolor':'red', 'alpha':0.5, 'pad':8})

    # Limpa as Variaveis
    #xmensal.clear()
    #ymensal.clear()   
    #somamensal = 0
    #totalmensal = 0    
    
# Define a versao do Cabecalhos
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

# Converte o dia juliano em dia normal
def diajuliano(dia):
    diasmes = [31 , 28 , 31 , 30 , 31, 30, 31, 31, 30, 31,30, 31];
    mes = 1;
    for m in range(1, 12):
        if(dia - diasmes[m-1] >= 1):
            dia = dia - diasmes[m-1]
            mes += 1
        else:
            return dia; #print(format(dia, '02d') + "/" + format(mes, '02d'))
            break;

# Converte minutos em horas
def horamin(x):
    hora = int(x/60)
    minuto = (x%60)/100
    return (hora + minuto)

# Encontra um Elemento em uma Lista
def findElement(elemento, lista):
    for i in range(len(lista)):
        if(elemento == lista[i]):
            return i;
            break;

# Pega o ID da Estação
def getID(sigla):
    with open(listaunica) as lista:
        reader = csv.reader(lista, delimiter='\t')
        for row in reader:
            if(sigla == row[6]):
                return row[0];
                break;
            
# Retorna o numero de dias de determinado mes            
def numerodiasmes(mes):
    diasmes = [31 , 28 , 31 , 30 , 31, 30, 31, 31, 30, 31,30, 31];
    return diasmes[mes-1]

# Soma todos os elementos de um array
def somararray(array):
    soma = 0;
    for i in range(len(array)): soma += array[i]
    return soma

# Formata determinado numero para duas casas.    
def formatn(numero):
    numero = "%.2f" % numero
    return float(numero)
    
# Atualiza estações
def atualizar():    
    with open(estacoesin, "r") as tsvin, open(estacoesout, "w+") as tsvout:
        reader = csv.reader(tsvin, delimiter=' ')
        output = csv.writer(tsvout, delimiter=' ')
        id = getID(sigla);
        for row in reader:
            if(id == row[0]): # Identifica a estação
                for coluna in range(xmensal[0]+4, xmensal[-1]+5): # Faz um loop durante as colunas dia.
                    if(row[coluna] == "-999"): # Verifica se o dado é Nulo(-999).
                        posicao = findElement(coluna-4, xmensal);
                        if(posicao != None): # Verifica se foi calculado a média para este dia;
                            row[coluna] = str(ymensal[posicao]);
                                         
            output.writerow(row);

# Faz a leitura da Estimativa do Modelo GL.
def GL():    
    with open(dadosGL, "r") as tsvGL:
        reader = csv.reader(tsvGL, delimiter=' ')
        id = getID(sigla);
        for row in reader:
            if(id == row[0]): # Identifica a estação
                for coluna in range(5, numerodiasmes(mes)+5): # Faz um loop durante as colunas dia.
                    GLdia.append(coluna-4)
                    GLir.append(float(row[coluna]))              
                break;
        
plot_sonda();
plt.show();
