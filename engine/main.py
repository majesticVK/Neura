import eel
import os
from command import *  # Ensure this path is correct
from playsound import playsound
from feature import *

# Set the path for the sound file
sound_file = r"C:\Users\vansh\Downloads\mixkit-sweeping-sparkle-presentation-intro-2633.wav"

# Play the sound file
playsound(sound_file)

# Define the project root as one level up from this file's directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
web_dir = os.path.join(project_root, 'engine', 'www')

# Initialize Eel with the path to 'www' directory inside 'engine'
eel.init(web_dir)

# Check for the presence of index.html for verification
index_path = os.path.join(web_dir, 'index.html')
if os.path.exists(index_path):
    print("index.html exists at:", index_path)
else:
    print("index.html NOT found at:", index_path)

# Attempt to launch the browser to open the app
try:
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')  # Change browser as needed
except Exception as e:
    print(f"Error launching browser: {e}")

# Start the Eel server to host index.html on localhost at port 8000
eel.start('index.html', mode=None, host='localhost', port=8000, block=True)
