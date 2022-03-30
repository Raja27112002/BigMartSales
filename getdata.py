from flask import Flask,request
import logger
class getdata():
    """
                   This class shall be used for getting data from the user!!.

                   Written By: iNeuron Intelligence
                   Version: 1.0
                   Revisions: None

                   """




    def __init__(self):
        self.file_object = open("Log.txt", 'a+')

        self.logwriter = logger.logger()
        try:
            self.Item_Weight = float(request.form['Item_Weight'])

            self.Item_Fat_Content = request.form['Item_Fat_Content']

            self.Item_Visibility = float(request.form['Item_Visibility'])

            self.Item_Type = request.form['Item_Type']

            self.Item_MRP = float(request.form['Item_MRP'])

            self.Outlet_Establishment_Year = (request.form['Outlet_Establishment_Year'])

            self.Outlet_Size = request.form['Outlet_Size']

            self.Outlet_Location_Type = request.form['Outlet_Location_Type']

            self.Outlet_Type = request.form['Outlet_Type']

            self.logwriter.log(self.file_object,"Getting input from the user is successfull")

        except Exception as e:
            self.logwriter.log(self.file_object,f"Didn't able to get data from the user due to {e}")


