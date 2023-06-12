import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Tampilan Streamlit
st.title('Uji Korelasi')

# Load data from Excel file
def load_data_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        st.error("Failed to load data from xlsx file.")
        st.error(e)
        return None

# Calculate correlation coefficient
def calculate_correlation(x, y):
    correlation = x.corr(y)
    return correlation

# Create a file uploader
st.subheader('Masukkan Data')
st.write('contoh input data excel lebih jelasnya lihat di bagian PMS')
uploaded_file = st.file_uploader("Upload xlsx File", type=['xlsx'])

# Check if a file is uploaded
if uploaded_file is not None:
    data = load_data_from_excel(uploaded_file)

    # Select variables for correlation
    variables = data.columns.tolist()
    x_variable = st.selectbox("Select X Variable", variables)
    y_variable = st.selectbox("Select Y Variable", variables)

    # Check if both variables are selected
    if x_variable and y_variable:
        x = data[x_variable]
        y = data[y_variable]

        # Calculate correlation coefficient
        correlation = calculate_correlation(x, y)

        # Display correlation result
        st.subheader("Correlation Result")
        st.write(f"Correlation coefficient between {x_variable} and {y_variable}:", correlation)

        # Create scatter plot
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        ax.set_xlabel(x_variable)
        ax.set_ylabel(y_variable)
        ax.set_title(f"Scatter Plot: {x_variable} vs {y_variable}")
        st.pyplot(fig)