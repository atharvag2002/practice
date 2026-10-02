
def wrap_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + (1 if current_line else 0) <= width:
            current_line.append(word)
            current_length += len(word) + (1 if current_line else 1)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines


def main():
    texts = [
        ("This is a sample text that needs to be wrapped", 10),
        ("Hello world this is a test", 5),
        ("Short", 20)
    ]
    for text, width in texts:
        print(f"Text: '{text}', Width: {width}")
        print(f"Wrapped: {wrap_text(text, width)}")


if __name__ == "__main__":
    main()
