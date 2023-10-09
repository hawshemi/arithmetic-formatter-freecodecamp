def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line, second_line, third_line, fourth_line = [], [], [], []

    for problem in problems:
        pieces = problem.split()
        first, operator, second = pieces

        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        third_line.append('-' * width)

        if answer:
            result = str(eval(problem))
            fourth_line.append(result.rjust(width))

    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    if answer:
        arranged_problems += "\n" + "    ".join(fourth_line)

    return arranged_problems
