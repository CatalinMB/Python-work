import itertools
from string import ascii_lowercase

print("xX PERMUTATION GENERATOR Xx")
print("-----------------------------")

nr = input("     Number of letters: ")

handler = open("permutations", "w")
keywords = [''.join(i) for i in itertools.product(ascii_lowercase, repeat=int(nr))]
str1 = '\n'.join(keywords)
handler.write(str1)
handler.close()

print("          Done!")


