from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter(prefix="/about", tags=["about"])


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def about():
    template_path = "templates/about.html"
    media_type = "text/html"
    return FileResponse(template_path, media_type=media_type)
