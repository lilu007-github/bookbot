def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_eachchar(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

#function that takes the dictionary of character counts and returns a sorted list
# of dictionaries each with 'char' and 'count' keys use sort method
#Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
#Use the .sort() method:
#Use a helper function to return the "num" key of each dictionary for comparison.
#Sort the list from greatest to least by the count.
def get_sorted_char_counts(char_count):
    char_count_list = [{"char": char, "num": count} for char, count in char_count.items()]
    
    def get_count(item):
        return item["num"]
    
    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list
