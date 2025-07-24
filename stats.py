def count_words(raw_text):
    split_text = raw_text.split()
    return len(split_text)

def get_char_counts(raw_test):
    char_counts = {}
    for char in raw_test:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sort_dictionary(raw_dictionary):
    dictionary_list = []
    for char in raw_dictionary:
        num = raw_dictionary[char]
        list_dictionary = {}
        list_dictionary["char"] = char
        list_dictionary["num"] = num
        dictionary_list.append(list_dictionary)

    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
