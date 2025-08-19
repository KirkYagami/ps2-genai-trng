from langchain import hub
from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


# llm = ChatOpenAI(temperature=0)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)


prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()
