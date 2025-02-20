from collections import deque


def check_parenthesis_balanced(string: str) -> bool:
    stack = deque()

    map = {"{": "}", "(": ")", "[": "]"}
    parenthesis = "{}()[]"
    for i in string:
        if i in parenthesis:
            if i in map:
                stack.append(i)
            elif not len(stack):
                return False
            elif map[stack.pop()] != i:
                return False

    return True
