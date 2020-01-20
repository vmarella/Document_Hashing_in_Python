import PyPDF2
import hashlib

pdf_file = open(r'location of the file in the computer','rb')
# File Location should be passed

page_content = ""
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
for i in range(0,number_of_pages-1):
    page = read_pdf.getPage(0)
    page_content += page.extractText()
print(page_content)

hash_object = hashlib.sha256(page_content.encode())
#Getting the Hash of the document

print(hash_object.hexdigest())
