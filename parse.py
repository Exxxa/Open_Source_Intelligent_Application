from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Initialize the Ollama LLM
model = OllamaLLM(model="llama3.2")


def parse_with_ollama(parse_description, dom_content):
    """
    Parses the given DOM content using the Ollama model with the provided description.
    """
    # Construct a prompt to pass to the LLM
    prompt = (
        f"You are a helpful assistant. Here's some scraped content:\n\n"
        f"{dom_content}\n\n"
        f"Now, based on the following description, extract or process the requested information:\n\n"
        f"{parse_description}\n\n"
        f"Provide a concise and clear response."
    )
    
    # Call the model with the prompt
    results = model(prompt)
    
    return results
