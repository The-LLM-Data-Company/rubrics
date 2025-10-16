from pydantic import BaseModel, ConfigDict


class Criterion(BaseModel):
    model_config = ConfigDict(frozen=True)

    weight: float
    requirement: str


class Rubric:
    pass
