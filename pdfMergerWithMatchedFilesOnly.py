import sys
import os
import PyPDF2

def retFirstPageOfPdf_1(inputFileName) -> PyPDF2.PdfReader.pages:
    #Open PDF file and read the first page and write it as different PDF
    print('Start of Process')
    pdfFH = open(inputFileName, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFH)
    pageObj = pdfReader.pages[0]
    pdfWriter = PyPDF2.PdfWriter()
    pdfWriter.add_page(pageObj)
    with open("output.pdf", 'wb') as pdfWFh:
      pdfWriter.write(pdfWFh)

    print(inputFileName)
    pass

def retFirstPageOfPdf(inputFileName, pageNumber = 0) -> PyPDF2.PdfReader.pages:
    #Open PDF file and read the first page and write it as different PDF
    print('Start of Process: ' + inputFileName  + ' ......' + str(pageNumber))
    print(inputFileName)
    print(type(inputFileName))
    pdfFH = open(str(inputFileName), "rb")
    pdfReader = PyPDF2.PdfReader(pdfFH)
    pageObj = pdfReader.pages[pageNumber]
    #Add Error handling and try catch block around this code to catch issues
    return pageObj
    
def retListOfFilesInADir(inputPath):
    listOfPdfFiles = []
    for dirpath, dirs, files in sorted(os.walk(inputPath)):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                listOfPdfFiles.append(os.path.join(dirpath, filename))
    return listOfPdfFiles            

if __name__ == "__main__":
# Driver code
    print(sys.argv[1], sys.argv[2])
    # Get list of files from input dir1
    inputList1 = retListOfFilesInADir(sys.argv[1])
    # print(inputList1)
    # Get list of files form input dir2
    inputList2 = retListOfFilesInADir(sys.argv[2])
    # print(inputList2)

    unmatchedItems = []
    for i in inputList1:
      matched = 0
      for j in inputList2:
        if i.split('\\')[5].split('-')[0] == j.split('\\')[5].split('-')[0]: 
           #print(i)
           matched = 1
      if ( matched != 1):
         unmatchedItems.append(i)
         inputList1.remove(i)
        
    for i in inputList2:
      matched = 0
      for j in inputList1:
        if i.split('\\')[5].split('-')[0] == j.split('\\')[5].split('-')[0]: 
           #print(i)
           matched = 1
      if ( matched != 1):
         unmatchedItems.append(i)
         inputList2.remove(i)

    print(unmatchedItems) 
    print(len(inputList1))
    print(len(inputList2))
    print(len(unmatchedItems))

    # Merge both input lists
    listOfPdfFiles_1 = zip(inputList1, inputList2)
    
    print(' # '*20)
    print(type(listOfPdfFiles_1))
    pdfWriter = PyPDF2.PdfWriter()
    pageIndex = 0
    for files in listOfPdfFiles_1:
      for file in files:
        print("----------------------------------------")
        print(file)  
        page1 = retFirstPageOfPdf(file, pageIndex % 2)
        pdfWriter.add_page(page1)
        pageIndex = pageIndex + 1
    with open("output.pdf", 'wb') as pdfWFh:  
       pdfWriter.write(pdfWFh)
