import operator

ops = {"+": operator.add, "-": operator.sub}


def arithmetic_arranger(problems, showResult=False):
    arranged_problems = ''
    sndValRow = []
    dashesRow = []
    resultsRow = []
    spaceBetweenExercise = ' '*4
    for i, problem in enumerate(problems):
        a, operator, b = problem.split(' ')
        dashes = (len(a) + 2)*'-' if len(a) > len(b) else (len(b) + 2)*'-'
        whiteSpacesA = (len(dashes) - len(a))*' '
        whiteSpacesB = (len(dashes) - len(b) - 1)*' '
        sndValRow.append(operator + whiteSpacesB + b + spaceBetweenExercise)
        dashesRow.append(dashes + spaceBetweenExercise)
        arranged_problems += whiteSpacesA + a + spaceBetweenExercise
        if i == len(problems) - 1:
            arranged_problems += '\n'
        if showResult:
            c = str(ops[operator](int(a), int(b)))
            whiteSpacesC = (len(dashes) - len(c))*' '
            resultsRow.append(whiteSpacesC + c + spaceBetweenExercise)
    for i, val in enumerate(sndValRow):
        arranged_problems += val
        if i == len(sndValRow) - 1:
            arranged_problems += '\n'
    for i, dashes in enumerate(dashesRow):
        arranged_problems += dashes
        if i == len(dashesRow) - 1:
            arranged_problems += '\n'
    if showResult:
        for result in resultsRow:
            arranged_problems += result
    print(arranged_problems)
    return arranged_problems


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
