import copy
slova=['a','b','c','d','e','f','g','h']
def kompjuter_potez(mod,figurice):
    moguci_potezi=[]
    for i in range(8):
        for j in range(8):
            if (figurice[i][j]=='x' or figurice[i][j]=='X') and mod==2:

                if i+1<8 and j-1>=0 and figurice[i+1][j-1]==None:
                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j-1))
                if i+2<8 and j-2>=0 and (figurice[i+1][j-1]=='o' or figurice[i+1][j-1]=='O') and figurice[i+2][j-2]==None:
                    
                    s=kompjuter_potez_2(i,j,i+2,j-2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j-2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)

                if i+1<8 and j+1<8 and figurice[i+1][j+1]==None:
                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j+1))
                if i+2<8 and j+2<8 and (figurice[i+1][j+1]=='o' or figurice[i+1][j+1]=='O') and figurice[i+2][j+2]==None:
                    
                    s=kompjuter_potez_2(i,j,i+2,j+2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j+2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)

                if figurice[i][j]=='X':
                    if i-1>=0 and j+1<8 and figurice[i-1][j+1]==None:
                        moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j+1))
                    if i-2>=0 and j+2<8 and (figurice[i-1][j+1]=='o' or figurice[i-1][j+1]=='O') and figurice[i-2][j+2]==None:
                        
                        s=kompjuter_potez_2(i,j,i-2,j+2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j+2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)

                    if i-1>=0 and j-1>=0 and figurice[i-1][j-1]==None:
                        moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j-1))
                    if i-2>=0 and j-2>=0 and (figurice[i-1][j-1]=='o' or figurice[i-1][j-1]=='O') and figurice[i-2][j-2]==None:
                        
                        s=kompjuter_potez_2(i,j,i-2,j-2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j-2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)
                    

            elif (figurice[i][j]=='x' or figurice[i][j]=='X') and mod==1:

                if i+2<8 and j-2>=0 and (figurice[i+1][j-1]=='o' or figurice[i+1][j-1]=='O') and figurice[i+2][j-2]==None:
                    

                    s=kompjuter_potez_2(i,j,i+2,j-2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j-2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)
                

                if i+2<8 and j+2<8 and (figurice[i+1][j+1]=='o' or figurice[i+1][j+1]=='O') and figurice[i+2][j+2]==None:
                    
                    
                    s=kompjuter_potez_2(i,j,i+2,j+2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j+2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)
                

                if figurice[i][j]=='X':
                    if i-2>=0 and j+2<8 and (figurice[i-1][j+1]=='o' or figurice[i-1][j+1]=='O') and figurice[i-2][j+2]==None:
                       

                        s=kompjuter_potez_2(i,j,i-2,j+2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j+2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)


                    if i-2>=0 and j-2>=0 and (figurice[i-1][j-1]=='o' or figurice[i-1][j-1]=='O') and figurice[i-2][j-2]==None:
                        

                        s=kompjuter_potez_2(i,j,i-2,j-2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j-2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)


    if(mod==1):
        if len(moguci_potezi)==0:
            for i in range(8):
                for j in range(8):
                        if figurice[i][j]=='x' or figurice[i][j]=='X':
                            if i+1<8 and j-1>=0 and figurice[i+1][j-1]==None:
                                moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j-1))
                            if i+1<8 and j+1<8 and figurice[i+1][j+1]==None:
                                moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j+1))
                            if figurice[i][j]=='X':
                                if i-1>=0 and j+1<8 and figurice[i-1][j+1]==None:
                                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j+1))
                                if i-1>=0 and j-1>=0 and figurice[i-1][j-1]==None:
                                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j-1))

    i=0
    while i<len(moguci_potezi):#izbacujem zarez na kraju svakog poteza
        if len(moguci_potezi[i].split(","))>1:
            pomocna=moguci_potezi[i]
            moguci_potezi[i]=pomocna[:len(pomocna)-1]
        i+=1
    return moguci_potezi


def igrac_potez(mod,figurice):
    moguci_potezi=[]
    for i in range(8):
        for j in range(8):
            if (figurice[i][j]=='o' or figurice[i][j]=='O') and mod==2:

                if i-1>=0 and j+1<8 and figurice[i-1][j+1]==None:
                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j+1))
                elif i-2>=0 and j+2<8 and (figurice[i-1][j+1]=='X' or figurice[i-1][j+1]=='x') and figurice[i-2][j+2]==None:
                    
                    s=kompjuter_potez_2(i,j,i-2,j+2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j+2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)

                if i-1>=0 and j-1>=0 and figurice[i-1][j-1]==None:
                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j-1))
                elif i-2>=0 and j-2>=0 and (figurice[i-1][j-1]=='x' or figurice[i-1][j-1]=='X') and figurice[i-2][j-2]==None:
                    
                    s=kompjuter_potez_2(i,j,i-2,j-2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j-2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)

                if figurice[i][j]=='O':
                    if i+1<8 and j-1>=0 and figurice[i+1][j-1]==None:
                        moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j-1))
                    elif i+2<8 and j-2>=0 and (figurice[i+1][j-1]=='x' or figurice[i+1][j-1]=='X') and figurice[i+2][j-2]==None:
                        
                        s=kompjuter_potez_2(i,j,i+2,j-2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j-2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)

                    if i+1<8 and j+1<8 and figurice[i+1][j+1]==None:
                        moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j+1))
                    elif i+2<8 and j+2<8 and (figurice[i+1][j+1]=='x' or figurice[i+1][j+1]=='X') and figurice[i+2][j+2]==None:
                       
                        s=kompjuter_potez_2(i,j,i+2,j+2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j+2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)
                    

            elif (figurice[i][j]=='o' or figurice[i][j]=='O') and mod==1:

                if i-2>=0 and j+2<8 and (figurice[i-1][j+1]=='x' or figurice[i-1][j+1]=='X') and figurice[i-2][j+2]==None:
                 

                    s=kompjuter_potez_2(i,j,i-2,j+2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j+2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)
                

                if i-2>=0 and j-2>=0 and (figurice[i-1][j-1]=='x' or figurice[i-1][j-1]=='X') and figurice[i-2][j-2]==None:
                 

                    s=kompjuter_potez_2(i,j,i-2,j-2,figurice)
                    potezi=s.split("/")
                    for z in range(len(potezi)-1):
                        potez=str(i)+"-"+str(j)+"|"+str(i-2)+"-"+str(j-2)+","+potezi[z]
                        if potez not in moguci_potezi:
                            moguci_potezi.append(potez)
                

                if figurice[i][j]=='O':
                    if i+2<8 and j-2>=0 and (figurice[i+1][j-1]=='x' or figurice[i+1][j-1]=='X') and figurice[i+2][j-2]==None:
                    

                        s=kompjuter_potez_2(i,j,i+2,j-2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j-2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)


                    if i+2<8 and j+2<8 and (figurice[i+1][j+1]=='x' or figurice[i+1][j+1]=='X') and figurice[i+2][j+2]==None:
                      

                        s=kompjuter_potez_2(i,j,i+2,j+2,figurice)
                        potezi=s.split("/")
                        for z in range(len(potezi)-1):
                            potez=str(i)+"-"+str(j)+"|"+str(i+2)+"-"+str(j+2)+","+potezi[z]
                            if potez not in moguci_potezi:
                                moguci_potezi.append(potez)
                    


    if(mod==1):
        if len(moguci_potezi)==0:
            for i in range(8):
                for j in range(8):
                        if figurice[i][j]=='o' or figurice[i][j]=='O':
                            if i-1>=0 and j+1<8 and figurice[i-1][j+1]==None:
                                moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j+1))
                            if i-1>=0 and j-1>=0 and figurice[i-1][j-1]==None:
                                moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i-1)+"-"+str(j-1))
                            if figurice[i][j]=='O':
                                if i+1<8 and j-1>=0 and figurice[i+1][j-1]==None:
                                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j-1))
                                if i+1<8 and j+1<8 and figurice[i+1][j+1]==None:
                                    moguci_potezi.append(str(i)+"-"+str(j)+"|"+str(i+1)+"-"+str(j+1))
    i=0
    while i<len(moguci_potezi):#izbacujem zarez na kraju svakog poteza
        if len(moguci_potezi[i].split(","))>1:
            pomocna=moguci_potezi[i]
            moguci_potezi[i]=pomocna[:len(pomocna)-1]
        i+=1


    return moguci_potezi
def procena_stanja_table(figurice):
    x_figurice=0
    o_figurice=0
    x_vrednost=0
    o_vrednost=0
    for i in range(8):
        for j in range(8):
            if figurice[i][j]=='x' or figurice[i][j]=='X':
                x_figurice+=1
            elif figurice[i][j]=='o' or figurice[i][j]=='O':
                o_figurice+=1
            if figurice[i][j]=='X':
                x_vrednost+=100
            elif figurice[i][j]=='x':
                x_vrednost+=50
            if figurice[i][j]=='O':
                o_vrednost+=100
            elif figurice[i][j]=='o':
                o_vrednost+=50
            if i==3 and j==4:
                if figurice[i][j]=='X':
                    x_vrednost+=10
                elif figurice[i][j]=='x':
                    x_vrednost+=5
                if figurice[i][j]=='O':
                    o_vrednost+=10
                elif figurice[i][j]=='o':
                    o_vrednost+=5
            elif i==4 and j==3:
                if figurice[i][j]=='X':
                    x_vrednost+=10
                elif figurice[i][j]=='x':
                    x_vrednost+=5
                if figurice[i][j]=='O':
                    o_vrednost+=10
                elif figurice[i][j]=='o':
                    o_vrednost+=5
            elif (i==0 and j==0) or( i==0 and j==7) or (i==7 and j==0) or (i==7 and j==7):
                if figurice[i][j]=='X':
                    x_vrednost-=10
                elif figurice[i][j]=='x':
                    x_vrednost-=5
                if figurice[i][j]=='O':
                    o_vrednost-=10
                elif figurice[i][j]=='o':
                    o_vrednost-=5
            if i==0 and not(j==0 or j==7):
                if figurice[i][j]=='X':
                    x_vrednost+=4
                elif figurice[i][j]=='x':
                    x_vrednost+=2
                if figurice[i][j]=='O':
                    o_vrednost+=4
                elif figurice[i][j]=='o':
                    o_vrednost+=2
            if i==7 and not(j==0 or j==7):
                if figurice[i][j]=='X':
                    x_vrednost+=4
                elif figurice[i][j]=='x':
                    x_vrednost+=2
                if figurice[i][j]=='O':
                    o_vrednost+=4
                elif figurice[i][j]=='o':
                    o_vrednost+=2
            if j==0 and not(i==0 or i==7):
                if figurice[i][j]=='X':
                    x_vrednost+=4
                elif figurice[i][j]=='x':
                    x_vrednost+=2
                if figurice[i][j]=='O':
                    o_vrednost+=4
                elif figurice[i][j]=='o':
                    o_vrednost+=2
            if j==7 and not(i==0 or i==7):
                if figurice[i][j]=='X':
                    x_vrednost+=4
                elif figurice[i][j]=='x':
                    x_vrednost+=2
                if figurice[i][j]=='O':
                    o_vrednost+=4
                elif figurice[i][j]=='o':
                    o_vrednost+=2
            if figurice[i][j]=='x' and i>3:
                x_vrednost+=5
            if figurice[i][j]=='o' and i<4:
                o_vrednost+=5
            if figurice[i][j]=='x' and i>5:
                x_vrednost+=10
            if figurice[i][j]=='o' and i<2:
                o_vrednost+=10
            if i-1>=0 and j-1>=0 and (figurice[i-1][j-1]=='x' or figurice[i-1][j-1]=='X') and (figurice[i][j]=='X'or figurice[i][j]=='x'):
                x_vrednost+=5
            if i-1>=0 and j+1<8 and (figurice[i-1][j+1]=='x' or figurice[i-1][j+1]=='X') and (figurice[i][j]=='X'or figurice[i][j]=='x'):
                x_vrednost+=5
            if i+1<8 and j-1>=0 and (figurice[i+1][j-1]=='o' or figurice[i+1][j-1]=='O') and (figurice[i][j]=='O'or figurice[i][j]=='o'):
                o_vrednost+=5
            if i+1<8 and j+1<8 and (figurice[i+1][j+1]=='o' or figurice[i+1][j+1]=='O')and (figurice[i][j]=='O'or figurice[i][j]=='o'):
                o_vrednost+=5

        
    konacna_vrednost=x_vrednost-o_vrednost
    kraj=False
    if x_figurice==0 or o_figurice==0:
        kraj=True
    if x_figurice==0:
        konacna_vrednost=float('-inf')
    elif o_figurice==0:
        konacna_vrednost=float('inf')
    return konacna_vrednost,kraj

def simuliraj_potez(red_stari,kolona_stara,red_novi,kolona_nova,figurice):
    figurice2=copy.deepcopy(figurice)
    if figurice2[red_stari][kolona_stara]=='x' and red_novi==7:
        figurice2[red_novi][kolona_nova]='X'
    elif figurice2[red_stari][kolona_stara]=='x' and red_novi!=7:
        figurice2[red_novi][kolona_nova]='x'
    elif figurice2[red_stari][kolona_stara]=='X':
        figurice2[red_novi][kolona_nova]='X'
    if figurice2[red_stari][kolona_stara]=='o' and red_novi==0:
        figurice2[red_novi][kolona_nova]='O'
    elif figurice2[red_stari][kolona_stara]=='o' and red_novi!=0:
        figurice2[red_novi][kolona_nova]='o'
    elif figurice2[red_stari][kolona_stara]=='O':
        figurice2[red_novi][kolona_nova]='O'
    if red_stari!=red_novi or kolona_stara!=kolona_nova:
        figurice2[red_stari][kolona_stara]=None
    if abs(red_novi-red_stari)==2:
        if red_novi>red_stari and kolona_nova>kolona_stara:
            figurice2[red_stari+1][kolona_stara+1]=None
        elif red_novi>red_stari and kolona_nova<kolona_stara:
            figurice2[red_stari+1][kolona_stara-1]=None
        elif red_novi<red_stari and kolona_nova>kolona_stara:
            figurice2[red_stari-1][kolona_stara+1]=None
        elif red_novi<red_stari and kolona_nova<kolona_stara:
            figurice2[red_stari-1][kolona_stara-1]=None
    return figurice2
            
def simuliraj_potez_visetruko(potez,figurice):
    figurice2=copy.deepcopy(figurice)
    rk_novi=potez.split("|")[-1]
    red_novi=int(rk_novi.split("-")[0])
    kolona_nova=int(rk_novi.split("-")[1])
    rk_stari=potez.split("|")[0]
    red_stari=int(rk_stari.split("-")[0])
    kolona_stara=int(rk_stari.split("-")[1])
    skokovi=potez.split(",")
    if len(skokovi)>1:
        for skok in skokovi:
            red_stari=int(skok.split("-")[0])
            kolona_stara=int(skok.split("|")[0].split("-")[1])
            red_novi=int(skok.split("|")[1].split("-")[0])
            kolona_nova=int(skok.split("|")[1].split("-")[1])
            if kolona_nova>kolona_stara and red_novi>red_stari:
                figurice2[red_stari+1][kolona_stara+1]=None
            elif kolona_nova>kolona_stara and red_novi<red_stari:
                figurice2[red_stari-1][kolona_stara+1]=None
            elif kolona_nova<kolona_stara and red_novi>red_stari:
                figurice2[red_stari+1][kolona_stara-1]=None
            elif kolona_nova<kolona_stara and red_novi<red_stari:
                figurice2[red_stari-1][kolona_stara-1]=None
            if figurice2[red_stari][kolona_stara]=='o' and red_novi==0:
                figurice2[red_stari][kolona_stara]='O' 
            elif figurice2[red_stari][kolona_stara]=='x' and red_novi==7:
                figurice2[red_stari][kolona_stara]='X'
    else:
        
        if kolona_nova>kolona_stara and red_novi>red_stari:
            figurice2[red_stari+1][kolona_stara+1]=None
        elif kolona_nova>kolona_stara and red_novi<red_stari:
            figurice2[red_stari-1][kolona_stara+1]=None
        elif kolona_nova<kolona_stara and red_novi>red_stari:
            figurice2[red_stari+1][kolona_stara-1]=None
        elif kolona_nova<kolona_stara and red_novi<red_stari:
            figurice2[red_stari-1][kolona_stara-1]=None
    
    rk_novi=potez.split("|")[-1]
    red_novi=int(rk_novi.split("-")[0])
    kolona_nova=int(rk_novi.split("-")[1])
    rk_stari=potez.split("|")[0]
    red_stari=int(rk_stari.split("-")[0])
    kolona_stara=int(rk_stari.split("-")[1])

    if figurice2[red_stari][kolona_stara]=='x' and red_novi==7:
        figurice2[red_novi][kolona_nova]='X'
    elif figurice2[red_stari][kolona_stara]=='x' and red_novi!=7:
        figurice2[red_novi][kolona_nova]='x'
    elif figurice2[red_stari][kolona_stara]=='X':
        figurice2[red_novi][kolona_nova]='X'
    if figurice2[red_stari][kolona_stara]=='o' and red_novi==0:
        figurice2[red_novi][kolona_nova]='O'
    elif figurice2[red_stari][kolona_stara]=='o' and red_novi!=0:
        figurice2[red_novi][kolona_nova]='o'
    elif figurice2[red_stari][kolona_stara]=='O':
        figurice2[red_novi][kolona_nova]='O'
    if red_stari!=red_novi or kolona_stara!=kolona_nova:
        figurice2[red_stari][kolona_stara]=None
    return figurice2

def kompjuter_potez_2(red_stari,kolona_stara,red_novi,kolona_nova,figurice):
    figurice2=simuliraj_potez(red_stari,kolona_stara,red_novi,kolona_nova,figurice)

    if abs(red_novi-red_stari)==2:
        s=''
        brojac=0
        if red_novi+2<8 and kolona_nova+2<8   and figurice2[red_novi][kolona_nova]=="O" and  (figurice2[red_novi+1][kolona_nova+1]=='x' or figurice2[red_novi+1][kolona_nova+1]=='X') and figurice2[red_novi+2][kolona_nova+2]==None:
            brojac+=1
            
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi+2,kolona_nova+2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi+2)+"-"+str(kolona_nova+2)+','+raskrsnica[i]+'/'
        if red_novi+2<8 and kolona_nova-2>=0  and figurice2[red_novi][kolona_nova]=="O" and (figurice2[red_novi+1][kolona_nova-1]=='x' or figurice2[red_novi+1][kolona_nova-1]=='X') and figurice2[red_novi+2][kolona_nova-2]==None:
            brojac+=1
            
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi+2,kolona_nova-2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi+2)+"-"+str(kolona_nova-2)+','+raskrsnica[i]+'/'

        if red_novi-2>=0 and kolona_nova+2<8  and (figurice2[red_novi][kolona_nova]=="o" or figurice2[red_novi][kolona_nova]=="O") and(figurice2[red_novi-1][kolona_nova+1]=='x' or figurice2[red_novi-1][kolona_nova+1]=='X') and figurice2[red_novi-2][kolona_nova+2]==None:
            brojac+=1
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi-2,kolona_nova+2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                    s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi-2)+"-"+str(kolona_nova+2)+','+raskrsnica[i]+'/'
           
        if red_novi-2>=0 and kolona_nova-2>=0  and (figurice2[red_novi][kolona_nova]=="o" or figurice2[red_novi][kolona_nova]=="O") and (figurice2[red_novi-1][kolona_nova-1]=='x' or figurice2[red_novi-1][kolona_nova-1]=='X') and figurice2[red_novi-2][kolona_nova-2]==None:
            brojac+=1
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi-2,kolona_nova-2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi-2)+"-"+str(kolona_nova-2)+','+raskrsnica[i]+'/'


        if red_novi+2<8 and kolona_nova+2<8   and (figurice2[red_novi][kolona_nova]=="x" or figurice2[red_novi][kolona_nova]=="X") and  (figurice2[red_novi+1][kolona_nova+1]=='o' or figurice2[red_novi+1][kolona_nova+1]=='O') and figurice2[red_novi+2][kolona_nova+2]==None:
            brojac+=1
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi+2,kolona_nova+2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi+2)+"-"+str(kolona_nova+2)+','+raskrsnica[i]+'/'

        if red_novi+2<8 and kolona_nova-2>=0  and (figurice2[red_novi][kolona_nova]=="x" or figurice2[red_novi][kolona_nova]=="X") and (figurice2[red_novi+1][kolona_nova-1]=='o' or figurice2[red_novi+1][kolona_nova-1]=='O') and figurice2[red_novi+2][kolona_nova-2]==None:
            brojac+=1
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi+2,kolona_nova-2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi+2)+"-"+str(kolona_nova-2)+','+raskrsnica[i]+'/'

        if red_novi-2>=0 and kolona_nova+2<8  and figurice2[red_novi][kolona_nova]=="X" and(figurice2[red_novi-1][kolona_nova+1]=='O' or figurice2[red_novi-1][kolona_nova+1]=='o') and figurice2[red_novi-2][kolona_nova+2]==None:
            brojac+=1
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi-2,kolona_nova+2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi-2)+"-"+str(kolona_nova+2)+','+raskrsnica[i]+'/'

        if red_novi-2>=0 and kolona_nova-2>=0  and figurice2[red_novi][kolona_nova]=="X" and (figurice2[red_novi-1][kolona_nova-1]=='o' or figurice2[red_novi-1][kolona_nova-1]=='O') and figurice2[red_novi-2][kolona_nova-2]==None:
            brojac+=1
            raskrsnica=(kompjuter_potez_2(red_novi,kolona_nova,red_novi-2,kolona_nova-2,figurice2)).split("/")
            for i in range(len(raskrsnica)-1):
                s=s+str(red_novi)+"-"+str(kolona_nova)+"|"+str(red_novi-2)+"-"+str(kolona_nova-2)+','+raskrsnica[i]+'/'
        if brojac==0:
            return s+"/"
        else:
            return s
def obrada_poteza(s):
    potezi=s.split(',')
    if len(potezi)==1:
        return s
    potez_obradjen=''
    for potez in potezi:
        if potez!='':
            red_stari=int(potez.split("-")[0])
            kolona_stara=int(potez.split('-')[1].split("|")[0])
            red_novi=int(potez.split("-")[1].split("|")[1])
            kolona_nova=int(potez.split("-")[2])
            s=slova[red_stari]+"-"+str(kolona_stara+1)+"|"+slova[red_novi]+"-"+str(kolona_nova+1)
            potez_obradjen=potez_obradjen+s+','
    return potez_obradjen[:len(potez_obradjen)-1]
        