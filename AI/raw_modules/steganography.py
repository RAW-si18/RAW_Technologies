# Updated 30/1/24

import subprocess

def image_hiding(image_path: str,txt_path: str,new_image: str) -> None:
    '''hide text in an image'''
    command = r"copy /b "+image_path+" + "+txt_path+" "+r"C:\Users\Admin\OneDrive\Pictures\Screenshot_by_Cosmos\hidden_images\\"+new_image+".jpg"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, input="No\n")
    if result.returncode == 1:
        print("Image with same name already exists. Not overwriting.")
    elif result.returncode == 0:
        print("Image hiding successful.")
    else:
        print("Unknown error:", result.stderr)

def image_unhide(image_path: str) -> str:
    '''Unhide and retrieve text hidden behind an image'''
    try:
        with open(image_path, 'rb') as file:
            file_content = file.read()
            start_marker = file_content.find(b'\xFF\xD9')
            if (start_marker != -1):
                hidden_text = file_content[(start_marker+2):].decode('utf-8')
                return hidden_text
            else:
                return "No hidden text found in the image."
    except FileNotFoundError:
        return "Image file not found."
    except Exception as e:
        return f"Error occurred while unhiding text: {str(e)}"
