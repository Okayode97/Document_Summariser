import os
import argparse
from openai import OpenAI


# get openai api key from enviroment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# following steps from OpenAI quickstart
# load the document
file = client.files.create(
    file=open(r"C:\workspace\Projects\Document_Summariser\frank-a5.pdf", "rb"),
    purpose="user_data",
    expires_after={
        "anchor": "created_at",
        "seconds": 2592000 # deletes the file after 30 days
    }
)

response = client.responses.create(
    model="gpt-4.1-nano",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "Can you provide a clear and concise summary on the contents of the uploaded file."
                }
            ]
        }
    ]
)

# delete the file after it's been uploaded and summarised
client.files.delete(file.id)
