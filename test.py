#AIzaSyD5ENeoFEJtPhgZ3-WVA-ucwv95QOmhRno

from google import genai
with open("/Users/faiththomas/Desktop/Portfolio Project 1/api_key.txt", "r") as file:
    api_key = file.read().strip()
client = genai.Client(api_key=api_key)

#step 1, give LLM specifc instructions
# where you tell the LLM what it does
llm_instructions = """Here is a list of ingredients, give me some yummy recipes
with these specific ingredients, dont add anything not in the list.""" #easy 

#step 2, get user input
# this is where you do the ingredients 
user_input = input("Give me a list of ingredients you have: ") #how do you get user input? 

prompt_for_LLM = llm_instructions + user_input #fixme
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=f"{prompt_for_LLM}"
)

print(response.text)