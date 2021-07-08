import pickle
import json
import numpy as np
import datetime
current_time = datetime.datetime.now()

_data_columns = None
_model = None

def read_artifacts():   
    global _data_columns
    global _model
    print('Accessing Artifacts...')

    with open('./air_traffic_columns.json','r') as f:
        _data_columns = json.load(f)['Data_columns']
    print(_data_columns)

    with open('./Predict_Adjusted_Passenger_count.pickle','rb') as f:
        _model = pickle.load(f)
    
    print('Loading Artifacts Done...')

def month_converter(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months.index(month) + 1
    
def predict_passanger(Passenger_Count,activity_period,operating_airline,operating_Airline_IATA_Code,published_airline,Published_Airline_IATA_Code,GEO_Summary,GEO_Region,Activity_Type_Code,Price_Category_Code,Terminal,Boarding_Area,Adjusted_Activity_Type_Code,year,month):
  input = np.zeros(len(_data_columns))
  months = (current_time.year-year)*12 + month_converter(month)
  print(months)
  input[0]=Passenger_Count
  input[1]=months
  ida=_data_columns.index(activity_period)
  idb=_data_columns.index(operating_airline)
  idc=_data_columns.index(operating_Airline_IATA_Code)
  idd=_data_columns.index(published_airline)
  ide=_data_columns.index(Published_Airline_IATA_Code)
  idf=_data_columns.index(GEO_Summary)
  idg=_data_columns.index(GEO_Region)
  idh=_data_columns.index(Activity_Type_Code) 
  idi=_data_columns.index(Price_Category_Code)
  idj=_data_columns.index(Terminal)
  idk=_data_columns.index(Boarding_Area) 
  idl=_data_columns.index(Adjusted_Activity_Type_Code)
  #idm=_data_columns.index(year) 
  #idn=_data_columns.index(month)

  input[ida]=1
  input[idb]=1
  input[idc]=1
  input[idd]=1
  input[ide]=1
  input[idf]=1
  input[idg]=1
  input[idh]=1
  input[idi]=1
  input[idj]=1
  input[idk]=1
  input[idl]=1
  #input[idm]=1
  #input[idn]=1

  return _model.predict([input])[0][0]
 
def show_data_columns():
    return _data_columns

show_data_columns()
read_artifacts()

#t=predict_passanger(22000,201603,'SkyWest Airlines','OO','United Airlines','UA','International','Canada','Enplaned','Other','Terminal 3','F','Enplaned',2016,'July')
#print(t)
