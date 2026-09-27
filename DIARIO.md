# Diario — Budget Quotidiano
24/09 — passo 0. Progetto creato, git attivo, .gitignore verificato con git check-ignore.
24/09 — passo 1. Prime variabili. Il programma calcola e stampa i 428 € spendibili al mese. Imparato che le virgolette fanno diventare testo il nome di una variabile
nel passo 2 ho imparato ad arrontondare con :.2f ed usare f string con le parentesi graffe che sono le variabili
nel passo 3 ho imparato ad usare i tool ed i sotto tool, python è più semplice di quello che sembra. ricordarsi di scegliere la strada più semplice perchè sembra quella errata ma non è così
passo 4 input chiede e aspetta, e restituisce sempre testo
- float trasforma il testo in numero — e senza, il + incolla invece di sommare
- with open(file, "a") apre in aggiunta e chiude da solo; il rientro dice cosa sta dentro il blocco
- il \n, se no va tutto su una riga
- leggere un errore: ultima riga = cosa non torna, line N = dove, ^ = il punto
- e due regole di progettazione che valgono ovunque: si salvano i fatti, non le conclusioni (la data e la spesa, non il residuo), e si salva il dato controllato, non quello grezzo (importo, non risposta)
for riga in f: scorre un file riga per riga senza sapere quante sono
.strip() toglie spazi e a capo dai bordi
.split(",") taglia una stringa e restituisce una lista; i pezzi si prendono con le quadre, contando da zero
dentro le graffe di una f-string può andare anche pezzi[1], non solo un nome
il rientro decide quante volte una riga gira — è la cosa che ti è costata più tempo oggi, e ora la sai per esperienza
e il concetto più importante: chi legge un file deve conoscere il formato di chi l'ha scritto. L'ordine dei campi è un accordo, e vale finché non lo cambi tu