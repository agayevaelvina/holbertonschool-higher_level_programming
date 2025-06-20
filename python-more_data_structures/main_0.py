number_keys = __import__('5-number_keys').number_keys

a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
nb_keys = number_keys(a_dictionary)
print(nb_keys)
