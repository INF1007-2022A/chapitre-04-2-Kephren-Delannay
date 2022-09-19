#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	# split the name
	first_name = name.split('-')[0]
	# makes it lower to ensure a good format
	first_name = str.lower(first_name)
	# makes first letter uppercase
	first_name = first_name.replace(first_name[0], first_name[0].upper())
	return 'Bonjour ' + first_name

def get_random_sentence(animals, adjectives, fruits):
	animal = random.choice(animals)
	adjective = random.choice(adjectives)
	fruit = random.choice(fruits)
	return (f"Aujourd'hui, j'ai vu un {animal} s'emparer d'un panier {adjective} plein de {fruit}")

def encrypt(text, shift):
	# makes the sentence lower to ease the calculations
	lower_case_text = text.lower()
	result = ""
	# loop through the sentence
	for char in lower_case_text:
		# get the ASCII code
		n = ord(char)
		if 97 <= n <= 122:
			# TODO: loop when n >= 123
			result += chr(n + shift)
	return result

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
