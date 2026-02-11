import streamlit as st

st.write("Тест по География и История")
st.write("Моля, отговорете на следните 5 въпроса:")

score = 0

st.write("1. Коя е столицата на Англия?")
q1 = st.text_input("Въведете град:", key="q1")

st.write("2. През коя година е освободена бългрия?")
q2 = st.text_input("Въведете година:", key="q2")

st.write("3. Кой е най-голеямата планина в света?")
q3 = st.text_input("Въведете планина:", key="q3")

st.write("4. Кой е известен като основателят на Старата Велика България?")
q4 = st.text_input("Въведете име:", key="q4")

st.write("5. Колко океана има на Земята?")
q5 = st.text_input("Въведете число:", key="q5")

if st.button("Провери резултата"):
    if q1.strip().lower() == "лондон":
        score = score + 1
    
    if q2.strip() == "1878":
        score = score + 1
        
    if q3.strip().lower() == "еверест":
        score = score + 1
        
    if q4.strip().lower() == "хан кубрат":
        score = score + 1
        
   if q5.strip() == "5":
        score = score + 1

    if score == 5:
        st.write("Отличен! Резултат: 5 от 5.")
    else:
        st.write("Вашият резултат е: " + str(score) + " от 5. Опитайте отново.")
