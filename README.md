# Voice Calculator

This project is a simple voice-activated calculator, built using Python. It allows the user to perform basic calculations through voice commands. The project leverages speech recognition for capturing voice input, text-to-speech for responding, and a basic graphical user interface (GUI) built with Tkinter.

## Requirements

To run this project, you need to install the following dependencies:

1. `pyttsx3` – For text-to-speech functionality.
2. `speech_recognition` – For capturing and recognizing voice commands.
3. `tkinter` – For creating the graphical user interface (GUI).
4. `datetime` – To handle date and time in the application.

To install the necessary libraries, run the following commands:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install tkinter
```

## Features
Voice Recognition: Listens to voice commands using the microphone.
Text-to-Speech: Responds to the user with voice feedback.
Wake Up/Shutdown: The application is triggered by saying "Wake up" and shuts down with "Finally sleep."
Voice Calculator: The user can perform calculations by saying commands like "Calculate 5 plus 3."
Graphical User Interface (GUI): A simple Tkinter-based interface to interact with the calculator.

## How to Use
When the program is run, a GUI will appear with a button.
Click the button or say the phrase "Wake up" to activate the voice recognition system.
Once activated, speak the calculation or command you want to perform, such as "Calculate 5 plus 3."
The application will perform the calculation and give feedback through voice.
Say "Finally sleep" to exit the program.
