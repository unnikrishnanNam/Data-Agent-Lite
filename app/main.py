from fastapi import FastAPI
from pydantic import BaseModel
from app.db import get_schema_info
from app.agent import clean_sql, generate_sql, run_query, process_results_with_gemini

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_agent(request: QueryRequest):
    user_prompt = request.question
    schema = get_schema_info()

    raw_sql = await generate_sql(user_prompt, schema)
    sql_query = clean_sql(raw_sql)
    result = await run_query(sql_query)
    final_response = await process_results_with_gemini(user_prompt, result)

    return {
        "sql_query": sql_query,
        "result": result,
        "explanation": final_response
    }
