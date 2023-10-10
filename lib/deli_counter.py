
katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
        return "The line is currently empty."
    else:
        names=""
        for index, name in enumerate(katz_deli):
            names=names + f' {index +1}. {name}'
        # print("The line is currently: 1. Ada 2. Grace 3. Kent")
        line=f'The line is currently:{names}'
        print(line)
        return line

def take_a_number(line, name):
    line.append(name)
    print(f'Welcome, {name}. You are number {len(line)} in line.')

    return line

def now_serving(line):
    if len(line)> 0:
        print(f'Currently serving {line[0]}.')
        name= line[0]
        del line[0]
    else:
        print("There is nobody waiting to be served!")
        return "There is nobody waiting to be served!"







