from cgi import test
from email.mime import image
import imp
from pyexpat import model
from unittest import result
import streamlit as st
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax
import os
import h5py
import cv2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

st.set_page_config(
    page_title="Lung Cancer",
    page_icon="🏥",
)

#title
st.title('Lung Cancer Detection')
st.sidebar.success("Select a page above")

#header
#st.header('Lung')

# SUBHEADER
#st.subheader('Cancer')

model = tf.keras.models.load_model("\daata\ResNet50_Best_new.h5")
### load file
uploaded_file = st.file_uploader("Choose a image file", type=['jpg','png','jpeg'])

# map_dict = {0: 'building',
#             1: 'forest',
#             2: 'glacier',
#             3: 'mountain',
#             4: 'sea',
#             5: 'street'
#             }

    

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(256,256))
    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="RGB")

    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis,...]

    Genrate_pred = st.button("Generate Prediction")    
    if Genrate_pred:
        preds = model.predict(img_reshape).argmax()
        
        preds=np.argmax(preds)
        if preds==0:
            st.success("Solid_Tissue_Normal")
        elif preds==1:
            st.error("LUAD")
        else:
            st.error("LUSC")
        st.write(preds)   
    
    
        
        # st.success("Predicted Label for the image is {}".format(map_dict [prediction]))

# def main():
#     file_uploaded = st.file.uploader("Choose the file", type=['jpg','png','jpeg'])
#     if file_uploaded is not None:
#         image=Image.open(file_uploaded)
#         figure = plt.figure()
#         plt.imshow(image)
#         plt.axis("off")
#         result = predict_class(image)
#         st.write(result)
#         st.pyplot(figure)

# def predict_class(image):
#     classifier_model=tf.keras.models.load_model("D:\Projects\cdac\my_model.hdf5")
#     shape = ((128,128,3))
#     model = tf.keras.Sequential(hub[hub.KerasLayer(classifier_model, input_shape=shape)])
#     test_image = image.resize(128,128)
#     test_image = preprocessing.image.img.to.array(test_image)
#     test_image = test_image/255.0
#     test_image = np.expand_dims(test_image,axis = 0)
#     class_names = ['building',
#                     'forest',
#                     'glacier',
#                     'mountain',
#                     'sea',
#                     'street']
#     model.predict(test_image)
#     tf.nn.softmax(predictions[0])
#     scores = scores.numpy()
#     image_class = class_names[np.argmax(scores)]
#     result = "The image uploaded is: {}".format(image_class)
#     return result

# if __name__ == "__Home__":
#     main()                
