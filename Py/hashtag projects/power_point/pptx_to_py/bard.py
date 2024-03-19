from pptx import Presentation
import os

def pptx_to_pdf_python_pptx(pptx_path, pdf_path):
    prs = Presentation(pptx_path)
    prs.save(pdf_path)  # No need for the 'format' argument

# Example usage
pptx_path = r"D:\Codigos\Py\hashtag projects\power_point\ai_test\aula3.pptx"
pdf_path = r"D:\Codigos\Py\hashtag projects\power_point\ai_test\aula3.pdf"
pptx_to_pdf_python_pptx(pptx_path, pdf_path)