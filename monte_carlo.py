import random

num_trials = 1000000
sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(num_trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    sum_counts[total] += 1

probabilities = {i: count / num_trials for i, count in sum_counts.items()}

print("Сума\tЙмовірність")
for total, probability in probabilities.items():
    print(f"{total}. {probability*100:.2f}")
