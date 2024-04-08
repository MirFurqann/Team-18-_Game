Pygame Number Game
Welcome to the Pygame Number Game repository! This project is a simple yet engaging game developed using Pygame, where players (the user and the computer) take turns removing numbers from a list, aiming to reduce their score to a target value. The game incorporates basic AI for the computer's moves, utilizing either the Minimax or Alpha-Beta pruning algorithm based on the player's choice.

Features
Interactive GUI to play the game.
User vs. Computer gameplay.
Choice of algorithm for computer moves: Minimax or Alpha-Beta pruning.
Sound effects for user and computer moves.
Dynamic game settings including adjustable string length.
Prerequisites
Before you start, ensure you have the following installed:

Python 3.x
Pygame library
Installation
Clone this repository to your local machine using:


git clone [https://github.com/MirFurqann/Team-18-_Game.git]
Navigate into the project directory:

Ensure you have Pygame installed. If not, you can install it via pip:

pip install pygame
Running the Game
To run the game, execute the following command in the project directory:


python main.py
Follow the on-screen prompts to choose the starting player, the algorithm for the computer's moves, and the length of the number string.

Game Instructions
Starting the Game: The game starts with a prompt asking who should start the game, the user or the computer, and which algorithm to use for the computer's moves.
Playing the Game: Players take turns to remove numbers from the list. For the user, click and drag the number you wish to remove and drop it in the designated area. The computer's move will be automatically decided based on the chosen algorithm.
Winning the Game: The game ends when all numbers are removed. The player with the lowest score wins.
Sound Effects
This game includes sound effects for both user and computer moves to enhance the gameplay experience. Ensure your device's volume is adjusted accordingly.

user_move.mp3: Played when the user makes a move.
computer_move.mp3: Played when the computer makes a move.
Contributing
Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.
