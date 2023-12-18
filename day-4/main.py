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
        int(card_id),
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


def process_cards(original_cards: dict, card_id):
    count = 1
    for card in original_cards[str(card_id)]['cards']:
        if original_cards[str(card_id)]['copies']:
            count += process_cards(original_cards, card)
        else:
            count += 1
    return count


def part2(lines):
    size = len(lines)
    original_cards = {}
    for line in lines:
        card = parse_line(line)
        _size = len(card.matching_numbers)
        cp = [i for i in range(card.id + 1, _size + 1 + card.id) if i <= size]
        original_cards[str(card.id)] = {
            "copies": True if cp else False,
            "cards": cp
        }
    
    count = 0
    for card in range(1, 207):
        count += process_cards(original_cards, card)
        print(count)

    return count


def main():
    lines = get_lines()
    print("\n========== Part - 1 ==========")
    print(f"Points: {part1(lines)}\n")
    print("\n========== Part - 2 ==========")
    print(f"Total: {part2(lines)}\n")


if __name__ == '__main__':
    main()
