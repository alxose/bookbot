def get_words(text):
        text_split = text.split()
        word_count = len(text_split)
        return word_count

def count_characters(text):
     char_count = {}
     lowered_string = text.lower()
     for character in lowered_string:
          if character.isalpha():
               char_count[character] = char_count.get(character, 0) + 1
     return char_count  

def sort_dict(dict):
     return dict["num"]

def convert_dict_to_list(my_dict):
     dict_list = []
     for key, value in my_dict.items():
          new_dict = {"char": key, "num": value}
          dict_list.append(new_dict)

     dict_list.sort(reverse=True, key=sort_dict)
     return dict_list      

          
def main():
    # Opens and reads the book file
    path = "books/frankenstein.txt"  
    with open(path) as f:
        file_contents = f.read()      
    print(f"--- Begin report of {path} ---")

    # Counts and displays the total number of words
    word_count = get_words(file_contents)
    print(f"{word_count} words found in the document\n")

    # Processes character frequency:
    # 1. Counts all characters in the text
    character_count = count_characters(file_contents)
    # 2. Convert to sorted list of character counts
    convert_dict = convert_dict_to_list(character_count)
    # 3. Display each character's frequency
    for char_dict in convert_dict:
         print(f"The '{char_dict['char']} character was found {char_dict['num']} times")
    
    print("--- End report ---")

    

if __name__ == "__main__":
    main()