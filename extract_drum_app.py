import zipfile
import os

# Extract the zip file
with zipfile.ZipFile('/workspace/user_input_files/3d-drum-machine-samplerv3.zip', 'r') as zip_ref:
    zip_ref.extractall('/workspace/drum_app_extracted')

# List the extracted contents
for root, dirs, files in os.walk('/workspace/drum_app_extracted'):
    level = root.replace('/workspace/drum_app_extracted', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f'{subindent}{file}')