# pdf_loader.py

import os
import pdfplumber

def extract_text_from_pdf(pdf_path):
    extracted_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract plain text
            text = page.extract_text()
            if text:
                extracted_text.append(text)

            # Extract tables and flatten rows into sentences
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row and any(row):
                        sentence = " | ".join([cell.strip() if cell else "" for cell in row])
                        extracted_text.append(f"Table Row: {sentence}")
    return "\n\n".join(extracted_text)

def build_insurance_docs(dataset_dir, output_path):
    all_texts = []
    for filename in os.listdir(dataset_dir):
        if filename.lower().endswith('.pdf'):
            full_path = os.path.join(dataset_dir, filename)
            print(f"Extracting from: {filename}")

            # Add document-level header
            doc_header = f"## SOURCE: {filename}\n"
            text = extract_text_from_pdf(full_path)

            combined_text = doc_header + text
            all_texts.append(combined_text)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(all_texts))

    print(f"\n✅ All PDF text extracted and saved to: {output_path}")


if __name__ == "__main__":
    dataset_path = r"C:\Users\cl502_11\Desktop\Insurance_Aaditya\Dataset"  # Change if needed
    output_txt = "data/insurance_docs.txt"

    os.makedirs("data", exist_ok=True)  # Make sure 'data/' exists
    build_insurance_docs(dataset_path, output_txt)
