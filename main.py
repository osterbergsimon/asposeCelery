import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

from tasks import *


if __name__ == "__main__":
    test_aspose_cells.delay("test_files/TestSpreadsheet.xlsx")
    test_aspose_diagram.delay("test_files/TestDrawing.vsdx")
    test_aspose_pdf.delay("test_files/TestPDF.pdf")
    test_aspose_slides.delay("test_files/TestPresentation.pptx")
    task = test_aspose_words.delay("test_files/TestDocument.docx")
