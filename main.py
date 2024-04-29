
def convert(text: str) -> str:
    table = {
        "a":"@",
        "A":"4",
        "B":"8",
        "b":"8",
        "E":"3",
        "e":"3",
        "I":"!",
        "i":"!",
        "L":"1",
        "l":"1",
        "O":"0",
        "o":"0",
        "S":"5",
        "s":"5",
    }

    new_str=""

    for i in text:
        if i in table:
            new_str += table[i]
        else:
            new_str += i
    return new_str

print(convert("Hello"))