# Part A - Question 4: Word Frequency Counter
# Count words, find top N words, unique words,
# invert frequency dictionary, group words by length,
# and search for a word.

paragraph = input("Enter a paragraph: ")

# Convert to lowercase and remove punctuation
clean_text = ""

for char in paragraph.lower():
    if char.isalnum() or char.isspace():
        clean_text += char

words = clean_text.split()

# Count word frequency using get()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n--- Word Frequency ---")
print(frequency)

# Top N words
try:
    n = int(input("\nEnter N for top N words: "))

    sorted_words = sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("\n--- Top", n, "Words ---")

    for word, count in sorted_words[:n]:
        print(word, ":", count)

except ValueError:
    print("Please enter a valid number.")

# Words appearing exactly once
unique_words = [
    word for word, count in frequency.items()
    if count == 1
]

print("\n--- Words Appearing Exactly Once ---")
print(unique_words)

# Invert frequency dictionary
inverted = {}

for word, count in frequency.items():
    inverted.setdefault(count, []).append(word)

print("\n--- Inverted Frequency Dictionary ---")

for count in sorted(inverted):
    inverted[count].sort()

print(inverted)

# Group words by length
grouped_words = {}

for word in frequency:
    length = len(word)
    grouped_words.setdefault(length, []).append(word)

for length in grouped_words:
    grouped_words[length].sort()

print("\n--- Words Grouped by Length ---")
print(grouped_words)

# Search for a word
search_word = input("\nEnter a word to search: ").lower()

if search_word in frequency:
    print(search_word, "appears", frequency[search_word], "times.")
else:
    print("Word not found.")

input("\nPress Enter to close the program...")