# Výkon a limity

Všetky čísla na tejto stránke sú **namerané**, nie odhadnuté, a to na
**najpomalšej doske, ktorú predávame** — klasický ESP32 na 240 MHz, s bežiacim
Ethernetom, WEBview a CAN masterom vedľa. Rýchlejšia doska (S3, P4) má viac
rezervy, nie menej.

## Deklarované limity

Editor projekt, ktorý ich prekročí, **odmietne pri tebe na stole** — nie ako
zasekávajúci sa panel na stroji. Sú to zároveň čísla do katalógového listu.

| Limit | Hodnota |
|---|---|
| Tagy | 512 |
| Alarmy | 128 |
| Obrazovky | 32 |
| Widgety na obrazovku | 64 |
| Bloky LD/FBD | 512 |
| Program (bytecode) | 32 kB |
| Inštančné dáta | 8 kB |
| Trendy | 4 |
| WEBview klienti | 2 |
| Osi (pohony) | 4 |
| PLC úlohy | 2 (rýchla + pomalá) |

## Koľko blokov sa naozaj zmestí

Program je N blokov AND nad 150 tagmi — každý blok číta dva tagy a jeden
zapisuje, čo je najhorší reálny pomer:

| Blokov | Priemerný cyklus | Z 10 ms periódy |
|---|---|---|
| 64 | 110 µs | 1,1 % |
| 100 | 153 µs | 1,5 % |
| 200 | 274 µs | 2,7 % |
| **400** | **515 µs** | **5,2 %** |

**Siemens LOGO! sa zastaví pri 400 blokoch.** My ich zvládneme na najslabšej
doske s cyklom, ktorý je z 95 % nečinný. Deklarovaný limit 512 nie je hranica
výkonu, ale rozpočtu bytecode: jednoduchý blok stojí ~10 B, takže 512 blokov
zaberie 16 % z 32 kB.

Prakticky sa skôr minie **tabuľka tagov** (512) než bloky.

## Reálny program, nie syntetický test

| Program | Riadkov ST | Tagov | Cyklus |
|---|---|---|---|
| polovica stroja | 100 | 110 | 168 µs |
| **celý stroj** | 190 | 215 | **304 µs** |

„Celý stroj" znamená: 40 analógových vstupov škálovaných a alarmovaných, 30
motorov s blokovaním, 40-krokovú sekvenciu a polohovaciu rampu. **3 % z 10 ms
cyklu**, nula prekročení.

Realistický riadok ST stojí ~1,6 µs, blok v rebríku ~1,3 µs.

## Čo cyklus naozaj stojí

Zaujímavá časť: **nie je to aritmetika, ale prístup k tagom.** Syntetická
slučka nad lokálnymi premennými beží 0,145 µs na inštrukciu; ten istý kód
dotýkajúci sa tagov je násobne pomalší.

Preto sa 16. 8. 2026 zrušil zámok v tabuľke tagov — každá hodnota je jedno
zarovnané 32-bitové slovo, takže hardvér už sám garantuje to, za čo sa platilo
mutexom. Výsledok na tých istých packoch a tej istej doske:

| | pred | po |
|---|---|---|
| 400 blokov | 2 660 µs | **515 µs** |
| celý stroj | 1 319 µs | **304 µs** |
| 10 000 inštrukcií (lokálne premenné) | 1 410 µs | 1 420 µs |

Posledný riadok je kontrolná vzorka: kód, ktorý sa tagov nedotýka, sa nepohol
ani o mikrosekundu. Všetko, čo sa pohlo, sa pohlo kvôli tagom.

## Pravidlo degradácie

Keď dôjde výkon, poradie je pevné a je zapísané priamo v kóde:

**logika > komunikácia > grafika**

Pri preťažení sa zahadzujú snímky obrazu. **Cyklus sa nikdy nepredlžuje.**
Displej môže sekať, riadenie stroja nie.

## Diagnostika, ktorú vidíš

Panel meria min/priemer/max cyklu a počítadlo prekročení a hlási ich editoru.
Keď niekto napíše ťažkú logiku a obraz začne sekať, uvidí prečo — a v hláseniach
je aj to, koľko stojí samotné sledovanie.

---

Merania sú zopakovateľné a čísla nie sú z papiera — číta ich sám panel
(min/priemer/max cyklu). Metodiku a testovacie projekty poskytneme na
vyžiadanie.
