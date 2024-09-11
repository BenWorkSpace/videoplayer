from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Welcome to the Video Player API"}

default_quality = 1080
qualities = [
    "1080p",
    "720p",
    "480p",
    "360p",
    "240p",
    "144p",
]

@app.get("/watch/", response_class=HTMLResponse)
async def watch_video(request: Request, urls: str):
    urls = urls.split(",")
    video_urls = { 
        qualities[i]: urls[i] for i in range(len(urls))
    }

    return templates.TemplateResponse("watch.html", {
        "request": request,
        "video_urls": video_urls,
        "default_quality": default_quality
    })
