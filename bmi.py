import streamlit as st
from PIL import Image

def EVA_calc(nopat,wacc,tc):
    EVA = nopat-(wacc*tc)
    
    if EVA >= 20000:
        return f"The EVA is {EVA}, the company is producing value."
    elif 2000 <= EVA <= 15000:
        return f"The EVA is {EVA}, the company is most likely producing value."
    elif 15000 <= EVA <= 10000:
        return f"The EVA is {EVA}, the company is likely producing value."
    elif 10000 <= EVA <= 5000:
        return f"The EVA is {EVA}, the company is less likely producing value."
    else:
        return f"Your EVA is {EVA}, the company is not producing value."

st.title("EVA Calculator")
st.subheader("Economic Value of ABZ Limited, Calculate the EVA")

img = Image.open("eva.jpeg")
st.image(img)
nopat = st.number_input("Enter calculated nopat figure")
wacc = st.number_input("Enter calculated wacc figure")
tc = st.number_input("Enter calculated tc figure")

st.sidebar.image("teemac.GIF")
st.sidebar.write("The purpose of EVA is to determine the value a company generates from the capital invested into it with the overall goal of improving the returns generated for shareholders.")

if st.button("Calculate"):
    eva_result = EVA_calc(nopat, wacc, tc)
    st.success(eva_result)
