from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):

    messages: Annotated[Sequence[BaseMessage], add_messages]
    sender: str
    execution_logs: Annotated[Sequence[str], operator.add]
    error_count: int