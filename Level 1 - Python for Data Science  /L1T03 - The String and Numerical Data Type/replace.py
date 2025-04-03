# Compulsory Task 1
#
# Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a single string
# Reprint this sentence as "The quick brown fox jumps over the lazy dog."
# Reprint the previous sentence in upper case
# Reprint the sentence in reverse 

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
sentence_replace = sentence.replace("!", " ")

print(sentence_replace)
print(sentence_replace.upper())
print(sentence_replace[ : :-1])