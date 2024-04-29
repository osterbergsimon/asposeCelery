import logging
import traceback

from celery import Celery
from celery.signals import after_setup_logger
from celery.utils.log import get_task_logger
import os

broker = os.getenv("BROKER", "redis://localhost:6379/0")
app = Celery('tasks', broker=broker, backend=broker)
logger = get_task_logger(__name__)

@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add filehandler
    fh = logging.FileHandler('celery-logs.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)


@app.task
def test_aspose_words(file="test_files/TestDocument.docx"):
    logger.info(f"Importing aspose.words")
    import aspose.words as aw
    logger.info(f"Testing Aspose Words with {file}")
    try:
        document = aw.Document(file)
        logger.info("Successfully opened document!")
        out = f"{file}.out.pdf"
        document.save(out)
        logger.info(f"Saved as {out}")
    except Exception:
        logger.exception()
        traceback.print_exc()

@app.task
def test_aspose_slides(file="test_files/TestPresentation.pptx"):
    logger.info(f"Importing Aspose.Slides")
    import aspose.slides as slides
    logger.info(f"Testing Aspose Slides with {file}")
    try:
        presentation = slides.Presentation(file)
        logger.info("Successfully opened presentation!")
        out = f"{file}.out.pdf"
        presentation.save(out, slides.export.SaveFormat.PDF)
        logger.info(f"Saved as {out}")
    except Exception:
        logger.exception()
        traceback.print_exc()


@app.task
def test_aspose_cells(file="test_files/TestSpreadsheet.xlsx"):
    logger.info(f"Importing aspose-cells-python")
    import aspose.cells as cells
    logger.info(f"Testing Aspose Cells with {file}")
    try:
        workbook = cells.Workbook(file)
        logger.info("Successfully opened workbook!")
        out = f"{file}.out.pdf"
        workbook.save(out, cells.SaveFormat.PDF)
        logger.info(f"Saved as {out}")
    except Exception:
        logger.exception()
        traceback.print_exc()

@app.task
def test_aspose_diagram(file="test_files/TestDrawing.vsdx"):
    logger.info(f"Importing aspose-diagram-python")
    import aspose.diagram as diagram
    logger.info(f"Testing Aspose Diagram with {file}")
    try:
        dia = diagram.Diagram(file)
        logger.info("Successfully opened diagram!")
        out = f"{file}.out.pdf"
        dia.save(out, diagram.SaveFileFormat.PDF)
        logger.info(f"Saved as {out}")
    except Exception:
        logger.exception()
        traceback.print_exc()


@app.task
def test_aspose_pdf(file="test_files/TestPDF.pdf"):
    logger.info(f"Importing aspose-pdf")
    import aspose.pdf as pdf
    logger.info(f"Testing Aspose PDF with {file}")
    try:
        document = pdf.Document(file)
        logger.info("Successfully opened PDF Document!")
        out = f"{file}.out.pdf"
        document.save(out)
        logger.info(f"Saved as {out}")
    except Exception:
        logger.exception()
        traceback.print_exc()


