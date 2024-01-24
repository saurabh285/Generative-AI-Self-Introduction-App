import os
from apikey import apikey

import streamlit as st
from langchain import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma 
#from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
# '''
# pip install streamlit==1.24.0 to avoid uploading error 
# AxiosError: Request failed with status code 403
# '''


os.environ["OPENAI_API_KEY"] = apikey 

def clear_history():
    if 'history' in st.session_state:
        del st.session_state['history']

st.title('Ask about Saurabh')

loader = TextLoader('./info.txt')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#\n\n, \n, ' '

chunks = text_splitter.split_documents(documents)    

embeddings = OpenAIEmbeddings()

vector_store = Chroma.from_documents(chunks, embeddings)

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

retriever=vector_store.as_retriever()
crc = ConversationalRetrievalChain.from_llm(llm,retriever)
st.session_state.crc = crc
st.success('I am ready for your questions now!! ')
question = st.text_input('What do you want to ask')

if question:
    if 'crc' in st.session_state:
        crc = st.session_state.crc
        if 'history' not in st.session_state:
            st.session_state['history'] = []

        response = crc.run({'question':question,'chat_history':st.session_state['history']})

        st.session_state['history'].append((question,response))
        st.write(response)

        #st.write(st.session_state['history'])
        for prompts in st.session_state['history']:
            st.write("Question: " + prompts[0])
            st.write("Answer: " + prompts[1])    