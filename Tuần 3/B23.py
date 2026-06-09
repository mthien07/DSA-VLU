import random
def bubble_sort(a):
    n = len(a)
    c = 0  
    s = 0  
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            c += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                s += 1
                swapped = True
        if not swapped:
            break
    return c, s

sizes = [10, 50, 100, 200, 500]
print(f"{'N':<5} | {'Best (Sorted)':<15} | {'Avg (Random)':<15} | {'Worst (Reverse)':<15}")
print("-" * 60)
for n in sizes:
    best_case = list(range(n))
    c_best, s_best = bubble_sort(best_case)
    avg_case = []
    for _ in range(n):
        avg_case.append(random.randint(1, 1000))
    c_avg, s_avg = bubble_sort(avg_case)
    worst_case = list(range(n, 0, -1))
    c_worst, s_worst = bubble_sort(worst_case)
    print(f"{n:<5} | C:{c_best:<4} S:{s_best:<4} | C:{c_avg:<4} S:{s_avg:<4} | C:{c_worst:<4} S:{s_worst:<4}")