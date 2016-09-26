# Plane Shooting
## Game Scale
The built-in relationship between **the size of game board** and **the number of planes** built on it is as follows:

| Size | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| #Planes | 14 | 13 | 11 | 9 | 8 | 6 | 5 | 4 | 3 | 2 | 2 | 1 |

## User Input 
The simplest way of input is like `1a`, which represents you want to shoot at upper-left corner of the game board. Besides, `processInput()` automatically recognizes coordinates information from players' input with other formats as follows:

- reversed order: `a1`
- leading zero: `01a`
- UPPERCASED: `1A`
- separated: `1 a`, `A,01`, etc.
