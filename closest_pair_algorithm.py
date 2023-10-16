class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight

def knapsack_fractional(W, items):
    items.sort(key=lambda x: x.value_per_weight, reverse=True)

    max_value = 0.0

    for item in items:
        if W >= item.weight:
            max_value += item.value
            W -= item.weight
        else:
            max_value += (item.value_per_weight * W)
            break

    return max_value

W = 50  # Knapsack capacity
items = [Item(10, 60), Item(20, 100), Item(30, 120)]  # Item weights and values

max_value = knapsack_fractional(W, items)
print("Maximum value:", max_value)
