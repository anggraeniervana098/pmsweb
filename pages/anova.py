import streamlit as st
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Fungsi untuk menghitung uji ANOVA
def perform_anova(data):
    model = ols('nilai ~ treatment', data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table

# Tampilan Streamlit
st.title('Uji ANOVA')

# Memuat data dari pengguna
st.subheader('Masukkan Data')
st.write('Format nilai di kolom 1 dan treatment di kolom 2')
st.write('untuk lebih jelasnya lihat di bagian PMS')
excel_file = st.file_uploader('Unggah file Excel', type=['xlsx', 'xls'])

# Membaca data dari file Excel
data = None
if excel_file is not None:
    try:
        data = pd.read_excel(excel_file)
    except Exception as e:
        st.write('Terjadi kesalahan saat membaca file:', str(e))

# Menampilkan data
if data is not None:
    st.subheader('Data')
    st.write(data)

    # Menjalankan uji ANOVA jika data valid
    if len(data) >= 3:
        st.subheader('Hasil Uji ANOVA')
        anova_result = perform_anova(data)
        st.write(anova_result)
    else:
        st.write('Minimal 3 baris data diperlukan untuk melakukan uji ANOVA.')
