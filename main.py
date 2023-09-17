from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import Response

# Set maximum file size to 100 MB
MAX_FILE_SIZE = 100 * 1024 * 1024

# Set allowed file extensions. 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'ico', 'svg', 'bmp', 'webp', 'tiff', 'psd'}


# Route to upload file 
@app.post("/cdn/v1/uploadfile/")
async def upload_file(file: UploadFile):
    """
    Upload a file to the CDN.

    - **file**: The file to upload.

    Returns:
    - **message**: A success message if the file was uploaded successfully.
    - **error**: An error message if the file could not be uploaded.
    """
    try:
        content = await file.read()

        # Check file size
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(status_code=413, detail="File too large")
        
        # Check file extension
        if not file.filename.endswith(tuple(ALLOWED_EXTENSIONS)):
            raise HTTPException(status_code=400, detail="File type not allowed")

        # Check if filename already exists
        if drive.get(file.filename):
            return {"error": "File already exists"}
        
        # Save uploaded file to Deta Drive 
        name = file.filename
        drive.put(name, content)

        # get file type
        file_type = file.filename.split('.')[-1]

        # Return success message to client
        return {"filename": name, "type": file_type, "message": "File uploaded successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))