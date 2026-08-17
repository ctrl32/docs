# Riešenie problémov

Zoznam skutočných hlášok, ktoré ti systém vypíše, a čo za nimi naozaj je. Ak
build zlyhá, editor otvorí okno s **celým** výpisom — text sa dá označiť myšou
aj skopírovať tlačidlom, a to isté je v súbore `build\last_build_error.txt`.

## Nahrávanie programu

### „the ST compiler (visu_stc) was not found"

Chýba prekladač ST. Od verzie, kde sa rebrík a FBD prekladajú do bytecode, ho
potrebuje **každý** projekt s logikou.

- **Nainštalovaný editor:** `visu_stc.exe` musí zostať vedľa `visu_editor.exe`.
  Ak si presúval súbory, vráť ho späť alebo preinštaluj.
- **Klon repozitára:** buď použi binárku z `dist\`, alebo si prekladač zostav:
  `cmake --build build --target visu_stc`.

### „tag 'NOT' has the name of an ST keyword"

Tag sa v generovanom programe stáva **identifikátorom**, takže meno ako `NOT`,
`VAR`, `REAL` alebo `TIME` v ňom znamená niečo iné. Premenuj tag — hláška
povie, o ktorý ide.

### „EQ 'b30': its parameters have no ST form yet"

Blok, ktorý editor vie nakresliť, ale generátor ho zatiaľ nevie preložiť.
Hláška vždy pomenuje **typ aj meno** bloku. Nahlás to na `bugs@ctrl32.com` —
býva to malá oprava.

### „logic cannot compile to bytecode: … did not compile"

Vygenerovaný program sa nepreložil — to je **naša chyba, nie tvojho projektu**.
Editor pri tom vypíše celý vygenerovaný zdroj aj s číslami riadkov; pošli ten
výpis.

### „project has N blocks, the limit is 512"

Skutočný limit. Pozri [Výkon a limity](limits.md); väčšinou sa skôr minie
tabuľka tagov.

## Panel

### Panel odmietol balík („invalid pack")

Balík neprešiel kontrolou — najčastejšie **nesedí cieľová doska** (projekt je
pre iný panel), alebo je runtime starší než formát balíka.

Dôležité: **starý balík zostáva a beží ďalej**. Nahrávaním sa panel nedá
odrovnať. Riešenie: skontroluj dosku v projekte, prípadne preflashuj runtime.

### „!! N FB RECORDS – this pack predates the one-engine build"

V paneli je balík z veľmi starého editora. Jeho **logika nebeží** — panel to
napíše na konzolu aj do diagnostického zásobníka. Zostav projekt znovu
aktuálnym editorom a nahraj ho.

### Panel odpovedá, ale `seq` sa nehýbe

Spojenie je v poriadku, **stojí PLC cyklus**. Pozri diagnostický zásobník
(*Debug → diagnostika*) — býva tam dôvod (chyba VM, prekročenie cyklu).

## Online sledovanie

### Ikona zástrčky je červená

Panel beží **iný program** než máš v editore. Hodnoty sa zámerne nezobrazia —
chodia podľa indexov a pri inom programe by ukazovali reálne čísla pri
nesprávnych menách. Editor rovno ponúkne nahratie.

### Ikona je oranžová a nič sa nedeje

Port sa nedá otvoriť: drží ho iný program (terminál, iný editor), panel sa
práve reštartuje, alebo je odpojený kábel. Skúša sa to raz za sekundu, takže
po zapojení kábla to nabehne samo.

### Vidím tagy, ale nie hodnoty na drôtoch medzi blokmi

Symboly sa nepodarilo overiť — editor ich použije len vtedy, keď preložený
program **bajt na bajt** sedí s tým v paneli. Stav napíše do stavového riadka;
najčastejšia príčina je, že panel má iný build.

### ONLINE a Deploy sú zamknuté

## Editor

### V novom projekte sa nedá pridať priečka

Toto bola chyba a je **opravená**: tlačidlo *+ Rung* si teraz BOOL tag vytvorí
samo a napíše, ktorý. Ak to stále nejde, máš starú binárku.

### Komentár pri premennej zmizol

Tiež opravené. Komentár sa píše na koniec riadka za `//` a číta sa späť; ak sa
riadok nechá bez komentára, komentár sa zmaže — text je pre svoj zoznam celá
pravda.

### Otvorený projekt má prázdny rebrík

Opravená chyba importu (projekt sa načítaval cez balík bez blokových záznamov).
Aktualizuj editor.

---

Ak sa problém nedá zaradiť sem, pošli **celý výpis chyby** (tlačidlo *Skopírovať
hlášku*) na `bugs@ctrl32.com` — ikona chrobáka je vpravo v hornom menu a otvorí
mail rovno.
