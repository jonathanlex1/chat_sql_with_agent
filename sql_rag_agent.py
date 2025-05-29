from dotenv import load_dotenv
import os
from langchain.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType

# Load LLM API key
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY') 

#databse configuration
db_config={
    "user":'root',
    "password":'12345', 
    "db_name":'database_belajar', 
    "host":"localhost:3306"
}

# SQL Server connection
def sql_server_db_engine(server_name:str, db_name:str):
    if not all([server_name, db_name]):
        raise ValueError('Input all parameters')
    else:
        engine = create_engine(
            f"mssql+pyodbc://{server_name}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        )
    return SQLDatabase(engine)

#mysql connection 
def mysql_db_engine(password:str=None, user:str=None, db_name:str=None, host:str=None) :
    if not all([password, user, db_name, host]): 
        raise ValueError('Input all parameters')
    else : 
        engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}")
    return SQLDatabase(engine) 


def llm_agent(api_key:str, db_type:str, db_config:dict) : 
    api_key = api_key or os.getenv('GROQ_API_KEY')
    if not api_key : 
        raise ValueError('GROQ API key is required')
    
    #llm calling
    llm = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct', api_key=api_key)

    #database connection 
    if db_type == 'sqlserver' : 
        db = sql_server_db_engine(server_name=db_config['server_name'], db_name=db_config['db_name'])

    elif db_type == 'mysql' :
        db = mysql_db_engine(user=db_config['user'], password=db_config['password'], host=db_config['host'], db_name=db_config['db_name'])

    else : 
        raise ValueError('Unsupported database type')
    
    #toolkit and agent 
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    return create_sql_agent(llm=llm, toolkit=toolkit, verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)


if __name__ == '__main__' : 
    agent = llm_agent(GROQ_API_KEY, db_type='mysql', db_config=db_config)
    response = agent.run('what name products from proucts table')
    print(response)