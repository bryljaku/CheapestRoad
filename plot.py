import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

if len(sys.argv) != 2:
    print("Wrong arguments")
    sys.exit(1)

df = pd.read_csv(sys.argv[1], sep=';', names=['num_nodes', 'num_edges','time', 'num_groups','reversable_nodes'])

v = df['num_nodes']
e = df['num_edges']
t = df['time']
num_groups = df['num_groups']
num_reversable_nodes = df['reversable_nodes']

X = df.iloc[:, [0,1]]
complexity = e + v*np.log(v)
y = t

regressor = linear_model.LinearRegression()
regressor.fit(X, t)
y_pred = regressor.predict(X)

mediana = int(len(df.index) / 2)
t_mediana = np.array(t)[mediana]
vm = np.array(v)[mediana]
em = np.array(e)[mediana]
T_mediana = vm*em*em + vm*vm*em
T = np.array(complexity)

print(complexity)
res = np.array([v, e, t * T_mediana / (T * t_mediana)])

res = np.transpose(res)
np.savetxt("tabelka.csv", res, delimiter=";", fmt="%f")

fig = plt.figure()
plt.scatter(num_reversable_nodes, y, color="black")
#plt.plot(complexity, y_pred, color="red", linewidth=3.0)
plt.xlabel('Predicted complexity: (E + V*log(V))^V')
plt.ylabel('Time')
plt.show()
fig.savefig("plot.png")
# Clear the current axes.
plt.cla() 
# Clear the current figure.
plt.clf() 
# Closes all the figure windows.
plt.close('all')   
plt.close(fig)