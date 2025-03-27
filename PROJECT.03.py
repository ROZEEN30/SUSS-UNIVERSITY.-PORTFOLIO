import random
import string

chars= string.punctuation + string.digits + string.ascii_letters
char_list=list(chars)
key=char_list.copy()
random.shuffle(key)
is_running=True
print(f"chars: {char_list}")
print(f"key: {key}")

while is_running:
  plain_text= input("Enter a message to encrypt: ")
  cipher_text= ""
  for text in plain_text:
    index=char_list.index(text)
    cipher_text += key[index]

  print(f"original message: {plain_text}")
  print(f"ciphered text: {cipher_text}")
  Question=input("Do you want to try again(y/n)?")
  if Question=="n":
    is_running=False
