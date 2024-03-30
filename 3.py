import json
import matplotlib.pyplot as plt

def main():
    with open('pokedex.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    type_count = {}
    for pokemon in data['pokemon']:
        for poke_type in pokemon['type']:
            if poke_type in type_count:
                type_count[poke_type] += 1
            else:
                type_count[poke_type] = 1

    plt.figure(figsize=(10, 6))
    plt.bar(type_count.keys(), type_count.values(), color='skyblue')
    plt.xlabel('Тип')
    plt.ylabel('Кількість покемонів')
    plt.title('Кількість покемонів кожного типу')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
