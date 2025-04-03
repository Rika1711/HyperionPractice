#  Compulsory Task 2

import xml.etree.ElementTree as ET

# Parse the XML file 'movie.xml' and create an ElementTree object.
tree = ET.parse('movie.xml')

# Get the root element of the XML tree.
root = tree.getroot()

# Use the iter() function to list all the child tags of the movie element.
print("\n##### All child tags of movie element #####")

for movie in root.iter('movie'):
    for child in movie:
        print(child.tag)

# Version above prints child tags for every time "movies" appears.
# That causes a lot of repetition.
# The code below prints a list with every unique child tag.
print("\n##### Unique child tags of the movie element #####")

child_list = []

for movie in root.iter('movie'):
    for child in movie:
        if child.tag not in child_list:
            child_list.append(child.tag)

print(*child_list, sep='\n')

#  Use the itertext() function to print out the movie descriptions.
print("\n##### Movie descriptions #####")
for description in root.iter('description'):
    description_text = "".join(description.itertext())
    # This code makes the descriptions a bit more readable.
    description_text = description_text.replace("  ", "").strip()
    print("- ", description_text)

# This code finds the number of favourites and non-favourites.
print("\n##### Favourite counter #####")

favourite_counter = 0
not_favourite_counter = 0

for movies in root.iter('movie'):
    is_fav = movies.get('favorite').lower()
    
    if is_fav == "true":
        favourite_counter += 1
    else:
        not_favourite_counter += 1

print(f'''Favourite movies:\t {favourite_counter}
Not favourite movies:\t {not_favourite_counter}''')
