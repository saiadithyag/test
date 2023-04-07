# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:49:33 2023

@author: Adith
"""
import pandas as pd
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np

filename = "C://Users//Adith//Desktop//Data Science_Excel R//Projects Datascience//final_model.sav"
loaded_model = pickle.load(open(filename,'rb'))


#creating a function 

def cluster_prediction(input_data):
 

    input_data_array = np.asarray(input_data)

    input_data_reshape = input_data_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0]==0):
      return'cluster 1 The purchases are moderate with least customers engaged on all days with the company but have highest acceptance to campaign offers and mostly they come from upper class background,most of them fall in the age groups of Gen X and and Boomers with higher background of education'
    elif(prediction[0]==1):
      return ' cluster 2 The purchases are lowest and moderately less customers engaged on all days with the company and the acceptance ratio to offers or campaigns is lesser compared to first cluster,most of the customers are from lower and middle class and most of them fall in the age category of Gen X and Boomers having higher education background ,we can also say that most of the families are having members near to 3'
    else:
      return'cluster 3 The purchases are highest with most of our customers engaged with the company on daily basis and have a moderate acceptance to any offers or campaigns, in the third cluster we observe that most of the customer come from middle and upper middle class and even in this cluster most of them fall in the age categories of GenX and  Boomers with highest education qualification'
      
      
def main():
      
      # giving a title 
      
      st.title("Customer Segmentation")
      
      # getting the input data from the user
      
      Purchases = st.text_input('Total Purchases')
      day_engaged = st.text_input('Number of Days with Company')
      Acceptance = st.selectbox('Number Of Campaign offers Accepted',('0','1','2','3','4'))
      Family = st.selectbox('Members In a Family',('1','2','3','4','5'))
      Income_Category_lower = st.selectbox('Lower Class', ('0','1'))
      Income_Category_middle =  st.selectbox('Middle Class', ('0','1'))
      Income_Category_upper_middle =  st.selectbox('Upper Middle Class', ('0','1'))
      Income_Category_upper =  st.selectbox('Upper Class', ('0','1'))
      Customer_Segment_Millennial =  st.selectbox('Millennial', ('0','1'))
      Customer_Segment_Gen_X	 =  st.selectbox('GenX	', ('0','1'))
      Customer_Segment_Boomer =  st.selectbox('Boomer', ('0','1'))
      Customer_Segment_Silent =  st.selectbox('Silent', ('0','1'))
      Education_Grad =  st.selectbox('Graduate', ('0','1'))
      Education_PostGrad =  st.selectbox('PostGraduate', ('0','1'))
      Education_Undergrad =  st.selectbox('Undergraduate', ('0','1'))
      
      
      #code for prediction 
      Analysis = ''
      
      #creating a button for prediction
      
      if st.button('Customer Cluster result'):
          
          Analysis = cluster_prediction([Purchases,day_engaged,Acceptance,Family,Income_Category_lower,Income_Category_middle, Income_Category_upper_middle, Income_Category_upper, Customer_Segment_Millennial, Customer_Segment_Gen_X, Customer_Segment_Boomer,Customer_Segment_Silent, Education_Grad, Education_PostGrad, Education_Undergrad])
          
      st.success(Analysis)
        
        
if __name__ == '__main__' :
        main()
          
        
        
        

     
      
      
    
      
      
      







