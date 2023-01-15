import streamlit as st
import pandas as pd
def bolge(isim):
  f=ev["neighbourhood"]==isim
  sonuc=ev[f]
  return sonuc
ev=pd.read_csv("ev.csv")
ev=ev[["name","host_name","neighbourhood","latitude","longitude","price"]]
ilceler=ev['neighbourhood'].unique()
ilce=st.sidebar.selectbox("İlce Seciniz",ilceler)
st.map(bolge(ilce))
