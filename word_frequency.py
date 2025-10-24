import re

def is_sentence(text):
    
    if not isinstance(text, str) or not text.strip():
        return False
    stripped = text.lstrip()

    if not stripped[0].isupper():
        return False

    if not re.search(r'[.!?]$', stripped):
        return False

    if not re.search(r'\w+', stripped):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while not is_sentence(user_sentence):

    print("This does not meet the criteria for a sentence.")

    user_sentence = input("Enter a sentence: ")



clean_sentence = re.sub(r'[^\w\s]', '', user_sentence).casefold()
words = clean_sentence.split()

unique_words = []
frequencies = []

for word in words:

    if word in unique_words:
        idx = unique_words.index(word)
        frequencies[idx] += 1

    else:
        unique_words.append(word)
        frequencies.append(1)

for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")
