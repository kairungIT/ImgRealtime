import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Streamlit WebRTC Example")
webrtc_streamer(key="key")