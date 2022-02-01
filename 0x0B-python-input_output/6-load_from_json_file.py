#!/usr/bin/python3
"""json"""
import json


def load_from_json_file(filename):
    """ function name load_from_json_file"""
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
