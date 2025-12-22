import streamlit as st

st.title("AWAS ADA UJANGGGGG 🏍️🏍️🏍️🏍️")
st.write(
    "irsyad TOP GLOBAL 85 EDITH SEASOn 38 [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.title("Upload Foto")

foto = st.file_uploader(
    "Upload foto",
    type=["jpg", "jpeg", "png"]
)

if foto:
    st.image(foto, caption="Foto yang diunggah", use_container_width=True)
