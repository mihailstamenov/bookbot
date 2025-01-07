def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    split = file_contents.split()
    print(len(split))

main()