import streamlit as st
from gcp import predict



def get_best_category_prediction(text):

    # Make prediction
    prediction = predict(text)

    # Find the index of the highest score
    max_score_index = prediction['scores'].index(max(prediction['scores']))

    # Use the index to find the corresponding class
    best_class = prediction['classes'][max_score_index]
    best_score = prediction['scores'][max_score_index]

    print(f"Best prediction: {best_class} with confidence {best_score:.2f}")

    return best_class



# Streamlit app layout
st.title("Cloud Topic Modeling App")


# Text input
user_input = st.text_area("Escreva abaixo o texto do chamado para ser classificado", "")

if st.button('Predict'):
    if user_input:  # Check if there is an input
        predicted_category = get_best_category_prediction(user_input)
        st.markdown(f"### Categoria predita:")
        
        # Display the category in green
        st.markdown(f"<h1 style='color: green;'>{predicted_category}</h1>", unsafe_allow_html=True)
    else:
        st.write("Por favor, insira o texto do chamado para ser classificado.")









