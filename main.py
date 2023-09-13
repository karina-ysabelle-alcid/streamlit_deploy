import streamlit_antd_components as sac
import streamlit_app
import dashboard
import index
import streamlit as st

st.set_page_config(layout="wide")

with st.sidebar:
    selected = sac.menu([
    sac.MenuItem('Home', icon='house'),
    sac.MenuItem('Recommender System', icon='app'),
    sac.MenuItem('Dashboard', icon='dashboard'),
], index=0, format_func='title', size='middle', indent=24, open_index=None, open_all=True, return_index=False)

pages = {
    "Home": index,
    "Recommender System": streamlit_app,
    "Dashboard": dashboard,
}

if selected == 'Home':
    index.app()
elif selected == "Recommender System":
    streamlit_app.app()
elif selected == "Dashboard":
    pages["Dashboard"].app()