from langchain_openai import ChatOpenAI
from .state import AgentState
from ops_agent.tools.network import ping_host
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools([ping_host])

def agent_node(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])

    return {"messages": [response], "sender": "agent"}

tool_node = ToolNode([ping_host])

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()