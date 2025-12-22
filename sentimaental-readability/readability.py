from cs50 import get_string

text = get_string("Text: ")

length = len(text)

letters = 0
words = 0
sentences = 0

for i in range(length):
    c = text[i]
    if c.isalpha():
        letters = letters + 1
    elif c == " ":
        words = words + 1
    elif c == "." or c == "!" or c == "?":
        sentences = sentences + 1
words = words + 1

L = float(letters / words * 100)
S = float(sentences / words * 100)
index = 0.0588 * L - 0.296 * S - 15.8

grade = round(index)

if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade ", grade)
