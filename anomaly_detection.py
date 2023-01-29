#import necessary libraries
import numpy as np 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score 

#define data points 
data = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]]) 
  
#create kmeans object with 2 clusters 
kmeans = KMeans(n_clusters=2) 
  
#fit the model to data points 
kmeans.fit(data) 
  
#predict the cluster for each data point 
labels = kmeans.predict(data) 

 #calculate silhouette score for the clusters created by kmeans algorithm  
silhouette_score = silhouette_score(data, labels) 

 #check if any of the data points are anomalies or not based on the silhouette score  
if silhouette_score < 0.5:    #threshold value can be changed as per requirement  

    print("Anomalies detected")    #anomalies detected in the dataset  

    for i in range(len(labels)):     #loop through all labels and find out which data points are anomalies  

        if labels[i] == 1:     #if label is 1 then it is an anomaly  

            print("Data point", i+1,"is an anomaly")     #print out which data point is an anomaly