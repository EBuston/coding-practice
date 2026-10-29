import numpy as np

g = np.zeros((15, 3)) #=> 2d matrix, 15x3
a = [[0,0,0]]
n_2 = np.zeros(15)
h=0

def check_multiples(x,y,z,a):
    for m in a:
         for p in range(-2,3,1):
            if [x,y,z] != m*p:
                a.append([x,y,z])
    '''if [x,y,z] not in a:
        a.append(z)
    elif z*(-1) not in a:
            a.append(z)'''
    return a


while h<125:
    for i in range(0,3,1): # loops through all options of $n_x$
        for j in range (0,3,1): # loops through $n_y$
            for k in range (0,3,1): # loops through $n_z$
                g[h,0] = -i+j+k
                g[h,1] = i-j+k
                g[h,2] = i+j-k

                x,y,z = g[h]
                #print(x,y,z)
                check_multiples(x,y,z,a)

                n_2[h]= g[h,0]**2 + g[h,1]**2 + g[h,2]**2

                h+=1
#print(g)
a_final=np.array(a)
print(a_final)
