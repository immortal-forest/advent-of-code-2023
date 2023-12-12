import re

def filter_number(items: list):
    _i = []
    for item in items:
        if item != '':
            if len(item) > 1:
                for i in list(item):
                    _i.append(i)
            else:
                _i.append(item)
    return _i

# both works, but second one seems better

def filter_word(line):
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    val = str(line)
    print(val)
    new_val = list(val)
    for i in range(len(val) + 1):
        for j in range(len(val) + 1):
            sstr = val[i:j]
            if sstr in words:
                new_val[i] = str(words.index(sstr) + 1)
    return "".join(new_val)

def filter_word_hmm(line):
    words_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    _line = str(line)
    parsed_line = list(_line)
    for key in words_map.keys():
        if key in _line:
            for _s in re.finditer(key, _line):
                parsed_line[_s.start()] = words_map[key]

    return "".join(parsed_line)



def get_numbers(numbers):
    nums = filter_number(numbers)
    if len(nums) > 1:
        val = nums[0] + nums[-1]
    elif len(nums) == 1:
        val = nums[0] + nums[0]
    else:
        val = 0
    return int(val)



def part1(lines: list[str]):
    calibrations = []
    for line in lines:
        numbers = re.split(r'\D', line.strip())
        val = get_numbers(numbers)
        calibrations.append(val)

    return sum(calibrations)


def part2(lines: list[str]):
    calibrations = []
    for line in lines:
        parsed_line = filter_word_hmm(line.strip())
        numbers = re.split(r'\D', parsed_line)
        num = get_numbers(numbers)
        calibrations.append(num)
    return sum(calibrations)

def get_lines():
    with open("input", 'r') as file:
        data = file.readlines()
    return data

def main():
    lines = get_lines()
    print("\n========== Part - 1 ==========")
    print(f"Calibration value: {part1(lines)}")
    print("==============================\n")
    print("\n========== Part - 2 ==========")
    print(f"Calibration value: {part2(lines)}")
    print("==============================\n")

if __name__ == "__main__":
    main()

