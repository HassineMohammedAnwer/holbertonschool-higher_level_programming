#!/usr/bin/python3
"""add args in a new_file """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    n_list = load_from_json_file("add_item.json")
except ValueError:
    n_list = []
save_to_json_file(n_list + sys.argv[1:], "add_item.json")
