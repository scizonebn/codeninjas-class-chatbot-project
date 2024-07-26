# Import the OpenAI library to use AI models
from openai import OpenAI

# Import Streamlit to create a web app interface
import streamlit as st

# Import the message function to display chat messages
from streamlit_chat import message


#################################################################################################
# Lets Build the Brain for our ChatBot
################################################################################################

# Set up a client to talk to OpenAI's API using a secret key
client = OpenAI(
  api_key="your-secret-key-here",  # This key is like a password! Keep it secret.
)

# Function to get a response from the AI using what you type
def get_query_response(user_input):
    openai_response = client.chat.completions.create(
        model='gpt-3.5-turbo',  # The version of the bot brain to use.
        messages=[{'role': 'user', 'content': user_input}]  # Send what you say as a user
    )

    # Return the AI's reply
    return openai_response.choices[0].message.content



##################################################################################################
# Lets Build the Body for our ChatBot
##################################################################################################

# Main function to set up and run the chat app
def main() -> None:

    # Show the chatbot's name at the top
    # Lets go online and get come emoji to make the chatbot beautiful
    st.markdown(
        '<h1>Your Bot\'s Name</h1>',
        unsafe_allow_html=True,
    )

    # Keep track of what you and the bot say
    if "history" not in st.session_state:
        st.session_state.history = []

    # Display a friendly greeting
    message("Hello, how may I help you?")

    # Create a sidebar for typing messages to the bot
    with st.sidebar:
        
        # Text box where you type messages to the bot
        user_input = st.text_input(
            "Ask your Bot", key="user_input", placeholder="Type something interesting here"
        )

    # If you type something, do this
    if user_input:
        # Show a loading spinner while the bot is "thinking"
        with st.spinner("Searching knowledge base ..."):
            
            # Get the bot's response to your message
            # Lets connect the brain to the body 
            bot_response = get_query_response(user_input)
        
        # Save what you and the bot said
        st.session_state.history.append({"user": user_input, "bot": bot_response})

    # Show the conversation so far
    if st.session_state.history:
        for i, chat in enumerate(st.session_state.history):
            # Show what you said
            message(chat["user"], is_user=True, key=str(i) + "_user")
            # Show what the bot replied
            message(chat["bot"], key=str(i) + "_bot")

# Run the main function if this file is executed
if __name__ == "__main__":
    main()

# To start the app, type this command in the terminal: streamlit run chatbot.py
