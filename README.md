# Personal Assistant

## About
- This is a simple personal assistant that can hold simple conversations and perform some simple tasks like    tell the time, date, etc.
- This project has been made entirely using python.

## Working
- Run run.py to start the program. A simple gui interface has been implemented using tkinter for easy access and use.
- The personal assistant is trained using tensorflow on a set of simple questions and corresponding answers. This model is used to differentiate between different types of input the user may provide.
- Input can be taken from the user in 2 ways via the gui. Either the user can type into an entry box or there is also an option to accept voice input. The speech recognition part of this project is implemented using the speech_recognition library.

## Contents
- The scripts directory contains all the python files used in the creation of this program.
- training.py and yml_to_json.py files are not needed for running the application. training.py was used to make the tensorflow model and yml_to_json.py was used to convert all the conversations(which were obtained in yml format) into json for easier access in the program.
- requirements.txt contains all the dependencies. Run the following command in terminal to install all the libraries required to run this program.
```
pip install -r requirements.txt
```

## Video Demonstration
Visit this url: https://youtu.be/FrlzSXRIK3Q
