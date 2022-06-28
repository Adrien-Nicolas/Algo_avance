from pulp import *
import numpy as np


X=[]
P = []
X_dict = {}
True_tab = []



# variables du problème
for i in range(len(complete_graph)):
    for j in range(len(complete_graph)):
        X.append(LpVariable("X_" + str(i) + "_" + str(j), 0, 1, LpInteger))
        X_dict[("X_" + str(i) + "_" + str(j))] = LpVariable("X_" + str(i) + "_" + str(j), 0, 1, LpInteger)
        P.append(complete_graph[i][j])

# probleme
prob = LpProblem("plus court chemin", LpMinimize)

# objectif
# Somme de la multiplication des poids de chaque arc
prob += lpSum([P[i] * X[i] for i in range(len(P))])

# contraintes
# La somme d'un arc doit etre egale a 1
X_np = np.array(X)
X_np_reshape = X_np.reshape(len(complete_graph), len(complete_graph))

for i in range(len(X_np_reshape)):
    prob += lpSum(X_np_reshape[i]) == 1
    prob += X_np_reshape[i][i] == 0
    for j in range(len(X_np_reshape)):
        if i != j:
            
            prob += lpSum(X_np_reshape[i])+lpSum(X_np_reshape[j]) == 2

            prob += X_np_reshape[i][j] + X_np_reshape[j][i] <= 1
            """if(X_np_reshape[i][j] == 1):
                True_tab.append((i,j))
                print(len(True_tab))
            if (len(True_tab) == len(complete_graph)-1):
                prob += X_np_reshape[i][0] == 1"""
                    


prob.solve()
"""print(LpStatus[prob.status])
print("Min=", value(prob.objective))"""

"""# variables resultat
for v in prob.variables():
    print("%s=%.2f"%(v.name,v.varValue), end=', ')"""
