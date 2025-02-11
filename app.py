import streamlit as st
from model_helper import predict
from PIL import Image
import io

st.set_page_config(page_title="Vehicle Damage Detection", page_icon="🚗", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>🚗 Vehicle Damage Detection 🚗</h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>Upload an image of your vehicle to detect damages.</p>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"], accept_multiple_files=False)

if uploaded_file:
    image = Image.open(uploaded_file)
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()
    
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Analyzing Image...🔍"):
        prediction = predict(uploaded_file)
    
    st.markdown(
        f"""
        <div style="text-align: center;">
            <div style="display: inline-block; background-color: #DFF2BF; color: #4F8A10; padding: 10px 20px; border-radius: 5px; font-size: 18px;">
                <b>Predicted Class:</b> {prediction}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )