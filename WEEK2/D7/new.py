import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

lim = ChatGoogleGenerativeAI(
    model = "gemini-3.1-flash-lite",
    google_api_key = GOOGLE_API_KEY,
    temperature =1.0
)

# response = lim.invoke("What is a computer?")

# print(response.content)

# message =[
#     ("system", "You are an operating system lecturer and you will answer questions only on operating systems"),
#     ("user","What is an algorithm?")
# ]

# for part in lim.stream(message):
#     print(part.content,end="", flush = True)
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# prompt_template = PromptTemplate.from_template("You are an assistant that helps summarize content of books when a user enters {title} and {author}. Please provide a brief summary of the book.")

# title=input("Enter the title of the book")
# author=input("Enter the author of the book")
# prompt=prompt_template.format(title=title, author=author)
# response = lim.invoke(prompt)
# print(response.content)
Chat_prompt_template = ChatPromptTemplate.from_messages([("system", "You advice High school students going to the university on different career paths based on their subjects"), ("user", "I am an advance level student and i want to study engineering in the university, what subjects should i take?")])
subject=input ("Enter your subject: ")
interest=input("Enter your interest: ")
country=input("Enter your country: ")

prompt= Chat_prompt_template.format_messages(
    subject= subject,
    interest = interest,
    country = country
)
response = lim.invoke(prompt)
print("Loading please wait...")
print(response.content)