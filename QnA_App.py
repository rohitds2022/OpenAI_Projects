#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import openai
from secret_key import api_key
openai.api_key = api_key


# In[2]:


def qa_app(input_text):
    # Create a list of messages containing the user input
    messages = [
        {
            "role": "system",
            "content": "You will be provided with a question, and your task is to answer it correctly."
        },
        {
            "role": "user",
            "content": input_text
        }
    ]

    # Generate response from the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=256
    )

    # Return the generated output
    return response['choices'][0]['message']['content']


# #### Deploying the QnA App

# In[3]:


#pip install streamlit


# In[4]:


import streamlit as st

def main():
    st.title("My Question and Answer Bot")
    st.write("Ask me a question.")
    
    conversation = []
    counter = 0
    
    while True:
        
        user_input = st.text_input("You:", key=f'user_input_{counter}') 
        #The key parameter is set to f'user_input_{counter}', where counter is a variable that likely increments on each iteration of the           loop. The key parameter is used to uniquely identify this particular text input widget, allowing Streamlit to update it correctly           when the app is rerun.
            
        if user_input:
            conversation.append({"role":"user","content": user_input})
            generated_output = qa_app(user_input)
            conversation.append({"role":"model","content": generated_output})
            
            st.write(f"{conversation[-1]['role']}: \n {conversation[-1]['content']}")
            
            counter+=1
            
        else:
            break
        
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




