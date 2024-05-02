from typing import List, Optional
from pydantic import BaseModel, AnyUrl


class ExternalUrls(BaseModel):
    spotify: AnyUrl


class Followers(BaseModel):
    href: Optional[str]
    total: int


class Image(BaseModel):
    height: int
    url: AnyUrl
    width: int


class Artist(BaseModel):
    external_urls: ExternalUrls
    followers: Followers
    genres: List[str]
    href: AnyUrl
    id: str
    images: List[Image]
    name: str
    popularity: int
    type: str
    uri: str