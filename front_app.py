import streamlit as st
from gcp import predict


def get_top_confidence_category(text):
    """
    Realiza a predição das categorias com base no texto fornecido, 
    selecionando a categoria com maior nível de confiança ('Confidence')
    gerada pelo modelo. Este método destina-se a identificar a 
    categoria mais provável para apresentação no aplicativo web Streamlit.

    Parâmetros:
        text (str): Texto que será analisado pelo modelo.

    Retorna:
        str: O label da categoria com maior confiança prevista pelo modelo.
    """

    # Make prediction
    prediction = predict(text)

    # Find the index of the highest score
    max_score_index = prediction['scores'].index(max(prediction['scores']))

    # Use the index to find the corresponding class (Categoria)
    categoria = prediction['classes'][max_score_index]

    return categoria


# Streamlit app layout
st.title("Cloud Topic Modeling App")

# Text input
user_input = st.text_area("Escreva abaixo o texto do chamado para ser classificado", "")

if st.button('Predict'):
    if user_input:  # Check if there is an input
        predicted_category = get_top_confidence_category(user_input)
        st.markdown(f"### Categoria predita:")
        
        # Display the category in green
        st.markdown(f"<h1 style='color: green;'>{predicted_category}</h1>", unsafe_allow_html=True)
    else:
        st.write("Por favor, insira o texto do chamado para ser classificado.")
