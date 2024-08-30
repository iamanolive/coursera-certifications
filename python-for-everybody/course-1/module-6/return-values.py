def primitive_greet():
    return "hello"

print(primitive_greet(), "glenn")
print(primitive_greet(), "sally")


def greet(lang):
    if lang == "es": return "hola"
    elif lang == "fr": return "bonjour"
    else: return "hello"

print(greet("en"), "glenn")
print(greet("es"), "sally")
print(greet("fr"), "michael")