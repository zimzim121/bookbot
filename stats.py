def num_of_words(file_contents):
    num_words = 0
    words = file_contents.split()
    for word in words:
        num_words += 1
    return num_words


def num_of_chars(file_contents):
    lowered = file_contents.lower()
    chars ={}
    for character in lowered:
        if character in chars:
            chars[character] += 1
        else: chars[character] = 1
    return chars

def sort_on(dict):
    return dict["num"]  # returns the count value for sorting

def chars_to_sorted_list(char_count):
    chars_list = [] #empty list

    for char, count in char_count.items():  # for each character and their count in the dictionary creates a new dictionary with the char and num keys and adds it to the list
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=sort_on) # sorts the list in descending (REVERSED) order using our sort_on function

    return chars_list




