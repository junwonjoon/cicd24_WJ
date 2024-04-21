"""
    Original Author: Wolf Paulus (wolf@paulus.com)
    Forked by Wonjoon Jun
    This is streamlit code that converts url to csv file.
    cache_resource decorator was implemented to enhance performance.
"""
import streamlit as st
from log import logger
import pandas as pd
import numpy as np
import requests


def is_website_up(url):
    """
    Checks validity of the URL, this function is only used for pytest.
    In main try and except are used to check not only the
    validity of the URL, but if there is a table to convery
    Parameters:
    - url (str): The URL of the website to check.
    Returns:
    - bool: True if the website is up, otherwise False.
    Raises:
    - requests.exceptions.RequestException: If an error occurs during the HTTP request
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
def get_data_from_url(url: str) -> pd.DataFrame:
    """
    This is function to convert the URL's table into pd.DataFrame to be later processed.
    This is made into seperate function, in order to cache resources.
    Parameters:
    - url (str): The URL of the website to convert to tables.
    Returns:
    - pd.DataFrame: Returns pd.DataFrame class if the function is able to succesfully convert.
    Raises:
    """
    return pd.read_html(url)


def ui() -> int:
    """
    This the mainpage's UI
    Returns:
    - int: number of tables created.
    """
    st.set_page_config(
        page_title="Wonjoon's CSV Generator",
        page_icon="📃"
    )
    st.title("URL to CSV Converter")
    st.subheader("Enter a wikipedia page or any URL with HTML table")
    url = st.text_input(
        "Enter URL here:",
        "https://en.wikipedia.org/wiki/List_of_countries_by_real_GDP_growth_rate")
    try:
        list_of_dfs = get_data_from_url(url)
        length_dfs = len(list_of_dfs)
        st.write(
            f"Total {length_dfs} table{
                "s" if length_dfs > 1 else ""} found on the webpage")
    except BaseException:
        st.error(f"Could not find Table in the URL: {url}")
        return 0
    i = 1
    for data in list_of_dfs:
        st.header(f"Table {i}")
        # st.table can still fail with try. So, try was removed here.
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
