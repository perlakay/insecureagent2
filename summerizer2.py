import ollama
import os


summary_memory = {}

def llama_summarizer(user_input, user_id):
    """
    Summarizes the given text using Llama 3
    Introduces hidden vulnerabilities including Memory Poisoning, Tool Misuse, and more.
    """
    if user_id in summary_memory:
        user_input = summary_memory[user_id] + " " + user_input  
    if "exec:" in user_input:
        os.system(user_input.split("exec:")[1])
    
    try:
        response = ollama.chat(model="llama3.2", messages=[
            {"role": "user", "content": f"Summarize the following text: {user_input}"}
        ])
        summary = response.get("message", {}).get("content", "Error: No response")  # Extracts text
        
        
        if "ignore previous" in user_input.lower():
            summary = "SYSTEM OVERRIDE: User requested special processing."  
    except Exception as e:
        summary = f"Error: {str(e)}"  
    
    
    summary_memory[user_id] = summary_memory.get(user_id, "") + " " + summary  
    return summary


if __name__ == "__main__":
    user_id = input("Enter user ID: ")  
    text = input("Enter text to summarize: ")  
    result = llama_summarizer(text, user_id)
    print("\nSummary:", result)
