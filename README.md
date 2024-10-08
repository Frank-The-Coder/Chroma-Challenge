# Chroma Challenge

**Chroma Challenge** is an interactive game developed in C for the Nios II FPGA board. The game tests players' color identification skills by combining visual and cognitive challenges. Utilizing VGA technology, it offers engaging graphics and sound effects to create an immersive gameplay experience.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Gameplay](#gameplay)
- [Controls](#controls)
- [Game Mechanics](#game-mechanics)
- [Implementation Details](#implementation-details)
- [Visual and Audio Design](#visual-and-audio-design)
- [License](#license)

## Introduction

Chroma Challenge is designed to test and improve players' ability to quickly identify colors under time pressure. The game displays colored words against random background colors, and players must respond correctly before time runs out. With increasing difficulty levels and dynamic feedback, it offers a fun and challenging experience.

## Features

- **Color Identification Challenge**: Tests players' ability to recognize colors of words or backgrounds.
- **Dynamic Difficulty**: Progress bar speeds up with each successful round, increasing the challenge.
- **Lives System**: Players start with 5 lives, adding stakes to each decision.
- **Visual Feedback**: Engaging graphics using VGA technology with double buffering for smooth animations.
- **Audio Feedback**: Sound effects for incorrect answers and game over events.
- **User-Friendly Controls**: Simple keyboard inputs to interact with the game.

## Gameplay

- The game displays a word representing a color (e.g., "Red") in a font color that may differ from the word's meaning.
- The background color is set to a random color different from the font color.
- An instruction at the top of the screen tells the player to input the initial of the color of either the **word's text** or the **background**.
- A progress bar at the bottom of the screen indicates the time remaining to answer.
- Players must input the correct key before the progress bar fills up or lose a life.
- The game starts with 5 lives displayed on the HEX display of the FPGA board.
- The difficulty increases as the progress bar speeds up with each round passed.
- The game ends when the player loses all lives.

## Controls

- **Keyboard Input**:
  - Press the **initial letter** of the correct color as instructed.
    - For example, press **'R'** for Red, **'G'** for Green, **'B'** for Blue.
- **Color Initials**:
  - **R**: Red
  - **G**: Green
  - **B**: Blue
  - **Y**: Yellow
  - **O**: Orange
  - **P**: Purple

## Game Mechanics

- **Lives System**:
  - Players start with **5 lives**.
  - Lose a life if:
    - The progress bar fills up before answering.
    - An incorrect key is pressed.
  - Lives are displayed on the FPGA's HEX display.
- **Progress Bar**:
  - Visual timer that progresses from left to right.
  - Speeds up slightly with each correct answer.
  - Resets after each round.
- **Difficulty Scaling**:
  - The game becomes progressively harder as the progress bar accelerates.
  - Challenges the player's quick thinking and reaction time.
- **Feedback**:
  - **Correct Answer**: Progress to the next round; the progress bar resets and speeds up.
  - **Incorrect Answer or Timeout**: Lose a life, and the game provides audio and visual feedback.

## Implementation Details

- **Programming Language**: C
- **Platform**: Nios II FPGA Board
- **Graphics**:
  - Utilizes **VGA technology** for display output.
  - Implements **double buffering** for smooth visual animations.
- **Audio Output**:
  - Integrated sound effects for incorrect answers and game over.
  - Managed through the FPGA's audio output capabilities.
- **Input Handling**:
  - Receives keyboard input via PS/2 or USB interface on the FPGA board.
  - Processes key presses in real-time to update game state.

## Visual and Audio Design

- **Visual Elements**:
  - Randomized background and font colors for each round.
  - Clear instructions displayed at the top of the screen.
  - Progress bar at the bottom indicating time remaining.
  - Smooth transitions and animations using double buffering.
- **Audio Elements**:
  - Sound effect for incorrect answers to alert the player.
  - Distinct sound for game over to signal the end of the game.
- **User Interface**:
  - Clean and intuitive layout.
  - Lives count displayed on the FPGA's HEX display for easy tracking.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This game was developed collaboratively, and the code is optimized for the Nios II FPGA board, which runs a single C file. The full source code is available in the repository.

---

_For any questions or contributions, please feel free to open an issue or submit a pull request._
