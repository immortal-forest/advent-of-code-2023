class Card:
    def __init__(self, id: int, winning_numbers: list, card_numbers: list) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
        self.matching_numbers = [i for i in card_numbers if i in winning_numbers]


def get_lines():
    with open("input", 'r') as file:
        data = file.readlines()
    return data


def parse_line(line: str):
    card_part, num_part = line.split(":")
    card_id = card_part.replace("Card ", '')
    winning_numbers, card_numbers = num_part.split("|")
    return Card(
        card_id,
        list(filter(None, winning_numbers.strip().split(" "))),
        list(filter(None, card_numbers.strip().split(" ")))
    )


def card_value(card: Card):
    val = 0
    size = len(card.matching_numbers)
    if size == 1:
        return 1
    elif size > 1:
        val = 1
        match = card.matching_numbers[1:size]
        for _ in range(len(match)):
            val *= 2
        return val
    else:
        return 0


def part1(lines):
    scratchcard_worth = []
    for line in lines:
        card = parse_line(line)
        card_val = card_value(card)
        scratchcard_worth.append(card_val)

    return sum(scratchcard_worth)


def main():
    lines = get_lines()
    print("\n========== Part - 1 ==========")
    print(f"Points: {part1(lines)}\n")


if __name__ == '__main__':
    main()
