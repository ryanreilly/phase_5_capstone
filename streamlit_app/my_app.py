import tensorflow as tf
model = tf.keras.models.load_model('model_dense2.h5')

import streamlit as st
st.write("""
         # Natural Disaster Prediction
         """
         )
st.write("This is an image classification app to predict natural disaster images.")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])


import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
    
        size = (224,224)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(224, 224),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img_resize[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("It looks like an Earthquake!")
    elif np.argmax(prediction) == 1:
       st.write("It looks like a fire!")
    elif np.argmax(prediction) == 2:
        st.write("It looks like a flood!")
    elif np.argmax(prediction) == 3:
        st.write("It looks like a hurricane!")
    elif np.argmax(prediction) == 4:
        st.write("It looks like a landslide!")
    elif np.argmax(prediction) == 5:
        st.write("This doesn't look like a natural disaster!")
    elif np.argmax(prediction) == 6:
        st.write("This looks like its another type of disaster")
    else:
        pass
    
    st.text("Probability (0: Earthquake, 1: Fire, 2: Flood, 3: Hurricane, 4: Landslide, 5: Non Disaster, 6: Other Disaster")
    st.write(prediction)
    