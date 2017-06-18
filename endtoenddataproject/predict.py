import os
import settings
import pandas as pd
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn import metrics

def split(dataframe):
	y = dataframe[settings.TARGET]
	features = [i for i in df.columns if i != 'Class']
	x = df[features]
	x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.4, random_state = 0)
	return x_train, x_test, y_train, y_test

def model_predictions(x_train,y_train,x_test):
	clf = RandomForestClassifier(n_estimators = 10)
	clf = clf.fit(x_train,y_train)
	predictions = clf.fit(x_train, y_train)
	return predictions

def compute_error(target, predictions):
    return metrics.accuracy_score(target, predictions)

def compute_false_negatives(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 1) & (df["predictions"] == 0)].shape[0] / (df[(df["target"] == 1)].shape[0] + 1)

def compute_false_positives(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 0) & (df["predictions"] == 1)].shape[0] / (df[(df["target"] == 0)].shape[0] + 1)

def read_data():
	dataframe = pd.read_csv(os.path.join(settings.PROCESSED_DATA,os.listdir(settings.PROCESSED_DATA)))
	return dataframe

if __name__ == "__main__":
	data = read_data()
	x_train, x_test, y_train, y_test = split(data)
	predictions = model_predictions(x,train,y_train,x_test)

	#results 
	print "accuracy_score: {}".format(compute_error(y_test,predictions))
