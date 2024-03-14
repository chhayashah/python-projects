!pip install openai
import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to interact with GPT-4
def chat_with_gpt4(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-4's model
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Chat with GPT-4")

    # Input field for the user's OpenAI API key
    openai_api_key = st.text_input("Enter your OpenAI API key")

    # Chat box
    user_input = st.text_area("You:", height=100)

    # Button to send user input and get response
    if st.button("Send"):
        if not openai_api_key:
            st.error("Please provide your OpenAI API key")
        else:
            # Set the OpenAI API key
            openai.api_key = openai_api_key

            # Get response from GPT-4
            gpt4_response = chat_with_gpt4(user_input)

            # Display conversation in chat format
            st.write("**You:**", user_input)
            st.write("**GPT-4:**", gpt4_response)

if __name__ == "__main__":
    main()
