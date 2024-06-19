import subprocess

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

class QueryMessage(BaseModel):
    id: int 
    request: str

@router.post("/api/echo/")
def echo(query: QueryMessage):
    return { 
        "type": "response", 
        "id": query.id + 1,
        "text": query.request
    }

@router.post("/api/clean/")
def clean(query: QueryMessage):
    input_file_path = "./clean.abc"
    
    # Save query.request content to input.abc file
    with open(input_file_path, 'w') as file:
        file.write(query.request)
    
    
    try:
        result = subprocess.run(["python", "../abc-utils/clean1.py", input_file_path], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"{result.stderr}")

        return { 
            "type": "response", 
            "id": query.id + 1,
            "text": result.stdout
        }
    except subprocess.CalledProcessError as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Script execution failed: {e.stderr}")
    
    

app.include_router(router)