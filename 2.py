import matplotlib.pyplot as plt

lorem_ipsum = "In the heart of the bustling city, amidst the cacophony of urban life, there exists a sanctuary—a place where time slows, and tranquility reigns. Here, towering skyscrapers give way to lush greenery, and the frenetic pace of the streets fades into a gentle murmur. It's a refuge for weary souls, a haven where one can escape the demands of modernity and reconnect with nature's rhythms. Surrounded by the symphony of birdsong and the rustle of leaves, one finds solace in the simple joys of existence. This sanctuary is not merely a physical space but a state of mind—a reminder to pause, breathe, and appreciate the beauty that surrounds us."


def prepare_data(input: str) -> dict:
    data = {}
    for char in input:
        if char.isalpha():
            char = char.lower()
            data[char] = data.get(char, 0) + 1
    return data


def draw_gist(data: dict):
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()))

    plt.savefig("image.png")
    plt.show()


def main():
    draw_gist(prepare_data(lorem_ipsum))


if __name__ == "__main__":
    main()