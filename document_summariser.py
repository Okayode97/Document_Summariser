import argparse
import os
from openai import OpenAI
from pathlib import Path
from abc import ABC, abstractmethod

SUPPORTED_FILE_TYPES = [".pdf", ".txt", ".word", ".py", ".md"]

class LLMModelBackend(ABC):
    @abstractmethod
    def summarise_document(self):
        pass

class OpenAISummariser(LLMModelBackend):
    
    def __init__(self):
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        if OPENAI_API_KEY is None:
            raise ValueError("OPENAI_API_KEY is not defined in local environment. Set API key to continue.")
        self.client = OpenAI(api_key=OPENAI_API_KEY)
    
    def load_pdf_file(self, document_path: Path):
        pass

class LLMDocumentSummariser:

    def __init__(self):
        self.model_summariser = OpenAISummariser()
        pass

    def summarise_document(self, document_path: Path):

        if not (document_path.suffix in SUPPORTED_FILE_TYPES):
            raise ValueError(f"Unsupported document type uploaded.\nSupported file types are {SUPPORTED_FILE_TYPES} and uploaded file `{document_path.name}`")
        
        # determine file type


        # modify how call to summarise model is made based on file type



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarise contents of loaded document")
    parser.add_argument('doc_path', type=str,
                        help=f"Path to document, to be uploaded and summarised. Currently supported documents are {SUPPORTED_FILE_TYPES}")

    args = parser.parse_args()
    llm_doc_summariser = LLMDocumentSummariser()
    llm_doc_summariser.summarise_document(Path(args.doc_path))