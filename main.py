def main():
    book_path = 'books/frankenstein.txt';
    with open(book_path) as f:
        file_content = f.read()
        num_words = count_words(file_content)
        char_dict = count_characters(file_content)
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        print()
        char_list = list(char_dict.items())
        char_list.sort(reverse=False, key=sort_on)
        for item in char_list:
            key = item[0];
            value = item[1];
            print(f"The '{key}' character was found {value} times")
        print("--- End report ---")


def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    words = string.split()
    dictionary = {
    "a": 0
}
    for word in words:
        for char in list(word):
            if (char.isalpha()):
                dictionary[char.lower()] = dictionary.get(char.lower(), 0) + 1
    return dictionary;

def sort_on(dict):
    return dict[0];
    
main()