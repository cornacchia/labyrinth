# Python Labyrinth #

This repository holds a simple python implementation of the [labyrinth](https://en.wikipedia.org/wiki/Labyrinth_%28board_game%29) board game.

## Installation ##
To get the code:
```
$ git clone https://github.com/cornacchia/labyrinth.git
```
To start the game:
```
$ python labyrinth.py
```

## How to play ##
Once the game is started, it will ask for the number of player for the match (up to 4).

After having chosen the number of players the game will start, showing a board like this:
```
Player 0's turn
'r' to rotate, ARROWS to move, ENTER to insert
Current treasure: l
           
       [ ]-
        |  
             |         |         |       
       [@]- [ ]--[a]- [ ] -[b]- [ ]--[@]
        |         |    |    |         |  
        |         |    |    |         |  
      -[p] -[t]- [q]- [r]- [ ]  [o]--[s]
             |              |    |    |  
        |         |    |              |  
       [c]--[ ]- [d]--[u] -[e]--[ ]--[f]
        |         |    |    |         |  
        |    |                        |  
       [ ] -[x] -[ ]  [ ]--[ ]--[ ]--[ ]
        |    |    |    |                 
        |         |    |    |    |    |  
       [g]--[ ]--[h]- [ ] -[i] -[n] -[j]
        |              |    |         |  
        |                        |    |  
      -[ ] -[ ] -[ ]--[ ]--[ ]  [ ] -[w]-
             |              |    |       
        |         |         |    |    |  
       [ ]--[v]--[k]--[ ]--[l]- [m]--[ ]
             |                           

```
* `[ ]` represents a room
* `|` represents a vertical exit from a room
* `-` represents a horizontal exit from a room
* `a...x` represent treasures
* `@` represents a player

Note: to be connected, two rooms must have each a path towards the other, e.g.
```
Connected rooms:
[ ]--[ ] (horizontally)

[ ]
 |
 |
[ ] (vertically)

#################

Unconnected rooms:
[ ]- [ ]

[ ]
 |

[ ]
```

Each turn is divided in two phases:
1. The _free room_ (the room outside the game board, in the upper left corner) must be rotated (with the *r* key), positioned with the arrow keys and inserted in the board with the enter key (only even rows and columns are allowed)
2. The player character (@) must be moved to its next treasure following the available paths in the labyrinth.

To win the game a player must get all their treasures (which are randomly split between every player) and then go back to their strating position.
