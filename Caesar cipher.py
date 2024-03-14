alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
new_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

from art import logo

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > len(alphabet):
  shift = shift % len(alphabet)


def reset_alphabet():
  new_alphabet.sort()


def caesar(direction, text, shift):
  new_text = ""
  for n in range(0, shift):
    new_alphabet.append(new_alphabet[0])
    new_alphabet.remove(new_alphabet[0])
  for i in range(len(text)):
    if text[i] in alphabet:
      for j in range(len(alphabet)):
        if direction == "encode":
          if text[i] == alphabet[j]:
            new_text += new_alphabet[j]
        elif direction == "decode":
          if text[i] == new_alphabet[j]:
            new_text += alphabet[j]
    else:
      new_text += text[i]
  print(f"The {direction}d text is : {new_text}")
  reset_alphabet()
  ask_user = input(
      "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if ask_user == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)


caesar(direction, text, shift)
