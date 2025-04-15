# Warrior-Runner Game in C++ - Terminal Based

## Why is implementing Warrior Runner harder than implementing Tetris?

Warrior Runner offers a more dynamic and visually engaging experience compared to Tetris. While Tetris is a timeless puzzle game focused on logic and spatial reasoning, Warrior Runner features action-packed gameplay with animated characters, enemy interactions, and real-time controls. It allows players to actively control a character, making it feel more immersive. For game developers, Warrior Runner is a better learning tool as it involves working with animations, collisions, sound, and modular code — offering more creative possibilities and expansion potential than the simpler mechanics of Tetris.

### Key Challenges in Warrior Runner : 

1. *Increasing Speed Over Time
 - The game's speed ramps up as the player survives longer, reducing reaction time and increasing difficulty progressively.

2. *Obstacle Timing & Coordination
  - Players must jump or avoid obstacles (like cacti or other objects) with precise timing. Missteps mean immediate failure.

3. *Limited Player Control
  - With only basic inputs (jump/run), the game tests reflexes and not strategy. It's a pure test of timing and focus.

4. *No Power-ups or Saves
  - There are no boosters, lives, or checkpoints. One mistake means restarting, adding pressure and tension.

5. *Endless Nature
  - The game has no defined end. It's all about survival time and high score, pushing players into a loop of self-competition.

6. *Minimal Visual Cues
  - Inspired by the minimalistic T-Rex aesthetic, this design means you rely entirely on twitch reflexes—no fancy HUDs or warnings.

//overall line remaining

# (emoji) Warrior-Runner Game in C++ - Terminal Based

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

## 🔖 Metadata and Project Overview

___

## 🎯 Game Objective

The game Warrior-Runner is an endless running game inspired by Google's Chrome T-Rex game. In this game, players control a character that continuously runs forward, and the objective is to avoid obstacles for as long as possible to achieve a high score. The game is implemented in Python and is available on GitHub

___

## 📁 Folder and File Structure

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
## Flowchart

## 💡 Game Features

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
## 🎮 Game Controls

| Key         | Action                     |
|-------------|----------------------------|
| ⁠ Arrow Up ⁠  | Jump                      |
| ⁠ Arrow Down ⁠| Duck                      |
| ⁠ Space ⁠     | Activate Power-Up         |
| ⁠ P ⁠         | Pause/Resume Game         |
| ⁠ Esc ⁠       | Quit Game                 |

___
## 🛠️ Code Architecture

### Core Data Members

### Core Functions


---
## **Description of some functions used in the game**


---

## 📊 Sample Gameplay Screenshots


### 🧩 Initial Game Grid


---

## 🔍 How to Compile and Run

### Requirements

### Compile

### Run


---

## 🧠 Learning Outcomes


---

## 📖 License


---

## 🧑‍💻 Contribution Guide


---

## ✍️ Acknowledgments


---

## 📌 Summary


---

...
