#------>Red Neuronal Artificial<------
"""Integrantes: 
   - Cruz Zavala Miguel Angel
   - Monroy Velázquez Alejandra Sarahí"""


#-------Procesando los datos-------
# Importamos la libreria numpy y pandas
import numpy as np
import pandas as pd

# Leemos el set de datos y metemos las variables dependientes 
# e independientes dentro de las matrices x,y
dataset = pd.read_csv('datosClientes.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Codificamos los datos categoricos utilizando la biblioteca sklearn
# para procesar los datos que no son numeros
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:,1:]

# Separamos los datos en un set de entrenamiento y un set de prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Hacemos un escalado de categorias
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#-------Creando la red neuronal-------
# Importamos la libreria keras, y los paquetes Seguential y Dense
import keras
from keras.models import Sequential
from keras.layers import Dense

# Inicializamos la Red Neuronal
clasificador = Sequential()

# Agregamos la capa de entrada y la primer capa oculta
clasificador.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim=11))

# Agregamos una segunda capa oculta
clasificador.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))

# Agregando la ultima capa o capa de salida
clasificador.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

# Compilamos la red neuronal
clasificador.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Ajustamos la red neuronal en el set de entrenamiento
clasificador.fit(X_train, y_train, batch_size=10, epochs=100)


#-------Probando el modelo y haciendo predicciones-------
# Predecimos el set de prueba
y_pred = clasificador.predict(X_test)
y_pred = (y_pred>0.5)

# Hacemos la matriz de confusion
from sklearn.metrics import confusion_matrix
mc = confusion_matrix(y_test,y_pred)



# Insertamos un nuevo cliente en el modelo para predecir si abandonara el banco
"""
•	País: Alemania
•	Puntaje de Crédito: 800
•	Sexo: Mujer
•	Edad: 30
•	Años que ha estado en el banco: 2
•	Saldo: 45,000
•	Numero de productos/servicios: 3
•	Tarjeta de crédito: Si
•	Miembro activo: Si
•	Salario: 40,000

"""

cliente = clasificador.predict(sc.transform(np.array([[0,1,100,0,27,5,2000000,0,0,1,50000]])))
#Observamos el resultado
cliente = (cliente>0.5)
print (cliente)















