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

## Game play
### Injury Levels

	INJURY_LEVELS = {0: 'No', 1: 'Minor', 2: 'Severe', 3:'Fatal'}
	
A player inputs a pair of coordinates and gets the feedback. The feedback will be one of following emojis:

- ☠️ (3) Fatal injury
- ‼️ (2) Severe injury
- ❗️ (1) Minor injury 
- ❌ (0) Missed

|  |  | ☠️ |  |  | 
|:---:|:---:|:---:|:---:|:---:|
| ❗️ | ❗️ | ‼️ | ❗️ | ❗️ | 
|  |  | ‼️ |  |  | 
|  | ❗️ | ‼️ | ❗️ |  | 

### Orientations of Planes

	ORIENTATIONS  = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	
so that `ORIENTATIONS[x]` and `ORIENTATIONS[3 - x]` have the exact opposite orientations.

#### Orientations[0]
|  |  | 🎯 |  |  | 
|:---:|:---:|:---:|:---:|:---:|
| 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 
|  |  | 🎯 |  |  | 
|  | 🎯 | 🎯 | 🎯 |  | 

#### Orientations[1]
|  |  | 🎯 |  |  
|:---:|:---:|:---:|:---:|
| 🎯 |  | 🎯 |  | 
| 🎯 | 🎯 | 🎯 | 🎯 |
| 🎯 |  | 🎯 |  |
|  |  | 🎯 |  |

#### Orientations[2]
|  | 🎯 | 🎯 | 🎯 |  | 
|:---:|:---:|:---:|:---:|:---:|
|  |  | 🎯 |  |  | 
| 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 
|  |  | 🎯 |  |  | 

#### Orientations[3]
|  | 🎯 |  |  |
|:---:|:---:|:---:|:---:|:---:|
|  | 🎯 |  | 🎯 |
| 🎯 | 🎯 | 🎯 | 🎯| 🎯 |
|  | 🎯 |  | 🎯|
|  | 🎯 |  | |



