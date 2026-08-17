# Rýchly štart

Cieľ tejto kapitoly: **od nainštalovaného editora po program bežiaci v paneli.**
Trvá to pár minút a nepotrebuješ na to nič okrem panela, USB kábla a PC.

## 1. Inštalácia

Spusti inštalátor `ctrl32-setup-<verzia>.exe`. Nainštaluje sa:

| Súbor | Načo je |
|---|---|
| `visu_editor.exe` | samotný editor |
| `visu_stc.exe` | prekladač ST — editor ho volá pri každom builde |
| `packbuild\` | staviteľ balíka (obsahuje aj schému a katalóg dosiek) |
| `ctrl32.dat` | katalóg dosiek a čipov |
| `examples\` | vzorové projekty na otvorenie |

!!! note "Prečo sú tam tri programy a nie jeden"
    Prekladač a staviteľ balíka sú tie isté nástroje, ktoré používame pri
    vývoji — takže balík, ktorý ti postaví editor, je **bajt na bajt** ten
    istý ako z príkazového riadka. Formát má jediného autora a nemá sa ako
    rozísť.

## 2. Otvor vzorový projekt

*File → Open* a vyber niečo z `examples\`. Dobrý začiatok:

- `ladder_sealin.yaml` — klasické samodržné zapojenie s TON, počítadlom a
  latch-om; uvidíš rebrík aj s komentármi pod premennými,
- `tubex_panel.yaml` — reálny panel s Ethernetom, Modbus slave a NeoPixel LED,
- `machine_blocks.yaml` — motory, ventily, PID a hysterézy.

## 3. Vyber dosku

V strome projektu klikni na uzol dosky. Doska určuje piny, pamäť aj to, aký
runtime sa do nej flashuje — projekt sa bez nej nedá nasadiť.

## 4. Nahraj runtime (prvýkrát)

Ak je panel nový alebo má starý firmvér, na stránke dosky je *Flash runtime*.
Zapíše sa cez USB (esptool), trvá to necháva desiatky sekúnd.

!!! warning "Starý runtime = nepodarí sa nahrať program"
    Formát balíka sa vyvíja. Ak je runtime starší než balík, panel ho odmietne
    a v editore uvidíš chybu. Riešenie je vždy to isté: **preflashovať runtime**.

## 5. Nahraj program

V hornej lište vyber COM port a klikni modrú ikonu ⭳ (*Download to panel*).
Editor projekt zostaví a nahrá. Čo sa deje pod tým:

1. projekt sa zostaví do binárneho balíka,
2. balík ide do **neaktívneho slotu** v paneli,
3. panel overí CRC, formát aj cieľovú dosku,
4. **až potom** prepne aktívny slot a reštartuje sa.

Preto sa panel nahrávaním nedá odrovnať: keď je čokoľvek zle, starý balík
zostáva a beží ďalej.

## 6. Pozri sa, čo stroj robí

Vedľa portu je ikona zástrčky — *ONLINE*. Po zapnutí ukazuje editor **živé
hodnoty priamo z panela**: v priečkach rebríka, na pinoch blokov, v zozname
tagov aj v náhľade obrazovky.

Podmienka je jediná: **editor a panel musia mať rovnaký program**. Ak nemajú,
editor to povie a rovno ponúkne nahratie — viac v kapitole
[Online sledovanie](online.md).

## Čo ďalej

- [Editor](editor.md) — ako je usporiadaný a čo kde je
- [Tagy](tags.md) — premenné, typy, deadband a odkiaľ hodnoty prichádzajú
- [Rebrík](ladder.md) — kreslenie priečok
- [Nahrávanie do panela](deploy.md) — dvojslot, runtime, čo sa kedy overuje
