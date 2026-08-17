# Editor

ctrl32 Editor je **nainštalovaná aplikácia**, nie webová stránka. Dôvod je
jednoduchý: kreslí presne tie pixely, ktoré uvidíš na paneli — je v ňom
zabudovaný ten istý renderer ako vo firmvéri, vrátane písiem, zaoblení a
farieb. Čo vidíš, to sa nahrá.

## Rozloženie

| Časť | Kde | Čo v nej je |
|---|---|---|
| **Menu** | hore | File, Edit, View, Project, Build, Online, Debug, Tools, Window, Help |
| **Panel nástrojov** | pod menu | nový, uložiť, späť/vpred, TEST, ONLINE, nahrať |
| **Strom projektu** | vľavo | doska a všetko, čo na nej beží |
| **Dokumenty** | v strede | každý uzol stromu má **stránku**, otvorí sa ako záložka |
| **Stavový riadok** | dole | výsledok posledného buildu, stav pripojenia |

Ikona **chrobáka vpravo hore** otvorí mail na `bugs@ctrl32.com` — hlásenie
chyby má byť jedno kliknutie odtiaľ, kde si na ňu narazil.

## Strom kopíruje hardvér, nie protokoly

```
projekt
  doska
    Application          programy, premenné, vizualizácie, osi
    CAN                  zbernica: rýchlosť, terminácia
      Raw CAN            mapovanie rámcov na tagy
      CANopen master     + zariadenia
    RS485                linka: baud, parita, stop bity
      Modbus RTU master  + zariadenia
      Modbus RTU slave   panel ako slave
    Ethernet             DHCP/statická IP, mDNS
      Modbus TCP         master aj slave
      MQTT               telemetria / Home Assistant
    I2C, SPI             lokálne zbernice a čipy
    Nastavenia
```

Jeden drôt môže niesť viac protokolov a ten istý protokol môže bežať na dvoch
drôtoch (Modbus na RS485 **aj** na Ethernete). Triedenie podľa protokolu by to
neumožnilo vyjadriť; takto to sedí s hardvérom aj s tým, ako je to v CoDeSyse.

!!! note "Nastavenia sú na stránkach, nie v pravom tlačidle"
    Kontextové menu obsahuje **akcie** — pridať, zmazať, premenovať. Nikdy
    nastavenia. Rýchlosť zbernice je na stránke zbernice, kde ju človek hľadá.
    Vyskakovacie okno je len na **výber z katalógu** (dosky, zariadenia,
    objekty slovníka).

Uzly funkcií, ktoré ešte nie sú hotové, sú v strome tiež — ich stránka to
povie. Zákazník musí vidieť, čo panel môže mať, nie to hádať.

## Panel nástrojov

| Ikona | Čo robí |
|---|---|
| ⊞ | nový projekt |
| 💾 | uložiť projekt |
| ↶ ↷ | späť / vpred (undo aj redo sú neobmedzené, počet je v menu Edit) |
| ▶ / ■ | **TEST** — simulácia priamo v editore, bez panela |
| ⏸ ⏭ | pauza a krok po cykloch (počas testu) |
| 🔌 | **ONLINE** — pripojenie na skutočný panel |
| **⭳** | **nahratie do panela** (F5) — jediná farebná ikona v lište |

Modrá je zámerne len jedna. Nahratie do stroja je akcia, ktorá sa nemá spliesť
so žiadnou inou; všetko ostatné je plochá ikona ako v bežnej aplikácii.

## TEST — simulácia bez panela

Tlačidlo ▶ prepne editor do behu: PLC cyklus beží na PC, obrazovky reagujú,
bloky počítajú, tagy sa menia. Dá sa pauzovať a krokovať po cykloch (*Debug →
Krok*).

Beží pri tom **ten istý bytecode a tá istá knižnica blokov**, aké sú v paneli —
VM sa prekladá aj pre PC. Preto sa dá logika odladiť pri stole a na stroj ísť
až s hotovou vecou.

Rozdiel oproti [online sledovaniu](online.md): TEST počíta hodnoty, ONLINE ich
**číta zo stroja**.

## Build (F7) a nahratie (F5)

**F7** projekt len zostaví a povie výsledok. **F5** ho zostaví a nahrá.

Keď build zlyhá, otvorí sa okno s **celým** výpisom — text sa dá označiť aj
skopírovať tlačidlom a to isté je v `build\last_build_error.txt`. Skrátená
hláška v stavovom riadku nikdy nestačila na to, aby sa dalo poradiť.

## Jazyk a téma

*View → Jazyk* a *View → Tmavá téma*. Voľba sa pamätá medzi spusteniami.

- **komunikácia so skutočným panelom** — nahratie aj online — je platená.

## Aktualizácie

*Help → Skontrolovať aktualizácie* sa pozrie na náš web a povie, či je novšia
verzia. Sťahovanie je manuálne — editor sa nikdy neaktualizuje sám za tvojím
chrbtom, lebo verzia editora súvisí s tým, čo je nahraté v paneloch u
zákazníkov.
