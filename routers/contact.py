from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter(prefix="/contact", tags=["contact"])


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def contact():
    template_path = "templates/contact.html"
    media_type = "text/html"
    return FileResponse(template_path, media_type=media_type)
