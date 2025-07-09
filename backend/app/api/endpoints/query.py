# app/api/endpoints/query.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
from app.core.agent import get_agent
import os

router = APIRouter()

DATA_PATH = "data/latest.csv"

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
async def query_agent(request: QueryRequest):
    
    if not os.path.exists(DATA_PATH):
        raise HTTPException(status_code=404, detail="CSV file not found. Please upload a file first.")

    try:
        df = pd.read_csv(DATA_PATH)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CSV loading failed: {str(e)}")

    try:
        agent = get_agent(df)
        result = agent.run(request.question)
        return {"question": request.question, "answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent failed to process query: {str(e)}")
