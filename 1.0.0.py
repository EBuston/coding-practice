import numpy as np

def find_gs(min, max, total_vectors):
    g = np.zeros((total_vectors, 3)) #=> 2d matrix, 125x3
    n_2 = np.zeros(total_vectors)
    h=0
    for i in range(min,max,1): # loops through all options of $n_x$
        for j in range (min,max,1): # loops through $n_y$
            for k in range (min,max,1): # loops through $n_z$
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
    #print(unique[0:num_lowest_n_2s])
    return np.array(first)

def V_g_dd_fcc(n_2, g, first_vectors, V_of_mag_g_d, considered_form_factors):
    #function to set up the V_g'' = V_(g-g') terms in the NxN matrix employing N lowest magnitude RLVs 
    #this only works for fcc lattices like Si, not GaAr, for which another function must be used
    S_of_g_dd, sum_of_n_d_sq, V_g_dd = [], [], []
    for i in range(len(first_vectors)):
        s = abs(first_vectors[i][0])**2 + abs(first_vectors[i][1])**2 + abs(first_vectors[i][2])**2
        if s in considered_form_factors:
            sum_of_n_d_sq.append(s)
 
            S_of_g_dd.append(np.cos(np.pi/4 * (first_vectors[i][0] + first_vectors[i][1] + first_vectors[i][2])))
            for j in V_of_mag_g_d:
                if s==j[0]:
                    V = j[1]
            V_g_dd.append(V)
    return np.array(S_of_g_dd)*np.array(V_g_dd) #, np.array(sum_of_n_d_sq)



V_of_mag = [[0,0],[3,0],[8,0],[11,0]] #for free electron
considered_form_factors_Si = [0,3,8,11] #considered form factors V0, V3, V8, V11

g, n_2 = find_gs(-2,3,125)
first_vectors = find_unique(n_2,g,5)
#print(first_vectors)
print(V_g_dd_fcc(n_2,g,first_vectors, V_of_mag, considered_form_factors_Si))



e_vals = np.linalg.eigvalsh([[1,0],[0,1]])
