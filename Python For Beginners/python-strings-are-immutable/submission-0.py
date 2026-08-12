def remove_fourth_character(word: str) -> str:
    word_start = word[:3]
    word_end = word[4:]
    return word_start + word_end


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
