import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Sarlavha
st.title("Gaz narxi bashorati")
st.write("Kelajakdagi sanani tanlang va bashoratlangan gaz narxini ko'ring.")

# 1. Modelni yuklash
model = joblib.load("gaznarxi.pkl")  # Gaz narxi model fayli yuklangan deb hisoblanadi

# 2. Foydalanuvchidan kelajakdagi sanani olish
future_date = st.date_input("Sanani tanlang:", value=datetime(2024, 12, 13))

# Sanani xususiyatlarga ajratish
year = future_date.year
month = future_date.month
day = future_date.day
day_of_year = future_date.timetuple().tm_yday

# 3. Bashorat qilish
if st.button("Bashoratni ko'rish"):
    input_data = pd.DataFrame({
        "Year": [year],
        "Month": [month],
        "Day": [day],
        "DayOfYear": [day_of_year]
    })
    prediction = model.predict(input_data)
    st.write(f"Bashorat qilingan gaz narxi: **{prediction[0]:,.2f} so'm**")

# 4. Qo'shimcha ma'lumot
st.write("Gaz narxi ma'lumotlari asosida bashorat qilingan modeldan foydalaniladi.")


# import streamlit as st
# import pandas as pd
# import joblib

# # Modelni yuklash
# model = joblib.load('gazmodel.pkl')

# # Web interfeysini yaratish
# st.title('Gaz Narxini Bashorat Qilish')

# # Foydalanuvchidan input olish
# open_price = st.number_input('Kun boshidagi Narxi:', min_value=0.0, value=50.0)
# high_price = st.number_input('High Narxi:', min_value=0.0, value=55.0)
# low_price = st.number_input('Kun so"ngidagi Narxi:', min_value=0.0, value=45.0)
# adj_close = st.number_input('So"ngi aniq Narxi:', min_value=0.0, value=50.0)
# volume = st.number_input('Bir kunlik gaz sotuvi $ da:', min_value=0, value=500000)

# # Foydalanuvchi parametrlarini DataFrame ga joylashtirish
# input_data = pd.DataFrame({
#     'Open': [open_price],
#     'High': [high_price],
#     'Low': [low_price],
#     'Adj Close': [adj_close],
#     'Volume': [volume]
# })

# # Bashorat qilish tugmasi
# if st.button("Bashorat qilish"):
#     # Model yordamida bashorat qilish
#     predicted_price = model.predict(input_data)
    
#     # Natijani ekranga chiqarish
#     st.success(f"Bashorat qilingan Gaz narxi: {predicted_price[0]:.2f}")



# # import streamlit as st
# # import pandas as pd
# # import joblib

# # # Modelni yuklash
# # model = joblib.load('gazmodel.pkl')

# # # Web interfeysini yaratish
# # st.title('Gaz Narxini Bashorat Qilish')

# # # Foydalanuvchidan input olish
# # open_price = st.number_input('Open Narxi:', min_value=0.0, value=50.0)
# # high_price = st.number_input('High Narxi:', min_value=0.0, value=55.0)
# # low_price = st.number_input('Low Narxi:', min_value=0.0, value=45.0)
# # adj_close = st.number_input('Adjusted Close Narxi:', min_value=0.0, value=50.0)
# # volume = st.number_input('Volume:', min_value=0, value=500000)

# # # Foydalanuvchi parametrlarini DataFrame ga joylashtirish
# # input_data = pd.DataFrame({
# #     'Open': [open_price],
# #     'High': [high_price],
# #     'Low': [low_price],
# #     'Adj Close': [adj_close],
# #     'Volume': [volume]
# # })

# # # Model yordamida bashorat qilish
# # predicted_price = model.predict(input_data)

# # # Natijani ekranga chiqarish
# # st.write(f"Bashorat qilingan Gaz narxi: {predicted_price[0]:.2f}")
