import numpy as np
global h_bar, m_e, e
h_bar = 1.054572*10**(-34)
m_e = 9.109384*10**(-31)
e = 1.6*10**(-19)

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

def V_g_dd_fcc(g_dd, g_dd_mag, V_of_mag_g_d, considered_form_factors):
    #function to set up the V_g'' = V_(g-g') terms in the NxN matrix employing N lowest magnitude RLVs 
    #this only works for fcc lattices like Si, not GaAr, for which another function must be used
    # currently doesn't take into account filtering out g'' with certain magnitudes

    S_of_g_dd, sum_of_n_d_sq, V_g_dd = [], [], []
    for i in range(len(g_dd)):
        V_row = []
        S_of_g_dd_row = []
        for j in range(len(g_dd)):
            s = abs(g_dd[i][j][0])**2 + abs(g_dd[i][j][1])**2 + abs(g_dd[i][j][2])**2
            #if g_dd_mag[i][j] in considered_form_factors:
            sum_of_n_d_sq.append(g_dd_mag[i][j])

            S_of_g_dd_row.append(np.cos(np.pi/4 * (g_dd[i][j][0] + g_dd[i][j][1] + g_dd[i][j][2])))
            for k in V_of_mag_g_d:
                if s==k[0]:
                    V = k[1]
                else:
                    V = 0
            V_row.append(V)
        S_of_g_dd.append(S_of_g_dd_row)
        V_g_dd.append(V_row)
    return np.array(S_of_g_dd)*np.array(V_g_dd) #, np.array(sum_of_n_d_sq)

#create matrix of g_dd s
def matrix_g_dd(gs):
    #g_dd = np.zeros((len(gs),len(gs)))
    g_dd = []
    g_dd_mag = []
    for i in range(len(gs)):
        row = []
        row_mag_sq = []
        for j in range(len(gs)):
            val = gs[i] - gs[j]
            row_mag_sq.append(val[0]**2 + val[1]**2 + val[2]**2)
            row.append(val)
        g_dd.append(row)
        g_dd_mag.append(row_mag_sq)
    print(np.array(g_dd))
    print(np.array(g_dd_mag))
    return np.array(g_dd), np.array(g_dd_mag)

V_of_mag = [[3,0],[8,0],[11,0]] #for free electron
considered_form_factors_Si = [3,8,11] #considered form factors V3, V8, V11
k = [1,1,1] #trial setting for vector k

g, n_2 = find_gs(-2,3,125)
first_vectors = find_unique(n_2,g,3)
#print(first_vectors)
g_dd, g_dd_mag = matrix_g_dd(first_vectors)
V_g_dd_vals = V_g_dd_fcc(g_dd,g_dd_mag, V_of_mag, considered_form_factors_Si)
#print(V_g_dd_vals)


def create_matrix(k,g):
    for i in range(len(g)):
        eqn = -h_bar**2/(2*m_e*e) * (abs(k + g[i]))**2
        #print(eqn)
    return eqn

e_vals = np.linalg.eigvalsh([[1,0],[0,1]])
#create_matrix(k,g)

