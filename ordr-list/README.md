# Visualization of Bubble Sort using Pygame

## Description
This project is a simple visualization of the **Bubble Sort** algorithm using **Pygame**. The program generates a list of random integers, scales them to fit the screen, and then sorts them using Bubble Sort while displaying the sorting process in real-time.

## Features
- Uses **Pygame** to visualize the sorting process.
- Generates **400 random numbers** between 1 and 100.
- Adjusts the height of the bars dynamically based on the maximum number.
- Animates the sorting process with a delay.

## Requirements
Make sure you have Python installed along with the required dependencies:

```bash
pip install pygame
```

## How to Run
1. Clone or download this repository.
2. Open a terminal or command prompt in the project directory.
3. Run the script using:
   ```bash
   python main.py
   ```
4. The visualization will start, showing the sorting process in action.
5. To exit, close the Pygame window.

## Code Explanation
- The script initializes a **Pygame window** with a white background.
- A **random list** of 400 integers (1-100) is generated.
- The numbers are scaled to fit the screen height.
- **Bubble Sort** is applied, swapping elements step by step while redrawing the screen.
- **Delays** are used to allow real-time visualization of sorting.

## Controls
- The program **automatically starts sorting** when executed.
- To **exit**, simply close the window.

## Future Improvements
- Add support for different sorting algorithms (Insertion Sort, Quick Sort, Merge Sort, etc.).
- Allow user interaction (e.g., start/pause sorting, adjust speed).
- Improve visualization with different colors to highlight swaps.

---
Created with ❤️ using **Python & Pygame**

