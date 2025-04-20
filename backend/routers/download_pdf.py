from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/download-summary")
def download_summary(
    pdf_filename: str = Query(..., title="PDF File", regex=r'^[\w\-. ]+\.pdf$', description="PDF file name to download")
):
    print("Received filename:", pdf_filename)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    APP_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
    PDF_DIR = os.path.join(APP_DIR, "pdfhub")
    pdf_path = os.path.join(PDF_DIR, pdf_filename)

    print("Full PDF path:", pdf_path)
    
    if not os.path.exists(pdf_path):
        print("File not found!")
        raise HTTPException(status_code=404, detail="PDF not found")

    return FileResponse(pdf_path, media_type="application/pdf", filename=pdf_filename)
