from datetime import date
import calendar
oggi = date.today()
print(oggi)
stipendio = 2000
spese_fisse = 1000
risparmio_mensile = 200
giorni_mese = calendar.monthrange(oggi.year , oggi.month)[1]
giorni_rimasti = giorni_mese - oggi.day + 1
print(f"{giorni_rimasti} giorni alla fine del mese")
spendibile = stipendio - spese_fisse - risparmio_mensile
print(spendibile, "€ spendibili al mese")
spendibile_al_giorno = spendibile / giorni_rimasti
print(f"oggi spendi {spendibile_al_giorno:.2f} euro")
