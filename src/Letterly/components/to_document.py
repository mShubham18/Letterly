from docx import Document
def create_docx(text, file_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(file_path)


def download_file(file_path):
    with open(file_path, "rb") as f:
        return f.read()