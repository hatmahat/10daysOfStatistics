def median(arr):
    '''Return median array

    Parameters
    ----------
    arr : float / int list
    '''
    arr.sort()
    if len(arr)%2 == 0:
        med = .5*(arr[int(len(arr)/2)] + arr[int(len(arr)/2-1)])
    else:
        med = arr[int(len(arr)/2)]
    return med

n = int(input().strip())
x_arr = input().strip().split(' ')

arr = [int(i) for i in x_arr]

Q2 = median(arr)

l_arr = [i for i in arr if i < Q2]
u_arr = [i for i in arr if i > Q2]

Q1 = median(l_arr); Q3 = median(u_arr)

print(int(Q1))
print(int(Q2))
print(int(Q3))