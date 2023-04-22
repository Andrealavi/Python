from tokenizer import Token
from tokenizer import tokenize

asso = {
    '^': "right",
    '*': "left",
    '/': "left",
    '+': "left",
    '-': "left"
}

prec = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2
}

symbolConversion = {
    "sin": "np.sin",
    "^": "**",
    "cos": "np.cos",
    "tan": "np.tan"
}


def shuntingYard(tokenList):
    outStack = []
    opStack = []

    for token in tokenList:
        if token.type == "Litteral":
            outStack.append(token)
        elif token.type == "Function":
            opStack.insert(0, token)

        elif token.type == "Variable":
            outStack.append(token)

        elif token.type == "Operator":
            while opStack != [] and opStack[0].type == "Operator" and (prec[opStack[0].value] > prec[token.value] or (prec[opStack[0].value] == prec[token.value] and asso[token.value] == "left")):
                opStack.pop(0)

            opStack.insert(0, token)

        elif token.type == "Comma":
            while opStack[0].type != "LeftParenthesis":
                outStack.append(opStack.pop(0))

        elif token.type == "LeftParenthesis":
            opStack.insert(0, token)
        elif token.type == "RightParenthesis":
            while opStack[0].type != "LeftParenthesis":
                outStack.append(opStack.pop(0))

            if opStack[0].type == "LeftParenthesis":
                opStack.pop(0)

    while opStack != []:
        outStack.append(opStack.pop(0))

    return outStack
