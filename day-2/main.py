class Cubes:
    def __init__(self) -> None:
        self.red = 0
        self.blue = 0
        self.green = 0

    def set_count(self, color: str, count: int):
        if color == 'red':
            self.red = count
        elif color == 'blue':
            self.blue = count
        else:
            self.green = count

    def get_count(self, color: str):
        if color == 'red':
            return self.red
        elif color == 'blue':
            return self.blue
        else:
            return self.green

    def __repr__(self) -> str:
        return f"<{self.red} red, {self.blue} blue, {self.green} green>"

    def __str__(self) -> str:
        return self.__repr__()


class Game:
    def __init__(self, id, c: list[Cubes]) -> None:
        self.id: int = id
        self.cubes: list[Cubes] = c


def get_lines():
    with open("input", 'r') as file:
        data = file.readlines()
    return data


def parse_cubes(subsets: list[str]):
    cubes_list: list[Cubes] = []
    for subset in subsets:
        _cubes = Cubes()
        for cube in subset.strip().split(", "):
            count, color = cube.split(" ")
            _cubes.set_count(color, int(count))
        cubes_list.append(_cubes)
    return cubes_list


def parse_game(line: str):
    # cubes -> red, green, blue
    # Game <game_id>: <list of cubes>; <list of cubes>, ...
    game_details, subsets = line.split(":")
    
    game_id = int(game_details.removeprefix("Game "))
    subsets = parse_cubes(subsets.split(";"))
    return Game(game_id, subsets)


def part1(lines):
    # constraints: 12 red, 13 green, 14 blue
    possible_games = []
    for line in lines:
        game = parse_game(line)
        for cubes in game.cubes:
            _r = cubes.red
            _g = cubes.green
            _b = cubes.blue
            if _r > 12 or _g > 13 or _b > 14:
                possible = False
                break
            else:
                possible = True
        if possible:
            possible_games.append(game.id)
    return sum(possible_games)


def part2(lines):
    power_of_minimum_cubes = []
    for line in lines:
        game = parse_game(line)
        red_cubes = []
        blue_cubes = []
        green_cubes = []
        for cube in game.cubes:
            red_cubes.append(cube.get_count('red'))
            blue_cubes.append(cube.get_count('blue'))
            green_cubes.append(cube.get_count('green'))
        min_red_cubes = max(red_cubes)
        min_blue_cubes = max(blue_cubes)
        min_green_cubes = max(green_cubes)
        power_of_minimum_cubes.append(min_red_cubes * min_blue_cubes * min_green_cubes)
    return sum(power_of_minimum_cubes)



def main():
    lines = get_lines()
    print("\n========== Part - 1 ==========")
    print(f"Sum: {part1(lines)}\n")
    print("\n========== Part - 2 ==========")
    print(f"Sum: {part2(lines)}\n")


if __name__ == "__main__":
    main()

