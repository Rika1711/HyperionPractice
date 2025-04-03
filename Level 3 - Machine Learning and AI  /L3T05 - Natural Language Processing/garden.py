import spacy

nlp = spacy.load('en_core_web_sm')

# Store 2 garden-path sentences in a list.
gardenpathSentences = ['I convinced her children are noisy.',
                       'The prime number few.']

# Add 3 more sentences to that list.
gardenpathSentences.append('Mary gave the child a Band Aid.')
gardenpathSentences.append('That Jill is never here hurts.')
gardenpathSentences.append('The cotton clothing is made of \
grows in Mississippi.')

# Check the new list.
print(gardenpathSentences)

# Tokenize each sentence.
token_sentences = [[token.orth_ for token in nlp(sentence)]
                   for sentence in gardenpathSentences]

print(token_sentences)

# Entity explanation: a “real-world object” that’s assigned a name.
# For example, a person, a country, a product or a book title.
# Source: spaCy. Linguistic features. spaCy Usage Documentation.
# Retrieved [26/03/2025],
# from https://spacy.io/usage/linguistic-features

# Perform named entity recognition.
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Print the meaning of entities.
print(spacy.explain('ORG'))
print(spacy.explain('GPE'))

# Entity: Band Aid - ORG.
# Explanation: Companies, agencies, institutions, etc.
# Yes, the explanation made sense.

# Entity: Mississippi - GPE.
# Explanation: Countries, cities, states.
# Yes, the explanation made sense.
