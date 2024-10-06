import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Mi primera aplicacion Python")
st.sidebar.title("Parametros")
st.image("descarga.jpeg")
modulos=st.sidebar.selectbox("Seleccione un modulo",["modulo1","modulo2","modulo3"])
st.radio("Seleccione una opcion",["opcion1","opcion2"])
ge=st.number_input("Ingrese un valor",max_value=1.0,min_value=0.1,value=0.9)
api=(141.5/ge)-131.5
st.write("El valor del API es",api)