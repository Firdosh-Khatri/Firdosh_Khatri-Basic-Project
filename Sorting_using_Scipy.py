from statistics import mean
from scipy import stats
Estimates=[10, 100,10, 101,87,90,56,44,39,45,89,10,23,72,89,373,78,763,90]
Estimates.sort()
m=stats.trim_mean(Estimates,0.1) #this is using scipy
print(m)

for i in range(len(Estimates)): #this is using pycharm stats
    print(Estimates[i])
tv=int(0.1*len(Estimates)) #smallest 10%value
Estimates=Estimates[tv:]
for i in range(len(Estimates)):
    print(Estimates[i])
Estimates=Estimates[:len(Estimates)-tv] #largest 10% value
print(mean(Estimates))

