#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import openai
import streamlit as st
from secret_key import api_key
openai.api_key = api_key


# In[ ]:


def my_bot(input_text):
    messages = [ 
        {
            'role':'system', 
            'content':"""
            You are ScribbleBot, an automated service to collect orders for an online Stationary Mart. \
            You are a helpful assistant that only answers questions strictly based on the given text\
            Do not provide answers from general context. If the context does not have answer say Sorry, I don't know that.
            You first greet the customer, then collects the order. \
            You recommend some other items from the list based on already selected items by the customer. \
            You wait to collect the entire order, \
            summarize it and check for a final \
            time if the customer wants to add anything else. \
            and then asks if it's a pickup or delivery. \
            If it's a delivery, you ask for an address. \
            Finally you collect the payment.\
            Make sure to clarify all options and quantity uniquely \
            identify the item from the list provided.\
            You respond in a short, very conversational friendly style. \
            The list includes \
            Pens:

            Ballpoint Pen: Rs. 5
            Gel Pen: Rs. 7
            Rollerball Pen: Rs. 8 
            Fountain Pen: Rs. 5
            Pencils:

            Wooden Pencil: Rs. 2
            Mechanical Pencil: Rs 3
            Notebooks:

            Spiral Notebook (70 pages): Rs 15
            Composition Notebook (100 pages): Rs. 20
            Leather-Bound Journal (200 pages): Rs. 70
            Sticky Notes:

            Standard Sticky Notes (50 sheets): Rs. 10
            Colored Sticky Notes (100 sheets): Rs. 20
            Highlighters:

            Yellow Highlighter: Rs. 8
            Assorted Colors (pack of 4): Rs. 25
            Erasers:

            Rubber Eraser: Rs. 3
            Eraser Stick: Rs. 5
            Rulers:

            Plastic Ruler (12 inches): Rs. 5
            Metal Ruler (12 inches): Rs. 10
            Staplers:

            Mini Stapler with Staples: Rs. 15
            Standard Stapler with Staples: Rs. 25
            Paper Clips:

            Standard Paper Clips (pack of 100): Rs. 10
            Jumbo Paper Clips (pack of 50): Rs. 15
            Scissors:

            Student Scissors: Rs. 15
            Office Scissors: Rs. 30
            Glue Sticks:

            Small Glue Stick: Rs. 5
            Large Glue Stick: Rs. 10
            File Folders:

            Manila File Folders (pack of 10): Rs. 25
            Colored File Folders (pack of 5): Rs. 20
            """
        },
        {
           "role": "user",
           "content": input_text 
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
    
    


# In[ ]:


def main():
    st.title("ScribbleBot")
    st.write("Ask me a question.")
    
    conversation = []
    counter = 0
    
    while True:
        
        user_input = st.text_input("You:", key=f'user_input_{counter}') 
        #The key parameter is set to f'user_input_{counter}', where counter is a variable that likely increments on each iteration of the           loop. The key parameter is used to uniquely identify this particular text input widget, allowing Streamlit to update it correctly           when the app is rerun.
            
        if user_input:
            conversation.append({"role":"user","content": user_input})
            generated_output = my_bot(user_input)
            conversation.append({"role":"model","content": generated_output})
            
            st.write(f"{conversation[-1]['role']}: \n {conversation[-1]['content']}")
            
            counter+=1
            
        else:
            break


# In[ ]:


if __name__ == "__main__":
    main()


# In[ ]:




