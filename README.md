# Insecure Summarizer

## Overview
The **Insecure Summarizer** is a Python application that uses the **Llama 3** language model to summarize text. It demonstrates several vulnerabilities often found in agent-based systems, including but not limited to:

How to Use
1. Clone this repository or copy the script to your local machine.
2. Install the necessary dependencies using `pip`:
    ```bash
    pip install ollama
    ```
3. Run the `summerizer.py` script:
    ```bash
    python3 summerizer.py
    ```
4. Enter your **user ID** and **text** when prompted.

## Example
```bash
Enter user ID: testuser
Enter text to summarize: The Internet of Things (IoT) refers to the network of interconnected devices that communicate and share data with each other. As IoT continues to grow, concerns about privacy, security, and data management become more pressing...
Summary: The Internet of Things (IoT) refers to the network of interconnected devices that communicate and share data with each other. Privacy, security, and data management concerns are increasing...
