def count_words(text: str) -> dict[str, int]:
    words = text.split()
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d
print(count_words("hello world hello"))


def add_em_up(nums: list[int]) -> int:
    total = 0
    for number in nums:
        total += number
    return total
print(add_em_up([1, 3, 5]))


def add_em_up2(nums: list[int | float]) -> int:
    total = 0
    for number in nums:
        total += number
    return total
print(add_em_up2([1, 3.5, 2.4]))