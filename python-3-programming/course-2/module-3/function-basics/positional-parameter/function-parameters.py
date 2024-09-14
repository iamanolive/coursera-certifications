def hello(name):
    print("hello", name)
    print("glad to meet you!")

hello("iman")
hello("jackie")


def another_hello(name, age):
    greeting = "hello {}".format(name)
    print(greeting * age)

another_hello("wei", 4)
another_hello("", 1)
another_hello("kitty", 11)