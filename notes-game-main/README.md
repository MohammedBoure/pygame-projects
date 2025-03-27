# Game Project with Sound Interaction

This project is part of a repository containing multiple projects. It is an interactive game that relies on sound, where real-time audio analysis is converted into musical notes that control the movement of game objects within Pygame.

## Downloading the Project Separately
You can download the project separately through the attached `Packaged-Project.rar` file, which contains all the necessary files to run the game.

## Features
- **Real-time Sound Detection**: Uses FFT to analyze audio frequencies from the microphone.
- **Frequency-to-Musical Note Conversion**: Displays the appropriate note on the screen.
- **Interactive Gameplay**:
  - The object moves based on the detected notes.
  - New objects can be added by clicking the mouse.
  - Moving lines interact with the objects.
- **Playing Notes as Sounds**: A sequence of musical notes can be played through the speaker.
- **Configurable Settings**: Game speed, object sizes, and other details can be adjusted via configuration files.

## How to Run the Project

### Requirements
- **Python 3.6+**
- **Pygame 2.x**
- **NumPy 1.x**
- **PyAudio 0.2.x**

### Steps to Run
1. Download and extract the `Packaged-Project.rar` file.
2. Navigate to the project directory:
   ```bash
   cd Packaged-Project
   ```
3. Install the dependencies:
   ```bash
   pip install pygame numpy pyaudio
   ```
4. Run the game:
   ```bash
   python main.py
   ```

## Main Files
```
Packaged-Project/
├── main.py              # Game entry point
├── _pygame.py           # Game logic and rendering
├── configofgame.py      # Game settings
├── configsound.py       # Sound settings
├── mixersound.py        # Playing notes as sound waves
├── sound_record.py      # Analyzing and displaying audio frequencies
└── functions/           
    └── f.py             # Helper functions for note processing
```

## Notes
- Ensure that your microphone is working properly before running the game.
- You can modify game and sound settings via `configofgame.py` and `configsound.py`.
- If you encounter issues, verify that all required libraries are installed.

## Future Improvements
- Add sound effects upon collision.
- Improve the accuracy of frequency detection.
- Support for custom musical note sequences.
- Enhance graphics and user interaction.

## License
This project is available under the [MIT License](LICENSE). You are free to use and modify it with proper attribution.

---

If you need any further modifications, feel free to ask! 😊

