import streamlit as st
import pandas as pd

# Example Write Function.
st.write(pd.DataFrame({
    'c1' : [1, 2, 3, 4],
    'c2' : [10,20,30,40],
}))

# Example markdown()
st.markdown(
    """
    # My First App
    Hello, para calon praktisi data masa depan!
    """
)

# Example title()
st.title('Belajar Analisis Data')

# Example Header()
st.header('Pengembangan Dashboard')

# Example Caption()
st.caption('Copyright (c) 2023')

# Example Code()
code = """ def hello():
    print("Hello, streamlit!")"""

st.code(code, language='python')

# Example Text()
st.text('Halo, calon praktisi data masa depan.')

# Example Latext()
st.latex(
    r"""
    \sum_{k=0}^{n-1} ar^k = 
    a \left(\frac{1-r^{n}}{1-r}\right)
    """
)
