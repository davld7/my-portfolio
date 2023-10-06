from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def projects():
    template_path = "templates/projects.html"
    media_type = "text/html"
    return FileResponse(template_path, media_type=media_type)
