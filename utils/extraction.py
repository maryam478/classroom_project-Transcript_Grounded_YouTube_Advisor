from docling.document_converter import DocumentConverter
import json
# pdf parsing
source = "https://arxiv.org/pdf/2408.09869"

# Initialize converter (enable OCR if PDF is scanned images)
converter = DocumentConverter()

# Load and convert the PDF
doc = converter.convert(source)
source = doc.document

# TO MARKDOWN
with open("../data/converted_to_markdown.md", "w", encoding="utf-8") as f:
    f.write(source.export_to_markdown())
    
# TO JSON
with open("../data/json_converted.json", "w", encoding="utf-8") as f:
    json.dump(source.export_to_dict(), f, indent=2, ensure_ascii=False)
    
# TO HTML
with open("../data/html_converted.md", "w", encoding="utf-8") as f:
    f.write(source.export_to_html())
    
    
# WEBSITE PARSING
source2 = converter.convert('https://docling-project.github.io/docling/')
web_source = source2.document

with open("../data/website_parse_to_md.md", "w", encoding="utf-8") as f:
    f.write(web_source.export_to_markdown())