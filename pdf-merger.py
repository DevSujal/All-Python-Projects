import PyPDF2

# taking pdf as input in the array
pdfArray = ["C:/java/oop exp-5.pdf", "C:/java/oop exp-6.pdf", "C:/java/oop exp-7.pdf"]

merger = PyPDF2.PdfMerger() 
for pdf in pdfArray:    #jab tak pdf khatam nahi hoti ye tab tak chalega 

    with open(pdf, "rb") as pdf1: #it auto closes the file by using with 
        pdfReader = PyPDF2.PdfReader(pdf1)
        merger.append(pdfReader)
        
merger.write("newMerged.pdf") 
