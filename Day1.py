import numpy as np

n = int(input())
element = str(input())
freq = str(input())

np_element_split = np.array(element.split(' '))
np_element_int = np_element_split.astype(np.int)

np_freq_split = np.array(freq.split(' '))
np_freq_int = np_freq_split.astype(np.int)

s = ''
for i in range(n):
    for j in range(np_freq_int[i]):
        s += str(np_element_int[i]) + ' '

np_s_split = np.array(s.split(' ')[:-1])
np_s_int = np_s_split.astype(np.int)
s_sort = np.sort(np_s_int)

l = s_sort[:int((len(s_sort)/2))] #upper
u = s_sort[int((len(s_sort)/2)):] #lower

r = float(np.median(u)-np.median(l))
print(r)