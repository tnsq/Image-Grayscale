import streamlit as st
from PIL import Image
#start the camera
camera_image=st.camera_input(label="Camera")

# create a pillow image instance
if camera_image is not None:
    img=Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)
else:
    st.warning("Please capture an image to proceed.")

