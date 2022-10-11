import luna.stack import ArrayStack

def is_matched_parentheses(exp):
    leftly = '([{'
    rightly = ')]}'
    S = ArrayStack()
    for c in exp:
        if c in leftly:
            S.push(c)
        elif c in rightly:
            if len(S) == 0:
                return False
            if rightly.index(c) != leftly.index(S.pop()):
                return False
    return len(S) == 0
