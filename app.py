import streamlit as st
import pandas as pd


def app_main():

    # build expander and place the app inside
    with st.expander('sdfjkdf', expanded=True):
        st.write('TUM.ai Makeathon')


if __name__ == '__main__':

    # run the main app function
    app_main()