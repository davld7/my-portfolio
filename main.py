from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, FileResponse
from routers import projects, about, contact

app = FastAPI()
app.title = "My Portfolio"
app.include_router(projects.router)
app.include_router(about.router)
app.include_router(contact.router)


@app.get("/", tags=["Index"], response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index() -> FileResponse:
    """
    Get the index.html template.

    Parameters:
    - `None`.

    Returns:
    - `FileResponse`: The index.html template.

    Raises:
    - `None`.
    """
    path = "templates/index.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)


@app.get("/styles.css", tags=["Index"], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def styles() -> FileResponse:
    """
    Get the styles.css file.

    Parameters:
    - `None`.

    Returns:
    - `FileResponse`: The styles.css file.

    Raises:
    - `None`.
    """
    path = "static/css/styles.css"
    media_type = "text/css"
    return FileResponse(path=path, media_type=media_type)


@app.get("/script.js", tags=["Index"], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def script() -> FileResponse:
    """
    Get the script.js file.

    Parameters:
    - `None`.

    Returns:
    - `FileResponse`: The script.js file.

    Raises:
    - `None`.
    """
    path = "static/js/script.js"
    media_type = "text/javascript"
    return FileResponse(path=path, media_type=media_type)


@app.get("/favicon.ico", tags=['Index'], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def favicon() -> FileResponse:
    """
    Get the favicon image.

    Parameters:
    - `None`.

    Returns:
    - `FileResponse`: The favicon image.

    Raises:
    - `None`.
    """
    path = "static/images/favicon.ico"
    media_type = "image/x-icon"
    return FileResponse(path=path, media_type=media_type)


@app.get("/user-interface.png", tags=['Index'], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def user_interface() -> FileResponse:
    """
    Get the user interface image.

    Parameters:
    - `None`.

    Returns:
    - `FileResponse`: The user interface image.

    Raises:
    - `None`.
    """
    path = "static/images/user-interface.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)
