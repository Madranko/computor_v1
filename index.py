import sys
import parser
import computor

# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

if len(sys.argv) == 2:

    parser = parser.Parser(sys.argv[1])
    try:
        parsedLine = parser.parseLine()
    except Exception as error:
        print(error)
        sys.exit()

    computor = computor.Computor(parsedLine)
    reducedForm = computor.makeReducedForm()
    degree = computor.getPolynomialDegree()
    print('Reduced form:', reducedForm)
    print('Polynomial degree:', degree)

    try:
        discriminant = computor.findDiscriminant()
        print('Discriminant:', discriminant)
    except Exception as error:
        print(error)
        sys.exit()

    solutions = computor.findSolutions()
    print(solutions)
