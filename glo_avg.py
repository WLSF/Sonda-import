import matplotlib.pyplot as plt
import csv

x=[]
y=[]

# http://sonda.ccst.inpe.br/infos/variaveis.html
# http://sonda.ccst.inpe.br/basedados/index.html

vezes = 0
line_count = 0


# Conforme é chamado a função myrange o numero de vezes é incrementado.

# 1 vez ou 1 dia = 1439 minutos --- grafico do minuto 0 ao 1439.

# 2 vez ou 2 dia = 2878 minutos --- grafico do minuto 1439 ao 2878.

def myrange():
    with open('BRB1511ED.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=';')
        global line_count
        global vezes
        vezes += 1 
        for row in plots:
            line_min = (vezes-1*1439)
            line_max = ((vezes*1439)+1)
            
            if  line_min < line_count & line_count < line_max:   # não funciona como deveria!
                x.append(int(row[3]))
                y.append(float(row[4]))
            line_count += 1

def myrange2():
    with open('BRB1511ED.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=';')
        global line_count
        global vezes
        vezes += 1
        for row in plots:
            line_min = (vezes-1*1439)
            line_max = ((vezes*1439)+1)
            
            if line_count > line_min:
                if line_count < line_max:
                    x.append(int(row[3]))
                    y.append(float(row[4]))
                else:
                    x.append(int(row[3]))
                    y.append(0)
                    
            else:
                x.append(int(row[3]))
                y.append(0)
                
            line_count += 1

		
		
		

# Gambiarra para ler uma celula especifica!
def read_cell(x, y):
       with open('BRB1511ED.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=';')
        y_count = 0
        for row in plots:
            if y_count == y:
                return row[x]
            y_count += 1
                
myrange()
	
plt.figure(1)
plt.subplot(211)
plt.plot(x,y, 'b-') #b- é azul

plt.title("Radiação Global Horizontal - Rede Sonda - Dia " + str(read_cell(2,((vezes)*1439))))
plt.ylabel('Irradiância (Wm-2)')
plt.xlabel('Minuto')

plt.show()
