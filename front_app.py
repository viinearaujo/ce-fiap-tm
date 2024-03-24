import streamlit as st
from gcp import predict

# Placeholder for your model loading function
# def load_model():
#     # Load your trained model
#     return model

# Placeholder for your prediction function
# Replace this with your actual model prediction logic
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

# Initialize your model (uncomment and modify the following line according to your model loading function)
# model = load_model()

# Streamlit app layout
st.title("Cloud Topic Modeling App")



# Text input
user_input = st.text_area("Enter the text to classify", "")

if st.button('Predict'):
    if user_input:  # Check if there is an input
        predicted_category = get_best_category_prediction(user_input)
        st.markdown(f"### Predicted Category:")
        
        # Display the category in green
        st.markdown(f"<h1 style='color: green;'>{predicted_category}</h1>", unsafe_allow_html=True)
    else:
        st.write("Please enter some text to classify.")









