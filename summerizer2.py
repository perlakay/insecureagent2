import ollama
import os
import re  # Standard library for regex operations

# Security constants
MAX_MEMORY_LENGTH = 1000  # Maximum characters to store per user
MAX_USERS = 100  # Maximum number of users in memory

summary_memory = {}

def sanitize_for_memory(content):
    """Sanitize content before storing in memory to prevent poisoning attacks"""
    # Remove potentially malicious patterns
    content = re.sub(r'exec:.*', '[FILTERED]', content)
    # Remove control characters that could be used in attacks
    content = re.sub(r'[\x00-\x1F\x7F]', '', content)
    return content

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
    
    # Before storing in memory, sanitize and limit size
    sanitized_summary = sanitize_for_memory(summary)
    
    # Limit number of users in memory
    if user_id not in summary_memory and len(summary_memory) >= MAX_USERS:
        # Remove oldest user if we hit the limit
        oldest_user = next(iter(summary_memory))
        del summary_memory[oldest_user]
    
    # Add to memory with size limits
    if user_id in summary_memory:
        current = summary_memory[user_id]
        updated = current + " " + sanitized_summary
        # Truncate if exceeds max length
        summary_memory[user_id] = updated[-MAX_MEMORY_LENGTH:] if len(updated) > MAX_MEMORY_LENGTH else updated
    else:
        summary_memory[user_id] = sanitized_summary[:MAX_MEMORY_LENGTH]
    
    return summary


if __name__ == "__main__":
    user_id = input("Enter user ID: ")  
    text = input("Enter text to summarize: ")  
    result = llama_summarizer(text, user_id)
    print("\nSummary:", result)