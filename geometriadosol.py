import matplotlib.pyplot as plt
import math

x=[]
y=[]
So=1357
pi=3.14159

def calculo():
    for dia in range(1, 365): 
        teta = 2 * pi * dia / 365; # teta em graus
        r2sun = 1.00011 + .034221 * math.cos(teta) + .000128 * math.sin(teta);
        S = r2sun * So;
        x.append(dia)
        y.append(S)

def diajuliano(dia , mes):
    diasmes = [31 , 28 , 31 , 30 , 31, 30, 31, 31, 30, 31,30, 31]
    diajuliano = 0;
    for m in range(1, mes):
        diajuliano = diajuliano+diasmes[m-1]
    return diajuliano+dia
        
def plot():    
    plt.figure(100)
    plt.plot(x,y, 'b-') #b- é azul
    plt.title("Distancia Terra Sol")
    plt.ylabel('Distancia')
    plt.xlabel('Dia')
    plt.show() 

print(diajuliano(15,3))          
calculo();
plot();
