from docx2pdf import convert

docx_path = input("Please enter docx folder/filename.docx path: ")
pdf_path = input("Please enter the destination converted folder/filename.pdf path: ")

convert(docx_path, pdf_path)
