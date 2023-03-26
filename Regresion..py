
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Datos de prueba ( diabetes ).

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=TRUE)

# Uso de los datos.

diabetes_X = diabetes_[:,np.newaxis,2]

# Separa los datos en conjuntos de entrenamiento / prueba.

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[:-20]

# Separa resultaods en conjuntos de entrenamiento/ prueba.

diabetes_y_train = diabetes_y[:-20]
print(diabetes_
diabetes_y_test = diabetes_y[:-20]

# Regresion lineal - objeto.

regr_lin.fit(diabetes_X_train,diabetes_y_train)

# Prediccion.

diabetes_y_pre = regr_lin.predict(diabetes_X_test)

# Coeficientes.

print("Coeficientes"\n",regr_lin.coef_)

#Error medio al cuadrado.

print("Error medio al cuadrado: %.2f" % mean_squared_error(diabetes_y_test,diabetes_y_pred))

# Coeficientes de determinacionv: 1 prediccion es perfecta.

print("Coeficientes de determinacion:%.2f" % r2_score(diabetes_y_test,diabetes_y_pred))

# Graficas.

plt.scatter(diabetes_X_test,diabetes_y_test,color= "black")
plt.plot(diabetes_X_test,diabetes_y_pred,color= "blue",linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()