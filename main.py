from tabla import *
from kompjuter import *
from minimax import *
import time

if __name__=="__main__":
    print("Izaberite mod igre: ")
    print("1. Obavezno pojedi")
    print("2. Ne mora da se jede")
    print()
    while True:
        mod=input("Unesite broj: ")
        try:
            mod=int(mod)
            if mod==1 or mod==2:
                break
            else:
                print()
                print("Unesite 1 ili 2!")
                print()
        
        except:
            print()
            print("Unesite broj!")
            print()
    popuni_figurice()

    

    iscrtaj_tablu()
    dubina=5
    while True:


        potez_igrac=pomeri_figuricu(mod)
        iscrtaj_tablu()
        if potez_igrac==0:
            print("Pobedio je igrac X!")
            break
        start=time.time()
        bodovi,potez=algoritam(figurice, dubina, 'X',False,mod,float('-inf'),float('inf'))
        
        print(bodovi,potez)
        if potez==None:
            print("Pobedio je igrac O!")
            break
        rk_novi=potez.split("|")[-1]
        red_novi=int(rk_novi.split("-")[0])
        kolona_nova=int(rk_novi.split("-")[1])
        rk_stari=potez.split("|")[0]
        red_stari=int(rk_stari.split("-")[0])
        kolona_stara=int(rk_stari.split("-")[1])
        if len(potez.split(","))>1:

            skokovi=potez.split(",")
            for skok in skokovi:
                red_stari=int(skok.split("-")[0])
                kolona_stara=int(skok.split("|")[0].split("-")[1])
                red_novi=int(skok.split("|")[1].split("-")[0])
                kolona_nova=int(skok.split("|")[1].split("-")[1])
                if kolona_nova>kolona_stara and red_novi>red_stari:
                    figurice[red_stari+1][kolona_stara+1]=None
                elif kolona_nova>kolona_stara and red_novi<red_stari:
                    figurice[red_stari-1][kolona_stara+1]=None
                elif kolona_nova<kolona_stara and red_novi>red_stari:
                    figurice[red_stari+1][kolona_stara-1]=None
                elif kolona_nova<kolona_stara and red_novi<red_stari:
                    figurice[red_stari-1][kolona_stara-1]=None

                if figurice[red_stari][kolona_stara]=='x' and red_novi==7:
                    figurice[red_stari][kolona_stara]='X'
        else:
            if kolona_nova>kolona_stara and red_novi>red_stari:
                figurice[red_stari+1][kolona_stara+1]=None
            elif kolona_nova>kolona_stara and red_novi<red_stari:
                figurice[red_stari-1][kolona_stara+1]=None
            elif kolona_nova<kolona_stara and red_novi>red_stari:
                figurice[red_stari+1][kolona_stara-1]=None
            elif kolona_nova<kolona_stara and red_novi<red_stari:
                figurice[red_stari-1][kolona_stara-1]=None

        rk_novi=potez.split("|")[-1]
        red_novi=int(rk_novi.split("-")[0])
        kolona_nova=int(rk_novi.split("-")[1])
        rk_stari=potez.split("|")[0]
        red_stari=int(rk_stari.split("-")[0])
        kolona_stara=int(rk_stari.split("-")[1])

        if figurice[red_stari][kolona_stara]=='x' and red_novi==7:
            figurice[red_novi][kolona_nova]='X'
        elif figurice[red_stari][kolona_stara]=='x' and red_novi!=7:
            figurice[red_novi][kolona_nova]='x'
        elif figurice[red_stari][kolona_stara]=='X':
            figurice[red_novi][kolona_nova]='X'
        if red_stari!=red_novi or kolona_stara!=kolona_nova:
            figurice[red_stari][kolona_stara]=None
        end=time.time()
        print("Vreme izvrsavanja: ",end-start)
        iscrtaj_tablu()
        br_o=0
        br_x=0
        for i in range(8):
            for j in range(8):
                if figurice[i][j]=='X' or figurice[i][j]=='x':
                    br_x+=1
                    
                if figurice[i][j]=='O' or figurice[i][j]=='o':
                    br_o+=1
        if br_o+br_x<=5:
            dubina=7
            
        if br_o==0:
            print("Pobedio je igrac X!")
            break
        if br_x==0:
            print("Pobedio je igrac O!")
            break
        
        