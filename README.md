# Generative AI Self-Introduction App

Welcome to the Generative AI Self-Introduction App! This project allows users to interact with a language model trained on a text file containing a narrative about my life. Users can run the app on their localhost, ask questions, and receive relevant and dynamically generated answers from the model.

## Project Components

1. **LangChain:**
   - LangChain is utilized for the Language Model (LLM) aspect of the project. It provides a powerful framework for working with natural language processing tasks.

2. **OpenAI API:**
   - OpenAI is integrated into the project to support API interactions. The OpenAI API facilitates advanced language generation and comprehension capabilities.

3. **StreamLit:**
   - StreamLit is employed to create a user-friendly graphical user interface (GUI). This allows users to seamlessly interact with the application and receive responses from the generative model.

## How to Run the Project

Follow these steps to run the project on your localhost:

1. Open Terminal.
2. Navigate to the folder containing the `chat.py` file.
3. Ensure all dependencies are installed. If not, install them using the following command:
   ```bash
   pip install streamlit langchain openai wikipedia chromadb tiktoken

Note: If encountering issues with StreamLit, use version 1.24.0 by running:

    
    pip install streamlit==1.24.0
1. After installation, run the following command:
    
        streamlit run chat.py

2. The model will take a few seconds to learn from the provided information. Once completed, a text input box will appear, allowing you to type any questions for the model to generate responses.

## Additional Information

This project is designed to provide users with an interactive experience to learn more about the creator's life. The integration of LangChain and OpenAI ensures sophisticated language interactions, while StreamLit enhances the overall user interface.



