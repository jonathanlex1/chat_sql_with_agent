import streamlit as st 
from langchain.callbacks.streamlit import StreamlitCallbackHandler
from sql_rag_agent import llm_agent

#database configuration
db_config = {}

if 'messages' not in st.session_state : 
    st.session_state['messages'] = [{'role' : 'assistant', 'content' : 'how can i help you'}] 

#sidebar
with st.sidebar : 
    st.title('🔗 Langchain : Chat your Database with Agent')
    
    select = st.radio(options=['sqlserver', 'mysql'], label='Choose database')

    if select == 'sqlserver' : 
        db_config["server_name"] = st.text_input('Server Name')
        db_config["db_name"] = st.text_input('Database Name')
            
    elif select == 'mysql' : 
        db_config["user"] = st.text_input('User')
        db_config["password"] = st.text_input('Password', type='password')
        db_config["host"] = st.text_input('Localhost')
        db_config["db_name"] = st.text_input('Database Name')
            

    api_key = st.text_input('LLM Groq API Key', type='password')

#mainbar
st.title('🤖 Chatbot')     

for message in st.session_state['messages']: 
    st.chat_message(message['role']).write(message['content'])


query = st.chat_input(placeholder='What do you need')

if not all([select, api_key, query]):   
    st.warning('Fill the all fields')
else :

    with st.spinner('Processing...') :
        st.session_state['messages'].append({'role' : 'user', 'content' : query})

        #to show all LLM thoughts
        callback_handler = StreamlitCallbackHandler(st.container())
        
        agent = llm_agent(api_key=api_key, db_type=select, db_config=db_config)
        response = agent.run(query, callbacks=[callback_handler])
        st.session_state['messages'].append({'role' : 'assistant', 'content' : response})
        st.chat_message('assistant').write(response)