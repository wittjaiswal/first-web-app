import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly.express as px


st.title('US Vehicle Sales Stats')

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)  # Replace with appropriate function (e.g., pd.read_excel for Excel files)
    except Exception as e:
        st.error(f"Error reading the data file: {e}")
        return None
    return data

# Streamlit app
def main():
    st.header("Data Loaded with Streamlit")

    # Example file path (modify this path according to your file location)
    file_path = 'vehicles_us.csv'

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

        # Create Plotly histogram
        fig = px.histogram(
            df, x='price', color='condition',
            title='Distribution of Vehicle Prices',
            labels={'price': 'Vehicle Price'},  # Can specify one label per df column
            opacity=0.8,
            category_orders={'condition': ['new', 'like new', 'good', 'fair', 'salvage', 'excellent']}
        )

        # Update layout
        fig.update_layout(bargap=0.1)  # Gap between bars

        # Show plot in Streamlit
        st.plotly_chart(fig)


        fig = px.scatter(df, x='odometer', y='price', color='fuel', 
                 title='Price vs. Odometer by Fuel Type', 
                 labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'}, 
                 opacity=0.5)

# To display in Streamlit
        st.plotly_chart(fig)





if __name__ == "__main__":
    main()

