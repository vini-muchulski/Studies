import comtypes.client

def convert_ppt_to_pdf(input_path, output_path):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = True

    ppt_file = powerpoint.Presentations.Open(input_path)
    ppt_file.SaveAs(output_path, FileFormat=32)  # FileFormat 32 representa PDF
    ppt_file.Close()

    powerpoint.Quit()

# Exemplo de uso:
pptx_path = r"D:\Codigos\Py\hashtag projects\power_point\ai_test\aula3.pptx"
pdf_path = r"D:\Codigos\Py\hashtag projects\power_point\ai_test\aula3.pdf"

convert_ppt_to_pdf(pptx_path, pdf_path)