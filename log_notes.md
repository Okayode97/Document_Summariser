# Document Summariser Log of events

22/12/2025


26/12/2025
- Read through File Inputs page

from notes on file input the model can accept PDF files as input.
The PDF files are provided as either Base64-encoded data or as file IDs obtained after uploading the files to the v1/files endpoint via the API or dashboard. In terms of extracting data and knowledge from the PDF content. Images of each page and the extracted text are used by the model to generate a response. w.r.t to using file input, only models that support text & image inputs can accept PDF files as input. This is currently limited to just gpt-4o, gpt-4o-mini, o1. W.r.t to file size. the size of individual files can be up to 512MB and the total size of the file uploaded by one account can be up to 1TB. looking through the API doc it seems that OI stores all the individual files that are uploaded during each test (Only files with purpose=batch are deleted after 30 days for others they persist until they are deleted.) Further update, you can also delete the uploaded file via the API endpoint.