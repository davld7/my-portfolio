from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, FileResponse
from routers import projects, about, contact

app = FastAPI()
app.title = "My Portfolio"
app.include_router(projects.router)
app.include_router(about.router)
app.include_router(contact.router)


@app.get("/", tags=["index"], response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index():
    template_path = "templates/index.html"
    media_type = "text/html"
    return FileResponse(template_path, media_type=media_type)


@app.get("/styles.css", tags=["styles"], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def styles():
    template_path = "static/css/styles.css"
    media_type = "text/css"
    return FileResponse(template_path, media_type=media_type)


@app.get("/script.js", tags=["script"], response_class=FileResponse, status_code=status.HTTP_200_OK)
async def script():
    template_path = "static/js/script.js"
    media_type = "text/javascript"
    return FileResponse(template_path, media_type=media_type)


@app.get('/favicon.png', tags=['favicon'], status_code=status.HTTP_200_OK)
async def favicon():
    favicon_path = 'static/images/favicon.png'
    return FileResponse(favicon_path, media_type="image/png")
