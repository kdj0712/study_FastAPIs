from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from routes.homes import router as event_router
# html 틀이 있는 폴더의 위치
app = FastAPI() 
from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_router, prefix='/home')


templates = Jinja2Templates(directory = "templates/")


@app.get("/")
async def root(request:Request):
    # html 틀로 호출
    # return {"message": "DeokJaeKim's World"}
    return templates.TemplateResponse("index.html",
                                      {'request':request})

# @event_router.get("/")
# @event_router.get("/list")
