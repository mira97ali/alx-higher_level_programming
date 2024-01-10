#!/usr/bin/python3
"""Create object from a JSON file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_data = load_from_json_file(filename)
except FileNotFoundError:
    existing_data = []

existing_data.extend(sys.argv[1:])
save_to_json_file(existing_data, filename)
