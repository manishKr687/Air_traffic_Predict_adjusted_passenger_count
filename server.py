from flask import Flask,jsonify,request

import utility

app = Flask(__name__)

@app.route('/get_feature_names')
def get_feature_names():
    response = jsonify({'Columns' : utility.show_data_columns()})
    return response

@app.route('/predicted_adjusted_passenger_count',methods=['POST'])
def predicted_adjusted_passenger_count(Passenger_Count,activity_period,operating_airline,operating_Airline_IATA_Code,
                                       published_airline,Published_Airline_IATA_Code,GEO_Summary,GEO_Region,Activity_Type_Code,Price_Category_Code,
                                       Terminal,Boarding_Area,Adjusted_Activity_Type_Code,year,month):
    Passenger_Count = int(request.form['Passenger Count'])
    activity_period = int(request.form['Activity Period'])
    operating_airline = request.form['Operating Airline']
    operating_Airline_IATA_Code = request.form['Operating Airline IATA Code']
    published_airline = request.form['Published Airline']
    Published_Airline_IATA_Code = request.form['Published Airline IATA Code']
    GEO_Summary = request.form['GEO Summary']
    GEO_Region = request.form['GEO Region']
    Activity_Type_Code = request.form['Activity Type Code']
    Price_Category_Code = request.form['Price Category Code']
    Terminal = request.form['Terminal']
    Boarding_Area = request.form['Boarding Area']
    Adjusted_Activity_Type_Code = request.form['Adjusted Activity Type Code']
    year = int(request.form['Year'])
    month = request.form['Month']

    response ={'estimate' :utility.predict_passanger(Passenger_Count,activity_period,operating_airline,operating_Airline_IATA_Code,published_airline,Published_Airline_IATA_Code,GEO_Summary,GEO_Region,Activity_Type_Code,Price_Category_Code,Terminal,Boarding_Area,Adjusted_Activity_Type_Code,year,month)}
    return response
app.run()
