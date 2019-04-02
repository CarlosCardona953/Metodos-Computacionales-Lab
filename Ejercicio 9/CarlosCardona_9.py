import numpy as np
import random
import sys
from scipy.stats import f
from scipy.stats import norm

param= int(sys.argv[1])
np.random.seed(param)

n=500 # mediciones efectuadas
p=100 # variables medidas
mu=0.0
sigma=1.0
X=np.random.normal(mu,sigma,size=(n,p))
Y=np.random.normal(mu,sigma,size=(n,1))
XT=X.T
YT=Y.T
Inv=np.linalg.inv(np.matmul(XT,X))
beta1=np.matmul(Inv,XT)
beta=np.matmul(beta1,Y)
Hhat=np.matmul(X,beta1)
Yideal=np.matmul(X,beta)

SST1=np.matmul(np.identity(n)-(1.0/n)*np.ones((n,n)),Y)
SST=np.matmul(YT,SST1)
SSR1=np.matmul(Hhat-(1.0/n)*np.ones((n,n)),Y)
SSR=np.matmul(YT,SSR1)
SSE1=np.matmul(np.identity(n)-Hhat,Y)
SSE=np.matmul(YT,SSE1)

Rsq=SSR[0,0]/SST[0,0]

sigma2=SSE[0,0]/(n-1.)
sigmamatrix=sigma2*Inv
sigma_i=np.zeros(p)
for i in range(p):
    sigma_i[i]=sigmamatrix[i,i]
sigma_i=np.sqrt(sigma_i)

MSE=SSE[0,0]/(n-p-1)
# Calculamos el MSR
MSR=SSR[0,0]/p
# Calculamos el MST
MST=SST[0,0]/(n-1)


F=(Rsq*(n-p-1))/((1-Rsq)*p)
    

Rango=0.9 # se define un rango, es decir cuanto porcentaje de la curva se quiere
Ftest=f.ppf(Rango,p,n-(p+1))
P_i=np.zeros(p)
if F > Ftest:
    tzeros=beta[:,0]/sigma_i
    P_value=2*(1-norm.cdf(tzeros)) # se integran las colas
    for i in range(p):
        if P_value[i]<0.5:
            P_i[i]=1
        else:
            P_i[i]=0
else:
   
    quit()
   

p_prime=np.sum(P_i)
X_new=np.zeros((n,int(p_prime)))


aux=0
for i in range(p):
    if P_i[i]==1:
        X_new[:,aux]=X[:,i]
        
        aux+=1
        


p=X_new.shape[1]

X=X_new

XT=X.T
YT=Y.T
Inv=np.linalg.inv(np.matmul(XT,X))
beta1=np.matmul(Inv,XT)
beta=np.matmul(beta1,Y)
Hhat=np.matmul(X,beta1)
Yideal=np.matmul(X,beta)

SST1=np.matmul(np.identity(n)-(1.0/n)*np.ones((n,n)),Y)
SST=np.matmul(YT,SST1)
SSR1=np.matmul(Hhat-(1.0/n)*np.ones((n,n)),Y)
SSR=np.matmul(YT,SSR1)
SSE1=np.matmul(np.identity(n)-Hhat,Y)
SSE=np.matmul(YT,SSE1)

Rnuevo= SSR[0,0]/SST[0,0]

Fnuevo= (Rnuevo*(n-p-1))/((1-Rnuevo)*p)


print(str(Rsq), str(F), str(Rnuevo), str(Fnuevo))
