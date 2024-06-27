from datetime import datetime
from bson import ObjectId

from pydantic import BaseModel, Field, validator


class News(BaseModel):
    id: ObjectId = Field(serialization_alias="_id")
    source_name: str
    title: str
    description: str
    publish_date: datetime
    cover_image: str | None
    link: str

    @validator("id", pre=True, always=True)
    def convert_to_objectid(cls, value):
        try:
            return ObjectId(value)
        except Exception as _:
            raise ValueError(f"Invalid ObjectId: {value}")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

