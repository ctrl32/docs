# ctrl32

**HMI a PLC pre malé stroje na jednom ESP32 paneli.** Nakreslíš obrazovky,
nadefinuješ tagy, napíšeš logiku v rebríku, blokovej schéme alebo v ST — a
nahráš to do panela. Tá istá vizualizácia beží aj v prehliadači.

Ekvivalent CoDeSys + WebVisu, len na hardvéri, ktorý stojí rádovo menej.

## Z čoho sa to skladá

| Časť | Čo robí |
|---|---|
| **Panel (firmware)** | beží na ESP32, kreslí vizualizáciu na dotykový displej, číta Modbus, riadi logiku |
| **ctrl32 Editor** | nainštalovaná aplikácia na PC — kreslíš v nej obrazovky, definuješ tagy, píšeš program a nahrávaš ho do panela |
| **WEBview** | tá istá vizualizácia v prehliadači, servírovaná priamo z panela |

## Základný princíp: vizualizácia je DÁTA, nie kód

Obrazovky sa **neprekladajú do firmvéru**. Editor ich zabalí do binárneho
balíka a panel ho číta priamo z flash pamäte. Zmena obrazovky preto znamená
nahratie súboru, **nie preflashovanie panela** — a keď sa niečo pokazí, starý
balík zostáva v druhom slote a panel beží ďalej.

## Čo panel naozaj zvládne

Čísla sú namerané na najpomalšej doske, ktorú predávame (klasický ESP32,
240 MHz), pri bežiacom Ethernete a CAN zbernici:

| | |
|---|---|
| 400 blokov v rebríku | **0,52 ms** z 10 ms cyklu (5 %) |
| celý strojový program (190 riadkov ST, 215 tagov) | **0,30 ms** (3 %) |
| 10 000 inštrukcií ST | 1,42 ms (14 %) |

Pre porovnanie: Siemens LOGO! sa zastaví pri 400 blokoch. My ich zvládneme
s cyklom, ktorý je z 95 % nečinný. Podrobnosti a metodika v kapitole
[Výkon a limity](limits.md).

## Čo to NIE JE

!!! danger "Bezpečnosť sa cez panel nerieši"
    Zariadenie **nie je určené na bezpečnostné funkcie**. Núdzové zastavenie,
    dvere a svetelné závory musia byť **tvrdo drôtované** — nie vedené cez
    logiku panela. Zastavenie pohonu cez CANopen nie je bezpečnostná funkcia;
    na to má menič svorky STO.

Ani to nie je systém reálneho času. Cyklus 10–20 ms drží spoľahlivo, ale
jitter zo sieťového zásobníka existuje a nikdy ho nesľubujeme preč.

## Kde začať

<div class="grid cards" markdown>

-   **Prvýkrát v ruke**

    ---

    Od inštalácie po prvý program v paneli za pár minút.

    [Rýchly štart](quickstart.md)

-   **Ako sa v tom pracuje**

    ---

    Rozloženie editora, strom projektu, obrazovky, tagy, POU.

    [Editor](editor.md)

-   **Keď stroj beží inak, než čakáš**

    ---

    Živé hodnoty priamo v priečkach rebríka, priamo z bežiaceho stroja.

    [Online sledovanie](online.md)

-   **Keď niečo nejde**

    ---

    Skutočné hlášky, ktoré ti systém vypíše, a čo za nimi je.

    [Riešenie problémov](troubleshooting.md)

</div>
