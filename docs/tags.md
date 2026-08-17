# Tagy

**Tag je premenná.** Je to zároveň jediné miesto, kde v celom systéme býva
hodnota — widget si hodnotu nedrží, drží si len index tagu. Preto obrazovka,
logika, WEBview aj Modbus vidia to isté číslo a nemá sa ako rozísť.

Tabuľka tagov je zároveň **procesný obraz** PLC (ekvivalent I/Q/M na S7).

## Založenie tagu

V strome projektu *Application → Tagy*. Každý tag má:

| Vlastnosť | Načo je |
|---|---|
| **meno** | jediné, čím sa naň odkazuješ; v ST je to identifikátor |
| **typ** | `BOOL`, `I16`, `U16`, `I32`, `U32`, `REAL` (f32), `STRING`, `TIME` |
| **prístup** | `ro` (len čítanie) / `rw` — platí pre WEBview a obsluhu, nie pre logiku |
| **zdroj** | odkiaľ hodnota prichádza (nižšie) |
| **gain / offset** | prepočet na fyzikálnu veličinu: `y = x · gain + offset` |
| **jednotka, desatinné miesta** | ako sa zobrazuje |
| **deadband** | odkedy sa zmena považuje za zmenu |

!!! warning "Meno tagu nesmie byť kľúčové slovo ST"
    Mená ako `NOT`, `AND`, `VAR`, `REAL`, `TIME` alebo `END_IF` sa v
    generovanom programe stanú niečím iným, ako čakáš. Editor to odmietne pri
    builde a povie, o ktorý tag ide.

## Odkiaľ hodnota prichádza

| Zdroj | Význam |
|---|---|
| **internal** | len v pamäti panela; s `persist` prežije reštart |
| **modbus** | z PLC, meniča alebo merača — jednotka, funkčný kód, adresa |
| **canopen** | objekt zo slovníka uzla (index/subindex), cez PDO alebo SDO |
| **gpio** | lokálny vstup/výstup panela, voliteľne invertovaný |
| **periph** | pin čipu na lokálnej zbernici (expandér, teplomer, LED) |

!!! danger "Poradie slov pri Modbus `f32`"
    Hodnota `REAL` sa cez Modbus prenáša v dvoch 16-bitových registroch a
    **poradie slov sa líši výrobca od výrobcu**. Je to najčastejší zdroj
    nezmyselných hodnôt. Máš na to prepínač `word_order`; keď vidíš namiesto
    23,5 °C hodnotu 3,4·10³⁸, začni tu.

!!! note "SDO nikdy v cykle"
    CANopen objekty čítané cez **SDO** sú pomalé a nepatria do cyklu — sú na
    parametrizáciu pri štarte alebo na zásah obsluhy. Do cyklu patrí **PDO**.

## TIME — čas, ktorý zadáva obsluha

Oneskorenia stroja patria **obsluhe**, nie prekompilovaniu. Tag typu `TIME`
je na to:

```yaml
- { name: delay, datatype: time, unit: s, decimals: 1, init: 2500 }
```

- **v tabuľke je vždy v milisekundách** — logika, zbernice aj Modbus vidia
  obyčajné celé číslo,
- **na paneli sa zobrazuje a zadáva v jednotke tagu** (`ms`, `s`, `min`,
  `h`). Pri `unit: s` ukáže widget „2.5 s", obsluha na klávesnici napíše
  `2.5` a do tagu sa uloží 2500,
- **`min`/`max` na widgete `input` sú v tej istej jednotke**, takže obsluhu
  ohraničujú čísla, ktoré vidí,
- **v ST je to `TIME`**, takže sa dá napísať `t1(PT := delay)` alebo
  `delay := T#1s500ms` bez akéhokoľvek prevodu.

Presne toto je spôsob, ako dať operátorovi „čas predohrevu" na obrazovku:
`input` naviazaný na `TIME` tag a ten istý tag ako `PT` časovača.

!!! note "Porovnania času sú bez znamienka"
    `TIME` beží aj za 2³¹ ms (24,8 dňa) — pri stroji, ktorý sa nevypína, je
    to bežné. Porovnania preto pracujú bez znamienka a `IF t1.ET > T#500ms`
    platí aj po mesiaci behu.

## Deadband — nie je to kozmetika

Analógový vstup šumí vždy. Bez pásma necitlivosti panel prekresľuje displej pri
každom zákmite posledného bitu a rovnaký zákmit posiela cez WebSocket každému
pripojenému prehliadaču.

Nastav deadband **väčší než šum a menší než to, čo ťa zaujíma**: pri tlaku
snímanom s rozlíšením 0,01 bar je 0,05 bar rozumné.

## Retencia (persist)

`internal` tag s `persist` prežije vypnutie. Platí pre to jedno tvrdé pravidlo:

!!! danger "Nezapisuj retentívne dáta pri každej zmene"
    Flash aj EEPROM majú konečný počet zápisov. Tag, ktorý sa mení každý
    cyklus a zapisuje sa pri každej zmene, zničí pamäť za mesiace. Retentívne
    má byť to, čo si potrebuješ pamätať cez vypnutie — počítadlo kusov,
    nastavená teplota, aktuálny krok — nie okamžitá hodnota merania.

## Prečo je čítanie tagu to najdrahšie v cykle

Tabuľka tagov je od 16. 8. 2026 **bez zámku**: hodnota je jedno zarovnané
32-bitové slovo, typ sa po registrácii nikdy nemení, takže čitateľ vždy dostane
buď starú, alebo novú hodnotu — nikdy polovicu z každej. Garantuje to hardvér a
mutex netreba.

Predtým sa za každý prístup platilo zámkom (~1,5 µs na dvojicu take/give), čo
bolo 20–100× viac než samotný prístup do pamäte. Strojový program preto zrýchlil
z 1,32 ms na **0,30 ms**. Podrobnosti v [Výkon a limity](limits.md).

Praktický dôsledok pre teba: **medzivýsledky drž v lokálnych premenných POU, nie
v tagoch.** Tag je rozhranie — na obrazovku, do Modbusu, do sledovania. Nie
odkladací priestor.

!!! warning "Typ širší než 32 bitov sa do tabuľky nezmestí"
    `LREAL`, `LINT` ani reťazec uložený priamo v hodnote nie sú podporované
    práve preto, že by rozbili bezzámkové čítanie. Reťazce sú indexy do
    tabuľky reťazcov.

## Snímka, nie okamih

Renderer aj online sledovanie čítajú **snímku**: každý tag je čerstvý sám o
sebe, ale nie je to konzistentný okamih naprieč všetkými tagmi. Nikdy to tak
nebolo — zapisovateľ ich aktualizuje tag po tagu. Pre zobrazovanie je to
správne; keď potrebuješ dve hodnoty zaručene z toho istého cyklu, spočítaj si
ich v logike a zapíš výsledok.

## Limit

**512 tagov.** V praxi je to to prvé, čo sa minie — skôr než bloky, skôr než
bytecode. Editor projekt s prekročeným limitom odmietne pri builde.
