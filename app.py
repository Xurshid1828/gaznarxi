import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model = joblib.load('gazmodel.pkl')

# Web interfeysini yaratish
st.title('Gaz Narxini Bashorat Qilish')

# Foydalanuvchidan input olish
open_price = st.number_input('Open Narxi:', min_value=0.0, value=50.0)
high_price = st.number_input('High Narxi:', min_value=0.0, value=55.0)
low_price = st.number_input('Low Narxi:', min_value=0.0, value=45.0)
adj_close = st.number_input('Adjusted Close Narxi:', min_value=0.0, value=50.0)
volume = st.number_input('Volume:', min_value=0, value=500000)

# Foydalanuvchi parametrlarini DataFrame ga joylashtirish
input_data = pd.DataFrame({
    'Open': [open_price],
    'High': [high_price],
    'Low': [low_price],
    'Adj Close': [adj_close],
    'Volume': [volume]
})

# Bashorat qilish tugmasi
if st.button("Bashorat qilish"):
    # Model yordamida bashorat qilish
    predicted_price = model.predict(input_data)
    
    # Natijani ekranga chiqarish
    st.success(f"Bashorat qilingan Gaz narxi: {predicted_price[0]:.2f}")



# import streamlit as st
# import pandas as pd
# import joblib

# # Modelni yuklash
# model = joblib.load('gazmodel.pkl')

# # Web interfeysini yaratish
# st.title('Gaz Narxini Bashorat Qilish')

# # Foydalanuvchidan input olish
# open_price = st.number_input('Open Narxi:', min_value=0.0, value=50.0)
# high_price = st.number_input('High Narxi:', min_value=0.0, value=55.0)
# low_price = st.number_input('Low Narxi:', min_value=0.0, value=45.0)
# adj_close = st.number_input('Adjusted Close Narxi:', min_value=0.0, value=50.0)
# volume = st.number_input('Volume:', min_value=0, value=500000)

# # Foydalanuvchi parametrlarini DataFrame ga joylashtirish
# input_data = pd.DataFrame({
#     'Open': [open_price],
#     'High': [high_price],
#     'Low': [low_price],
#     'Adj Close': [adj_close],
#     'Volume': [volume]
# })

# # Model yordamida bashorat qilish
# predicted_price = model.predict(input_data)

# # Natijani ekranga chiqarish
# st.write(f"Bashorat qilingan Gaz narxi: {predicted_price[0]:.2f}")
