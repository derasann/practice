import streamlit as st
from PIL import Image

st.title('好きな映画')

st.write('Display Image')
img_path = '/Users/onoderakyoko/project-dir/topgun.jpg'  # 画像のパスを直接指定

try:
    img = Image.open(img_path)
    st.image(img, caption='マーベリック！', use_column_width=False, width=300)
except FileNotFoundError:
    st.error(f'Error: File not found at {img_path}')

option = st.slider(
    'この映画をどのくらい好きですか、',
    min_value=1, max_value=10, value=5
)
'あなたの評価は、', option, 'です。'
