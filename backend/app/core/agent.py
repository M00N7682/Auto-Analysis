from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI
import os

def get_agent(df):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=openai_api_key)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return agent
