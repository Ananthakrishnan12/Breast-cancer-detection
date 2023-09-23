# -*- coding: utf-8 -*-
"""Breastcancer web app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qpypo3RJMQW1nEHr1puip2bMvDnbiEhi
"""

#! pip install streamlit

import numpy as np
import pickle
import streamlit as st

load_model=pickle.load(open(r"E:\Protfolio Projects\Machince Learning\Breast Cancer Detection with Machine Learning/Breastcancer.pkl","rb"))

# creating a function for Prediction:
def Breastcancerdetection(input_data):
  #changing the input data to numpy array
  input_data_as_numpy_array=np.asarray(input_data)
  # Reshape the array we are predicting for one instances..
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

  prediction=load_model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0] == 0):
      return 'Malignant'
  else:
      return 'Benign'

def main():
    # Creating title for the web App...
    st.title("BreastCancerDetection")

    smoothness_mean = st.text_input("smoothness_mean")
    compactness_mean = st.text_input("compactness_mean")
    concave_points_mean = st.text_input("concave_points_mean")
    fractal_dimension_mean = st.text_input("fractal_dimension_mean")
    smoothness_se = st.text_input("smoothness_se")
    compactness_se = st.text_input("compactness_se")
    concavity_se = st.text_input("concavity_se")
    concave_points_se = st.text_input("concave_points_se")
    smoothness_worst = st.text_input("smoothness_worst")
    concavity_worst = st.text_input("concavity_worst")
    symmetry_worst = st.text_input("symmetry_worst")
    fractal_dimension_worst = st.text_input("fractal_dimension_worst")

    detection = " "

    # Code for prediction:
    # Creating a button for prediction:
    if st.button("Click for results"):
        detection = Breastcancerdetection([smoothness_mean, compactness_mean, concave_points_mean,
                                           fractal_dimension_mean, smoothness_se, compactness_se,
                                           concavity_se, concave_points_se, smoothness_worst,
                                           concavity_worst, symmetry_worst, fractal_dimension_worst])
        st.success(detection)

if __name__ == "__main__":
    main()