# Diario — Budget Quotidiano

Un blocco per passo: cosa ho costruito e cosa ho imparato.

---

## Passo 0 — La cartella, git, il .gitignore — 24/09

Progetto creato, git attivo, `.gitignore` verificato con `git check-ignore`.

`config.txt` e `spese.csv` restano fuori da git: il codice è pubblico, i miei dati no.

---

## Passo 1 — I tre numeri — 24/09

Prime variabili. Il programma calcola e stampa i **428 €** spendibili al mese.

- una variabile è un nome attaccato a un valore
- l'`=` non significa "è uguale", significa "metti dentro": si legge da destra a sinistra
- le virgolette fanno diventare testo il nome di una variabile

---

## Passo 2 — Quanto al giorno — 24/09

Il programma divide il mensile per i giorni e stampa la cifra giornaliera.

- la divisione `/` restituisce **sempre** un numero con la virgola
- `:.2f` arrotonda a due decimali, ma **solo a schermo**: dentro la variabile il numero resta preciso
- le f-string: la `f` prima delle virgolette, il nome della variabile dentro le graffe

---

## Passo 3 — I giorni veri — 25/09

Il `30` scritto a mano sparisce: il programma ricava i giorni del mese dal calendario e conta quelli che restano.

- la libreria standard sono cassette di attrezzi, si aprono con `import` una volta sola, in cima
- le parentesi significano "esegui", il punto significa "di" (`oggi.day` = il giorno di oggi)
- `monthrange` restituisce due valori, `[1]` prende il secondo
- **una variabile si aggiorna da sola, una cifra scritta nel codice è un numero morto**

*Python è più semplice di quello che sembra. Ricordarsi di scegliere la strada più semplice, anche quando sembra quella sbagliata.*

---

## Passo 4 — Registrare una spesa — 26/09

Il programma chiede la spesa e la scrive in fondo a `spese.csv`.

- `input` chiede e aspetta, e restituisce **sempre** testo
- `float` trasforma il testo in numero: senza, il `+` incolla invece di sommare
- `with open(file, "a")` apre in aggiunta e chiude da solo; il rientro dice cosa sta dentro il blocco
- il `\n` in fondo, se no le righe si incollano
- leggere un errore: ultima riga = cosa non torna, `line N` = dove, `^` = il punto preciso
- due regole di progettazione: **si salvano i fatti, non le conclusioni** (la data e la spesa, non il residuo) e **si salva il dato controllato, non quello grezzo** (`importo`, non `risposta`)

---

## Passo 5 — Rileggere le spese — 27/09

Il programma apre `spese.csv` e stampa ogni spesa in italiano.

- `for riga in f:` scorre un file riga per riga senza sapere quante sono
- `.strip()` toglie spazi e a capo dai bordi
- `.split(",")` taglia una stringa e restituisce una **lista**; i pezzi si prendono con le quadre, contando da zero
- dentro le graffe di una f-string può andare anche `pezzi[1]`, non solo un nome
- **il rientro decide quante volte una riga gira** — è la cosa che mi è costata più tempo
- chi legge un file deve conoscere il formato di chi l'ha scritto: l'ordine dei campi è un accordo, e vale finché non lo cambio io

---

## Passo 6 — Il totale — 28/09

Il programma somma quanto ho speso **in questo mese**.

- l'**accumulatore**: una variabile a zero prima del ciclo, che dentro si somma addosso un pezzo per volta. È lo schema più usato in programmazione
- `True` e `False`: una condizione non è un valore, è una domanda che risponde sì o no
- `if` esegue il blocco rientrato solo quando la risposta è sì
- `.startswith()` riconosce l'inizio di una stringa
- `:02d` per avere `09` invece di `9`
- il rientro di nuovo, da tutti e due i lati: la somma doveva stare **dentro**, la stampa **fuori**

---

## Passo 7 — Il numero vero — 28/09

La cifra giornaliera adesso toglie quello che ho già speso, e il programma dice se sono dentro o se ho sforato.

- nessun attrezzo nuovo: era tutta composizione
- una scatola si può usare solo **dopo** la riga che la crea — per questo il calcolo è sceso in fondo al file
- `/` e `*` vengono prima di `+` e `-`: la sottrazione va fra parentesi
- `if` / `else`: due rami, ne gira sempre uno solo
- l'errore che mi è costato di più: confrontare la spesa con la cifra **dopo** invece che con quella **prima**. Misurare un salto col metro di dopo il salto dà sempre il numero sbagliato

---

## Passo 8 — La riga settimanale — 28/09

Il programma dice quanto posso spendere da qui a domenica.

- `.weekday()` dà il giorno della settimana come numero: 0 = lunedì, 6 = domenica
- `7 - weekday()` sono i giorni che mancano a domenica, oggi compreso
- `min(a, b)` restituisce il minore: vale sempre la scadenza più vicina, domenica o fine mese
- i numeri con la virgola hanno code tipo `249.50000000000003`: non si correggono, si nascondono con `:.2f`
