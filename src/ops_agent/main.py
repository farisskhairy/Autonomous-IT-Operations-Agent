from langchain_core.messages import HumanMessage
from ops_agent.agent.graph import graph

if __name__ == "__main__":
    initial_state = {"messages": [HumanMessage(content="Can you ping 8.8.8.8 for me?")]}

    result = graph.invoke(initial_state)

    print(result["messages"][-1].content)