# Jump-and-Run

"Jump and Run" is an action-packed 2D platformer where players control a character running to avoid obstacles. Players use on-screen buttons to jump and move, while obstacles appear slowly from random directions. The goal is to survive as long as possible while earning high scores.



# Stack Usage for Game Logic and Optimization

(1) Game Framework: It’s built using Pygame, which helps with graphics, animations, and handling user input like mouse clicks.

(2) Classes and Objects: The game organizes different parts into "blueprints" called classes:

- The Player class manages the character’s movement and jumping.
- The Obstacle class handles moving obstacles.
- The Button class creates clickable buttons for user control.

(3) Player Controls: Players can move the character using on-screen buttons like "Move Up" or "Jump."

(4) Collision Detection: The game checks if the player touches an obstacle, which ends the game.

(5) Random Obstacles: Obstacles appear randomly at different positions to make the game more challenging and unpredictable.

(6) Score System: Every obstacle avoided increases the score, which is displayed on the screen.

(7) Visuals and Interaction: The game features a background, a larger character and obstacles, and colorful buttons for a user-friendly experience.

(8) Performance: It removes obstacles once they’re off the screen to keep the game running smoothly.

- I am still working on it. So there might be additional backend support in future as well. I still need to figure out a few more concepts before I start doing so.
- For now, I am aiming to develop it primarily accessible and efficient for users. 
- might include low-level custom implementations as well using C++ and C
- 2D or 3D game flavours can be implemented in enhanced implementation as well, which I look forward to working for.









- Work in progress
