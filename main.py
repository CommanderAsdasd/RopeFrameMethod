import random

with open("ostrov.txt", "r") as text_file:
    words = text_file.read().split(' ')
    
with open("make_schema.html") as html:
    lines = text_file.readlines()
# print(lines)
for i in range(10):
    print(random.choice(lines) + " ", end="")