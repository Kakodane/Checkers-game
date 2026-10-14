from kompjuter import *

def algoritam(figurice, dubina, igrac,kraj,mod,alfa,beta):
    if dubina==0 or kraj:
        return procena_stanja_table(figurice)[0],None
    if igrac=='X':
        izabran_potez=None
        trenutna_vrednost=float('-inf')
        najbolja_vrednost=alfa
        najgora_vrednost=beta
        moguci_potezi=[]
        moguci_potezi=kompjuter_potez(mod,figurice)
        if len(moguci_potezi)==0:
            return float('inf'),None
        for potez in moguci_potezi:
            if len(potez.split(","))==1:
                red_stari=int(potez.split("-")[0])
                kolona_stara=int(potez.split('-')[1].split("|")[0])
                red_novi=int(potez.split("-")[1].split("|")[1])
                kolona_nova=int(potez.split("-")[2])
                figurice2=simuliraj_potez(red_stari,kolona_stara,red_novi,kolona_nova,figurice)
            else:
                figurice2=simuliraj_potez_visetruko(potez,figurice)
            privremena_vrednost,kraj=procena_stanja_table(figurice2)
            vrednost,_=algoritam(figurice2,dubina-1,'O',kraj,mod,najbolja_vrednost,najgora_vrednost)
            if vrednost>trenutna_vrednost:
                trenutna_vrednost=vrednost
                if vrednost>najbolja_vrednost:
                    najbolja_vrednost=vrednost
                izabran_potez=potez
                if vrednost>=najgora_vrednost:
                    break
        return trenutna_vrednost,izabran_potez
    else:
        trenutna_vrednost=float('inf')
        najbolja_vrednost=beta
        najgora_vrednost=alfa
        izabran_potez=None
        moguci_potezi=[]
        moguci_potezi=igrac_potez(mod,figurice)
        if len(moguci_potezi)==0:
            return float('-inf'),None
        for potez in moguci_potezi:
            if len(potez.split(","))==1:
                red_stari=int(potez.split("-")[0])
                kolona_stara=int(potez.split('-')[1].split("|")[0])
                red_novi=int(potez.split("-")[1].split("|")[1])
                kolona_nova=int(potez.split("-")[2])
                figurice2=simuliraj_potez(red_stari,kolona_stara,red_novi,kolona_nova,figurice)
            else:
                figurice2=simuliraj_potez_visetruko(potez,figurice)
            privremena_vrednost,kraj=procena_stanja_table(figurice2)
            vrednost,_=algoritam(figurice2,dubina-1,'X',kraj,mod,najgora_vrednost,najbolja_vrednost)
            if vrednost<trenutna_vrednost:
                trenutna_vrednost=vrednost
                if vrednost<najbolja_vrednost:
                    najbolja_vrednost=vrednost
                izabran_potez=potez
                if vrednost<=najgora_vrednost:
                    break
        return trenutna_vrednost,izabran_potez

