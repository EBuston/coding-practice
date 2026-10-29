import numpy as np

g = np.zeros((125, 3)) #=> 2d matrix, 15x3
n_2 = np.zeros(125)
h=0

for i in range(-2,3,1): # loops through all options of $n_x$
    for j in range (-2,3,1): # loops through $n_y$
        for k in range (-2,3,1): # loops through $n_z$
            g[h,0] = -i+j+k
            g[h,1] = i-j+k
            g[h,2] = i+j-k

            n_2[h]= g[h,0]**2 + g[h,1]**2 + g[h,2]**2

            h+=1

unique=[] #the list of unique n_2 values
first_15_vectors = [] #list of 15 vectors with lowest n_2 values
for m in n_2:
    if m not in unique:
        unique.append(float(m))
list.sort(unique)
counts=[] #list of indices of vectors with lowest 3 values of n_2 
for q in range(len(n_2)):
    if float(n_2[q]) == unique[0] or float(n_2[q])==unique[1] or float(n_2[q])==unique[2]:
        counts.append(q)
        first_15_vectors.append(g[q])

first_15_vectors = np.array(first_15_vectors)
print(first_15_vectors)