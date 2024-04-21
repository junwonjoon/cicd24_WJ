"""
    Easy Azure Streamlit Demo
    Original Author: Wolf Paulus (wolf@paulus.com)
    Forked by Wonjoon Jun
    This code is used to convert data from html to different chart. This time I have
    implemented cache to optimize data handling.
"""
import streamlit as st
from log import logger
import pandas as pd
import numpy as np
import requests

def is_website_up(url):
    """
    Checks validity of the URL, this is used for pytest.
    In main try and except are used to check not only the
    validity of the URL, but prescence of 
    """
    try:
        response = requests.get(url, timeout=10)  
        if response.status_code < 400:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking website: {e}")
        return False
    
@st.cache_resource()
def get_data_from_url(url):
    return pd.read_html(url)

def ui() -> int:
    st.set_page_config(
    page_title="Wonjoon's CSV Generator",
    page_icon="📃"
    )
    st.title("URL to CSV Converter")
    st.header("Enter a wikipedia page, or any URL with HTML table")
    url = st.text_input("Enter URL here:","https://en.wikipedia.org/wiki/List_of_countries_by_real_GDP_growth_rate")
    try:
        list_of_dfs = get_data_from_url(url)
        st.write(f"Total {len(list_of_dfs)} table(s) found on the webpage")
    except:
        st.error(f"Could not find Table in the URL: {url}")
        return 0
    i = 1
    for data in list_of_dfs:
        st.header(f"Table {i}")
        #st.table can still fail with try. So, try was removed here.
        st.table(data)
        csv = data.to_csv().encode('utf-8')
        st.download_button(
        label=f"Download Table {i} as CSV",
        data=csv,
        file_name=f'Table_{i}.csv',
        mime='text/csv',
        )
        i += 1
    return len(list_of_dfs)


if __name__ == "__main__":
    data_converted = ui()
    logger.info(f"Converted {data_converted} of table(s)")

