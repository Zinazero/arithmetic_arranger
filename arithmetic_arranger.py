def arithmetic_arranger(problems, boolean=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ""
    bottom_line = ""
    separator = ""
    result_line = ""
    for problem in problems:
        split_problem = problem.split(" ")

        if split_problem[0].isdigit() == False or split_problem[2].isdigit() == False:
            return "Error: Numbers must only contain digits."
        
        if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        num1 = int(split_problem[0])
        num2 = int(split_problem[2])
        operator = split_problem[1]
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
                
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2

        if problem != problems[0]:
            top_line += "    "
            bottom_line += "    "
            separator += "    "
            result_line += "    "

        max_length = max(len(split_problem[0]), len(split_problem[2]))
        top_line += str(num1).rjust(max_length + 2)
        bottom_line += operator + " " + str(num2).rjust(max_length)
        separator += "-" * (max_length + 2)
        result_line += str(result).rjust(max_length + 2)

    arranged_problems = top_line + "\n" + bottom_line + "\n" + separator

    if boolean:
        return arranged_problems + "\n" + result_line
    else:
        return arranged_problems



print(arithmetic_arranger(["3222 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 2"], True))