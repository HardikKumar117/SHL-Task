from langchain_groq import ChatGroq
from utils.format import HiringRequirements
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


llm = ChatGroq(
    model="openai/gpt-oss-120b"

)

structured_llm = llm.with_structured_output(
    HiringRequirements
)
def extract_hiring_requirements(text: str):
    """
    Extracts hiring requirements from the given chatbot-human conversation using the structured LLM.
    
    Args:
        text (str): The input text containing hiring information."""
    EXTRACTION_PROMPT = """
You are an information extraction system.

Extract hiring requirements from the conversation.

Do NOT answer the user.
Do NOT continue the conversation.
Do NOT recommend assessments.

Return only structured data.

Conversation:

{conversation}
"""
    result=structured_llm.invoke(
        EXTRACTION_PROMPT.format(
            conversation=text
        )
    )
    return result

def build_query(text:HiringRequirements):
    """
    Builds a query based on the given text using the structured LLM.
    
    Args:
        text (HiringRequirements): The structured hiring requirements for query building."""
    prompt = f"""
    You are helping retrieve SHL assessments.

    Given these hiring requirements:

    {text.model_dump_json()}

    Generate a short semantic search query
    for retrieving relevant SHL assessments
    from a vector database.

    Return ONLY the query text.

    Do not generate SQL.
    Do not generate explanations.
    Do not generate recommendations.
    """
    result=llm.invoke(
        prompt)
    return result.content