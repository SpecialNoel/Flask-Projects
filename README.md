# Flask-Projects
This repository contains projects I'm working on while learning the Python Flask framework. I intend to use Flask to connect the front end (GUI) with back end (message transmission between server and clients) for Giraffael, my chatting application. 

## Project: [Flask in VSCode](https://github.com/SpecialNoel/Flask-Projects)
You can find the instruction of this project by navigating [the official tutorial published on VSCode's website](https://code.visualstudio.com/docs/python/tutorial-flask#_create-a-project-environment-for-the-flask-tutorial)

This project contains the following files and folders under the Flask-Projects repository: ```.vscode```, ```__pychache__```, ```flask_in_vscode_tutorial```.

### How to run this project?
**Step1**: Download needed files and folders for this project. Make sure that you have Python 3 installed on your device as well before going further.

**Step2**: In VS Code, open the Command Palette (View > Command Palette). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment you want to use to create it. Remember to select the requirements.txt to install used dependencies for this project. Alternatively, use command 
```
pip install -r requirements.txt
```
to reinstall the packages (dependencies) in the original environment.

**Step3**: In VS Code, create a new Terminal (Terminal > New Terminal), which creates a terminal and automatically activates the virtual environment by running its activation script.

**Step4**: Install Flask in the virtual environment by running the following command in the VS Code Terminal:
```
python -m pip install flask
```

**Step5**: In the Integrated Terminal, run the app by entering 
```
python -m flask run
```
which runs the Flask development server.

If you see an error that the Flask module cannot be found, make sure you've run the command 
```python -m pip install flask```
in your virtual environment as described in previous steps.

**Step6**: ```Ctrl+Click``` the URL ```http://127.0.0.1:5000/``` in the terminal to open your default browser to the rendered page.

