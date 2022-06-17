print("Hello Python interpreter!")

name = "ada lovelace sss"

print(name.title())


#Adding whitespace to string with tabs or newlines

print("Python")
print("\tPython")


#To add a newline in a string
print("Languages:\nPython\nC\nJavaScript")


#stripping whitespace
favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)

# stripping whitespace right, left , all

favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

# avoiding syntax errors with stings

message = "One of Python's strengths is its diverse community."
print(message)

#floats

print(0.2+0.1) # sometimes is a problem and is of little concert

#Avoiding type errors with the str() Function

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# Zen of python 

"Beautiful is better than ugly."
"Simple is better than complex."
"Complex is better than complicated."
"Readability counts."
"There should be one-- and preferably only one --obvious way to do it."
"Now is better than never."