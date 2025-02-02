import streamlit as st
from PIL import Image
with st.expander("Start camera"):
    #start the camera
    camera_image=st.camera_input(label="Camera")
uploaded_image = st.file_uploader("Or upload an image", type=["jpg", "jpeg", "png"])


image_source = camera_image if camera_image is not None else uploaded_image
# create a pillow image instance
if image_source is not None:
    img=Image.open(image_source)
    gray_img = img.convert("L")
    st.image(gray_img)
else:
    st.warning("Please capture an image to proceed.")


# create a pillow image instance

# img=Image.open(camera_image)

# convert the pillow image to grayscale
# gray_img=img.convert("L")

# render the grayscale image on the webpage
# st.image(gray_img)

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
