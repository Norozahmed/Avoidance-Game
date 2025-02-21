# Avoidance Game

## Overview

This is a simple avoidance game created using Pygame. The player controls a neon cyan circle and must avoid deep purple enemies while collecting neon green items to increase their score.

## Features

*   **Player Control:** Move the player using the arrow keys or on-screen buttons.
*   **Items:** Collect neon green items to increase your score.
*   **Enemies:** Avoid deep purple enemies that move across the screen.
*   **Score:** Track your score by collecting items.
*   **Game Over:** The game ends when the player collides with an enemy.
*   **Restart/Quit:** Options to restart or quit the game after game over.
*   **Sound Effects:** Includes background music and sound effects for item collection, player hits, and button clicks.

## How to Play

1.  **Requirements:**
    *   Python 3
    *   Pygame library

2.  **Installation:**

    *   Make sure you have Python 3 installed.
    *   Install Pygame:

        ```
        pip install pygame
        ```

3.  **Running the Game:**

    *   Save the `game.py` file and the `bg.jpg` background image (optional, but recommended) in the same directory.
    *   Also, place the sound files (`backgroundsound.mp3`, `itemsCollect.mp3`, `hitsound.mp3`, `game-start.mp3`, `quite.mp3`) in the same directory.
    *   Open a terminal or command prompt, navigate to the directory, and run:

        ```
        python game.py
        ```

4.  **Controls:**

    *   **Arrow Keys:** Move the player up, down, left, and right.
    *   **On-Screen Buttons:** Use the on-screen buttons for movement (alternative to arrow keys).
    *   **ESC Key:** Quit the game.
    *   **Mouse:** Click the "Restart" button to start a new game after game over, or click "Quit" to exit the game.

## Game Mechanics

*   **Objective:** Avoid the enemies and collect items to score points.
*   **Player:**
    *   Controlled by the player using arrow keys or on-screen buttons.
    *   If the player collides with an enemy, the game is over.
*   **Items:**
    *   Spawn randomly on the screen.
    *   Collecting an item increases the player's score.
*   **Enemies:**
    *   Spawn on the right side of the screen and move towards the left.
    *   The player must avoid colliding with them.
*   **On-Screen Buttons:**
    *   Alternative to arrow keys for controlling player movement.
    *   Highlight on hover and stay highlighted when pressed (for continuous movement).

## Customization

*   **Colors:** You can change the colors of the player, items, enemies, outlines, and text by modifying the RGB values in the `game.py` file.
*   **Background:** Replace the `bg.jpg` file with your own background image.  If you don't have a `bg.jpg` file, the game will default to a black background.
*   **Sound Effects:**  You can change the sound effects by replacing the `.mp3` files with your own. Ensure that the file names in the code match your sound file names. You can also adjust the volume levels for each sound.
*   **Game Difficulty:** Adjust the `base_speed`, `max_items`, `max_enemies`, and enemy speed range (`random.randint(2, 5)`) to modify the game's difficulty.

## Credits

*   This game was created using Pygame.

## License

This project is open source and It is for Learning purposes.
