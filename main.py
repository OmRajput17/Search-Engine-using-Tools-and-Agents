"""
LangChain Chat with Search (Streamlit App)
------------------------------------------
A chatbot that uses Groq LLM + LangChain Agents 
with integrated Wikipedia, Arxiv, and DuckDuckGo search tools.
"""

import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv  

load_dotenv()

## Used inbuilt tool of wikipediap
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

### Used inbuilt tool of arxiv
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv_tool = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name = "search")

st.title("LangChain - Chat with Search")


groq_api_key = os.getenv("GROQ_API_KEY")

## Creating session history
if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {"role":"assistant", "content":"Hi! I'm a chatbot who can search the web. How can I help you?"}
    ]

### For printing msgs in the UI
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

### If prompt is added

if prompt:=st.chat_input(placeholder="What is machine Learning?"):

    ### Taking input from the user and printing it
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    ### Initializing LLM

    llm=ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant", 
        streaming = True
    )

    ### Tools for AI agent
    tools = [search, arxiv_tool, wiki_tool]

    ## Initializing Agent

    search_agent = initialize_agent(
        tools=tools, 
        llm=llm, 
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handling_parsing_errors = True
    )

    ### assistant’s answer
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant', "content":response})
        st.write(response)