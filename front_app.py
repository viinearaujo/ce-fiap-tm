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



st.empty()
st.empty()
st.empty()



# Custom function to display text examples in styled bubbles
def display_example(text, background_color="#f0f2f6", text_color="#333"):
    """
    Display the example text in a styled bubble.
    Args:
    - text: The example text to display.
    - background_color: The background color of the bubble.
    - text_color: The text color.
    """
    html = f"""
    <div style='background-color: {background_color}; border-radius: 10px; padding: 10px; margin: 10px 0;'>
    <p style='color: {text_color}; margin:0;'>{text}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Sidebar for category selection
st.sidebar.header("Precisa de ajuda?")
category = st.sidebar.selectbox("Categoria", ["Escolha uma Categoria", "Hipotecas / Empréstimos", "Cartão de crédito / Cartão pré-pago", "Serviços de conta bancária"])

# Example texts mapped to categories
example_texts = {
    "Hipotecas / Empréstimos": "Estou tentando refinanciar minha hipoteca há meses, mas não consigo obter uma taxa de juros satisfatória. Preciso de orientação sobre como proceder para conseguir uma melhor oferta.",
    "Cartão de crédito / Cartão pré-pago": "Meu cartão de crédito foi clonado e observei transações não autorizadas. Como posso contestar essas cobranças e obter um novo cartão com segurança reforçada?",
    "Serviços de conta bancária": "Houve um problema com a transferência que tentei fazer para outra conta. O valor foi debitado da minha conta, mas o destinatário não recebeu o dinheiro. Preciso de ajuda urgente para resolver essa questão."
}



# Main area: Displaying the example based on selection
st.header("Exemplo de texto para ser Predito")
if category and category != "Escolha uma Categoria":
    st.write(f"Exemplo para **{category}**:")
    display_example(example_texts[category])
else:
    st.write("Seleciona uma Categoria de Chamados para ver o texto de exemplo.")
    st.empty()