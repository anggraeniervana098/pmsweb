import streamlit as st
import pandas as pd

def main():
    st.title("WEB PMS DENGAN STREAMLIT")

    # Data untuk tabel pertama
    data1 = {
        "nilai": ["49.2", "44.54", "45.8", "97.07", "73.4", "68.5", "62.1", "94.95", "142.5", "110.6", "57.1", "117.6"],
        "treatment": ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"]
    }

    # Data untuk tabel kedua
    data2 = {
        "Variabel X" : ["3", "4.7", "8.3", "9.3", "9.9", "11", "12.3", "12.5", "12.6", "15.9", "16.7", "18.8"],
        "Variabel Y" : ["0.971", "0.979", "0.982", "0.971", "0.957", "0.961", "0.956", "0.972", "0.889", "0.961", "0.982", "0.975"]
    }

    # Membuat DataFrame dari data pertama
    df1 = pd.DataFrame(data1)

    # Menampilkan tabel pertama
    st.write("Contoh Data di Excel untuk Uji ANOVA:")
    st.dataframe(df1)

    # Membuat DataFrame dari data kedua
    df2 = pd.DataFrame(data2)

    # Menampilkan tabel kedua
    st.write("Contoh Data di Excel untuk Uji Korelasi:")
    st.dataframe(df2)


if __name__ == "__main__":
    main()
