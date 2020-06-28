import re


def arithmetic_arranger(problems, show_result=None):
    """Main logic goes here"""

    error = validate_problems(problems)
    if error:
        return "Error: {}".format(error)

    arranged_data = []
    for problem in problems:
        operand1, operator, operand2, max_len = parse_problem(problem)
        operand1 = int(operand1)
        operand2 = int(operand2)
        max_len += 2

        arranged_item = {
            'operand1': operand1,
            'operator': operator,
            'operand2': operand2,
            'separator': ['-' for i in range(max_len)],
            'result_line': operand1 + operand2 if operator == '+' else operand1 - operand2,
            'max_len': max_len
        }

        arranged_data.append(arranged_item)

    first_line = second_line = third_line = fourth_line = ''
    for i in range(len(arranged_data)):
        first_line += print_part(arranged_data[i]['operand1'], arranged_data[i]['max_len'])
        first_line += '    ' if i < len(arranged_data)-1 else ''

        second_line += '{} '.format(arranged_data[i]['operator'])
        second_line += print_part(arranged_data[i]['operand2'], arranged_data[i]['max_len']-2)
        second_line += '    ' if i < len(arranged_data)-1 else ''

        third_line += ''.join(arranged_data[i]['separator'])
        third_line += '    ' if i < len(arranged_data)-1 else ''

        fourth_line += print_part(arranged_data[i]['result_line'], arranged_data[i]['max_len'])
        fourth_line += '    ' if i < len(arranged_data)-1 else ''

    if show_result:
        return '{}\n{}\n{}\n{}'.format(first_line, second_line, third_line, fourth_line)
    return '{}\n{}\n{}'.format(first_line, second_line, third_line)


def validate_problems(problems):
    """Validate all initial data"""

    error = None
    if len(problems) > 5:
        error = "Too many problems."
    else:
        for problem in problems:
            operand1, operator, operand2, max_len = parse_problem(problem)
            if operator not in ['+', '-']:
                error = "Operator must be '+' or '-'."
            elif len(operand1) > 4 or len(operand2) > 4:
                error = "Numbers cannot be more than four digits."
            elif re.search('[^0-9]+', operand1) or re.search('[^0-9]+', operand2):
                error = "Numbers must only contain digits."

    return error


def parse_problem(problem):
    """Receives initial problem and prepare it for future manipulations"""

    operand1, operator, operand2 = problem.split()
    operator = operator.strip()
    max_len = len(operand1) if len(operand1) > len(operand2) else len(operand2)
    return [operand1, operator, operand2, max_len]


def print_part(operand, required_length):
    """Return part of the string formatted with spaces"""

    # Fill with required spaces to imitate right-alignment
    result = [' ' for i in range(required_length - len(str(operand)))]

    return ''.join(result) + str(operand)