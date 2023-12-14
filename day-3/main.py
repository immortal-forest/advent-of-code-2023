from itertools import chain

symbols = ['@', '#', '$', '%', '&', '*', '-', '+', '/', '=']


def get_lines():
    with open('input', 'r') as file:
        data = file.readlines()
    return data


def iter_left(line: str, pos: int):
    digit_list = []
    _pos = pos
    
    while True:
        _pos -= 1
        # no number adjacent
        if line[_pos] == '.' or line[_pos] in symbols:
            break

        if line[_pos].isdigit():
            digit_list.append(line[_pos])

    return "".join(reversed(digit_list))


def iter_right(line: str, pos: int):
    digit_list = []
    _pos = pos

    while True:
        _pos += 1
        # no number on right
        if line[_pos] == '.' or line[_pos] in symbols:
            break

        if line[_pos].isdigit():
            digit_list.append(line[_pos])

    return "".join(digit_list)


def find_numbers(line: str, pos: int):
    sep_nums = True if (line[pos] == '.' or line[pos] in symbols) else False

    if sep_nums:
        middle_digit = ''
    else:
        middle_digit = line[pos]

    # padding the line with '.' to avoid exceptions
    line = '...' + line + '...'
    pos += 3 # since we added 3 chars at the beginning of the line

    # we check if number exists on either side of the line from pos by 1
    left_flag = False if not line[pos - 1].isdigit() else True
    right_flag = False if not line[pos + 1].isdigit() else True

    left_digits = ''
    right_digits = ''

    if left_flag:
        left_digits = iter_left(line, pos)
    if right_flag:
        right_digits = iter_right(line, pos)

    if sep_nums:
        if left_digits == '' and right_digits == '':
            return []
        elif left_digits == '':
            return [int(right_digits)]
        elif right_digits == '':
            return [int(left_digits)]
        else:
            return [int(left_digits), int(right_digits)]

    number = left_digits + middle_digit + right_digits

    if number == '':
        return []
    return [int(number)]


def find_adjacent(l_index: int, c_pos: int):
    lines =  get_lines()
    
    current_line_pos = l_index
    
    prev_line_pos = -1
    prev_line_nums = []

    next_line_pos = -1
    next_line_nums = []

    if l_index > 0:
        prev_line_pos = l_index - 1
        prev_line_nums = find_numbers(lines[prev_line_pos], c_pos)

    if (l_index + 1) < len(lines):
        next_line_pos = l_index + 1
        next_line_nums = find_numbers(lines[next_line_pos], c_pos)
    
    current_line_nums = find_numbers(lines[current_line_pos], c_pos)

    _t = [prev_line_nums, current_line_nums, next_line_nums]
#    filter_t = [i for i in _t if len(i) != 0]
    filter_t = list(chain.from_iterable(_t))

    return filter_t


def part1(lines):
    adjacent_numbers = []

    for index, line in enumerate(lines):
        for pos, char in enumerate(line):
            if char in symbols:
                 # get the numbers adjacent to the char
                 nums = find_adjacent(index, pos)
                 if len(nums) == 0:
                     continue
                 adjacent_numbers.extend(nums)

    return sum(adjacent_numbers)


def main():
    lines = get_lines()
    print("\n========== Part - 1 ==========")
    print(f"Sum: {part1(lines)}\n")
    print("\n========== Part - 2 ==========")
    print("\n")


if __name__ == "__main__":
    main()

