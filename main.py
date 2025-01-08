def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    print(f"{word_count} words found in the document")
    print(char_count)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_word_count(text):
    split = text.split()
    return len(split)

def get_character_count(text):
    dict = {}
    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
    return dict

main()