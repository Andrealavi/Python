import re


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


REGEX_EXPRESSIONS = {
    "digit": "[0-9]",
    "comma": ",",
    "decimalPoint": '\.',
    "equal": '=',
    "function": "(sin)|(cos)|(tan)|(log)|(arcsin)|(arccos)|(arctan)",
    "letter": "([a-z])|([A-Z])",
    "operator": "\+|\-|\*|\/|\^",
    "leftParenthesis": '\(',
    "rightParenthesis": '\)'
}


def emptyBuffer(tokenList, charBuffer, bufferType):
    if charBuffer:
        if bufferType == "number":
            tokenList.append(Token("Litteral", "".join(charBuffer)))
        elif bufferType == "letter":
            joinedBuffer = "".join(charBuffer)

            if re.search(REGEX_EXPRESSIONS["function"], joinedBuffer):
                tokenList.append(Token("Function", joinedBuffer))
            else:
                for i in range(len(charBuffer)):
                    tokenList.append(Token("Variable", charBuffer[i]))

                    if i != len(charBuffer) - 1:
                        tokenList.append(Token("Operator", '*'))

        charBuffer.clear()

        return True

    return False


def addOperator(tokenList, op):
    tokenList.append(Token("Operator", "" + op))


def tokenize(str):
    tokens = []

    numberBuffer = []
    letterBuffer = []

    str = str.replace(" ", "")

    for i in range(len(str)):

        if re.search(REGEX_EXPRESSIONS["digit"], str[i]):
            emptyBuffer(tokens, letterBuffer, "letter")

            numberBuffer.append(str[i])

        elif re.search(REGEX_EXPRESSIONS["comma"], str[i]):
            emptyBuffer(tokens, letterBuffer, "letter")
            emptyBuffer(tokens, numberBuffer, "number")

            tokens.append(Token("Comma", str[i]))

        elif re.search(REGEX_EXPRESSIONS["letter"], str[i]):
            if emptyBuffer(tokens, numberBuffer, "number"):
                addOperator(tokens, '*')

            letterBuffer.append(str[i])

        elif re.search(REGEX_EXPRESSIONS["decimalPoint"], str[i]):
            numberBuffer.append(str[i])

        elif re.search(REGEX_EXPRESSIONS["operator"], str[i]):
            emptyBuffer(tokens, numberBuffer, "number")
            emptyBuffer(tokens, letterBuffer, "letter")

            addOperator(tokens, str[i])

        elif re.search(REGEX_EXPRESSIONS["leftParenthesis"], str[i]):
            emptyBuffer(tokens, numberBuffer, "number")
            emptyBuffer(tokens, letterBuffer, "letter")

            tokens.append(Token("LeftParenthesis", str[i]))

        elif re.search(REGEX_EXPRESSIONS["rightParenthesis"], str[i]):
            emptyBuffer(tokens, numberBuffer, "number")
            emptyBuffer(tokens, letterBuffer, "letter")

            tokens.append(Token("RightParenthesis", str[i]))

        elif re.search(REGEX_EXPRESSIONS["equal"], str[i]):
            emptyBuffer(tokens, numberBuffer, "number")
            emptyBuffer(tokens, letterBuffer, "letter")

            tokens.append(Token("Equal", str[i]))

    emptyBuffer(tokens, numberBuffer, "number")
    emptyBuffer(tokens, letterBuffer, "letter")

    return tokens


tokenize("456.7xy + 6sin(7.04x) - arctan(a, 7)")
