import streamlit as st
import pandas as pd
import os

st.title("Starbucks Locations Worldwide")
st.markdown("--by Parita--")

# ⚠️ IMPORTANT: Change this filename to the exact name of your downloaded CSV file
CSV_FILENAME = 'directory.csv' 

# Construct the file path (assumes the CSV is in the parent directory)
# st.session_state is used here just to demonstrate setting a variable.
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', CSV_FILENAME)

# Use st.cache_data for efficient data loading (it only runs once)
@st.cache_data
def load_local_data(file_path):
    try:
        # Load the CSV directly from the local file path
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file '{CSV_FILENAME}' was not found at the expected location.")
        st.info("Please make sure your CSV is in the root 'week11_streamlit' folder.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
        return pd.DataFrame()

# Load the data and check if it was successful
data_df = load_local_data(FILE_PATH)

if not data_df.empty:
    st.subheader("Raw Data Preview")
    st.write(f"Dataset successfully loaded with {len(data_df)} rows and {len(data_df.columns)} columns.")
    
    # Display the interactive DataFrame table
    st.dataframe(data_df.head()) 

    # Display some basic data information
    st.subheader("Column Information")
    st.table(data_df.dtypes.rename('Data Type'))