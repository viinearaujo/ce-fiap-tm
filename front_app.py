import streamlit as st
from gcp import get_top_confidence_category
import setup_spacy as ss
from spacy.lang.pt.stop_words import STOP_WORDS

nlp = ss.download_spacy_model()

# Function to clean and lemmatize text
def clean_and_lemmatize(text):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if token.lemma_ not in STOP_WORDS and token.lemma_.isalpha():
            tokens.append(token.lemma_.lower())
    return " ".join(tokens)

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

# Streamlit app layout
st.title("Cloud Topic Modeling App")

# Text input
user_input = st.text_area("Escreva abaixo o texto do chamado para ser classificado", "")

if st.button('Classificar texto'):
    if user_input:  # Check if there is an input
        lemmatized_user_input = clean_and_lemmatize(user_input)
        predicted_category = get_top_confidence_category(lemmatized_user_input)
        st.markdown(f"### Categoria predita:")
        
        # Display the category in green
        st.markdown(f"<h1 style='color: green;'>{predicted_category}</h1>", unsafe_allow_html=True)
    else:
        st.write("Por favor, insira o texto do chamado para ser classificado.")

# Sidebar for category selection
st.sidebar.header("Precisa de ajuda?")
category = st.sidebar.selectbox(
    "Categorias exemplo",
    ["Escolha uma Categoria",
    "Hipotecas / Empréstimos",
    "Roubo / Relatório de disputa",
    "Serviços de conta bancária"
    ]
)

# Example texts mapped to categories
example_texts = {
    "Hipotecas / Empréstimos": "Estou tentando refinanciar minha hipoteca há meses, mas não \
        consigo obter uma taxa de juros satisfatória. Preciso de orientação sobre como proceder \
            para conseguir uma melhor oferta.",
    "Roubo / Relatório de disputa": "Meu cartão de crédito foi clonado e observei transações \
        não autorizadas. Como posso contestar essas cobranças e obter um novo cartão com segurança \
            reforçada?",
    "Serviços de conta bancária": "Houve um problema com a transferência que tentei fazer para outra \
        conta. O valor foi debitado da minha conta, mas o destinatário não recebeu o dinheiro. \
            Preciso de ajuda urgente para resolver essa questão."
}

# Main area: Displaying the example based on selection
st.header("Exemplo de texto para ser Predito")
if category and category != "Escolha uma Categoria":
    st.write(f"Exemplo para **{category}**:")
    display_example(example_texts[category])
else:
    st.write("Seleciona uma Categoria de Chamados para ver o texto de exemplo.")
