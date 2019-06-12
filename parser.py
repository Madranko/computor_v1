import re


class Parser:

    fullPattern = r"^[+-]?(((?:\d+)?(?:(?<=\d)(\.\d+))?)(((?<=\d)\*)?(?<!\d)X(\^[0-9]+)?(?!\d))?([+-](?!=))?)+=" \
                  r"((\d+)?((?<=\d)(\.\d+))?(((?<=\d)\*)?(?<!\d)X(\^[0-9]+)?(?!\d))?([+-](?!$))?)+$"

    tokenPattern = r"(?:([+-])?(?!(?:=|$))(\d+(?:\.\d+)?)?)(?:(X)(?:\^([0-9]+))?)?"
    
    colors = {'fail': '\033[91m', 'endcolor': '\033[0m'}

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
            raise Exception(self.colors['fail'] + 'Parse error' + self.colors['endcolor'])

    def parseLineOnTokens(self, line):

        result = re.findall(self.tokenPattern, line)
        tokens = []

        for group in result:
            value = self.buildValue(group)
            power = self.buildPower(group)
            tokens.append({
                'value': value,
                'power': power
            })
        return tokens

    def buildValue(self, group):
        if group[1] == '' and group[2] == 'X':
            strValue = '1'
        elif group[1] == '':
            strValue = '0'
        else:
            strValue = group[1]
        if strValue != '0' and strValue != '0.0':
            value = (float(strValue) if "." in strValue else int(strValue))
            value = value * -1 if group[0] == '-' else value
        else:
            value = 0
        return value

    def buildPower(self, group):
        if group[2] == 'X' and group[3] == '':
            strPower = '1'
        elif group[3] == '':
            strPower = '0'
        else:
            strPower = group[3]
        return int(strPower)


    def moveRightSideToLeft(self):
        for index, token in enumerate(self.rightLine):
            self.rightLine[index]['value'] *= -1
        return self.leftLine + self.rightLine

