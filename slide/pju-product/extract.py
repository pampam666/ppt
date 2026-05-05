# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pdfplumber",
# ]
# ///
import os
import pdfplumber
from datetime import datetime

base_dir = r"d:\PT DBSN\ppt\slide\pju-product"
attachment_dir = os.path.join(base_dir, "src", "attachment")
product_dir = os.path.join(base_dir, "docs", "product")

os.makedirs(product_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "src", "structure"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "output"), exist_ok=True)

for filename in os.listdir(attachment_dir):
    if filename.lower().endswith(".pdf"):
        filepath = os.path.join(attachment_dir, filename)
        with pdfplumber.open(filepath) as pdf:
            extracted_text = ""
            for i, page in enumerate(pdf.pages):
                extracted_text += f"\n\n## Page {i + 1}\n\n"
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text
                tables = page.extract_tables()
                for j, table in enumerate(tables):
                    extracted_text += f"\n\n### Table {j + 1} (Page {i + 1})\n\n"
                    for row in table:
                        extracted_text += "| " + " | ".join(str(cell or "").replace("\n", " ") for cell in row) + " |\n"
            
            output_filename = os.path.splitext(filename)[0] + ".md"
            output_path = os.path.join(product_dir, output_filename)
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"source_file: {filename}\n")
                f.write(f"extracted_at: {datetime.utcnow().isoformat()}Z\n")
                f.write(f"pages_extracted: {len(pdf.pages)}\n")
                f.write(f"---\n")
                f.write(extracted_text)
        print(f"Extracted {filename}")
