from fastapi import FastAPI
from pydantic import BaseModel
from llm.llm_engine import question_to_sql
from sql.db_connector import run_sql_query

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Question):
    sql = question_to_sql(q.question)
    result = run_sql_query(sql)
    return {
        "question": q.question,
        "generated_sql": sql,
        "answer": result
    }
