def faltadados():
    array = [29 , -999 , 30 , 31, -999, -999, 30, -999, 30, 35, 31, 30, 31,30, 31, -999, 30];
    menor=0
    maior=0
    abre=[]
    fecha=[]
    chave=False
    for i in range(len(array)):
        if(array[i] == -999):
            if chave == False: # Abre
                abre.append(i)
                chave = True;
        else:
            if(chave == True): # Fecha
                fecha.append(i-1)
                chave = False;

            if(menor == 0): menor = array[i] # Menor
        
        if(array[i] > maior): maior= array[i] # Maior

        if(i+1 == len(array) and chave == True): # Verifica o fim do array
            fecha.append(i-1)
            chave = False;

    # Onde começa a falta de dados
    for i in range(len(abre)): print(abre[i])
    print('-----------')

    # Onde termina a falta de dados
    for i in range(len(fecha)): print(fecha[i])
    print('-----------')

    # Imprime o Intervalo onde falta dados.
    for i in range(len(abre)):
        intervalo = ((fecha[i]-abre[i])+1)
        print(intervalo)
    print('-----------')

    # Calcula os valores
    for i in range(len(abre)):
        intervalo = ((fecha[i]-abre[i])+1)
        for m in range(intervalo):
            #if((len(fecha) > i+1) and (i-1 >= 0)): # Apenas entra na condição caso o inicio seja maior que 0, e o fim menor que o limite.
            S = (array[abre[i]-1]+array[fecha[i]+1])*intervalo/2
            print(S)
            #array[abre[i]+m] = S; # Atualiza o valor
            #print(array[abre[i]+m])
        print('-----')
        
faltadados();
