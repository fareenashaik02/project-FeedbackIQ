from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_ai_analysis(feedback):


    text = "\n".join(feedback)


    prompt = f"""

You are an AI business analyst.

Analyze these customer reviews:

{text}


Generate:

## Overall Customer Sentiment

## Positive Customer Experiences

## Main Problems Reported

## Business Improvement Suggestions

## Final Recommendation


Give clear business insights.
"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.3
    )


    return response.choices[0].message.content