from typing import List

def contains_duplicate(words: List[str]) -> bool:
    con = set()
    for word in words:
        if word not in con:
            con.add(word)
        else:
            return True    
    return False
        

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
