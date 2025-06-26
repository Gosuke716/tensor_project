import streamlit as st

st.set_page_config(
    page_title='hello'
)

st.write('안녕하세요 반갑습니다.')

st.sidebar.success('데모 선택')

st.markdown("""
# Hello World
""")

name = st.text_input('이름')
print(name)

st.write(name)