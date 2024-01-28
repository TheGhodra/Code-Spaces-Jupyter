import re

def find_words_with_prefix(text, prefix):
    pattern = r'\b' + re.escape(prefix) + r'\w*\b'
    matching_words = re.findall(pattern, text, flags=re.IGNORECASE)
    return matching_words

if __name__ == "__main__":
    input_text = "Python ist eine populäre Programmiersprache. Viele Programmierer mögen Python."
    target_prefix = "py"

    matching_words = find_words_with_prefix(input_text, target_prefix)

    if matching_words:
        print(f"Wörter mit dem Präfix '{target_prefix}':")
        for word in matching_words:
            print(word)
    else:
        print(f"Keine Wörter mit dem Präfix '{target_prefix}' gefunden.")