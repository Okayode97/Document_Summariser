import argparse
import os
from openai import OpenAI
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Dict


PROMPT = """
Can you read through the uploaded document and respond with a concise and clear summary of the document, with the expectation that more questions would be asked about the contents of the document.
In your response as well can you answer the questions listed below.
- What is the first line in page 129
"""
SUPPORTED_FILE_TYPES = [".pdf", ".txt", ".py", ".md"]


class LLMModelBackend(ABC):
    @abstractmethod
    def summarise_document(self, path: Path, prompt: str):
        pass


class OpenAIBackend(LLMModelBackend):
    
    def __init__(self):
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        if OPENAI_API_KEY is None:
            raise ValueError("OPENAI_API_KEY is not defined in local environment. Set API key to continue.")
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = "gpt-4.1-nano"
    
    def summarise_document(self, document_path: Path, prompt: str):        
        if document_path.suffix == ".pdf":
            extracted_contents_dict = self.handle_pdf_document(document_path, prompt)
        
        if document_path.suffix in [".txt", ".py", ".md"]:
            extracted_contents_dict = self.handle_text_document(document_path, prompt)
    
        # get chat to summarise the contents of the model
        response = self.client.responses.create(model=self.model,
            input=[
                {
                    "role": "user",
                    "content": [
                        extracted_contents_dict,
                        {
                            "type": "input_text",
                            "text": f"File type: {document_path.suffix}"
                        },
                        {
                            "type": "input_text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )
        print(f"Generated Response: {response.output_text}")

        if document_path.suffix == ".pdf":
            assert "file_id" in extracted_contents_dict
            self.client.files.delete(extracted_contents_dict["file_id"])

    def handle_pdf_document(self, document_path: Path, prompt: str) -> Dict:
        # upload the pdf file to openai
        file = self.client.files.create(file=open(str(document_path), "rb"), purpose="user_data",
            expires_after={"anchor": "created_at", "seconds": 2592000}) # deletes the file after 30 days

        return {"type": "input_file", "file_id": file.id}

    def handle_text_document(self, document_path: Path, prompt: str) -> Dict:
        # open the file and read it's contents
        with open(document_path, "r", encoding="utf-8") as f:
            extracted_text = f.read()

        return {"type": "input_text", "text": f"Document contents.\n\n{extracted_text}"}


class LLMDocumentSummariser:

    def __init__(self):
        self.model_summariser = OpenAIBackend()
        self.prompt = PROMPT

    def summarise_document(self, document_path: Path):

        if not (document_path.suffix in SUPPORTED_FILE_TYPES):
            raise ValueError(f"Unsupported document type uploaded.\nSupported file types are {SUPPORTED_FILE_TYPES} and uploaded file `{document_path.name}`")
        
        # call the summarise document function
        # - model summariser class would have handlers for different file types
        self.model_summariser.summarise_document(document_path, self.prompt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarise contents of loaded document")
    parser.add_argument('doc_path', type=str,
                        help=f"Path to document, to be uploaded and summarised. Currently supported documents are {SUPPORTED_FILE_TYPES}")

    args = parser.parse_args()
    llm_doc_summariser = LLMDocumentSummariser()
    llm_doc_summariser.summarise_document(Path(args.doc_path))