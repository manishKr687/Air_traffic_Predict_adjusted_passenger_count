from os import access
from flask import Flask,jsonify,request,render_template

import utility

app = Flask(__name__)


@app.route('/get_feature_names')
def get_feature_names():
    response = jsonify({'Columns' : utility.show_data_columns()})
    return response

@app.route('/Predict_Adjusted_Passenger_Count',methods=['GET','POST'])
def Predict_Adjusted_Passenger_Count():
    if request.method=='POST':
        Passenger_Count = int(request.form['PsgCont'])
        activity_period = int(request.form['ActCont'])
        operating_airline = request.form['OprAr']
        operating_Airline_IATA_Code = request.form['OprArIC']
        published_airline = request.form['PubAr']
        Published_Airline_IATA_Code = request.form['PubArIC']
        GEO_Summary = request.form['GoSum']
        GEO_Region = request.form['GoReg']
        Activity_Type_Code = request.form['AtvTyCod']
        Price_Category_Code = request.form['PrcTy_Cod']
        Terminal = request.form['trmi']
        Boarding_Area = request.form['BorAr']
        Adjusted_Activity_Type_Code = request.form['AdjActTC']
        year = int(request.form['Yr'])
        month = request.form['Mont']

    response =jsonify({'estimate' : utility.predict_passanger(Passenger_Count,activity_period,operating_airline,operating_Airline_IATA_Code,published_airline,Published_Airline_IATA_Code,GEO_Summary,GEO_Region,Activity_Type_Code,Price_Category_Code,Terminal,Boarding_Area,Adjusted_Activity_Type_Code,year,month)})
    
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


utility.read_artifacts()
app.run(debug=True)
