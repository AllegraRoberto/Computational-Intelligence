
# Quixo player


I utilized the Minimax algorithm with Alpha-Beta pruning to implement a Quixo player. This algorithm searches for the best move in a two-player game by evaluating all possible moves up to a certain depth. It selects the move that maximizes the score for the maximizing player and minimizes the score for the minimizing player.
## MiniMax_Player class
In the implementation, I created the `MiniMax_Player` class in the `minmax.py` file, along with the declaration of methods `evaluate_game` and `get_possible_moves`. The `evaluate_game` method assesses the points of a game state. It computes the maximum sequence of cells (sum) for the player and the opponent (sum_opponent), as well as the sum of each cell on the board (sum_tot) for the player. It returns a score based on these calculations: `sum + (sum - sum_opponent) + (sum_tot * 0.5)`, adding +30 for the player's win and -30 for the player's loss. The depth variable determines the evaluated state's possible distance from the current state.

The code uses recursion to explore possible moves up to a certain depth, evaluating the consequent state and returning the best move. Before starting the recursion of Minimax, the `get_possible_moves` function saves possible moves for the player and initiates Minimax on each move. Hence, the depth passed to the Minimax function is `depth`, but for the stats, I decided to print `depth+1` because there is the first cycle before Minimax.
## Provided files 
 The `main.py` file remains unchanged, but modifications were made to the `game.py` file. I introduced the `print_board` function to display the board with 'x' or 'o' symbols. I also enhanced the `play` function by adding an `interactive` variable as input. This variable can be 0 (no change), 1 (play against AI, where each move prints the board), or 2 (also with value 1, where the game's move count is printed).
I introduced variables to count repeated moves. If both players repeat the same move ten times, the game ends in a draw. 
## My files
In the `clone_game` file, functions to create a game copy are provided.
The `interactive_player.py` file contains the code for the interactive interface to play against AI. The `stats.ipynb` notebook includes functions to start the interactive interface, print stats against a Random Player,

![Instance 1](Screenshots/AIvsRandom.png)

And show AI vs AI game stats.

![Instance 1](Screenshots/AIvsAi_1.png)
![Instance 1](Screenshots/AIvsAi_2.png)
## Conclusion
In conclusion, the Minimax algorithm implementation for Quixo lays a solid foundation for developing artificial intelligence capable of playing well. However, one must consider the algorithm's computational complexity and limitations in more complex game scenarios.

## Note
LABs have been made in collaboration with Lorenzo Greco and Giuseppe Roberto Allegra. QUIXO has not been developed together but strategy has been discussed.