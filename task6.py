items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    _items = dict(sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True))
    food_list = []
    
    for item in _items:
        if budget >= _items[item]['cost']:
            budget -= _items[item]['cost']
            food_list.append(item)
            
    return food_list

def dynamic_programming(budget):
    num_items = len(items)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            current_item = items[list(items.keys())[i - 1]]

            if current_item["cost"] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(
                    dp_table[i - 1][j],
                    dp_table[i - 1][j - current_item["cost"]]
                    + current_item["calories"],
                )

    selected_items = []
    i, j = num_items, budget

    while i > 0 and j > 0:
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    selected_items.reverse()

    return selected_items

def main():
    budget =input("Please, enter your budget >>>>>")
        
    if budget.isdigit():
        print(f'Greedy algorithm: {greedy_algorithm(int(budget))}')
        print(f'Dynamic programming: {dynamic_programming(int(budget))}')
    else:
        print('Invalid budget. Enter the integer, please')
        main()
        
if __name__ == '__main__':
    main()
