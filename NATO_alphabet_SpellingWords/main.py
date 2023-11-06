
# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
df = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = list(input("Input your word to spell in NATO alphabet: ").upper())
spelling_list = [nato_dict[letter] for letter in word]
print(spelling_list)

# Create a dictionary of the phonetic code words from a word that the user inputs in the format
# {"A": "Alfa", "B": "Bravo"}
spelling_dict = {letter: nato_dict[letter] for letter in word}
print(spelling_dict)
