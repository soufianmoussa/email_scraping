import fitz  # PyMuPDF
import re
import csv

# Function to extract email addresses from text
def extract_emails(text):
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails

# Function to extract text from a PDF file using PdfReader
def extract_text_from_pdf(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text

# Function to write emails to a CSV file
def write_emails_to_csv(emails, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Emails'])
        for email in emails:
            writer.writerow([email])

# Example usage
pdf_path = 'test.pdf'  # Replace with the path to your PDF file
csv_filename = 'emails.csv'  # Replace with the desired CSV file name

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Extract emails from text
emails = extract_emails(pdf_text)

# Write emails to CSV file
write_emails_to_csv(emails, csv_filename)

print("Emails have been extracted and saved to", csv_filename)