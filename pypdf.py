import csv
import PyPDF2
import re

def extract_data_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    extracted_data = []

    # Extract data from page 1
    page1_text = pdf_reader.pages[0].extract_text()
    number_match = re.search(r'N° (\d+)', page1_text)
    print(number_match)
    if number_match:
        extracted_data.append(number_match.group(1))

    # Extract data from page 3
    page3_text = pdf_reader.pages[2].extract_text()
    extracted_data.append(page3_text)

    pdf_file.close()

    return extracted_data


def save_data_to_csv(data, csv_path):
    
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

pdf_path = './Contract.pdf'
csv_path = './Contracts.csv'

data = extract_data_from_pdf(pdf_path)
save_data_to_csv(data, csv_path)