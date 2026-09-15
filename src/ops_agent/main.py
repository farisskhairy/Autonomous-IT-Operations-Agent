from langchain_core.messages import HumanMessage
from ops_agent.agent.graph import graph

if __name__ == "__main__":
    initial_state = {"messages": [HumanMessage(content="Can you check if port 443 is open on github.com, and then check if the website https://github.com is returning a healthy HTTP status?")]}

    result = graph.invoke(initial_state)

    print(result["messages"][-1].content)