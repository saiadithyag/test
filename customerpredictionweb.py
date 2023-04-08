#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('Downloads\trained_model.sav', 'rb'))


def customer_prediction(input_data):
    
    
    input_data =(52458,50,166,72,19,175,25,35,5,3,1,15,5,1532,0,22,222,69.636)
    new_point= np.asarray(input_data)
    new_point = new_point.reshape(1,-1)
    new_point_std = scaler.transform(new_point)
    new_point_pca = pca.transform(new_point_std)
    predicted_cluster = kmeans.predict(new_point_pca)
    print(predicted_cluster)  

    if (predicted_cluster[0] == 0):
        print('customer with high expense ')
    elif (predicted_cluster[0] == 1):
        print('customer with low expense')
    else :
        print('customer with moderate expense')

        
def main(): 
    st.title('customer segmentation Web App')
    
    
    Income = st.text_input('Income of customer')
    Recency = st.text_input('Recency of customer')
    MntWines = st.text_input('MntWines purchase of customer')
    MntFruits = st.text_input('MntFruits purchase of customer')
    MntMeatProducts = st.text_input('MntMeatProducts purchase of customer')
    MntFishProducts = st.text_input('MntFishProducts of customer')
    MntSweetProducts = st.text_input('MntSweetProducts of customer')
    MntGoldProds = st.text_input('MntGoldProds of customer')
    NumDealsPurchases = st.text_input('NumDealsPurchases of customer')
    NumWebPurchases = st.text_input('NumWebPurchases of customer')
    NumCatalogPurchases = st.text_input('NumCatalogPurchases of customer')
    NumStorePurchases  = st.text_input('NumStorePurchases  of customer')
    NumWebVisitsMonth = st.text_input('NumWebVisitsMonth of customer')
    total_expense = st.text_input('total_expense of customer')
    total_accepted = st.text_input('total_accepted of customer')
    total_purchase = st.text_input('total_purchase of customer')
    Engaged_in_days = st.text_input('Engaged_in_days of customer')
    AmountPerPurchase = st.text_input('AmountPerPurchase of customer')
    
    
    result = ''
    
    if st.button('Customer segmentation Test Result'):
        result = customer_prediction([Income,Recency,MntWines,MntFruits,MntMeatProducts,MntFishProducts,MntSweetProducts,MntGoldProds,NumDealsPurchases,NumWebPurchases,NumCatalogPurchases,NumStorePurchases,NumWebVisitsMonth,total_expense,total_accepted,total_purchase,Engaged_in_days,AmountPerPurchase])
        
    st.success(result)  
    
if __name__ == '__main__':
    main()
    

            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




