# Plane Shooting
## Game Scale
The built-in relationship between **the size of game board** and **the number of planes** built on it is as follows:

| Size | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| #Planes | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 9 | 11 | 13 | 14 |

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
- ❌ (X) Missed

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


---
# Run as App
Open **Automator** and create an **Application** to **Run AppleScript**:

	on run {input, parameters}
		set currentDir to POSIX path of ((path to me as text) & "::") --get path to parent folder
		tell application "Terminal"
			activate
			do script with command "python " & (quoted form of POSIX path of currentDir) --& "src/"
		end tell
	end run

And then save it in the same folder of the `*.py` files.
