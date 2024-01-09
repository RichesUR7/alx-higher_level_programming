#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save them to a file.
"""
import sys
from os import path

# Import the required functions
from _5_save_to_json_file import save_to_json_file
from _6_load_from_json_file import load_from_json_file



FileName = "add_item.json"

# Check if file exists
if path.exists(FileName):
    # If file exists, load the list from the file
    my_list = load_from_json_file(FileName)
else:
    # If file doesn't exist, create a new list
    my_list = []

# Add all arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the list to the file
save_to_json_file(my_list, FileName)
