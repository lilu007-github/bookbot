from stats import get_number_of_words ,get_number_of_eachchar, get_sorted_char_counts
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():    
    #file_path = 'books/frankenstein.txt'
    #print("Reading book from:", file_path)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        book_text = get_book_text(file_path)
        word_count = get_number_of_words(book_text)
        char_count = get_number_of_eachchar(book_text)
        sorted_char_count = get_sorted_char_counts(char_count)
        # print results
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("------------ Word Count ------------")
        print(f"Found {word_count} total words")
        print("-------- Character Counts ---------")
        for char_info in sorted_char_count:
            if char_info['char'].isalpha():  
               print(f"{char_info['char']}: {char_info['num']}")
        #print(char_count)
        print("===================================")
        # Uncomment to see unsorted character counts

        #for char, count in char_count.items():
        #    print(f"'{char}': {count}")
        
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        return
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return

    #print(book_text)


if __name__ == '__main__':
    main()