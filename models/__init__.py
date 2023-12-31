#!/usr/bin/env python3
"""
    defines a module `__init__` that initializes and
    creates a unique FileStorage instance for the application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
