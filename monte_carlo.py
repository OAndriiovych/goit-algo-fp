import random

num_trials = 1000000
sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(num_trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    sum_counts[total] += 1

probabilities = {i: count / num_trials for i, count in sum_counts.items()}

l = list()
l.append(2.78)
l.append(5.56)
l.append(8.33)
l.append(11.11)
l.append(13.89)
l.append(16.67)
l.append(13.89)
l.append(11.11)
l.append(8.33)
l.append(5.56)
l.append(2.78)
print("Сума | Експериментальна ймовірність | Істина ймовірність | Різниця")
print("--- | --- | --- | ---")
for total, probability in probabilities.items():
    true_probabilities = l.pop()
    print(f"{total} | {probability*100:.2f} | {true_probabilities} | {true_probabilities-probability*100:.2f}")
