def diajuliano(dia):
            diasmes = [31 , 28 , 31 , 30 , 31, 30, 31, 31, 30, 31,30, 31];
            mes = 1;
            for m in range(1, 12):
                if(dia - diasmes[m-1] >= 1):
                    dia = dia - diasmes[m-1]
                    mes += 1
                else:
                    #print(format(dia, '02d') + "/" + format(mes, '02d'))
                    return dia;
                    break;
print(diajuliano(56))
