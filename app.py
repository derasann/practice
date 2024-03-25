import streamlit as st
from PIL import Image

st.title('好きな映画')

st.write('Display Image')
#img = Image.open('/Users/onoderakyoko/project-dir/topgun.jpg')
img = Image.open('topgun.jpg')
st.image(img, caption='マーベリック！', use_column_width=False, width=300)

import os
os.chdir('/Users/onoderakyoko/project-dir')
img = Image.open('topgun.jpg')

option = st.slider(
    'この映画をどのくらい好きですか、',
    min_value=1, max_value=10, value=5
)
'あなたの評価は、', option, 'です。'
