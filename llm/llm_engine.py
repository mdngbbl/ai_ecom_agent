import requests

GEMINI_API_KEY = "your_api_key_here"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def question_to_sql(question: str) -> str:
    prompt = f"""Convert the following natural language question into an SQL query. Assume we have these tables:
    - ad_sales_metrics
    - total_sales_metrics
    - product_eligibility

    Question: {question}

    SQL:"""
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    params = {"key": GEMINI_API_KEY}
    response = requests.post(GEMINI_URL, headers=headers, params=params, json=payload)
    sql = response.json()['candidates'][0]['content']['parts'][0]['text']
    return sql.strip()
