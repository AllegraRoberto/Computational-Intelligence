# Lab 4

**N.B.**  
I don't know if it's an official rule of the game, but we assumed that X always moves first. This information can be useful as a key for interpretation and understanding of some experiments.

# Objectives
For the resolution of this laboratory, we started from the professor's strategy and tried to improve it, testing how artificial intelligence behaved in different scenarios.

# Experiments conducted

## AI muoves first ( X )

As we started, we focused on implementing the training model into the algorithm of an AI-controlled player.   
The underlying idea is that a player should be able to find the best move for each position.  
The algorithm we implemented leverages the knowledge of all states acquired during the training phase to find the best move for each state.  
Of course, the effectiveness of this solution depends on the success of the training session. With a sufficient number of games during the training phase, for a simple game like tic-tac-toe, we can assume to have visited all possible states multiple times, thus having an optimal dictionary capable of suggesting the best move in every situation.  
The training games use random moves to try to explore as many states and as many times as possible.

After implementing this algorithm, we wondered how good this player actually was.  
Then we put it to the test in a series of 10,000 games against a player who moves randomly, obtaining excellent results:

Statistics against the random player over 10,000 games (Using X):  
Wins: 9896,
Loses: 0,
Draws: 104

From these results, we can assume that the AI has reached the highest possible level and (with the X) plays perfectly.

But winning doesn't necessarily mean making the best moves.
So, to be sure that it didn't make mistakes, we implemented the function that prints move by move the various states of a single game.
The tests performed, showed that every time the AI had the opportunity to win, it closed the game, confirming our hypothesis that it had now reached perfection.

It may seem obvious, but it's not. With a low number of games during training, it could happen that, not exploring all possible combinations of moves sufficiently, it chose non-optimal moves while still winning. This happened to us with a number of games in the training phase equal to 100.000, prompting us to opt for a greater number of games, equal to 1.000.000 .

## AI moves second ( O )

After achieving this result, we wondered how the AI would behave if it had to use O and move second.

Initially, we adapted the algorithm that selects intelligent moves to find the best moves for O.  
Instead of choosing the move that led us to the best state for X, we selected moves that led us to the worst state, therefore more advantageous for O.  
Although it played quite decently, it tied and lost a bit too much. Starting second, when X plays well, if you are skilled, you can manage to draw. Therefore, we were not concerned about the number of draws, but there were too many losses for it to be considered a good AI.

In addition, the training (for X) stored and updated the state value based on how advantageous it was for X, also considering the difference between the final result of the game and the value of that state up to that point.  
Therefore, it didn't fit perfectly to our case.  
Then we decided to create a training program exclusively for O, with a dictionary that learns the best moves in every situation and that could, at least, draw even against the best opponents.

The training was the same as for X.  
The initial results were not very satisfying. We managed to reduce the losses a bit, but the AI was still far from being a very good player.

The major weakness come out when we tried to make this AI play against the one that plays perfectly with X.  
The 10000 test games ended with a score of 10000 to 0 for X.  
This experiment highlighted how O did not know the strategy to draw against a perfect X. This is because, in the 1,000,000 randomly played training games, the times the computer randomly plays the best moves for X and O's best moves to draw are too few, or not highly valued enough, for O to learn and memorize the optimal defensive strategy in its dictionary.

Then we introduced a second reward function, different from the one used during training for X player, which would reward draws more significantly.

With this reward function the statisticd go up and AI using O against a random player did:
Wins: 8924,
Loses: 167,
Draws: 909

instead, AI  using O player against AI using X player had only draws;
AI O player wins: 0,
AI X player wins: 0,
Draws: 10000

I think these results are due to the fact that during the training phase, there were states that led to both victories/draws and defeats, and the latter are penalized specifically by the losses, resulting in poor evaluations.

I believe that by changing the values assigned by the reward function, it is possible to achieve perfect gameplay. We have tried altering and testing them, but the values of: +3 for victory, +2 for a draw, and -1 for defeat proved to be the most effective.

## Challenge the AIs!

After finishing our experiments, we thought it could be fun to challenge ourselves against the AIs we created.

They are unbeatable...

The few combinations that O fails to block are so rare and suboptimal that any human player would never play them, effectively being unable to beat the AIs (both with X and O) ever!