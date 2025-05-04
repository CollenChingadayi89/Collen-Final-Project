# -*- coding: utf-8 -*-


import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('farming_model.sav', 'rb'))

#creating function for prediction
def prediction(input_data):
   
    #changing the data into numpy array
    input_data_as_nparray=np.asarray(input_data)

    #reshaping the data since there is only one instance
    input_data_reshaped=input_data_as_nparray.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction==0):
      return 'The farmer is Risk for insurance'
    else:
      return 'The farmer is Non Risk for insurance'
  
    
def main():
    
    #giving a title
    st.title('Agriculture Insurance Risk Assessment')
    
    #getting input from the user
    Region=st.selectbox(label=("Select Region :"),options=["Region 1","Region 2","Region 3","Region 4","Region 5"])
    #Pregnancies=st.text_input('Region:')
    Assets=st.text_input('Assets Ammount:')
    Land=st.text_input('Land Size(Ha):')
    Insurance=st.text_input('Insurance Required:')
    Workers=st.text_input('Number of Workers:')
    Irrigation=st.selectbox(label=("Do you have irrigation? :"),options=["Yes","No"])
    #BMI=st.text_input('Irrigation(1/0):')
    Type=st.selectbox(label=("Select Crop Type :"),options=["Maize","Wheat","Sorghum","Rapoko","Beans"])
    Age=st.text_input('Age:')

    if(Region=="Region 1"):
      region=1.0
    elif(Region=="Region 2"):  
       region=2.0
    elif(Region=="Region 3"):  
       region=3.0
    elif(Region=="Region 4"):  
       region=4.0
    elif(Region=="Region 5"):  
       region=5.0

    if(Type=="Maize"):
      farminType=1.0
    elif(Type=="Wheat"):  
       farminType=2.0
    elif(Type=="Sorghum"):  
       farminType=3.0
    elif(Type=="Rapoko"):  
       farminType=4.0 
    elif(Type=="Beans"):  
       farminType=5.0      

    if(Irrigation=="Yes"):
      irrigation=1.0
    elif(Irrigation=="No"):  
       irrigation=0       
    #code for prediction
    diagnosis=''
    
    #making a button for prediction
    if st.button('Predict'):
        diagnosis=prediction([region,Assets,Land,Insurance,Workers,irrigation,farminType,2,Age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    
    