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

## Classes do albúm

class ExternalURLs(BaseModel):
    spotify: str


class Image(BaseModel):
    url: str
    height: int
    width: int


class Singer(BaseModel):
    external_urls: ExternalURLs
    href: str
    id: str
    name: str
    type: str
    uri: str


class Album(BaseModel):
    album_type: str
    total_tracks: int
    available_markets: List[str]
    external_urls: ExternalURLs
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    type: str
    uri: str
    artists: List[Singer]
    album_group: str


class Album(BaseModel):
    href: str
    limit: int
    next: Optional[str]
    offset: int
    previous: Optional[str]
    total: int
    items: List[Album]