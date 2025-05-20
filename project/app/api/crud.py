# project/app/api/crud.py


from typing import List, Optional

from app.models.pydantic import SummaryPayloadSchema, SummaryUpdatePayloadSchema
from app.models.tortoise import TextSummary
from app.summarizer import generate_summary


async def post(payload: SummaryPayloadSchema) -> int:
    article_summary = generate_summary(str(payload.url))
    summary = TextSummary(
        url=payload.url,
        summary=article_summary,
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> None:
    await TextSummary.filter(id=id).first().delete()


async def put(id: int, payload: SummaryUpdatePayloadSchema) -> int:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url,
        summary=payload.summary,
    )
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary
    return None
