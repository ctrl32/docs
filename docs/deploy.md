# Nahrávanie do panela

Nahratie je **jedno tlačidlo v editore** (modrá ikona ⭳, alebo `F5`). Nie je na
to samostatná aplikácia, nepotrebuješ Python ani PlatformIO a nemusíš vedieť,
čo sa deje pod tým. Táto kapitola je o tom, čo sa deje pod tým — lebo pri
uvádzaní stroja do prevádzky sa to raz zíde.

## Dve rôzne veci: runtime a program

| | Runtime | Program (balík) |
|---|---|---|
| čo to je | firmvér panela | tvoje obrazovky, tagy a logika |
| kedy sa nahráva | pri novej doske alebo pri novej verzii ctrl32 | pri každej zmene projektu |
| ako | *Flash runtime* na stránke dosky (USB, esptool) | tlačidlo ⭳ / `F5` |
| trvá | desiatky sekúnd | sekundy |

**Zmena obrazovky neznamená preflashovanie panela.** Vizualizácia je dáta, nie
kód — panel ich číta priamo z flash pamäte.

## Čo sa stane po stlačení ⭳

1. Editor projekt **zostaví do binárneho balíka**. Ak build zlyhá, ďalej sa
   nejde a otvorí sa okno s celým výpisom.
2. Balík ide cez sériový port po blokoch (2 kB, každý potvrdený).
3. Zapisuje sa do **neaktívneho slotu** — panel má dva (`visu_a`, `visu_b`) a
   práve beží z jedného z nich.
4. Panel **overí celý balík**: CRC, formát, verziu schémy a cieľovú dosku.
5. **Až potom** prepne aktívny slot a reštartuje sa.

!!! success "Nahrávaním sa panel nedá odrovnať"
    Keď je čokoľvek zle — pretrhnutý kábel, zlý balík, nesprávna doska —
    prepnutie sa jednoducho nevykoná. Starý balík zostáva v druhom slote
    a panel beží ďalej. To nie je náhoda, je to zmysel dvoch slotov.

## Prečo panel balík odmietne

| Hláška | Príčina |
|---|---|
| `ERR: size/slot` | balík je väčší než partícia (alebo sa nedá otvoriť slot) |
| `ERR: crc` | prenos sa pokazil — skús znovu, skontroluj kábel |
| neplatný cieľ | projekt je pre **inú dosku**, než ktorá je pripojená |
| stará verzia formátu | runtime je starší než balík → **preflashovať runtime** |

Kontrola cieľovej dosky je zámerne tvrdá. Balík pre panel s iným displejom a
inými pinmi by sa načítal a bežal — a stroj by robil niečo iné, než čakáš.

## Prenos: vždy sériový port

Nahrávanie ide **cez USB / sériovú linku**, nie cez WiFi ani Ethernet. Je to
vedomé rozhodnutie: pri uvádzaní stroja do prevádzky je kábel jediná vec, ktorá
funguje vždy, a nahrávanie programu do stroja cez sieť je vec, ktorú treba
najprv poriadne zabezpečiť. Sieťové nahrávanie príde neskôr.

Ten istý port sa používa aj na [online sledovanie](online.md) — sledovanie sa
preto počas nahrávania samo odparkuje a po reštarte panela sa samo pripojí.

!!! warning "Nahrávaj do stojaceho stroja"
    Zápis do flash pamäte zastavuje prístup do cache **pre obe jadrá**, takže
    počas neho logika nebeží, aj keď má najvyššiu prioritu. Panel preto
    nahrávanie povoľuje len v STOP — je to ten istý dôvod, pre ktorý má S7
    prepínač RUN/STOP.

## Runtime

Firmvér sa zapisuje z katalógu hotových binárok pre danú dosku (`runtimes/`),
**nie prekladom na tvojom PC**. Nepotrebuješ nainštalovaný toolchain a dostaneš
presne tú binárku, ktorú sme testovali.

Beží na vlastnom vlákne, takže editor medzitým normálne kreslí, a slotov s
balíkmi sa nedotýka — po preflashovaní runtimu zostáva tvoj program v paneli.

## Čo sa nahráva spolu s programom

Balík obsahuje všetko, čo panel potrebuje, v jednom súbore:

- hlavičku (magic, verzia schémy, cieľová doska, CRC32),
- tabuľku reťazcov, tagov, alarmov a štýlov,
- assety (písma, ikony, obrázky),
- obrazovky,
- **bytecode programu** a zdroj ST (kvôli overeniu totožnosti pri online).

Panel z neho nič neparsuje — namapuje si ho z flash a číta priamo. Načítanie
obrazovky trvá menej než milisekundu.

