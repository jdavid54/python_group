import matplotlib.pyplot as plt

def proba_bday(n):
    if n <= 0:
        return 0
    elif n > 365:
        return 1
    else:
        proba = 1.0
        for i in range(1, n):
            proba *= (365 - i) / 365
        return 1 - proba

# data for the graph
number_persons = list(range(1, 101))
proba_bday_list = [proba_bday(n) for n in number_persons]

# tracing graph
plt.figure(figsize=(10, 6))
plt.plot(number_persons, proba_bday_list, marker='o', linestyle='-')
plt.title("Probability to have 2 persons in a group with same birthday date")
plt.xlabel("Number of persons")
plt.ylabel("Probability")
plt.grid(True)
plt.xticks(range(0, 101, 5))
plt.yticks([i * 0.1 for i in range(11)])
plt.show()
