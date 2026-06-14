from app.processors.document_processor import (
    DocumentProcessor
)

processor = DocumentProcessor()

result = processor.process(
    "data/raw/sample.pdf"
)

print("\nMETADATA\n")
print(result["metadata"])

print("\nNUMBER OF CHUNKS\n")
print(len(result["chunks"]))

print("\nFIRST CHUNK\n")
print(result["chunks"][0])