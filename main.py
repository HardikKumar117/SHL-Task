from docs_builder import build_docs
from Vector_store import build_vector_store
from utils.functions import extract_hiring_requirements, build_query
from langchain_core.messages import HumanMessage

from agent import Agent



def main(conv:str):
    print("building docs")
    docs=build_docs()
    print("building vector store")
    collection=build_vector_store(docs)
   
    info= extract_hiring_requirements(conv)
    print("built requirements")
    query=build_query(info)
    print("invoking agent ")
    agent_response = Agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=f"""
    Conversation History:

    {conv}

    Extracted Requirements:

    {info.model_dump_json(indent=2)}
    """
                )
            ]
        }
    )
    print(agent_response)
    return agent_response


# if __name__ == "__main__":
#     main("""{
#   "messages": [
#     {
#       "role": "user",
#       "content": "We need a solution for senior leadership."
#     },
#     {
#       "role": "assistant",
#       "content": "Who is this intended for?"
#     },
#     {
#       "role": "user",
#       "content": "CXOs and directors with 15+ years experience."
#     }
#   ]
# }""")