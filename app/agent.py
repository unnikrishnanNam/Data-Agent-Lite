import os
import httpx
from dotenv import load_dotenv
from app.db import engine
from sqlalchemy import text
import re

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + GEMINI_API_KEY

HEADERS = {"Content-Type": "application/json"}


def clean_sql(raw_sql: str) -> str:
    # Remove markdown formatting like ```sql ... ```
    return re.sub(r"```sql|```", "", raw_sql).strip()

async def generate_sql(prompt, schema):
    full_prompt = f"""
You are an AI SQL agent. Given a natural language query and a database schema, your task is to generate a valid PostgreSQL query.

Instructions:
- Use only standard PostgreSQL syntax.
- Return ONLY the raw SQL string.
- DO NOT include markdown formatting like triple backticks (```), `sql`, or any explanations.
- DO NOT add comments or headers — only return executable SQL.

Schema:
{schema}

User Query:
{prompt}
"""
    payload = {
        "contents": [
            {"parts": [{"text": full_prompt}]}
        ]
    }
    async with httpx.AsyncClient(timeout=20.0) as client:
        res = await client.post(GEMINI_API_URL, json=payload, headers=HEADERS)
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]

async def process_results_with_gemini(prompt, result):
    explanation_prompt = f"""
User asked: {prompt}
SQL result: {result}

Explain the result in simple business terms.
"""
    payload = {
        "contents": [
            {"parts": [{"text": explanation_prompt}]}
        ]
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(GEMINI_API_URL, json=payload, headers=HEADERS)
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]

async def run_query(sql):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        return [dict(row._mapping) for row in result]
