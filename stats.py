def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    num_letters = {}
    for ch in text:
        if not ch.isalpha():
            continue

        letter = ch.lower()
        num_letters[letter] = num_letters.get(letter,0) + 1

    return sort_dict(num_letters)

def sort_dict(d):
    new_dict = []
    for key in d:
        new_dict.append({key : d[key]})
    new_dict.sort(reverse=True, key=sort_helper)

    return new_dict

def sort_helper(entry):
    return list(entry.values())[0]

def print_stats(filepath):
    text = get_book_text(filepath)
    letters = get_num_letters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for l in letters:
        for key in l:
            print(f"{key}: {l[key]}")
    print("============= END ===============")
