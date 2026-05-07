#!/usr/bin/env python3
"""
Module for serializing and deserializing custom objects using pickle.
"""

import pickle


class CustomObject:
    """Custom object class."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError,
                pickle.UnpicklingError,
                EOFError):
            return None
        except Exception:
            return None
