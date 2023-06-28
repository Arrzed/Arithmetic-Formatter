def arithmetic_arranger(x,show_results=False):
    top = ''
    middle = ''
    dash = ''   # variable for updating the dash count to print
    dashes = ''
    result = ''
    # keeps track of the current total between the numbers in the loop and
    # returns the whole thing once finished
    total = 0  

    if len(x) > 5:
        return 'Error: Too many problems'
    
    for elem in x:
        pieces = elem.split()
        length = max(len(pieces[0]),len(pieces[2]))
        dash = '-' * (length + 2)

        try:
            int(pieces[0])
            int(pieces[2])
        except:
            return 'Error: Numbers must only contain digits.'

        if len(pieces[0]) > 4 or len(pieces[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if pieces[1] == '+' or pieces[1] == '-':
            if pieces[1] == '+':
                total = int(pieces[0]) + int(pieces[2])
            else:
                total = int(pieces[0]) - int(pieces[2])
        else:
            return 'Error: Operator must be \'+\' or \'-\'.'

        top = top + pieces[0].rjust(length + 2,' ') + '    '
        middle = middle + pieces[1] + ' ' + pieces[2].rjust(length,' ') + '    '
        dashes = dashes + dash + '    '
        result = result + str(total).rjust(length + 2,' ') + '    '
        
    total = top + '\n' + middle + '\n' + dashes
    if show_results == True:
        return total + '\n' + result

    return total
