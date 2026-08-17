# Online sledovanie

Editor pripojený k bežiacemu panelu ukazuje **živé hodnoty na miestach, kam sa
aj tak pozeráš**: pri kontaktoch v priečke, na pinoch blokov, v zozname
premenných aj v náhľade obrazovky. Je to ten istý pohľad ako testovací režim,
len hodnoty nepočíta simulácia, ale **stroj**.

## Zapnutie

V hornej lište vyber COM port a klikni ikonu zástrčky. Farba hovorí stav:

| Farba | Význam |
|---|---|
| **zelená** | panel odpovedá a beží ten istý program |
| **oranžová** | hľadá sa port (odpojený kábel, panel sa reštartuje) |
| **červená** | panel odpovedá, ale beží **iný program** |

V bublinke nad ikonou sú tri čísla, ktoré stoja za pozretie: koľko panel stojí
sledovanie (v µs), ako staré je posledné čítanie a počítadlo vzoriek.

!!! tip "Zamrznuté počítadlo vzoriek nie je porucha spojenia"
    Ak panel odpovedá, ale `seq` sa nehýbe, **stojí PLC cyklus**. To je
    diagnóza, nie timeout — a ušetrí hodinu hľadania na nesprávnom mieste.

## Rovnaký program, inak nič

Hodnoty chodia z panela **podľa indexov**, nie podľa mien. Keby editor mal
novší projekt než panel, ukazoval by reálne čísla pri nesprávnych menách —
živo vyzerajúca lož, ktorá je horšia než prázdne políčko.

Preto si obe strany pri pripojení porovnajú dve čísla:

- **odtlačok tabuľky tagov** — mená a typy všetkých tagov v poradí indexov,
- **CRC balíka** — presná identita programu (zmenená priečka nechá tagy tak,
  ale offsety lokálnych premenných sa posunú).

Keď nesedia, editor napíše *„Panel má iný program – nahrávam tento"* a otvorí
nahrávanie. Sledovanie sa medzitým odparkuje (upload potrebuje ten istý port) a
po reštarte sa samo pripojí.

Odtlačok si vieš pozrieť aj z príkazového riadka:

```powershell
visu_editor.exe projekt.yaml --tag-hash
# TAGHASH 43943135  (215 tags)
```

Na mieste tým odlíšiš „panel má iný program" od „je zlý kábel" bez hádania.

## Čo sa dá sledovať

| Druh | Odkiaľ | Poznámka |
|---|---|---|
| **tagy** | tabuľka tagov panela | funguje vždy |
| **drôty medzi blokmi** | inštančná pamäť VM | mená sa odvodia z preloženého programu |
| **členy blokov** (`t1.ET`, `c1.CV`) | inštančná pamäť VM | to isté |
| **stav panela** | cyklus, overruny, heap | aj cena samotného sledovania |

Drôty a členy blokov nie sú tagy — od prechodu na bytecode sú to slová
inštančnej pamäte (a práve preto je cyklus 5× rýchlejší). Editor si ich mená
zistí tak, že projekt zostaví a preložený program **porovná bajt po bajte** s
tým, čo je v balíku. Keď sedia, offsety sú preukázateľne tie z panela; keď
nie, ukáže len tagy a povie to.

V priečke to znamená konkrétne veci: pri počítadle **koľko napočítalo**
(`CV`), pri časovači **ako dlho už beží** (`ET`, časy pod sekundu v ms,
nad ňou v sekundách) a s akým `PT` či `PV` blok **naozaj** pracuje — nie
s akým je nakreslený. Keď je parameter vedený z tagu, tento rozdiel je
presne to, čo hľadáš.

## Koľko to stojí cyklus

Panel vzorkuje len to, na čo sa práve pozeráš, a len desaťkrát za sekundu —
rýchlejšie oko aj tak neprečíta. Namerané na klasickom ESP32 (10 ms cyklus,
strojový program):

| stav | logika | celé telo úlohy |
|---|---|---|
| nikto nesleduje | 299 µs | 287 µs |
| 8 tagov | 299 µs | 288 µs |
| 64 tagov (maximum) | 299 µs | ~289 µs |

Jedna sledovaná hodnota stojí **~0,34 µs na vzorku**, takže 64 hodnôt desaťkrát
za sekundu je **2,2 µs na cyklus** — 0,02 % z desaťmilisekundovej periódy. Keď
nie je nikto online, zoznam je prázdny a nevykoná sa ani to.

## Zápis hodnôt (force)

Zatiaľ **nie je** — políčka sú počas online len na čítanie. Vynútená hodnota na
výstupe je presne to, čím sa ľudia zrania, takže to príde ako samostatná vec:
viditeľne, s časovým limitom a nikdy ticho.

## Buffer (osciloskop)

Živý pohľad desaťkrát za sekundu ukáže ustálený stav a **krátke udalosti
minie** — impulz dlhý jeden cyklus sa doň jednoducho netrafí. Na to je buffer:
až 8 hodnôt vzorkovaných **každý cyklus** do kruhového zásobníka v paneli, so
spúšťou (nábežná/dobežná hrana, úroveň).

Kruh beží stále, kým je nahrávanie spustené, a spúšť rozhoduje len o tom, **kedy
skončiť** — preto máš v zázname aj históriu spred udalosti.

!!! success "Vypnuté nahrávanie nestojí nič"
    Nie „takmer nič" — cyklus vykoná jediné porovnanie a do vzorkovania vôbec
    nevojde. Počas nahrávania stojí 8 hodnôt každý cyklus ~5 µs, teda 0,05 %
    periódy.

Zobrazenie záznamu v editore ešte nie je hotové; zatiaľ sa buffer ovláda cez
servisný protokol panela.
