# Bélyeg

A Posta szeretné korlátozni az egy levélre ragasztható bélyegek számát. 
Biztosítania kell, hogy bármely 1 és K közötti egész szám értékű viteldíj leróható legyen 
korlátozott számú bélyeg felragasztásával is.

Készíts programot, amely kiszámítja, azt a legkisebb M értéket, amelyre teljesül, hogy bármely 1
és K közötti egész szám értékű viteldíj leróható legfeljebb M számú bélyeg felragasztásával!

## Bemenet

A standard bemenet első sorában a bélyegek száma (`1≤N≤200`) és a legnagyobb viteldíj
értéke (`1≤K≤100 000`) van. A második sor pontosan N egész számot tartalmaz, a bélyegek értékeit. 
Az első szám `1`, és minden bélyeg értéke legfeljebb `1000`.

## Kimenet

A standard kimenet első és egyetlen sora azt a legkisebb `M` egész számot tartalmazza,
amelyre teljesül, hogy bármely `1` és `K` közötti egész szám értékű viteldíj leróható legfeljebb `M`
számú bélyeg felragasztásával!

## Példa


| Bemenet           | Kimenet | 
|-------------------|---------|
| `3 10`<br>`1 2 3` | `4`     |

## Korlátok

+ Időlimit: 0.1 mp.
+ Memórialimit: 32 MiB
+ Pontozás: A tesztek 40%-ában a `N≤50`, `K≤1 000`
