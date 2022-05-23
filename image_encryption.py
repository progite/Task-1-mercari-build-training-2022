import hashlib
from os import rename 

def hash_func(file_name : str):
    new_file_name = ""
    with open(file_name,"rb") as file:
        bytes = file.read()
        encrypted_image_filename = hashlib.sha256(bytes).hexdigest()
        new_file_name = "images/" + encrypted_image_filename + ".jpg"
        # print(new_file_name)
        # new_file_name = "images/{generated_hash}.jpg"
    rename(file_name,new_file_name)
    return encrypted_image_filename + ".jpg"