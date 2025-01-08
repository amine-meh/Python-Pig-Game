# Python Pig Game

This repository contains a Python-based dice rolling game for multiple players. The game allows 2 to 4 players to compete to reach a target score by rolling a dice.

## How to Play

1. **Set the Number of Players**: Players can input the number of participants (between 2 and 4).
2. **Take Turns Rolling**: Players roll a dice to accumulate points in their turn. Rolling a `1` ends the turn with no points added.
3. **Accumulate Points**: Continue rolling to add to your score, or stop to secure the accumulated points for the turn.
4. **Winning the Game**: The first player to reach a score of 50 or more wins the game.

## Features

- Supports 2 to 4 players.
- Automatic turn management.
- Real-time scoring updates.
- Interactive gameplay with user input.
- Simple and intuitive command-line interface.

## How to Run the Game

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/number_guessing_game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd number_guessing_game
   ```
3. Run the game script:
   ```bash
   python3 number_guessing_game.py
   ```

## Code Overview

### Functionality

- **Dice Roll**: The `roll()` function simulates rolling a dice and returns a random value between 1 and 6.
- **Turn Management**: Each player's turn is handled with user input to roll or stop rolling.
- **Scoring**: Scores are tracked and updated for each player.
- **Win Condition**: The game checks for a player reaching the maximum score of 50.

### Code Structure

```python
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Game Initialization
while True:
    players_number = input("Enter the number of players for this turn (2 - 4): ")
    if players_number.isdigit():
        players_number = int(players_number)
        if 2 <= players_number <= 4:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number between 2 and 4.")

max_score = 50
players_score = [0 for _ in range(players_number)]

# Main Game Loop
while max(players_score) < max_score:
    for player_index in range(players_number):
        print("\nPlayer number:", player_index + 1, "turn has just started!")
        print("\nYour total score is", players_score[player_index], "\n")
        current_score = 0

        while True:
            start_rolling = input("Would you like to roll the dice (y): ").lower()
            if start_rolling != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1! Your turn is done.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled", value)

            print("Your score is", current_score)

        players_score[player_index] += current_score
        print("Your total score is", players_score[player_index])

# Determine Winner
max_score = max(players_score)
wining_index = players_score.index(max_score)
print("Player number:", wining_index + 1, "is the winner with a score of", max_score)
```

## Requirements

- Python 3.6 or higher

## Future Enhancements

- Add a graphical user interface (GUI).
- Allow customization of the target score.
- Add player names instead of using player numbers.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.


