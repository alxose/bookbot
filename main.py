def get_words(text):
        text_split = text.split()
        word_count = len(text_split)
        return word_count

def count_characters(char):
     char_count = {}
     lowered_string = char.lower()
     for character in lowered_string:
          char_count[character] = char_count.get(character, 0) + 1
     return char_count     
          
def main():
    # Opens the text file with a relative path and read its contents.
    # This loads the full content of "frankenstein.txt" into a string.
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()      
    
    # Counts the number of words in the text content and prints the result.
    word_count = get_words(file_contents)
    print(word_count)

    # Counts the occurrence of each character (dynamically) and prints the result.
    character_count = count_characters(file_contents)
    print(character_count)


if __name__ == "__main__":
    main()