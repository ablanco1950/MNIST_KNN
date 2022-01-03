import numpy as np

import time

from sklearn.neighbors import KNeighborsClassifier
inicio=time.time()
arr=[]
arry=[]
StartTest=1
ContMaxTest=100;
StartTraining=1
# should be, ContMaxTraining=60000, limit memory
ContMaxTraining=60000
f=open("C:\\mnist_test.csv","r")

Conta=0;
for linea in f:
    Conta=Conta+1
    if Conta<=StartTest: continue
    if Conta > ContMaxTest :break
    lineadelTrain =linea.split(",")
   
 
    linea_x =[""]
    z=0
    for x in lineadelTrain:
       
        z=z+1
        if z==785: break
        if z==1: linea_x[0]=int(lineadelTrain[z])
        else:  linea_x.append(int(lineadelTrain[z]))
  
    arr.append(linea_x)
    arry.append(lineadelTrain[0])
     

X_test=np.array(arr)

Y_test=np.array(arry)


f=open("C:\\mnist_train.csv","r")

Conta=0;
for linea in f:
    Conta=Conta+1
    if Conta==1: continue
    if Conta > ContMaxTraining :break
    lineadelTrain =linea.split(",")
  
 
    linea_x =[""]
    z=0
    for x in lineadelTrain:
   
        z=z+1
        if z==785: break
        if z==1: linea_x[0]=int(lineadelTrain[z])
        else:  linea_x.append(int(lineadelTrain[z]))
  
    arr.append(linea_x)
    arry.append(lineadelTrain[0])
    


X_train=np.array(arr)

Y_train=np.array(arry)

n_train, n_test = len(X_train), len(X_test)
   
Y_predict, pred_test = [np.zeros(n_train), np.zeros(n_test)]
#######################################################################333
#KNN NEIGHBOR
######################################################################333
Inicio2=time.time()
model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, Y_train)

TotAciertos=0.0
TotFallos=0.0

  
Y_predict_test=model.predict(X_test)

Y_test_arr=np.array(Y_test)

TotAciertos=0.0
TotFallos=0.0


i=1   
for i in range (len(Y_predict_test)):
    
    Cadena=""
    ContColumna=0
    
    for j in range (783):
                    
       if int(X_test[i,j+1]) <= 90:
          Cadena=Cadena + " "
       else:
          Cadena=Cadena + "*"
       ContColumna=ContColumna +1
       if ContColumna== 28:
             print(Cadena)
             Cadena=""
             ContColumna=0  
    print ("Predicted class= "+ str(Y_predict_test[i]) + " True class ="
             +  str(Y_test_arr[i]))
    if (Y_predict_test[i]==Y_test_arr[i]):
        TotAciertos=TotAciertos+1
    else:
        TotFallos =TotFallos + 1
        
print("")  
print("RESULTS FOR KNN")     
print("Total Hits TEST = " + str(TotAciertos))
print("Total Failures TEST = " + str(TotFallos))
Fin2=time.time()

  
print ( "procesing time of " + str(ContMaxTest - StartTest) + "  images = "  + str(Fin2 - Inicio2))
print( "Average processing time per image = " + str((Fin2 - Inicio2)/(ContMaxTest - StartTest))) 
print ("")


