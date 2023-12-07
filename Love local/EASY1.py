import re

def length_of_last_word(s):

  s = re.sub(r'^"|"$', '', s.strip())

  words = s.split()
  if not words:
    return 0

  return len(words[-1])

user_input = input("Input: ")

last_word_length = length_of_last_word(user_input)
print(f"Output: {last_word_length}")
