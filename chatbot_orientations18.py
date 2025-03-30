import streamlit as st
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# Charger les embeddings et le vectorstore sauvegardé
embeddings = OpenAIEmbeddings(openai_api_key="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")
vectorstore = Chroma(persist_directory="chroma_db18", embedding_function=embeddings)
retriever = vectorstore.as_retriever()

# Initialiser le modèle de chat (par exemple GPT-4) avec la clé API
llm = ChatOpenAI(model_name="gpt-4", openai_api_key="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")

# Créer la chaîne de questions-réponses avec le modèle et le retriever
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Interface utilisateur avec Streamlit
st.title("🎓 Chatbot Orientation Universitaire")
st.write("Posez vos questions concernant les formations et universités !")

# Demander une question à l'utilisateur
user_query = st.text_input("Votre question :")

# Si l'utilisateur a posé une question, générer une réponse et l'afficher
if user_query:
    st.write(f"👤   {user_query}")
    
    # Obtenir la réponse du modèle
    response = qa_chain.run(user_query)
    
    # Afficher la réponse du chatbot
    st.write(f"🤖   {response}")
