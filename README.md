# Avoidance Game

A simple avoidance game created with Pygame. Dodge enemies, collect items, and achieve the highest score possible!

## Features

*   Neon-themed visuals for an engaging experience.
*   Player-controlled movement using keyboard or on-screen buttons.
*   Increasing difficulty with more enemies spawning over time.
*   Score tracking.
*   Game over screen with restart and quit options.

## How to Play

*   Run the game.py file using Python.
*   Use the Up, Down, Left, and Right arrow keys to move the player.
*   Alternatively, use the on-screen buttons for movement.
*   Avoid the deep purple, star-like enemies.
*   Collect the neon green items to increase your score.
*   If you collide with an enemy, the game is over.
*   Click the "Restart" button to play again or the "Quit" button to exit.

## Controls

*   **Arrow Keys:** Move the player.
*   **On-Screen Buttons:** Alternative movement controls.
*   **Escape Key:** Quit the game.

## Requirements

*   Python 3.x
*   Pygame library

## Installation

1.  Make sure you have Python 3.x installed.
2.  Install the Pygame library:

    ```
    pip install pygame
    ```

3.  Save the `game.py` file.
4.  (Optional) Save a background image as `bg.jpg` in the same directory for a more immersive experience.

## Usage

1.  Open a terminal or command prompt.
2.  Navigate to the directory where you saved `game.py`.
3.  Run the game:

    ```
    python game.py
    ```

## Customization

*   **Colors:** Modify the RGB values in the color definitions (e.g., `NEON_CYAN`, `NEON_GREEN`, `DEEP_PURPLE`) to change the game's color scheme.
*   **Player Speed:** Adjust the `base_speed` variable to control the player's movement speed.
*   **Item/Enemy Spawn Rate:** Modify the probabilities (`0.02` for items, `0.03` for enemies) to control how frequently items and enemies spawn.
*   **Maximum Items/Enemies:** Change `max_items` and `max_enemies` to set the maximum number of items and enemies on the screen at once.
*   **Background Image:** Replace `bg.jpg` with your own image to customize the background.
*   **Button Size:** Modify the `button_size` to change the size of the on-screen buttons.
*   **Speed Multiplier:** Adjust the `speed_multiplier` to change the speed boost gained when holding down a button.

## Credits

*   This game was created using the Pygame library.

## License

This project is open source. Feel free to use and modify the code as you wish.
