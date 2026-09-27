from datetime import date
import calendar
oggi = date.today()
print(oggi)
stipendio = 1628
spese_fisse = 900
risparmio_mensile = 300
giorni_mese = calendar.monthrange(oggi.year , oggi.month)[1]
giorni_rimasti = giorni_mese - oggi.day + 1
print(f"{giorni_rimasti} giorni alla fine del mese")
spendibile = stipendio - spese_fisse - risparmio_mensile
print(spendibile, "€ spendibili al mese")
spendibile_al_giorno = spendibile / giorni_rimasti
print(f"oggi spendi {spendibile_al_giorno:.2f} euro")
tipo_spesa = input("qual era la spesa? ")
risposta = input("quanto era la spesa? ")
importo = float(risposta)
print(f"ti restano {spendibile_al_giorno - importo:.2f} da spendere")
print(f"{tipo_spesa} pagato {importo}")
with open("spese.csv", "a") as f:
    f.write(f"{oggi},{tipo_spesa},{importo:.2f}\n")
with open("spese.csv", "r") as f:
    for riga in f:
        riga_pulita = riga.strip()
        pezzi = riga_pulita.split(",")
        print(f"il {pezzi[0]} hai speso {pezzi[2]}€ per {pezzi[1]}")