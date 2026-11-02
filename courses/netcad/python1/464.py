dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

dictionary['cat'] = 'minou'
dictionary['swan'] = 'cygne'
dictionary.update({"duck":"canard"})

# for english, french in dictionary.items():
#     print(english, "->", french)
 
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

# for french in dictionary.values():
#     print(french)