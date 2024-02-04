def is_palindrome(input_str):
    # remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = ''.join(input_str.split()).lower()

    # compare original and reversed strings
    return cleaned_str == cleaned_str[::-1]

word_or_phrase = input("Enter a word or phrase: ")
result = is_palindrome(word_or_phrase)

if result:
    print(f"{word_or_phrase} is a palindrome.")
else:
    print(f"{word_or_phrase} is not a palindrome.")
