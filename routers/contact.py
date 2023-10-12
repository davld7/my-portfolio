from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter(prefix="/contact", tags=["contact"])


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def contact() -> FileResponse:
    """
    Get the contact.html template.

    Parameters:
    - `None`.

    Returns:
    - `HTMLResponse`: The contact.html template.

    Raises:
    - `None`.
    """
    path = "templates/contact.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)
