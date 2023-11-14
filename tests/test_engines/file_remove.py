#!/usr/bin/env python3
"""defines a module that deletes files"""
import os


def delete_file(file_path):
    """deletes a file"""
    if os.path.exists(file_path):
        os.remove(file_path)
        if not os.path.exists(file_path):
            print("file removed")
        else:
            print("file present")


if __name__ == "__main__":
    delete_file("file.json")
