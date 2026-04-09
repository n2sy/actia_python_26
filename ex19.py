sample_story = """Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python."""

print(len("interesting"))


def count_longest_word(text):
    text = text.replace(",", " ").replace(".", " ")
    words = text.split()
    # nbMax = 0
    longest_word = ""
    for word in words:
        print(word)
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(count_longest_word(sample_story))
