# PDF to Speech Converter

This project converts the text from a PDF file into an audio file (MP3) using Python.  
It uses [PyPDF2](https://pypi.org/project/PyPDF2/) to extract text from PDFs and [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech synthesis.

## Features

- Extracts text from all pages of a PDF.
- Converts the extracted text to speech.
- Saves the speech as an `output_audio.mp3` file.
- Adjustable speech rate and voice.

## Requirements

- Python 3.x
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/YourUsername/your-repo-name.git
    cd your-repo-name
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install pyttsx3 PyPDF2
    ```

## Usage

1. Place your PDF file (e.g., `sample.pdf`) in the project directory.
2. Edit `TextToSpeechEngine.py` if you want to change the PDF filename or settings.
3. Run the script:
    ```sh
    python TextToSpeechEngine.py
    ```
4. The audio will be saved as `output_audio.mp3` in the same directory.

## Customization

- Change the `words_per_minute` variable to adjust the speech speed.
- Change the `voice` index to select a different system voice.

## License

This project is licensed under the MIT License.
