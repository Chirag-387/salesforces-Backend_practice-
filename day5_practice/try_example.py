def to_number(text):
    try:
        return int(text)
    except ValueError:
        print("This is not a number")
        return None

print(to_number("42"))
print(to_number("abc"))