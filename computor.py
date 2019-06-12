import re
import math

class Computor:

    colors = {'fail': '\033[91m', 'endcolor': '\033[0m'}

    def __init__(self, equation):
        self.equation = equation
        self.reducedForm = ''
        self.polynomialDegree = 0
        self.discriminant = None
        self.solutions = {
            'comment': '',
            'first': None,
            'second': None
        }
        self.coefficients = {
            'a': 0,
            'b': 0,
            'c': 0
        }

    def makeReducedForm(self):
        self.addEqualPowers()
        for token in self.equation:
            value = self.makeReadableValue(token['value'])
            power = self.makeReadablePower(token['power'])
            self.reducedForm += value + power
        self.findPolynomialDegree()
        self.writeCoefficients()
        self.formatReducedForm()
        return self.reducedForm

    def addEqualPowers(self):
        powers = [token['power'] for token in self.equation]
        newEquation = []
        for i in range(0, max(powers) + 1):
            listOfEqualPowers = [item for item in self.equation if item['power'] == i]
            member = self.addPowers(listOfEqualPowers)
            if member['value']:
                newEquation.append(member)
        self.equation = newEquation

    def addPowers(self, equalPowers):
        if equalPowers:
            newValue = {'value': 0, 'power': equalPowers[0]['power']}
            for token in equalPowers:
                newValue['value'] += token['value']
        else:
            newValue = {'value': None, 'power': None}
        return newValue


    def findPolynomialDegree(self):
        powers = [token['power'] for token in self.equation]
        if powers:
            self.polynomialDegree = max(powers)
        else:
            self.polynomialDegree = 0
        return self.polynomialDegree


    def makeReadableValue(self, intVal):
        return str(intVal) if intVal <= 0 else '+' + str(intVal)

    def makeReadablePower(self, intPower):
        if intPower == 0:
            power = ''
        elif intPower == 1:
            power = '*X'
        else:
            power = '*X^' + str(intPower)
        return power

    def formatReducedForm(self):
        if self.reducedForm and self.polynomialDegree:
            if self.reducedForm[0] == '+':
                self.reducedForm = self.reducedForm[1:]
            self.reducedForm = " ".join(self.reducedForm) + ' = 0'
            pattern = re.compile(r"(?:( (?=(\.|\^)))|((?<=(\.|\^)) ))|((?<=\d) (?=\d))")
            self.reducedForm = re.sub(pattern, '', self.reducedForm)
        elif self.reducedForm == '':
            self.reducedForm = '0 = 0'
        else:
            raise Exception(self.colors['fail'] + 'Invalid equation' + self.colors['endcolor'])

    def findDiscriminant(self):
        if self.polynomialDegree > 2:
            raise Exception(self.colors['fail'] + "The polynomial degree is stricly greater than 2, I can't solve." + self.colors['endcolor'])
        else:
            if self.polynomialDegree == 2:
                self.discriminant = self.coefficients['b']**2 - 4 * self.coefficients['a'] * self.coefficients['c']
        return self.discriminant

    def writeCoefficients(self):
        a = [item for item in self.equation if item['power'] == 2]
        b = [item for item in self.equation if item['power'] == 1]
        c = [item for item in self.equation if item['power'] == 0]
        self.coefficients['a'] = 0 if not a else a[0]['value']
        self.coefficients['b'] = 0 if not b else b[0]['value']
        self.coefficients['c'] = 0 if not c else c[0]['value']

    def findSolutions(self):
        if self.discriminant != None:
            if self.discriminant >= 0:
                if self.discriminant > 0:
                    self.solutions['comment'] = 'Discriminant is strictly positive, the two solutions are:'
                else:
                    self.solutions['comment'] = 'Discriminant zero, equation has two equal solutions:'
                self.solutions['first'] = self.calcSolutionByDiscriminant(-1)
                self.solutions['second'] = self.calcSolutionByDiscriminant(1)
            else:
                self.solutions['comment'] = 'Discriminant is strictly negative, thee are no solutions:'
        else:
            if self.polynomialDegree:
                self.solutions['comment'] = 'The solution is:'
                self.solutions['first'] = self.calculateOneSolution()
            else:
                self.solutions['comment'] = 'All the real numbers are solution'
        return self.solutions

    def calcSolutionByDiscriminant(self, discrCoefficient):
        numerator = -1 * self.coefficients['b'] + discrCoefficient * math.sqrt(self.discriminant)
        denominator = 2 * self.coefficients['a']
        return numerator / denominator

    def calculateOneSolution(self):
        result = self.coefficients['c'] / (-1 * self.coefficients['b'])
        return result





















