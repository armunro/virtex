#!/usr/bin/python3
import HID
import lorem

from HID import CODE

if __name__ == "__main__":
    def generate_lorem(num_paragraphs=3):
        paragraphs = [lorem.paragraph() for _ in range(num_paragraphs)]
        return "\n\n".join(paragraphs)
    HID.type_string(generate_lorem(3))