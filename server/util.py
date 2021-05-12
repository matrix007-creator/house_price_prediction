import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None



def get_location_names():
    return __locations
def load_saved_artifacts():
    print("loading_saved_artifacts")
    global __data_columns
    global __locations
    global __model
    with open("server/assets/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]
    with open("server/assets/house_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

if __name__=='__main__':
    load_saved_artifacts()
    #print(get_location_names())    
    print(get_estimated_price('nagarbhavi',1200,2,2)) 
    print(get_estimated_price('cunningham road',1200,2,2))        


