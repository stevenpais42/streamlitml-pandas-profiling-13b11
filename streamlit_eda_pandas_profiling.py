import pandas as pd
import ydata_profiling as pp
import streamlit as st
import streamlit.components.v1 as components


df = pd.read_csv("iris.csv")

profile = pp.ProfileReport(df, title="Iris Data").to_html()

st.title("Pandas Profiling in Streamlit!")

st.write(df)

components.html(profile, height=1000, width=950,scrolling=True)

output = pp.ProfileReport(df, title="Iris Data").to_file('output.html', silent=False)

        
