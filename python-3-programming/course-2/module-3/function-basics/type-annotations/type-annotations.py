x = 3
x = "hello"
print(x)


def duplicate(msg: str) -> str:
    """ returns a string containing two copies of `msg` """
    return msg + msg

result = duplicate("hello")
print(result)


def get_number(msg: str) -> float:
    """ prompts with `msg` for input
    returns numeric response """
    return float(input(msg))


def display_msg(msg: str) -> None:
    """ displays `msg` with dashed lines underneath """
    print(msg)
    print("-----------------------------------")