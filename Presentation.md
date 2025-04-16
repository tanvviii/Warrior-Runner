# Warrior-Runner Game in Python - Terminal Based

## Why is implementing Warrior Runner harder than implementing Tetris?

Warrior Runner offers a more dynamic and visually engaging experience compared to Tetris. While Tetris is a timeless puzzle game focused on logic and spatial reasoning, Warrior Runner features action-packed gameplay with animated characters, enemy interactions, and real-time controls. It allows players to actively control a character, making it feel more immersive. For game developers, Warrior Runner is a better learning tool as it involves working with animations, collisions, sound, and modular code — offering more creative possibilities and expansion potential than the simpler mechanics of Tetris.

___
## *Project Modeling in Warrior-Runner*

Based on the GitHub repository shared (Warrior-Runner), here’s how things appear to be modeled in this 2D endless runner game:

### Core Game Elements

#### *Player Character*
•⁠  ⁠Modeled as a warrior with running, jumping, and attacking animations.
•⁠  ⁠Likely implemented as a sprite with physics properties (rigidbody, colliders).

#### *Obstacles/Enemies*
•⁠  ⁠Various obstacles that the player must jump over or attack.
•⁠  ⁠Probably implemented as prefabs with colliders for interaction detection.

#### *Environment*
•⁠  ⁠Parallax scrolling background layers.
•⁠  ⁠Ground segments that generate procedurally as the player runs.

---

### Technical Modeling

#### *Game States*
•⁠  ⁠Menu state.
•⁠  ⁠Playing state.
•⁠  ⁠Game over state.
•⁠  ⁠Pause state.

#### *Movement System*
•⁠  ⁠Player movement (running forward automatically).
•⁠  ⁠Jump mechanics (likely using Unity's physics system).
•⁠  ⁠Attack animations and hit detection.

#### *Scoring/Progress*
•⁠  ⁠Distance-based scoring.
•⁠  ⁠Possibly coin/collectible system.

#### *Object Pooling*
•⁠  ⁠For efficient obstacle/enemy generation and recycling.

___

### *Key Challenges in Warrior Runner* : 

1. *Increasing Speed Over Time*
 - The game's speed ramps up as the player survives longer, reducing reaction time and increasing difficulty progressively.

2. *Obstacle Timing & Coordination*
  - Players must jump or avoid obstacles (like cacti or other objects) with precise timing. Missteps mean immediate failure.

3. *Limited Player Control*
  - With only basic inputs (jump/run), the game tests reflexes and not strategy. It's a pure test of timing and focus.

4. *No Power-ups or Saves*
  - There are no boosters, lives, or checkpoints. One mistake means restarting, adding pressure and tension.

5. *Endless Nature*
  - The game has no defined end. It's all about survival time and high score, pushing players into a loop of self-competition.

6. *Minimal Visual Cues*
  - Inspired by the minimalistic T-Rex aesthetic, this design means you rely entirely on twitch reflexes—no fancy HUDs or warnings.

//overall line remaining

# (emoji) *Warrior-Runner Game in Python - Terminal Based*

Welcome to the Warrior Runner Game in Python (Pygame). 

A fast-paced, side-scrolling endless runner that puts you in control of a pixel-art warrior dodging obstacles, defeating enemies, and surviving for as long as possible. Built with Python and Pygame, this game showcases interactive gameplay, smooth animation, and modular code architecture — all packed into a well-structured multi-file project.

This document provides a comprehensive overview of the entire project, including:

🎯 Game Objective and User Experience

🧠 Code Architecture and Modules

🎮 Input Controls

❤️ Health and Collision Systems

🎨 Visual and Audio Assets

⚙️ How to Run and Play

📚 Educational Insights and Learning Outcomes

___

## 🔖 *Metadata and Project Overview*

___

## 🎯 *Game Objective*

The game Warrior-Runner is an endless running game inspired by Google's Chrome T-Rex game. In this game, players control a character that continuously runs forward, and the objective is to avoid obstacles for as long as possible to achieve a high score. The game is implemented in Python and is available on GitHub

___

## 📁 *Folder and File Structure*

```bash
warrior-runner/
│
├── main.py              # Entry point – runs the game loop
├── requirements.txt     # Dependencies
├── README.md            # Project info
├── .gitignore           # Git settings
│
└── warrior_runner/      # Game package
    ├── _init_.py
    ├── assets/          # Sprites, sounds, fonts
    ├── player.py        # Handles player character
    ├── obstacles.py     # Handles obstacles/enemies
    ├── game.py          # Main game logic
    └── utils.py         # Helper functions
```
___
## *Flowchart*

## 💡*Game Features*

| Feature             | Description                                                        |
|--------------------|--------------------------------------------------------------------|
| Endless Runner     | Inspired by Google's T-Rex game, players navigate obstacles endlessly. |
| Warrior Character  | Play as a warrior with unique animations and abilities.            |
| Obstacle Manager   | Dynamic obstacle generation and management to challenge players.   |
| Power-Up System    | Collect power-ups to gain temporary advantages during gameplay.    |
| Parallax Scrolling | Multi-layered background movement for immersive visuals.           |
| Lives System       | Players start with 3 lives, represented visually by heart icons.   |
| Score Tracking     | Tracks current and best scores, with speed increasing as score rises. |
| Menu System        | Includes start, restart, and game-over menus with interactive options. |
| Background Music   | Engaging soundtracks that change between menu and gameplay.        |


___
## 🎮 *Game Controls*

| Key         | Action                     |
|-------------|----------------------------|
| ⁠ Arrow Up ⁠  | Jump                      |
| ⁠ Arrow Down ⁠| Duck                      |
| ⁠ Space ⁠     | Activate Power-Up         |
| ⁠ P ⁠         | Pause/Resume Game         |
| ⁠ Esc ⁠       | Quit Game                 |

___
## 🛠️*Code Architecture*

The game is encapsulated within a class named ⁠ Game ⁠, which includes both the game state and its operations. It manages the main game loop, event handling, rendering, and updates for all components such as the player, obstacles, and power-ups. The architecture is modular, with dedicated managers for obstacles and power-ups, ensuring scalability and maintainability.

### *Core Data Members*

•⁠  ⁠⁠ Warrior player ⁠ – Represents the main character of the game with attributes like position and type.
•⁠  ⁠⁠ ObstacleManager obstacle_manager ⁠ – Manages obstacles, including their creation, updates, and collisions.
•⁠  ⁠⁠ PowerUpManager power_up_manager ⁠ – Handles power-ups, their spawning, activation, and duration.
•⁠  ⁠⁠ int lives_left ⁠ – Tracks the number of lives the player has left (starts at 3).
•⁠  ⁠⁠ int score ⁠ – Keeps track of the current score during gameplay.
•⁠  ⁠⁠ int best_score ⁠ – Stores the highest score achieved across all game sessions.
•⁠  ⁠⁠ float game_speed ⁠ – Determines the movement speed of objects, increases as score rises.
•⁠  ⁠⁠ list heart_vec ⁠ – Stores the current heart images to visually represent lives on the screen.
•⁠  ⁠⁠ list x_pos_bg ⁠ – X-axis positions for parallax background layers to create scrolling effects.
•⁠  ⁠⁠ pygame.Surface screen ⁠ – Game window where all rendering is performed.

### *Core Functions*

| Function         | Purpose                                      |
|------------------|----------------------------------------------|
| ⁠ execute() ⁠      | Starts the main menu loop and initializes the game. |
| ⁠ run() ⁠          | Begins the gameplay loop, handling events, updates, and rendering. |
| ⁠ reset() ⁠        | Resets game variables like lives, score, and speed. |
| ⁠ events() ⁠       | Processes user inputs and system events (e.g., quit). |
| ⁠ update() ⁠       | Updates the state of the player, obstacles, power-ups, and score. |
| ⁠ update_score() ⁠ | Increments the score and adjusts game speed at milestones. |
| ⁠ update_heart() ⁠ | Updates the visual representation of lives left. |
| ⁠ draw_text() ⁠    | Renders text on the screen at specified positions. |
| ⁠ draw_score() ⁠   | Displays the current score with a shadow effect. |
| ⁠ draw_hearts_left() ⁠ | Draws heart icons to represent remaining lives. |
| ⁠ draw_power_up_time() ⁠ | Displays the remaining duration of active power-ups. |
| ⁠ draw() ⁠         | Handles rendering of all game elements (background, player, obstacles, etc.). |
| ⁠ parallax() ⁠     | Implements parallax scrolling for multi-layered backgrounds. |
| ⁠ show_menu() ⁠    | Displays the start or game-over menu based on game state. |
| ⁠ handle_events_on_menu() ⁠ | Processes menu-specific events like starting or quitting the game. |

This table outlines the core functions that drive the Warrior Runner game’s mechanics and visuals. Let me know if you need further elaboration or additional sections!

___
## *Data Structures used in Project*

The game utilizes several fundamental data structures to manage game objects, state, and rendering. Here's a breakdown:

## *1. Lists (Arrays)*
•⁠  ⁠*Primary Purpose*: Storing and managing multiple game objects
•⁠  ⁠*Key Uses*:
  - ⁠ self.heart_vec = [HEARTS[0]] * 3 ⁠ - Tracks lives (hearts) as a list of images
  - ⁠ self.x_pos_bg = [0, 0, 0, 0, 0] ⁠ - Stores positions for parallax background layers
  - Obstacle and power-up collections in ⁠ ObstacleManager ⁠ and ⁠ PowerUpManager ⁠ classes

## *2. Dictionaries*
•⁠  ⁠*Primary Purpose*: Mapping keys to values for efficient lookups
•⁠  ⁠*Key Uses*:
  - Image/sound resources (constants like ⁠ HEARTS ⁠, ⁠ SCORE ⁠, etc.)
  - Power-up type mappings (likely used internally in ⁠ PowerUpManager ⁠)

## *3. Classes (Custom Objects)*
•⁠  ⁠*Primary Purpose*: Organizing game entities and logic
•⁠  ⁠*Key Classes*:
  - ⁠ Warrior ⁠ - Player character with state (position, power-ups, etc.)
  - ⁠ ObstacleManager ⁠ - Handles obstacle spawning/updating using lists
  - ⁠ PowerUpManager ⁠ - Manages power-up spawns and effects

## *4. Queues (Conceptual)*
•⁠  ⁠*Primary Purpose*: Managing object spawn timing
•⁠  ⁠*Implementation*:
  - Obstacles and power-ups spawn sequentially (though not a formal queue structure)
  - Event timing uses ⁠ pygame.time.get_ticks() ⁠

## *5. State Variables (Primitives)*
•⁠  ⁠*Primary Purpose*: Tracking game conditions
•⁠  ⁠*Examples*:
  - ⁠ self.score ⁠ (integer)
  - ⁠ self.game_speed ⁠ (integer)
  - ⁠ self.playing ⁠ (boolean)

## *Why These Structures?*
•⁠  ⁠*Lists*: Ideal for dynamic collections needing frequent iteration (e.g., drawing all obstacles)
•⁠  ⁠*Dictionaries*: Efficient lookups for resources/configuration
•⁠  ⁠*Classes*: Encapsulation of game object logic (player, enemies, etc.)
•⁠  ⁠*No complex structures needed*: The game's simplicity avoids trees/graphs

The design focuses on *O(1) access* for critical operations (e.g., player input) and *O(n) iteration* for rendering/updating objects—a optimal tradeoff for a 2D runner.

---
## **Description of some functions used in the game**

The `Obstacle` class represents obstacles that the player's character must avoid or jump over in the game. These could be things like rocks, pits, or other barriers.

### Role and Functionality:

1. **Inheritance**: 
   - The class inherits from `pygame.sprite.Sprite`, which provides basic sprite functionality.

2. **Initialization (`__init__`)**:
   - Takes an image (likely a sprite sheet or animation sequence) and a type (to select which frame/variant to use)
   - Sets up the obstacle's visual representation (`self.image`), position (`self.rect`), and collision mask (`self.mask`)
   - Positions the obstacle just off the right side of the screen (`SCREEN_WIDTH`)

3. **Update Method**:
   - Moves the obstacle leftward across the screen at the game's speed (`self.rect.x -= game_speed`)
   - Removes the obstacle from the obstacles list when it moves completely off the left side of the screen
   - This creates the illusion of the player character running past stationary obstacles

4. **Draw Method**:
   - Renders the obstacle on the screen at its current position

### How It Fits in the Game:
- This class would be used to create and manage all obstacles in your endless runner game
- Multiple instances would be created at intervals to challenge the player
- The game would check for collisions between the player character and these obstacles
- The leftward movement creates the endless runner effect where obstacles approach the player

### Key Features:
- Uses Pygame's sprite system for efficient rendering and collision detection
- Includes a mask for pixel-perfect collision detection (important for irregularly shaped obstacles)
- Automatically cleans up obstacles that have moved off-screen
- Supports different obstacle types/variants through the `type` parameter

  
#### ⁠ def update_score(self) ⁠
•⁠  ⁠*Purpose*: Tracks and updates the player’s score during gameplay.
•⁠  ⁠*Functionality*: 
  - Increases the score by 1 each frame (or tick).
  - Increments the game speed by 2 every time the score is a multiple of 100, progressively increasing difficulty.
•⁠  ⁠*Use*: Ensures the player’s progress is reflected and adjusts the challenge dynamically.
  ```python
  def update_score(self):
      self.score += 1
      if self.score % 100 == 0:
          self.game_speed += 2
```

---

## 📊 Sample Gameplay Screenshots

### 🧩 Initial Game Grid

The Warrior-Runner game is a side-scrolling endless runner, not based on a grid system. Instead, it uses pixel-based coordinates to manage player and obstacle positions on a continuous horizontal plane. Screen dimensions define the playable area, and all movement is smooth and continuous, not tile-based.

---

## 🔍 How to Compile and Run

### Requirements
Open your terminal or command prompt and run:

*git clone https://github.com/tanvviii/Warrior-Runner.git*
*cd Warrior-Runner&*

### Compile
Install the required Python packages using pip:

*pip install -r requirements.txt*

### Run
Execute the main Python script to start the game:

*python main.py*

---

## 🧠 Learning Outcomes

- **OOP in Games**  
  - Use inheritance, encapsulation, and polymorphism to structure characters and obstacles.

- **Game Loop & Events**  
  - Understand how real-time input and updates drive the game.

- **Collision & Obstacle Handling**  
  - Implement obstacle generation, movement, and collision detection.

- **Sprite Animation**  
  - Use frame-based animations for characters and enemies.

- **Project Structure**  
  - Explore real-world project organization and GitHub collaboration.

---
## *Future Work Suggestions for Warrior-Runner*



Based on the project's current state, here are several directions for future development:



---



### Gameplay Enhancements



#### *New Character Abilities*

•⁠  ⁠Double jumps or dash moves

•⁠  ⁠Special attacks with cooldowns

•⁠  ⁠Character classes with unique skills



#### *Expanded Obstacle System*

•⁠  ⁠Moving/platform obstacles

•⁠  ⁠Environmental hazards (fire, spikes, etc.)

•⁠  ⁠Boss encounters at milestones



#### *Progression System*

•⁠  ⁠Character upgrades/unlockables

•⁠  ⁠Skill trees or ability progression

•⁠  ⁠Daily/weekly challenges



---



### Technical Improvements



#### *Performance Optimization*

•⁠  ⁠Enhanced object pooling

•⁠  ⁠Background loading/unloading

•⁠  ⁠Improved asset management



#### *Advanced Visuals*

•⁠  ⁠Dynamic lighting effects

•⁠  ⁠Weather/day-night cycles

•⁠  ⁠More detailed animations



#### *AI Enhancements*

•⁠  ⁠Smarter enemy behaviors

•⁠  ⁠Adaptive difficulty scaling

•⁠  ⁠Procedural obstacle generation



---



### Content Expansion



#### *New Environments*

•⁠  ⁠Different thematic worlds (desert, ice, forest)

•⁠  ⁠Interactive background elements



#### *Multiplayer Features*

•⁠  ⁠Local co-op mode

•⁠  ⁠Online leaderboards

•⁠  ⁠Ghost runs (compete against others' best times)



#### *Meta Game Systems*

•⁠  ⁠Achievements system

•⁠  ⁠Cosmetic unlocks

•⁠  ⁠Story elements/narrative progression

---
## *Future Work Suggestions for Warrior-Runner*

Based on the project's current state, here are several directions for future development:

### Gameplay Enhancements

#### *New Character Abilities*
•⁠  ⁠Double jumps or dash moves
•⁠  ⁠Special attacks with cooldowns
•⁠  ⁠Character classes with unique skills

#### *Expanded Obstacle System*
•⁠  ⁠Moving/platform obstacles
•⁠  ⁠Environmental hazards (fire, spikes, etc.)
•⁠  ⁠Boss encounters at milestones

#### *Progression System*
•⁠  ⁠Character upgrades/unlockables
•⁠  ⁠Skill trees or ability progression
•⁠  ⁠Daily/weekly challenges

---

### Technical Improvements

#### *Performance Optimization*
•⁠  ⁠Enhanced object pooling
•⁠  ⁠Background loading/unloading
•⁠  ⁠Improved asset management

#### *Advanced Visuals*
•⁠  ⁠Dynamic lighting effects
•⁠  ⁠Weather/day-night cycles
•⁠  ⁠More detailed animations

#### *AI Enhancements*
•⁠  ⁠Smarter enemy behaviors
•⁠  ⁠Adaptive difficulty scaling
•⁠  ⁠Procedural obstacle generation

---

### Content Expansion

#### *New Environments*
•⁠  ⁠Different thematic worlds (desert, ice, forest)
•⁠  ⁠Interactive background elements

#### *Multiplayer Features*
•⁠  ⁠Local co-op mode
•⁠  ⁠Online leaderboards
•⁠  ⁠Ghost runs (compete against others' best times)

#### *Meta Game Systems*
•⁠  ⁠Achievements system
•⁠  ⁠Cosmetic unlocks
•⁠  ⁠Story elements/narrative progression

---

...
