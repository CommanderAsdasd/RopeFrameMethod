import random

text_file = open("ostrov.txt", "r")
lines = text_file.read().split(' ')
# print(lines)
for i in range(10):
    print(random.choice(lines) + " ", end="")