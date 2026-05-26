# --- 1:

grades = [5, 3, 4, 2, 1, 5, 3]
result = []

for grade in grades:
    match grade:
        case 5:
            result.append([grade, 'отлично'])
        case 3 | 4:
            result.append([grade, 'хорошо'])
        case 2 | 1:
            result.append([grade, 'неудовлетворительно'])

print(result)


# --- 2:

string = '{[3([475,(){}789]7,45)]} '

stack = []
is_valid = False

brackets = {')': '(',
            ']': '[',
            '}': '{'}
            
def check_valid(string):
    
    for char in string:
        if char in brackets.values():
            stack.append(char)

        elif char in brackets:
            if not stack:
                return False
            
            last_open = stack.pop()

            if last_open != brackets[char]:
                return False
    return not stack

is_valid = check_valid(string)

print(is_valid)