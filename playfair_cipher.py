import string
characters = string.ascii_lowercase.replace("j", ".")
print(characters)

key = "playfair example"
key_matrix = ['' for i in range(5)]

i = 0
j = 0
for c in key:
    if c in characters:
        key_matrix[i] += c
        characters = characters.replace(c, ".")

        j += 1
        if j > 4:
            i += 1
            j = 0
for c in characters:
    if c != ".":
        key_matrix[i] += c

        j += 1
        if j > 4:
            i += 1
            j = 0

print(key_matrix)