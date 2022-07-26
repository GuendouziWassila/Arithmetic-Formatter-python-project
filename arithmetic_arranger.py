import re


def arithmetic_arranger(arithProblems, bool=False):
    '''for each element in the list "arithProblems" (each problem) we will         retreive in differents lists  the right operands,         the left ones,      the operators and the results (if bool is true) and then print them in       the appropriate format
    '''
    try:
        if (len(arithProblems) > 5):
            raise Exception("Error: Too many problems.")

        rightOps = []
        leftOps = []
        operators = []
        results = []

        for elt in arithProblems:

            list = []
            list = elt.split()

            #check the constraints
            if (len(list) != 3):
                raise Exception("Error: the syntax is not correct.")

            if (list[1] != '+' and list[1] != '-'):
                raise Exception("Error: Operator must be '+' or '-'.")

            t1 = re.search('[^0-9]', list[0])
            t2 = re.search('[^0-9]', list[2])
            if t1 is not None or t2 is not None:
                raise Exception("Error: Numbers must only contain digits.")

            if (len(list[0]) > 4 or len(list[2]) > 4):
                raise Exception(
                    "Error: Numbers cannot be more than four digits.")

            leftOps.append(list[0])
            rightOps.append(list[2])
            operators.append(list[1])

            if (bool):
                if (list[1] == '+'):
                    results.append(str(int(list[0]) + int(list[2])))
                if (list[1] == '-'):
                    results.append(str(int(list[0]) - int(list[2])))

        displayLine1 = ''
        displayLine2 = ''
        displaydashes = ''
        displayresults = ''

        # FOR LOOP TO CONSTRUCT THE FIRST HORIZONTAL LINE AND THE DASHES LINE
        for i in range(len(leftOps)):

            displaydashes = displaydashes + '--'  # 2 dashes
            displayLine1 = displayLine1 + '  '  # 2 spaces

            sous = len(leftOps[i]) - len(rightOps[i])
            if (sous < 0):
                for _ in range(sous * (-1)):
                    displayLine1 = displayLine1 + ' '
                    displaydashes = displaydashes + '-'
            displayLine1 = displayLine1 + leftOps[i]
            for _ in range(len(leftOps[i])):
                displaydashes = displaydashes + '-'
            if i != len(leftOps) - 1:
                displayLine1 = displayLine1 + '    '  # 4 spaces
                displaydashes = displaydashes + '    '  # 4 spaces
            i = i + 1

        #FOR LOOP TO CONSTRUCT THE SECOND HORIZONTAL LINE
        for i in range(len(rightOps)):

            displayLine2 = displayLine2 + operators[i] + ' '  # with 1 space

            sous = len(rightOps[i]) - len(leftOps[i])
            if (sous < 0):
                for _ in range(sous * (-1)):
                    displayLine2 = displayLine2 + ' '

            displayLine2 = displayLine2 + rightOps[i]
            if i != len(rightOps) - 1:
                displayLine2 = displayLine2 + '    '  # with 4 space
            i = i + 1

        # ANOTHER FOR LOOP TO CONSTRUCT THE HORIZONTAL LINE THAT REPRESENTS RESULTS
        if (bool):
            for i in range(len(results)):

                if (((len(results[i]) > len(leftOps[i])) and
                     (len(results[i]) > len(rightOps[i])))
                        or (int(results[i]) < 0)):
                    displayresults = displayresults + ' ' + results[
                        i]  # add one space

                else:
                    displayresults = displayresults + '  ' + results[
                        i]  # Add 2 spaces
                if i != len(results) - 1:
                    displayresults = displayresults + '    '  #4spaces
                i = i + 1

        # the final display
        if (bool):
            f = displayLine1 + '\n' + displayLine2 + '\n' + displaydashes + '\n' + displayresults
        else:
            f = displayLine1 + '\n' + displayLine2 + '\n' + displaydashes

    except Exception as e:
        return str(e)

    return f
