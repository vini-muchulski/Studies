import os
import comtypes.client

def pptx_to_pdf_com(pptx_path, pdf_path):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if os.path.isabs(pptx_path):
        abs_pptx_path = pptx_path
    else:
        abs_pptx_path = os.path.abspath(pptx_path)

    deck = powerpoint.Presentations.Open(abs_pptx_path)
    deck.SaveAs(pdf_path, 32)  # 32 corresponds to the PDF format
    deck.Close()
    powerpoint.Quit()

pptx_path = r"D:\Codigos\Py\hashtag projects\power_point\ai_test\aula4.pptx"
pdf_path = r"D:\Codigos\Py\hashtag projects\power_point\ai_test\aula4.pdf"
pptx_to_pdf_com(pptx_path, pdf_path)
