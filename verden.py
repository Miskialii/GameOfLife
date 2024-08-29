from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f"generasjonsnummeret er:  {self._generasjonsnummer}")
        print(f"antall levende celler er: {self._rutenett.antall_levende()}")


    def oppdatering(self):
        celler = self._rutenett.hent_alle_celler()
        for celle in celler:
            celle.tell_levende_naboer()
        for celle in celler:
            celle.oppdater_status()

        self._generasjonsnummer +=1
