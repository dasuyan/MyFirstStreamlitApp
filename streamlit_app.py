import streamlit as st

st.title("Tłumacz angielsko-niemiecki")
st.write("Ta aplikacja służy do tłumaczenia tekstu z języka angielskiego na niemiecki oraz określania wydźwięku "
         "emocjonalnego tekstu w języku angielskim. "
         "Stanowi też mój pierwszy projekt w Streamlit."
         "\n\nAby sprawdzić funkcjonalność aplikacji, wybierz poniżej jedną z dwóch opcji, wprowadź tekst, a następnie "
         "kliknij czerwony przycisk i poczekaj na wynik działania aplikacji :)")

st.header("Przetwarzanie języka naturalnego")

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Tłumaczenie tekstu (en -> de)",
        "Wydźwięk emocjonalny tekstu (en)",
    ],
)

text = st.text_area(label="Wpisz tekst")
answer = ""
st.spinner()


with st.spinner(text='Przetwarzanie...'):
    if option == "Tłumaczenie tekstu (en -> de)":
        if st.button("Tłumacz", type="primary"):
            classifier = pipeline("translation_en_to_de")
            answer = classifier(text)[0]["translation_text"]
            if text != "":
                st.write(f"Wynik: {answer}")
                st.success('Sukces!')
                st.balloons()
            else:
                st.error("Wprowadź tekst w polu powyżej")

    if option == "Wydźwięk emocjonalny tekstu (en)":
        if st.button("Analizuj", type="primary"):
            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
            if text != "":
                st.write(f"Wynik: {answer}")
                st.success('Sukces!')
                st.balloons()
            else:
                st.error("Wprowadź tekst w polu powyżej")

st.subheader("Numer indeksu: s23711")
