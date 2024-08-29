from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett(self._lag_tom_rad())

    def _lag_tom_rad(self):
        innvendig_liste = []
        for  i in range(self._ant_kolonner):
            innvendig_liste.append(None)
        return innvendig_liste

    def _lag_tomt_rutenett(self, liste):
        utvendig_liste = []
        for  i in range(self._ant_rader):
            utvendig_liste.append(self._lag_tom_rad())
        return utvendig_liste

    def fyll_med_tilfeldige_celler(self):
        for kol in range(self._ant_kolonner):
            for rad in range(self._ant_rader):
                self.lag_celle(rad, kol)

    def lag_celle(self, rad, kol):
        celle_instans = Celle()
        randome = randint(0,30)
        if randome == 1:
            celle_instans.sett_levende()
        self._rutenett[rad][kol] = celle_instans

    def hent_celle(self, rad, kol):
        if rad in range(self._ant_rader) and kol in range(self._ant_kolonner):
            return self._rutenett[rad][kol]
        return None

    def tegn_rutenett(self):
        for kol in range(self._ant_kolonner):
            for rad in range(self._ant_rader):
                celle_instans =  self._rutenett[rad][kol]
                print(celle_instans.hent_status_tegn(), end="")
            print()

    def _sett_naboer(self, rad, kol):
        celle_instans = self.hent_celle(rad, kol)
        for nabo_rad in range(-1,2):
            for nabo_kolonne in range(-1,2):
                nabo = self.hent_celle(rad + nabo_rad, kol + nabo_kolonne)
                if nabo != self.hent_celle(rad, kol):
                    if nabo != None:
                        celle_instans.legg_til_nabo(nabo)

    def koble_celler(self):
        for kol in range(self._ant_kolonner):
            for rad in range(self._ant_rader):
                self._sett_naboer(rad, kol)

    def hent_alle_celler(self):
        celle_liste = []
        for rad in self._rutenett:
            for celle in rad:
                celle_liste.append(celle)
        return celle_liste


    def antall_levende(self):
        indeks = 0
        for nabo in self.hent_alle_celler():
            if nabo.er_levende() == True:
                indeks +=1
        return indeks
