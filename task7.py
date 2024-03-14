import random
import matplotlib.pyplot as plt

def monte_carlo(n):
    dices_amount = {i: 0 for i in range(2, 13)}
    for _ in range(n):
        num = random.randint(1, 6) + random.randint(1, 6)
        dices_amount[num] += 1
    
    dices_amount = {key: "{:.2f}".format((val / n) * 100) for key, val in dices_amount.items()}
    return dices_amount

    
    
    
probabilities =monte_carlo(10000000)
y_values = sorted([float(x) for x in list(probabilities.values())])

def addlabels(y):
    for i in range(len(y)):
        plt.text(i,y[i],y[i])
        
plt.bar(probabilities.keys(), y_values, color='teal')
addlabels(y_values)
plt.xlabel('Amount on the dices')
plt.ylabel('Probability (%)')
plt.title('Probability of each amount when rolling two dice')
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


print(f"| {'Amount':<20} | {'Result':<20} |")
print(f"| {'-'*20} | {'-'*20} |")
for key, val in probabilities.items():
    print(f"| {key:<20} | {f'{val}%':<20} |")