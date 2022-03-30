import logger
import getdata
categorical_encode = {'Low Fat': 1, 'Regular': 2, 'low fat': 3, 'LF': 0, 'reg': 4, 'Dairy': 4,
                                  'Soft Drinks': 14, 'Meat': 10,
                                  'Fruits and Vegetables': 6, 'Household': 9,
                                  'Baking Goods': 0, 'Snack Foods': 13, 'Frozen Foods': 5, 'Breakfast': 2,
                                  'Health and Hygiene': 8, 'Hard Drinks': 7, 'Canned': 3, 'Breads': 1,
                                  'Starchy Foods': 15,
                                  'Others': 11, 'Seafood': 12, 'Medium': 1, 'High': 0, 'Small': 2, 'Tier1': 0, "Tier2": 1,
                                  "Tier3": 2,
                                  'Supermarket Type1': 1,
                                  'Supermarket Type2': 2, 'Grocery Store': 0,
                                  'Supermarket Type3': 3}


class data_transform():

    """
                       This class shall be used for tranforming the categorical data into numerical data !!.

                       Written By: iNeuron Intelligence
                       Version: 1.0
                       Revisions: None

                       """


    def __init__(self):
        self.file_object = open("Log.txt", 'a+')

        self.logwriter = logger.logger()

        self.data = getdata.getdata()

        self.logwriter.log(self.file_object, "Transformation Started Successfully")
        try:
            self.New_Item_Fat_Content = categorical_encode[self.data.Item_Fat_Content]

            self.New_Item_Type = categorical_encode[self.data.Item_Type]

            self.New_Outlet_Size = categorical_encode[self.data.Outlet_Size]

            self.New_Outlet_Location_Type = categorical_encode[self.data.Outlet_Location_Type]

            self.New_Outlet_Type = categorical_encode[self.data.Outlet_Type]

            self.logwriter.log(self.file_object,"Transformation Finished Successfull")
        except Exception as e:
            self.logwriter.log(self.file_object,f"Transformation failed due to {e}")


