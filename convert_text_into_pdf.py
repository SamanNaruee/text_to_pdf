from fpdf import FPDF


def file_name_converter(file_path):
    file_name = file_path.split('/')[-1]
    
    if file_name.endswith('.srt'):
        return f"{file_path}/{file_name.replace('.srt', '.txt')}"
    else:
        raise ValueError("File must be a .srt file")


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
    


text_dir = str(input("Enter the text file path: "))
text = read_text_from_file(text_dir)

filename = "Converted.pdf"
create_pdf(text, filename)
print(f"PDF created successfully: {filename}")

print(file_name_converter("C:/Users/admin/Downloads/The.Sixth.Sense-en.srt"))