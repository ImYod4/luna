import luna.stack import ArrayStack

def is_mathced_html(exp):
    S = ArrayStack()
    j = exp.find('<')
    while j != -1:
        k = exp.find('>', j + 1)
        if k == -1:
            return False
        tag = exp[j + 1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if len(S) == 0:
                return False
            if tag[1:] != S.pop():
                return False
        j = exp.find('<', k + 1)
        print(S)
    return len(S) == 0
