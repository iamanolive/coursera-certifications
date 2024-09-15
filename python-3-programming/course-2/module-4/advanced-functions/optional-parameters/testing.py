def count_long_words(words, min_length = 5):
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count

test_words = ["", "1", "12", "123", "1234", "12345", "123456"]
assert count_long_words(test_words) == 2
assert count_long_words(test_words, min_length = 0) == 7
assert count_long_words(test_words, min_length = 4) == 3
assert count_long_words(test_words, min_length = 100) == 0