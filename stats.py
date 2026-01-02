def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    characters = {}
    words = text.split()
    for word in words:
        for char in word:
            if char.isalpha():
                char = char.lower()
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
    return characters

def sorting(char_dict):
    list = []
    for char, count in char_dict.items():
        list.append({'char': char, 'num': count})
    list.sort(key=lambda x: x['num'], reverse=True)

    return list
