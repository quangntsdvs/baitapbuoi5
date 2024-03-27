from typing import Dict, List

def count_words(words: List[str]) -> Dict[str, int]:
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

sentence = "'apple', 'orange', 'banana', 'apple', 'orange', 'apple'"
words = sentence.split()
word_counts = count_words(words)
for word, count in word_counts.items():
    print(f"{word}: {count}")

