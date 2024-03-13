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
    ratios = [(item, item_info["calories"] / item_info["cost"]) for item, item_info in items.items()]
    sorted_ratios = sorted(ratios, key=lambda x: x[1], reverse=True)
    n = len(sorted_ratios)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    print(n)
    
    print(sorted_ratios)
    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 and w == 0:
                dp[i][w] = 0
            elif ratios[i - 1][1] <= w:
                # print(dp[i - 1][w - ratios[i - 1][1]])
                dp[i][w] = max(items[ratios[i - 1][0]]['calories'] + dp[i - 1][w - int(ratios[i - 1][1])], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][budget]

def main():
    budget =input("Please, enter your budget >>>>>")
        
    if budget.isdigit():
        print(greedy_algorithm(int(budget)))
        dynamic_programming(int(budget))
    else:
        print('Invalid budget. Enter the integer, please')
        main()
        
if __name__ == '__main__':
    print(dynamic_programming(50))
