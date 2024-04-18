"""
    Easy Azure Streamlit Demo
    Original Author: Wolf Paulus (wolf@paulus.com)
    Forked by Wonjoon Jun
"""
from random import randint
import streamlit as st
from log import logger


def ui(items: [int]) -> None:

    st.title("Streamlit Demo v0.4")
    st.subheader(".. on Azure")
    st.line_chart(items)


if __name__ == "__main__":
    data = [randint(0, 100) for _ in range(25)]
    logger.info(f"Created a list with {len(data)} items.")
    ui(data)
