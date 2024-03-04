def count_word_frequency(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

# Example usage:
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
frequency = count_word_frequency(words)

# Format output
output = {word: frequency[word] for word in sorted(frequency.keys())}
print(output)