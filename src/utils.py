import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import pickle
def save_object(file_path, obj):
    try:
        dir_path = os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
        with open(file_path, 'wb') as f:
            dill.dump(obj, f)  # Save object as pickle
    except Exception as e:
        raise CustomException(e, sys)
def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        # X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]  
            # model.fit(X_train,y_train) # train model
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            y_train_pred = model.predict(X_train)
            y_test_predict = model.predict(X_test)
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_predict)
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise CustomException(e, sys)