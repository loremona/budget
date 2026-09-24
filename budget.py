stipendio = 1628
spese_fisse = 900
risparmio_mensile = 300
giorni_mese = 30
spendibile = stipendio - spese_fisse - risparmio_mensile
print(spendibile, "€ spendibili al mese")
spendibile_al_giorno = spendibile / giorni_mese
print(f"oggi spendi {spendibile_al_giorno:.2f} euro")
