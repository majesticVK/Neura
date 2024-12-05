import os

# Define the path to the features directory
features_dir = r"C:\Users\vansh\Downloads\Neura\engine\features"

# Create the features directory if it doesn't exist
if not os.path.exists(features_dir):
    os.makedirs(features_dir)  # Create the directory along with any necessary parent directories
    print(f"Created directory: {features_dir}")

# Define the path to __init__.py
init_file_path = os.path.join(features_dir, "__init__.py")

# Create the __init__.py file if it doesn't exist
if not os.path.exists(init_file_path):
    with open(init_file_path, "w") as init_file:
        init_file.write("# This is an init file for the features package.\n")
    print(f"Created: {init_file_path}")
else:
    print(f"{init_file_path} already exists.")
