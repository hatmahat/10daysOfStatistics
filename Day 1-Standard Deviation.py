def std(n, nums):
    int_nums = [int(i) for i in nums]
    mean = sum(int_nums)/n
    var = [(x - mean)**2 for x in int_nums]
    std = (sum(var)/n)**(1/2)
    return round(std, 1)

N = int(input().strip())
X = input().strip().split()

print(std(N, X))