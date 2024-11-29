import Keys
import lorem

def generate_lorem(num_paragraphs):
    paragraphs = [lorem.paragraph() for _ in range(num_paragraphs)]
    Keys.type_string("\n\n".join(paragraphs))
    