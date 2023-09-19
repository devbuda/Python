# Arithmetic Formatter - Victor Freire (devbuda)

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_width = max(len(num1), len(num2))
        line1 = num1.rjust(max_width + 2)
        line2 = operator + num2.rjust(max_width + 1)
        dashes = '-' * (max_width + 2)

        arranged_problems.extend([line1, line2, dashes])

    arranged = '    '.join(arranged_problems)

    if show_answers:
        answers = []
        for problem in problems:
            parts = problem.split()
            num1 = int(parts[0])
            operator = parts[1]
            num2 = int(parts[2])

            if operator == '+':
                result = num1 + num2
            else:
                result = num1 - num2

            answers.append(str(result).rjust(max_width + 2))

        arranged += '\n' + '    '.join(answers)

    return arranged
