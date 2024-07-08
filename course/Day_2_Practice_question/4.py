scores = ['100','50','90','50','70','60','10']

scores = [int(score) for score in scores]

total_sum = sum(scores)

average = total_sum / len(scores)

print(f"Sum: {total_sum}")
print(f"Average: {average}")