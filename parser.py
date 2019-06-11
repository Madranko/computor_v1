import re


class Parser:

    fullPattern = r"^[+-]?(\d+(\.\d+)?(\*X(\^[0-9]+)?(?!\d))?([+-](?!=))?)+=" \
                  r"[+-]?(\d+(\.\d+)?(\*X(\^[0-9]+)?(?!\d))?([+-](?!$))?)+$"

    tokenPattern = r"(?:([+-]?)(\d+(?:\.\d+)?))(?:X(?:\^([0-9]+))?)?"

    def __init__(self, line):
        self.line = line
        self.leftLine = line
        self.rightLine = line

    def parseLine(self):
        self.line = "".join(self.line.split())
        if self.lineIsValid():
            self.line = self.line.replace("*", "")
            splittedLine = self.line.split("=")
            self.leftLine = self.parseLineOnTokens(splittedLine[0])
            self.rightLine = self.parseLineOnTokens(splittedLine[1])
            return self.moveRightSideToLeft()

    def lineIsValid(self):
        if re.fullmatch(self.fullPattern, self.line):
            return True
        else:
            raise Exception('Invalid argument')

    def parseLineOnTokens(self, line):

        result = re.findall(self.tokenPattern, line)
        tokens = []
        for group in result:
            value = self.buildValue(group)
            tokens.append({
                'value': value,
                'power': int(0 if group[2] == '' else group[2]),
            })
        return tokens

    def buildValue(self, group):
        strValue = '0' if group[1] == '' else group[1]

        if strValue != '0' and strValue != '0.0':
            value = (float(strValue) if "." in strValue else int(strValue))
            value = value * -1 if group[0] == '-' else value
        else:
            value = 0
        return value


    def moveRightSideToLeft(self):
        for index, token in enumerate(self.rightLine):
            self.rightLine[index]['value'] *= -1
        return self.leftLine + self.rightLine

