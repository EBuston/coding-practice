import numpy as np

def find_gs(min, max, total_vectors):
    g = np.zeros((total_vectors, 3)) #=> 2d matrix, 125x3
    n_2 = np.zeros(total_vectors)
    h=0
    for i in range(-2,3,1): # loops through all options of $n_x$
        for j in range (-2,3,1): # loops through $n_y$
            for k in range (-2,3,1): # loops through $n_z$
                g[h,0] = -i+j+k
                g[h,1] = i-j+k
                g[h,2] = i+j-k

                n_2[h]= g[h,0]**2 + g[h,1]**2 + g[h,2]**2

                h+=1
    return np.array(g), np.array(n_2)

def find_unique(n_2, g, num_lowest_n_2s):
    unique=[] #the list of unique n_2 values
    for m in n_2:
        if m not in unique:
            unique.append(float(m))
    list.sort(unique)
    first = [] # first vectors with (num_lowest_n_2s) lowest magnitude values
    
    for h in range(num_lowest_n_2s):
        for q in range(len(n_2)):
            if float(n_2[q]) == unique[h]:
                first.append(g[q]) 
    print(unique[0:num_lowest_n_2s])
    return np.array(first)


g, n_2 = find_gs(-2,3,125)

first_15_vectors = find_unique(n_2,g,5)
print(first_15_vectors)
