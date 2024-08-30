def greet(lang):
    if lang == "es": print("hola")
    elif lang == "fr": print("bonjour")
    else: print("hello")

greet("en") # hello
greet("es") # hola
greet("fr") # bonjour



# multiple parameters
def add_two(a, b):
    added = a + b
    return added
x = add_two(3, 5)
print(x)