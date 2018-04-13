# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    counter = 0
    position = 0

    for i, next in enumerate(text):
        if next in "([{":
            stack.append(next)
            position = i + 1
            pass

        if next in ")]}":
            
            if len(stack) > 0:
                opening = stack.pop()
                position -= 1
            
                if opening == None or not are_matching(opening, next):
                    counter = i + 1
                    break

            else:
                counter = i + 1
                break

    if counter > 0:
        return(counter)
    elif len(stack) > 0:
        return(position)
    else:
        return("Success")


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
