from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STaskAddResponse(BaseModel):
    ok: bool
    task_id: int


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)
