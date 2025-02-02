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

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("For Reporting an issue, Kindly email at tanishqmirdha2005@gmail.com .",
        unsafe_allow_html=True)
st.write("Do not message <b>Unnecessarily</b>.Only message if you are facing any <b>problem<b>.",
        unsafe_allow_html=True)
st.write("Otherwise it can be problematic for \"You\"",
        unsafe_allow_html=True)
