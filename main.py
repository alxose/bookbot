def get_words(text):
        text_split = text.split()
        word_count = len(text_split)
        return word_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()      
    word_count = get_words(file_contents)
    print(word_count)    

if __name__ == "__main__":
    main()