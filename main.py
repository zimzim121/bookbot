import sys


print(sys.argv[0])
 
if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: filepath = sys.argv[1]




def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    from stats import num_of_words
    results = get_book_text(filepath)
    #print(results)

    from stats import num_of_chars
    from stats import chars_to_sorted_list
    
    sorted_chars = chars_to_sorted_list(num_of_chars(results))

    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath)
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(results)} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    
    

    #print (num_of_words(results),"words found in the document")



main()