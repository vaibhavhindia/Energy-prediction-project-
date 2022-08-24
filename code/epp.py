import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Loading in the Model to predict on the data
pickle_in = open('rf_model.pkl','rb')
rf_model = pickle.load(pickle_in)


def welcome():
    return 'welcome all'

# defining the function which will make the prediction using the data which the user inputs
def prediction(temperature,exhaust_vacuum,amb_pressure,r_humidity):  
   
    prediction = rf_model.predict(
        [[temperature,exhaust_vacuum,amb_pressure,r_humidity]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("ENERGY PREDICTOR")
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:tomato;padding:10px">
    <h2 style ="color:black;text-align:center;">Streamlit Energy Predictor ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    temperature = st.text_input("Temperature", "Type Here")
    exhaust_vacuum=st.text_input("exhaust_vacuum", "Type Here")
    amb_pressure = st.text_input("amb_pressure", "Type Here")
    r_humidity= st.text_input("r_humidity", "Type Here")
 
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(temperature,exhaust_vacuum,amb_pressure,r_humidity)
    st.success('Energy Production is {}'.format(result))
     
if __name__=='__main__':
    main()