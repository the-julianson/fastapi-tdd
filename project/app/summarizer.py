# project/app/summarizer.py
# import asyncio


import nltk
from newspaper import Article

from app.models.tortoise import TextSummary


async def generate_summary(summary_id: int, url: str) -> None:
    article = Article(url)
    article.download()
    article.parse()
    try:
        nltk.data.find("tokenizers/punkt_tab")
    except LookupError:
        nltk.download("punkt_tab")
    finally:
        article.nlp()

    summary = article.summary

    # Testing the background task
    # await asyncio.sleep(10)
    await TextSummary.filter(id=summary_id).update(summary=summary)
