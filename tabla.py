from kompjuter import *

figurice=[]
slova=['a','b','c','d','e','f','g','h']
def iscrtaj_tablu():
    print("    1   2   3   4   5   6   7   8")
    print("  ---------------------------------")
    for i in range(8):
        print(slova[i]+" ",end='|')
        for j in range(8):
            if figurice[i][j]==None:
                print('   ',end='|')
            else:
                print(" "+figurice[i][j]+" ",end='|')
        print()
        print("  ---------------------------------")
def popuni_figurice():
    for i in range(8):
        figurice.append([])
        for j in range(8):
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                if i<3:
                    figurice[i].append('x')
                elif i>4:
                    figurice[i].append('o')
                else:
                    figurice[i].append(None)
            else:
                figurice[i].append(None)


def pomeri_figuricu(mod):
    moguci_potezi_figurice=[]
    moguci_potpotezi=[]

    for i in range(8):
        for j in range(8):
            if (figurice[i][j]=='o' or figurice[i][j]=='O') and mod==2:
                if i-1>=0 and j-1>=0 and figurice[i-1][j-1]==None:
                    moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                elif i-2>=0 and j-2>=0 and (figurice[i-1][j-1]=='x' or figurice[i-1][j-1]=='X') and figurice[i-2][j-2]==None:
                    moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                elif i-1>=0 and j+1<8 and figurice[i-1][j+1]==None:
                    moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                elif i-2>=0 and j+2<8 and (figurice[i-1][j+1]=='x' or figurice[i-1][j+1]=='X') and figurice[i-2][j+2]==None:
                    moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                if figurice[i][j]=='O':
                    if i+1<8 and j+1<8 and figurice[i+1][j+1]==None:
                        if slova[i]+"-"+str(j+1) not in moguci_potezi_figurice:
                            moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                    elif i+2<8 and j+2<8 and (figurice[i+1][j+1]=='x' or figurice[i+1][j+1]=='X') and figurice[i+2][j+2]==None:
                        if slova[i]+"-"+str(j+1) not in moguci_potezi_figurice:  
                            moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                    elif i+1<8 and j-1>=0 and figurice[i+1][j-1]==None:
                        if slova[i]+"-"+str(j+1) not in moguci_potezi_figurice:
                            moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                    elif i+2<8 and j-2>=0 and (figurice[i+1][j-1]=='x' or figurice[i+1][j-1]=='X') and figurice[i+2][j-2]==None:
                        if slova[i]+"-"+str(j+1) not in moguci_potezi_figurice:
                            moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                    

            elif (figurice[i][j]=='o' or figurice[i][j]=='O') and mod==1:

                if i-2>=0 and j-2>=0 and (figurice[i-1][j-1]=='x' or figurice[i-1][j-1]=='X') and figurice[i-2][j-2]==None:
                    moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                    
                

                if i-2>=0 and j+2<8 and (figurice[i-1][j+1]=='x' or figurice[i-1][j+1]=='X') and figurice[i-2][j+2]==None:
                    if slova[i]+"-"+str(j+1) not in moguci_potezi_figurice:
                        moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                
                

                if figurice[i][j]=='O':
                    if i+2<8 and j+2<8 and (figurice[i+1][j+1]=='x' or figurice[i+1][j+1]=='X') and figurice[i+2][j+2]==None:
                        if (slova[i]+"-"+str(j+1) not in moguci_potezi_figurice):
                                moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))



                    if i+2<8 and j-2>=0 and (figurice[i+1][j-1]=='x' or figurice[i+1][j-1]=='X') and figurice[i+2][j-2]==None:
                        if slova[i]+"-"+str(j+1) not in moguci_potezi_figurice:
                                moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                    


    if(mod==1):
        if len(moguci_potezi_figurice)==0:
            for i in range(8):
                for j in range(8):
                        if figurice[i][j]=='o' or figurice[i][j]=='O':
                            if i-1>=0 and j-1>=0 and figurice[i-1][j-1]==None:
                                moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                            if i-1>=0 and j+1<8 and figurice[i-1][j+1]==None:
                                if (slova[i]+"-"+str(j+1) not in moguci_potezi_figurice):
                                    moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                            if figurice[i][j]=='O':
                                if i+1<8 and j+1<8 and figurice[i+1][j+1]==None:
                                    if (slova[i]+"-"+str(j+1) not in moguci_potezi_figurice):
                                        moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))
                                if i+1<8 and j-1>=0 and figurice[i+1][j-1]==None:
                                    if (slova[i]+"-"+str(j+1) not in moguci_potezi_figurice):
                                        moguci_potezi_figurice.append(slova[i]+"-"+str(j+1))

                
    if len(moguci_potezi_figurice)==0:
        return 0           
    print("Izaberite figuricu sa kojom zelite da odigrate potez: ")
    print()
    i=1
    for potez in moguci_potezi_figurice:
        print(str(i)+". "+potez)
        i+=1
    while True:
        potez=input("Unesite redni broj poteza: ")
        try:
            potez=int(potez)
            potez-=1
            if potez<0 or potez>=len(moguci_potezi_figurice):
                print()
                print("Uneli ste pogresan broj!")
                print()
                continue
            break
        except:
            print()
            print("Unesite broj!")
            print()
    
    red_kolona=moguci_potezi_figurice[potez].split('-')
    red_kolona[1]=int(red_kolona[1])
    red_kolona[1]-=1
    for slovo in slova:
        if red_kolona[0]==slovo:
            red_kolona[0]=slova.index(slovo)
            break

    if mod==1:
        if figurice[red_kolona[0]][red_kolona[1]]=='o' or figurice[red_kolona[0]][red_kolona[1]]=='O':

            if red_kolona[0]-2>=0 and red_kolona[1]-2>=0 and (figurice[red_kolona[0]-1][red_kolona[1]-1]=='x' or figurice[red_kolona[0]-1][red_kolona[1]-1]=='X'):
                if figurice[red_kolona[0]-2][red_kolona[1]-2]==None:
                    s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]-2,red_kolona[1]-2,figurice)
                    potezi=s.split("/")
                    for i in range(len(potezi)-1):
                        potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]-2)+"-"+str(red_kolona[1]-2)+","+potezi[i]
                        if potez not in moguci_potpotezi:
                            moguci_potpotezi.append(potez)
                    # moguci_potpotezi.append(slova[red_kolona[0]-2]+"-"+str(red_kolona[1]-2+1))
           
            if red_kolona[0]-2>=0 and red_kolona[1]+2<8 and (figurice[red_kolona[0]-1][red_kolona[1]+1]=='x' or figurice[red_kolona[0]-1][red_kolona[1]+1]=='X'):
                if figurice[red_kolona[0]-2][red_kolona[1]+2]==None:
                    #moguci_potpotezi.append(slova[red_kolona[0]-2]+"-"+str(red_kolona[1]+2+1))
                    s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]-2,red_kolona[1]+2,figurice)
                    potezi=s.split("/")
                    for i in range(len(potezi)-1):
                        potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]-2)+"-"+str(red_kolona[1]+2)+","+potezi[i]
                        if potez not in moguci_potpotezi:
                            moguci_potpotezi.append(potez)


           
        
        if figurice[red_kolona[0]][red_kolona[1]]=='O':

            if red_kolona[0]+2<8 and red_kolona[1]-2>=0 and (figurice[red_kolona[0]+1][red_kolona[1]-1]=='x' or figurice[red_kolona[0]+1][red_kolona[1]-1]=='X'):
                if figurice[red_kolona[0]+2][red_kolona[1]-2]==None:
                   
                    s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]+2,red_kolona[1]-2,figurice)
                    potezi=s.split("/")
                    for i in range(len(potezi)-1):
                        potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]+2)+"-"+str(red_kolona[1]-2)+","+potezi[i]
                        if potez not in moguci_potpotezi:
                            moguci_potpotezi.append(potez)
            
            if red_kolona[0]+2<8 and red_kolona[1]+2<8 and (figurice[red_kolona[0]+1][red_kolona[1]+1]=='x' or figurice[red_kolona[0]+1][red_kolona[1]+1]=='X'):
                if figurice[red_kolona[0]+2][red_kolona[1]+2]==None:
                    
                    s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]+2,red_kolona[1]+2,figurice)
                    potezi=s.split("/")
                    for i in range(len(potezi)-1):
                        potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]+2)+"-"+str(red_kolona[1]+2)+","+potezi[i]
                        if potez not in moguci_potpotezi:
                            moguci_potpotezi.append(potez)
           
        if len(moguci_potpotezi)==0:
            if red_kolona[0]-1>=0 and red_kolona[1]+1<8 and figurice[red_kolona[0]-1][red_kolona[1]+1]==None:
                moguci_potpotezi.append(slova[red_kolona[0]-1]+"-"+str(red_kolona[1]+1+1))
            if red_kolona[0]-1>=0 and red_kolona[1]-1>=0 and figurice[red_kolona[0]-1][red_kolona[1]-1]==None:
                moguci_potpotezi.append(slova[red_kolona[0]-1]+"-"+str(red_kolona[1]-1+1))
            if figurice[red_kolona[0]][red_kolona[1]]=='O':
                if red_kolona[0]+1<8 and red_kolona[1]-1>=0 and figurice[red_kolona[0]+1][red_kolona[1]-1]==None:
                    moguci_potpotezi.append(slova[red_kolona[0]+1]+"-"+str(red_kolona[1]-1+1))
                if red_kolona[0]+1<8 and red_kolona[1]+1<8 and figurice[red_kolona[0]+1][red_kolona[1]+1]==None:
                    moguci_potpotezi.append(slova[red_kolona[0]+1]+"-"+str(red_kolona[1]+1+1))
    if mod==2:
        if figurice[red_kolona[0]][red_kolona[1]]=='o' or figurice[red_kolona[0]][red_kolona[1]]=='O':
            if red_kolona[0]-1>=0 and red_kolona[1]-1>=0 and figurice[red_kolona[0]-1][red_kolona[1]-1]==None:
                moguci_potpotezi.append(slova[red_kolona[0]-1]+"-"+str(red_kolona[1]-1+1))
            
            if red_kolona[0]-2>=0 and red_kolona[1]-2>=0 and (figurice[red_kolona[0]-1][red_kolona[1]-1]=='x' or figurice[red_kolona[0]-1][red_kolona[1]-1]=='X') and figurice[red_kolona[0]-2][red_kolona[1]-2]==None:
                
                s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]-2,red_kolona[1]-2,figurice)
                potezi=s.split("/")
                for i in range(len(potezi)-1):
                    potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]-2)+"-"+str(red_kolona[1]-2)+","+potezi[i]
                    if potez not in moguci_potpotezi:
                        moguci_potpotezi.append(potez)

            if red_kolona[0]-1>=0 and red_kolona[1]+1<8 and figurice[red_kolona[0]-1][red_kolona[1]+1]==None:
                moguci_potpotezi.append(slova[red_kolona[0]-1]+"-"+str(red_kolona[1]+1+1))
            if red_kolona[0]-2>=0 and red_kolona[1]+2<8 and (figurice[red_kolona[0]-1][red_kolona[1]+1]=='x' or figurice[red_kolona[0]-1][red_kolona[1]+1]=='X') and figurice[red_kolona[0]-2][red_kolona[1]+2]==None:
                
                s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]-2,red_kolona[1]+2,figurice)
                potezi=s.split("/")
                for i in range(len(potezi)-1):
                    potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]-2)+"-"+str(red_kolona[1]+2)+","+potezi[i]
                    if potez not in moguci_potpotezi:
                        moguci_potpotezi.append(potez)
           
            if figurice[red_kolona[0]][red_kolona[1]]=='O':
                if red_kolona[0]+1<8 and red_kolona[1]-1>=0 and figurice[red_kolona[0]+1][red_kolona[1]-1]==None:
                    moguci_potpotezi.append(slova[red_kolona[0]+1]+"-"+str(red_kolona[1]-1+1))
                
                if red_kolona[0]+2<8 and red_kolona[1]-2>=0 and (figurice[red_kolona[0]+1][red_kolona[1]-1]=='x' or figurice[red_kolona[0]+1][red_kolona[1]-1]=='X') and figurice[red_kolona[0]+2][red_kolona[1]-2]==None:
                    
                    s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]+2,red_kolona[1]-2,figurice)
                    potezi=s.split("/")
                    for i in range(len(potezi)-1):
                        potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]+2)+"-"+str(red_kolona[1]-2)+","+potezi[i]
                        if potez not in moguci_potpotezi:
                            moguci_potpotezi.append(potez)

                if red_kolona[0]+1<8 and red_kolona[1]+1<8 and figurice[red_kolona[0]+1][red_kolona[1]+1]==None:
                    moguci_potpotezi.append(slova[red_kolona[0]+1]+"-"+str(red_kolona[1]+1+1))
                
                if red_kolona[0]+2<8 and red_kolona[1]+2<8 and (figurice[red_kolona[0]+1][red_kolona[1]+1]=='x' or figurice[red_kolona[0]+1][red_kolona[1]+1]=='X') and figurice[red_kolona[0]+2][red_kolona[1]+2]==None:
                    
                    s=kompjuter_potez_2(red_kolona[0],red_kolona[1],red_kolona[0]+2,red_kolona[1]+2,figurice)
                    potezi=s.split("/")
                    for i in range(len(potezi)-1):
                        potez=str(red_kolona[0])+"-"+str(red_kolona[1])+"|"+str(red_kolona[0]+2)+"-"+str(red_kolona[1]+2)+","+potezi[i]
                        if potez not in moguci_potpotezi:
                            moguci_potpotezi.append(potez)
                
    iscrtaj_tablu()
    
    
    print("Izaberite potez: ")
    print()
    i=1
    for potez in moguci_potpotezi:
        potez=obrada_poteza(potez)
        if len(potez.split(","))>1:
            print(str(i)+". "+ potez)
        elif len(potez.split("|"))>1:           
            print(str(i)+". "+potez.split("|")[1])
        else:
            print(str(i)+". "+potez)
        i+=1
    while True:
        try:
            izbor=int(input("Unesite redni broj poteza: "))
            izbor-=1
            if izbor<0 or izbor>=len(moguci_potpotezi):
                print()
                print("Unesite odgovarajuci broj")
                print()
                continue
            break
        except:
            print()
            print("Unesite broj!")
            print()
    potez=obrada_poteza(moguci_potpotezi[izbor])
    rk_novi=potez.split("|")[-1]
    red_kolona_novi=rk_novi.split("-")
    red_kolona_novi[0]=slova.index(red_kolona_novi[0])
    red_kolona_novi[1]=int(red_kolona_novi[1])-1
    skokovi=potez.split(",")
    if len(skokovi)>1:
        for skok in skokovi:
            red_stari=slova.index(skok.split("-")[0])
            kolona_stara=int(skok.split("|")[0].split("-")[1])-1
            red_novi=slova.index(skok.split("|")[1].split("-")[0])
            kolona_nova=int(skok.split("|")[1].split("-")[1])-1
            if kolona_nova>kolona_stara and red_novi>red_stari:
                figurice[red_stari+1][kolona_stara+1]=None
            elif kolona_nova>kolona_stara and red_novi<red_stari:
                figurice[red_stari-1][kolona_stara+1]=None
            elif kolona_nova<kolona_stara and red_novi>red_stari:
                figurice[red_stari+1][kolona_stara-1]=None
            elif kolona_nova<kolona_stara and red_novi<red_stari:
                figurice[red_stari-1][kolona_stara-1]=None
            if figurice[red_stari][kolona_stara]=='o' and red_novi==0:
                figurice[red_stari][kolona_stara]='O' # dole u kodu se proverava da li je dama pa pa se stavlja na O ali posto se preskace prvi red nece mi se pretvoriti u O pa mora ovde
    else:
        
        if red_kolona_novi[1]>red_kolona[1] and red_kolona_novi[0]>red_kolona[0]:
            figurice[red_kolona[0]+1][red_kolona[1]+1]=None
        elif red_kolona_novi[1]>red_kolona[1] and red_kolona_novi[0]<red_kolona[0]:
            figurice[red_kolona[0]-1][red_kolona[1]+1]=None
        elif red_kolona_novi[1]<red_kolona[1] and red_kolona_novi[0]>red_kolona[0]:
            figurice[red_kolona[0]+1][red_kolona[1]-1]=None
        elif red_kolona_novi[1]<red_kolona[1] and red_kolona_novi[0]<red_kolona[0]:
            figurice[red_kolona[0]-1][red_kolona[1]-1]=None

    


    if figurice[red_kolona[0]][red_kolona[1]]=='O':
        figurice[red_kolona_novi[0]][red_kolona_novi[1]]='O'
    else:
        figurice[red_kolona_novi[0]][red_kolona_novi[1]]='o'
    if red_kolona[0]!=red_kolona_novi[0] or red_kolona[1]!=red_kolona_novi[1]:
        figurice[red_kolona[0]][red_kolona[1]]=None
    if red_kolona_novi[0]==0 and figurice[red_kolona_novi[0]][red_kolona_novi[1]]=='o':
        figurice[red_kolona_novi[0]][red_kolona_novi[1]]='O'

    

            

