import streamlit as st
# import pandas as pd


def run_app():

    # build expander and place the app inside
    st.subheader('TUM.ai Makeathon')
    with st.expander('sdfjkdf', expanded=True):
        if st.button('click me'):
            st.write('hello')


if __name__ == '__main__':

    # run the main app function
    run_app()
