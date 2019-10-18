weather=['s','s','o','r','r','r','o','s','s','r','s','o','o','r']
temp=['h','h','h','h','n','n','n','h','n','n','n','h','n','h']
wind=['s','w','w','s','w','w','w','w','s','s','w','s','s','w']
play=['n','n','y','y','y','n','y','n','y','y','y','y','y','n']
import maplotlib.pyplot as plt
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(weather)
print("Weather:",weather_encoded)
wind_encoded=le.fit_transform(wind)

temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print("Wind:",wind_encoded)
print("Temp:",temp_encoded)
print("Play:",label)
features=zip(weather_encoded,temp_encoded,wind_encoded)
print(features)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[2,2,0]])
print("Predicted Value:",predicted)

