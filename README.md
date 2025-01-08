# Virtual Keyboard with Hand Gesture Recognition

This project implements a virtual keyboard that detects hand gestures using a webcam and converts them into letters based on predefined gesture mappings. The program uses **OpenCV** for image processing and **MediaPipe** for hand tracking.

## Features
- **Real-time hand gesture detection**: Recognizes the number of fingers raised on each hand.
- **Text generation**: Converts gestures into corresponding letters and appends them to a text.
- **Save detected text**: Outputs the detected text to a file named `detected_text.txt`.
- **On-screen display**: Shows the real-time detected letter and the full text on the video feed.

## Gesture Mapping
Each combination of fingers raised on the left and right hands corresponds to a specific letter:

| Left Hand Fingers | Right Hand Fingers | Letter |
|-------------------|--------------------|--------|
| 1                 | 0                  | A      |
| 2                 | 0                  | B      |
| 3                 | 0                  | C      |
| 4                 | 0                  | D      |
| 0                 | 1                  | E      |
| 0                 | 2                  | F      |
| ...               | ...                | ...    |
| 5                 | 0                  | Z      |

## Requirements
To run this project, you need:

- Python 3.7 or higher
- OpenCV
- MediaPipe

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install opencv-python mediapipe
   ```

## Usage
1. Run the script:
   ```bash
   python <script-name>.py
   ```
2. Allow access to your webcam.
3. Perform gestures with your hands to see the corresponding letters displayed on the screen.
4. The detected text will be saved in `detected_text.txt`.
5. Press `ESC` to exit the program.

## Files
- `script.py`: The main script for hand gesture detection and text generation.
- `detected_text.txt`: The output file where the detected text is stored.

## Future Improvements
- Add support for more gestures.
- Improve robustness under varying lighting conditions.
- Implement multi-language gesture support.

## Acknowledgments
- [OpenCV](https://opencv.org/) for image processing.
- [MediaPipe](https://mediapipe.dev/) for hand tracking.

---

Feel free to contribute or suggest improvements!
