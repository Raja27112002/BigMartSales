import getdata
import pickle
import data_transform
import logger



class prediction_():
    """
                       This class shall be used for predicting the user input with the model!!.
                       Written By: iNeuron Intelligence
                       Version: 1.0
                       Revisions: None
                       """

    def __init__(self,data,data2):
        self.data = data
        self.file_object = open("Log.txt", 'a+')
        self.logwriter=logger.logger()
        self.data2 = data2

        self.filename = 'refgressors.pickle'
        try:
            self.loaded_model = pickle.load(open(self.filename, 'rb'))
            self.logwriter.log(self.file_object,"Model loaded Successfully")
        except Exception as e:
            self.logwriter.log(self.file_object,f"Model doesn't load , Model loading failed due to {e}")
        try:
            self.predic = self.loaded_model.predict([[self.data.Item_Weight, self.data2.New_Item_Fat_Content,self.data.Item_Visibility,
                          self.data2.New_Item_Type,self.data.Item_MRP,
                          self.data.Outlet_Establishment_Year, self.data2.New_Outlet_Size,
                          self.data2.New_Outlet_Location_Type, self.data2.New_Outlet_Type]])
            self.logwriter.log(self.file_object, "Prediction Successfull")
        except Exception as e:
            self.logwriter.log(self.file_object,f"Prediction Failed due to {e}")