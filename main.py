def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    report = get_report(char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("\r")
    for i in range(len(report)):
        print(f"The '{report[i]['char']}' character was found {report[i]['count']} times")
    print("\r")
    print("--- End report ---")
    

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

def sort_on(dict):
    return dict['count']

def get_report(dict):
    list=[]
    for item in dict:
        if item.isalpha():
            list.append({"char": item, "count": dict[item]})
    list.sort(reverse=True, key=sort_on)    
    return list


main()