def word_count(text):
    return len(text.split())

def get_character_count(text):
    character_counts = {}
    for char in text.lower():        
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def chars_dict_to_sorted_list(character_counts):
    sorted_tuple = []

    for i in character_counts.items():
        sorted_tuple.append(i)
        sorted_tuple = sorted(sorted_tuple, key=sort_on, reverse=True)
    return sorted_tuple

def sort_on(item):
    return item[1]

