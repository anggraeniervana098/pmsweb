import streamlit as st
import numpy as np
from scipy.stats import ttest_ind

# Header
st.title('Uji Hipotesis untuk k Populasi')

# Input jumlah populasi (k)
k = st.number_input('Jumlah Populasi (k)', min_value=2, value=2, step=1)

# Input data sampel untuk setiap populasi
sample_data = []
for i in range(k):
    st.header(f'Populasi {i+1}')
    sample_size = st.number_input(f'Jumlah Sampel (Populasi {i+1})', min_value=1, value=10, step=1)
    samples = []
    for j in range(sample_size):
        sample = st.number_input(f'Sampel {j+1} (Populasi {i+1})', value=0.0, step=0.01)
        samples.append(sample)
    sample_data.append(samples)

# Uji Hipotesis
st.header('Uji Hipotesis')

# Pilih tingkat signifikansi (alpha)
alpha = st.number_input('Tingkat Signifikansi (alpha)', min_value=0.01, max_value=0.10, value=0.05, step=0.01)

# Hitung statistik uji dan p-value
statistic, p_value = ttest_ind(*sample_data)

# Tampilkan hasil uji hipotesis
st.write(f'Statistik Uji: {statistic:.4f}')
st.write(f'p-value: {p_value:.4f}')

# Evaluasi hasil uji hipotesis
if p_value < alpha:
    st.write('Kami menolak hipotesis nol.')
else:
    st.write('Kami gagal menolak hipotesis nol.')
