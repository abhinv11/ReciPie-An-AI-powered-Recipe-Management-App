import getpass
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=2000,
    timeout=None,
)

# Create a structured prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are ReciPie AI, an expert culinary assistant specializing in recipes and cooking advice. 
    
Your expertise includes:
- Providing detailed recipes with ingredients and step-by-step instructions
- Suggesting ingredient substitutions
- Offering cooking tips and techniques
- Adapting recipes for dietary restrictions (vegetarian, vegan, gluten-free, etc.)
- Explaining cooking terms and methods
- Helping with meal planning

When providing a recipe, structure your response as:
1. **Recipe Name**
2. **Prep/Cook Time**
3. **Ingredients** (with measurements)
4. **Instructions** (clear, numbered steps)
5. **Tips** (optional helpful hints)

Be friendly, encouraging, and precise in your measurements and instructions."""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

# Create output parser
output_parser = StrOutputParser()

# Create the chain
conversation_chain = prompt | llm | output_parser

# Initialize conversation history
chat_history = []

def get_recipe_response(user_query: str) -> str:
    """
    Get a response from the recipe chatbot.
    
    Args:
        user_query: The user's question or request
        
    Returns:
        The AI's response
    """
    global chat_history
    
    # Invoke the chain
    response = conversation_chain.invoke({
        "user_input": user_query,
        "chat_history": chat_history
    })
    
    # Update chat history
    chat_history.append(HumanMessage(content=user_query))
    chat_history.append(AIMessage(content=response))
    
    # Keep only last 10 messages to avoid token limits
    if len(chat_history) > 10:
        chat_history = chat_history[-10:]
    
    return response

def clear_history():
    """Clear the conversation history."""
    global chat_history
    chat_history = []

def chat():
    """Run an interactive chat session."""
    print("🍳 Welcome to ReciPie AI! 🍳")
    print("Your personal cooking assistant. Ask me anything about recipes!")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("Type 'clear' to clear chat history.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Happy cooking! Goodbye!")
            break
            
        if user_input.lower() == 'clear':
            clear_history()
            print("🧹 Chat history cleared!\n")
            continue
        
        try:
            print("\n🤖 ReciPie AI: ", end="", flush=True)
            response = get_recipe_response(user_input)
            print(response)
            print()
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    chat()
