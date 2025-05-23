import string

# === TEXT CLEANING AND TOKENIZATION ===
def load_text_file(filepath):
    lines = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.lower()
            if line:
                lines.append(line)
    return lines

def tokenize(text):
    return text.split()

def process_text_file(filepath):
    cleaned_lines = load_text_file(filepath)
    tokenized_data = [tokenize(line) for line in cleaned_lines]
    return tokenized_data

if __name__ == "__main__":
    tokens = process_text_file("sample_text.txt")
    for line in tokens:
        print(line)
