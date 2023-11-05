import streamlit as st
import pprint
import google.generativeai as palm


palm.configure(api_key='AIzaSyDrwSf5widLeJ63y4lpgfZgQKxM6Fqb8Ug')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
print(models)
model = models[0].name
print(model)

st.title("NITT CHAT BOT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
message=''
if prompt := st.chat_input("Have any queries?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        message=prompt
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


completion=palm.generate_text(
        model=model,
        prompt=message,
        temperature=0,
        max_output_tokens=1000,
    )

response = f": {completion.result}"
# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
