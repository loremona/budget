# ---- Attrezzi presi dalla libreria standard (passo 3) ----
# "from X import Y" pesca un attrezzo solo, si usa col nome nudo: date
# "import X" apre la cassetta intera, si usa col punto: calendar.monthrange
from datetime import date
import calendar

# ---- Che giorno e' oggi, e quanti giorni restano (passo 3) ----
oggi = date.today()          # le parentesi = "fallo adesso": va a leggere l'orologio
print(oggi)
stipendio = 1628
spese_fisse = 900
risparmio_mensile = 300
# monthrange restituisce DUE valori; [1] prende il secondo = quanti giorni ha il mese
# oggi.year e oggi.month: il punto significa "di" -> l'anno DI oggi
giorni_mese = calendar.monthrange(oggi.year , oggi.month)[1]
giorni_rimasti = giorni_mese - oggi.day + 1   # +1 perche' oggi si puo' ancora spendere
print(f"{giorni_rimasti} giorni alla fine del mese")

# ---- Quanto posso spendere (passi 1 e 2) ----
spendibile = stipendio - spese_fisse - risparmio_mensile
print(spendibile, "€ spendibili al mese")

# ---- Chiedo la spesa di oggi (passo 4) ----
tipo_spesa = input("qual era la spesa? ")     # input chiede e ASPETTA
risposta = input("quanto era la spesa? ")     # input restituisce SEMPRE testo
importo = float(risposta)                     # float trasforma il testo in numero
print(f"{tipo_spesa} pagato {importo}")

# ---- Scrivo la spesa nel file (passo 4) ----
# "a" = append, aggiunge in fondo.  "w" cancellerebbe tutto: mai usarlo qui.
# il with chiude il file da solo quando il blocco rientrato finisce
with open("spese.csv", "a") as f:
    f.write(f"{oggi},{tipo_spesa},{importo:.2f}\n")   # \n = a capo, se no si incollano

# ---- Rileggo il file e sommo il mese corrente (passi 5 e 6) ----
totale = 0                                    # accumulatore: PRIMA del ciclo, parte da zero
mese_corrente = f"{oggi.year}-{oggi.month:02d}"   # :02d = due cifre -> "09", non "9"
with open("spese.csv", "r") as f:             # "r" = read, sola lettura
    for riga in f:                            # gira una volta per ogni riga del file
        riga_pulita = riga.strip()            # strip toglie spazi e \n dai due lati
        pezzi = riga_pulita.split(",")        # split taglia alle virgole -> lista di 3
        # pezzi[0] data, pezzi[1] descrizione, pezzi[2] importo (si conta da zero)
        print(f"il {pezzi[0]} hai speso {pezzi[2]}€ per {pezzi[1]}")
        if pezzi[0].startswith(mese_corrente):        # True o False: e' di questo mese?
            totale = totale + float(pezzi[2])         # solo se True: 12 spazi, dentro l'if
print(f"totale speso: {totale:.2f}€")         # margine: gira una volta, a ciclo finito


spendibile_al_giorno = (spendibile - totale) / giorni_rimasti
print(f"oggi puoi spendere {spendibile_al_giorno:.2f}€")
speso_prima = totale - importo
disponibile_oggi = (spendibile - speso_prima) / giorni_rimasti
print(f"oggi avevi {disponibile_oggi:.2f}€ da spendere")
if importo > disponibile_oggi:
    print(f"hai sforato di {importo - disponibile_oggi:.2f}€")
else:
    print(f"sei dentro, ti restano {disponibile_oggi - importo:.2f}")
giorni_a_domenica = 7 - oggi.weekday()
print(f"mancano {giorni_a_domenica} giorni a domenica")
giorni_validi = min(giorni_a_domenica , giorni_rimasti)
print(f"{spendibile_al_giorno * giorni_validi:.2f}€ rimasti da spendere (o no)")