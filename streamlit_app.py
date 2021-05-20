# Dependencies and Libraries
import streamlit as st
import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib as plt
import seaborn as sns

st.write("""
# System Web Application Version
A [CS 321 | CS 322] Project
""")

# Residential Status Features
rs_1, rs_2 = st.beta_columns(2)

with rs_1:
    residential_status = st.selectbox(
    label="Region", 
    options=[
        'Autonomous Region in Muslim Mindanao',
        'Bicol', 
        'Cagayan Valley',
        'Calabarzon',
        'Caraga',
        'Central Luzon',
        'Central Visayas', 
        'Cordillera', 
        'Davao',
        'Eastern Visayas', 
        'Ilocos', 
        'Mimaropa',
        'National Capital', 
        'Northern Mindanao', 
        'Soccskargen', 
        'Western Visayas', 
        'Zamboanga Peninsula', 
        ],
    index=7
    )

with rs_2:
    rural_area = st.selectbox(
    label="Area",
    options=[
        'Rural',
        'Urban'
    ],
    index=1
)


# Age Features