from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain_core.runnables import RunnableConfig
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.memory import ConversationBufferMemory

def search_response(memory,prompt="Sample"):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True)
    tools = [DuckDuckGoSearchRun(name="Search")]
    chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)

    search_memory = ConversationBufferMemory(
                    chat_memory=memory.chat_memory, 
                    return_messages=True, 
                    memory_key="chat_history", 
                    output_key="output"
                )

    executor = AgentExecutor.from_agent_and_tools(
        agent=chat_agent,
        tools=tools,
        memory=search_memory,
        return_intermediate_steps=True,
        handle_parsing_errors=True,
    )
    print(memory)
    return executor
# .invoke({
#         "input":prompt
#         })['output']