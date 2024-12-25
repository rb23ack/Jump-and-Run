# Jump-and-Run

"Jump and Run" is an action-packed 2D platformer where players control a character running to avoid obstacles. Players use on-screen buttons to jump and move, while obstacles appear slowly from random directions. The goal is to survive as long as possible while earning high scores.



# Stack Usage for Game Logic and Optimization


- Game Loop: The main loop runs the game and handles all logic like player input, movement, obstacle generation, and collision detection.
  
- Event Handling: When processing events, Python uses the event queue but doesn't rely on a stack for event handling.
  
- Memory Management: Objects (like obstacles and the player) are created and destroyed dynamically. Python’s garbage collector handles cleanup, so we don't need to worry about managing memory manually with a stack.


















- Work in progress
