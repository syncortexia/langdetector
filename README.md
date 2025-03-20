# Language Detector

A simple GUI application that detects the language of input text using the `langdetect` module.

## Features

- Clean and intuitive graphical user interface
- Supports detection of over 100 languages
- Displays both language code and full language name
- Real-time language detection

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- langdetect module

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python language_detector.py
   ```
2. Enter any text in the input field
3. Click "Detect Language" to see the detected language
4. The result will be displayed below the button

## Notes

- The application uses ISO 639-1 language codes internally
- For best results, enter at least a few words of text
- The detection accuracy improves with longer text samples
- Some languages may require more text for accurate detection

## Example

Enter the text "Hello, how are you?" and the application will detect it as English.
Enter "Bonjour, comment allez-vous?" and it will detect it as French. 