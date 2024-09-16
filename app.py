import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly.express as px


st.header('US Vehicle Sales Stats')

import streamlit as st
import pandas as pd

# Load data function
def load_data(file_path):
    try:
        data = pd.read_csv('C:/Users/ayush/documents/python_vs_code/first-web-app/vehicles_us.csv')  # Replace with the appropriate function, e.g., pd.read_excel for Excel files
    except Exception as e:
        st.error(f"Error reading the data file: {e}")
        return None
    return data

# Streamlit app
def main():
    st.title("Data Loader with Streamlit")

    # Example file path (modify this path according to your file location)
    file_path = 'path/to/your/data.csv'

    # Load data
    df = load_data(file_path)

    if df is not None:
        # Display data
        st.write("DataFrame:")
        st.write(df)

        # Display basic information
        st.write("Data Types:")
        st.write(df.dtypes)

        st.write("Basic Statistics:")
        st.write(df.describe())

if __name__ == "__main__":
    main()


