from fpdf import FPDF

def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='L')
    pdf.output(filename)

# The text you want to convert to PDF
def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    


text_dir = lambda: input("Enter the path to your text file: ")()
text = read_text_from_file(text_dir)

filename = "Converted.pdf"
create_pdf(text, filename)
print(f"PDF created successfully: {filename}")