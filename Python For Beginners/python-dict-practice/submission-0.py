from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    new_map = {}
    for i in range(len(word)):
        if word[i] in new_map:
            new_map[word[i]] = new_map[word[i]] + 1
        else:
            new_map[word[i]] = 1
    return new_map

    




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
