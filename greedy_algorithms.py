def calculate_efficiency(items):
    for item, details in items.items():
        details['efficiency'] = details['calories'] / details['cost']

    return sorted(items.items(), key=lambda x: x[1]["efficiency"], reverse=True)


def greedy_algorithm(target_cost, items):
    result = {}
    for item in items:
        count = target_cost // item[1]['cost']
        if count >= 1:
            target_cost = target_cost - count * item[1]['cost']
            result[item[0]] = count
    if target_cost != 0:
        raise Exception("you have no pennies to spend the rest")
    return result


def dynamic_programming(target_cost, items):
    matrix = [[0 for _ in range(target_cost + 1)] for _ in range(len(items) + 1)]
    result = {}
    for i in range(len(items) + 1):
        for j in range(target_cost + 1):
            if i == 0 or j == 0:
                continue
            item = items[i - 1]
            previous_best_count = matrix[i][j - 1]
            count = target_cost // item[1]['cost']
            if count >= 1:
                target_cost = target_cost - count * item[1]['cost']
                result[item[0]] = count
            matrix[i][j] = previous_best_count + count
    return result


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
items = calculate_efficiency(items)
print("greedy_algorithm")
print(greedy_algorithm(1000, items))
print("dynamic_programming")
print(dynamic_programming(1000, items))
