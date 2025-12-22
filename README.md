# Document_Summariser

This project aims to develop a tool to analyse documents or large body of texts. The developed tools should have the following capabilities.

- From it's initial analysis, it should provide a summary of the contents of the document.
- In the provided summary highlight any issue that might be of concern to the user.
- It should provide reference to the original document, to support any response given to the user, this is done to ensure that it's not hallucinating in it's response.
- The user should be able to ask further questions regarding the contents of the uploaded document.

In terms of performance,
- The returned responses should be accurate, concise, clear and grounded based on the original contents of the text.

The above are the capabilities and performance i can think of at the start, i'll update it as needed.

## Suggested Plan for Document Summariser
- Start with simple prompting
    - Build basic summarizer using available API or frameworks to parse document to LLM models.
    - Add document parsing to account for limited context window.

- Add RAG when context limits is reached.
    - Implement RAG (Using vector DB, chunking strategies, retrieval)
    - Add in evaluation metrics and experiment with different models.
    - Add in fine tunning if generic models doesn't work.

- Add Agents/MCP or anything else.

- Deploy the tool
    - Deploy the tool and add in user features to allow for personalisation with the tool.

The suggested plan is not concentre and could change or be adapated as needed.
