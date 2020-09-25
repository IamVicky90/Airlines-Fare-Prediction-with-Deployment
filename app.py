from flask import Flask,request,render_template
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
app= Flask(__name__)
model = pickle.load(open('Random Forest Airlines Fare Predictions.pkl', 'rb'))
@app.route('/',methods=["GET"])
def Home():
    return render_template('index.html')
@app.route('/predict',methods=["POST"])
def predict():
    if request.method == 'POST':
        Airlines=request.form["Airlines"]
        if Airlines=='IndiGo':
            Jet_Airways=0
            IndiGo=1
            Air_India=0                            
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0
        elif Airlines=='Air India':
            Jet_Airways=0
            IndiGo=0
            Air_India=1                            
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0   
        elif Airlines=='Jet Airways':
            Jet_Airways=1
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0   
        elif Airlines=='SpiceJet':
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=1                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0   
        elif Airlines=='Multiple carriers':
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=1                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0   
        elif Airlines=='GoAir':
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=1                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0   

        elif Airlines=='Vistara Premium economy':
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=1                 
            Trujet=0   
        elif Airlines=='Jet Airways Business':
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=1                    
            Vistara_Premium_economy=0                 
            Trujet=0   
        elif Airlines=='Multiple carriers Premium economy':
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=1      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0   
        elif Airlines=='Trujet':
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=1  
        else:
            Jet_Airways=0
            IndiGo=0
            Air_India=0                          
            Multiple_carriers=0                    
            SpiceJet=0                              
            Vistara=0                              
            Air_Asia=0                              
            GoAir=0                                 
            Multiple_carriers_Premium_economy=0      
            Jet_Airways_Business=0                    
            Vistara_Premium_economy=0                 
            Trujet=0
        Total_Stops=request.form["Total_Stops"]
        if Total_Stops=="non-stop":
            Total_Stops_int=0
        if Total_Stops=="1 stop":
            Total_Stops_int=1
        if Total_Stops=="2 stops":
            Total_Stops_int=2
        if Total_Stops=="3 stops":
            Total_Stops_int=3
        if Total_Stops=="4 stops":
            Total_Stops_int=4
          
        Source=request.form["Source"]
        if Source=='Delhi':
            Source_Chennai=0
            Source_Delhi=1
            Source_Kolkata=0      
            Source_Mumbai=0
        elif Source=='Kolkata':
            Source_Chennai=0
            Source_Delhi=0
            Source_Kolkata=1      
            Source_Mumbai=0

        elif Source=='Mumbai':
            Source_Chennai=0
            Source_Delhi=0
            Source_Kolkata=0      
            Source_Mumbai=1
        elif Source=='Chennai':
            Source_Chennai=1
            Source_Delhi=0
            Source_Kolkata=0      
            Source_Mumbai=0
        else:
            Source_Chennai=0
            Source_Delhi=0
            Source_Kolkata=0      
            Source_Mumbai=0
        Source=request.form["Destination"]     
        if Source=='Cochin':
            Destination_Cochin=1
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=0
        elif Source=='Kolkata':
            Destination_Cochin=0
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=1
            Destination_New_Delhi=0
        elif Source=='Delhi':
            Destination_Cochin=0
            Destination_Delhi=1
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=0
        elif Source=='New Delhi':
            Destination_Cochin=0
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=1
        elif Source=='Hyderabad':
            Destination_Cochin=1
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=0
        else:
            Destination_Cochin=0
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=0
        Date_of_Journey=request.form["Date_of_Journey"]
        Date_of_Journey=pd.Series(Date_of_Journey)    
        Journey_Day=pd.to_datetime(Date_of_Journey).dt.day   
        Journey_Month=pd.to_datetime(Date_of_Journey).dt.month
        Dep_Time=request.form["Dep_Time"]
        
        Dep_Time=pd.Series(Dep_Time)
        Dep_Time_hour=pd.to_datetime(Dep_Time).dt.hour +12
 
        Arrival_Time=request.form["Arrival_Time"]
        Arrival_Time=pd.Series(Arrival_Time)  
        Arrival_Time_in_Hour=pd.to_datetime(Arrival_Time).dt.hour           
        Duration=request.form["Duration"]
        prediction=model.predict([[ Total_Stops_int,Air_India, GoAir,
       IndiGo, Jet_Airways, Jet_Airways_Business,
       Multiple_carriers,
       Multiple_carriers_Premium_economy, SpiceJet,
       Trujet, Vistara, Vistara_Premium_economy,
       Source_Chennai, Source_Delhi, Source_Kolkata, Source_Mumbai,
       Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Destination_New_Delhi, Journey_Day,
       Journey_Month, int(Duration), Dep_Time_hour,
       Arrival_Time_in_Hour]])
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text="Your ticket for {} is {}".format(Airlines,output))
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=False)





      

