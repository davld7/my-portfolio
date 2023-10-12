from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter(prefix="/about", tags=["about"])


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def about() -> FileResponse:
    """
    Get the about.html template.

    Parameters:
    - `None`.

    Returns:
    - `HTMLResponse`: The about.html template.

    Raises:
    - `None`.
    """
    path = "templates/about.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)


@router.get("/me.png", response_class=FileResponse, status_code=status.HTTP_200_OK)
async def me() -> FileResponse:
    """"
    Get the me.png file.

    Parameters:
    - `None`.

    Returns:
    - `FileResponse`: The me.png file.

    Raises:
    - `None`.
    """
    path = "static/images/me.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)
