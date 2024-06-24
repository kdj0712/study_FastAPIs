from fastapi import APIRouter
router = APIRouter()
from starlette.responses import HTMLResponse

from fastapi import Request
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory = "templates/")

# @router.get("/",response_class=HTMLResponse)
# async def home():
#     # return {"message": "DeokJaeKim's home World"}
#     html = "<body> <h2>It's Home </h2> </body>"
#     return html

# response_class=HTMLResponse
@router.get("/")
async def home(request:Request):
    return templates.TemplateResponse(name="homes/standards.html",
                                           context={'request':request})
# @router.get("/list",response_class=HTMLResponse) # 어노테이션 (웹에서 function을 호출하는 기능)
# async def home_list():
#     # pass
#     # return 0
#     html = "<body> <h2>It's Home List </h2> </body>"
#     return html

