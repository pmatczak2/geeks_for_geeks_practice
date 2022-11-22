import string

uencoded_caracters = string.ascii_letters + string.digits
encoded_characters = uencoded_caracters[-15:] + uencoded_caracters[:-15]
print(uencoded_caracters)
print(encoded_characters)



message = "hello there you guys form the moon"

def cyper_encode(message):
    answer = ""
    for _ in message:
        answer += chr((ord(_) + 7))
    return answer

encoded_message = cyper_encode(message)

def cypher_decode(encoded_message):
    answer = ""
    for i in encoded_message:
        answer += chr(ord(i) - 7)
    return answer

print(encoded_message)
print(cypher_decode(encoded_message))

# def cypher(text, shift):
#     if type(text) != str:
#         return "the input is not a string"
#     else:
#         code = ""
#         for i in text:
#             code += chr(ord(i) + shift)
#         return code
#
# print(cypher(message, 2))
assert message == cypher_decode(cyper_encode(message))
