# 🐍 Snake

A classic Snake Game implemented in `pygame-ce`.  
The player controls a snake that grows longer each time it eats food. The game ends when the snake collides with itself or the window boundaries.

This project demonstrates real-time rendering, collision detection, keyboard event handling, and simple game logic — all implemented with clean Python code.

## ✨ Features

- **Classic Gameplay**
  - Control the snake using arrow keys.
  - Grow longer by eating food.
  - Avoid collisions with walls and yourself.

- **Dynamic Food Spawning**
  - Food appears at random positions.
  - Food never overlaps with the snake’s body.

- **Scoring System**
  - The snake’s length reflects your score.
  - Final score is displayed when the game ends.

- **Restart System**
  - Press `SPACE` after death to instantly restart.

- **Configurable Settings**
  - Adjustable speed, frame rate, growth rate, and window dimensions. (Easily configurable in the code)

## 🎮 Controls

| Key            | Action              |
| -------------- | ------------------- |
| ⬆️ Up Arrow    | Move Up             |
| ⬇️ Down Arrow  | Move Down           |
| ⬅️ Left Arrow  | Move Left           |
| ➡️ Right Arrow | Move Right          |
| ␣ Spacebar    | Restart after death |
| ❌ Close Window | Quit the game       |

## 🛠️ Tech Highlights

- Built with Pygame-ce for graphics, input, and collision detection.
- Uses `pygame.Rect` objects for efficient movement and hitbox logic.
- Clean `Player` class to manage snake state.
- Self-collision detection.
- Configurable constants for quick gameplay tweaking.

## 🖼️ Gallery

<p align="left">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/e0bda87e-97cd-46c4-b2e8-90c39418feba"/>
</p>

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/TubeDev/Snake-Game.git
   cd Snake-Game
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python Snake.py
   ```

After running the main script, a window should open.  
Enjoy the game!

---

### 📜 License

This project is licensed under the [**MIT License**](https://opensource.org/licenses/MIT).  
You are free to use, modify, and distribute this project as permitted by the license.

![TubeDev](https://img.shields.io/badge/TubeDev--lime)
![Python](https://img.shields.io/badge/Python--blue?logo=python&logoColor=white)
![MIT](https://img.shields.io/badge/License-MIT-gold)

<p align="left">
  <img width="500" src="https://github.com/user-attachments/assets/f5a0f154-dee7-4653-9451-caa52513573a" alt="logo" />

</p>
