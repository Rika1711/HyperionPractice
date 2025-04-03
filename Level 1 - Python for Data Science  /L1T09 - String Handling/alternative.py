# Compulsory Task 1
#
# Create program that takes user input.
# Create a variable that makes each alternate character upper and lower case.
# Print that variable.
# Create a cariable that makes each alternate word upper and lower case. User split() and join().
# Print that variable.

user_sentence = input("Please enter a random sentence. \n")

split_sentence = user_sentence.split()

sentence_alt_char = ""
sentence_alt_word = []

for i in range(len(user_sentence)):
    if i % 2 != 1:
        sentence_alt_char += user_sentence[i].upper()
    else:
        sentence_alt_char += user_sentence[i].lower()

print(sentence_alt_char)

for i in range(len(split_sentence)):
    if i % 2 == 1:
        sentence_alt_word.append(split_sentence[i].upper())
    else:
        sentence_alt_word.append(split_sentence[i].lower())

print(" ".join(sentence_alt_word))
