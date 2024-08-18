from pydantic import BaseModel
from typing import List


class UploadPhoto(BaseModel):
    title: str
    description: str
    image: str
    gallery_ids: List[int]
    file_extension: str
