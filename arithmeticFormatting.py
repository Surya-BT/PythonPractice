def arithmetic_arranger(problems, show_answers=False):
    empty_space = [' ']
    space_btw_operator_and_num = 1
    space_btw_operations = 4
    fstring_op_line1 =''
    fstring_op_line2 =''
    fstring_horiz = ''
    fstring_res = ''

    if len(problems) > 5:
        return "Error: Too many problems."

    num1 = [x.split(' ')[0] for x in problems]
    print(num1)
    num2 = [x.split(' ')[2] for x in problems]
    print(num2)
    operator = [x.split(' ')[1] for x in problems]
    print(operator)
    res = []

    checkOperator = lambda x: x in ["+","-"]

    crtOperations = list(filter(checkOperator,operator))

    # check conditions
    if not len(crtOperations) == len(problems):
        return "Error: Operator must be '+' or '-'."

    for i in range(len(problems)):
        if num1[i].isdigit() and num2[i].isdigit():
            print(len(num1[i]),len(num2[i]))
            if len(num1[i]) > 4 or len(num2[i]) > 4:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Numbers must only contain digits."
    
    # print the problem
    for i in range(len(num1)):

        if operator[i] == '+':
            res.append(str(int(num1[i])+int(num2[i])))
        else:
            res.append(str(int(num1[i])-int(num2[i])))
        print(res)
        horiz_line = ['-']
        if len(num1[i]) < len(num2[i]):
            #print("num1 less than num2")
            num2[i] = ''.join(empty_space*(space_btw_operator_and_num)) + num2[i]
            num1[i] = ''.join(empty_space*abs(len(num1[i])-len(num2[i]))) + num1[i]
            horiz_line = ''.join(horiz_line*(len(num2[i])+1))
            res[i] = ''.join(empty_space*abs(len(res[i])-len(num2[i]))) + res[i]
        else:
            #print("num2 less than num1")
            num1[i] = ''.join(empty_space*(space_btw_operator_and_num)) + num1[i]
            num2[i] = ''.join(empty_space*abs(len(num1[i])-len(num2[i]))) + num2[i]
            horiz_line = ''.join(horiz_line*(len(num1[i])+1))
            res[i] = ''.join(empty_space*abs(len(res[i])-len(num1[i]))) + res[i]

        
         
        fstring_op_line1 +=  ' ' + num1[i]
        fstring_op_line2 += operator[i]+num2[i]
        fstring_horiz += horiz_line
        fstring_res += ' ' + res[i]

        # insert space between operations
        if i < len(num1)-1:
            fstring_op_line1 += ''.join(empty_space*space_btw_operations)
            fstring_op_line2 += ''.join(empty_space*space_btw_operations)    
            fstring_horiz += ''.join(empty_space*space_btw_operations)
            fstring_res += ''.join(empty_space*space_btw_operations)
    
    if show_answers:
        problems = f"{fstring_op_line1}\n{fstring_op_line2}\n{fstring_horiz}\n{fstring_res}"
    else:
        problems = f"{fstring_op_line1}\n{fstring_op_line2}\n{fstring_horiz}"
    
    return problems

#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
# test 1
#print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
#test 10
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')