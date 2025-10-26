from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict


class Measurement(BaseModel):
    elementName: str
    elementDescription: Optional[str] = None
    elementMeasurements: Dict[str, float]


class Tag(BaseModel):
    term: str
    AAT_URL: Optional[HttpUrl] = None
    Wikidata_URL: Optional[HttpUrl] = None


class Constituent(BaseModel):
    constituentID: int
    name: str
    role: str
    constituentULAN_URL: Optional[str] = None
    constituentWikidata_URL: Optional[str] = None
    gender: str


class Artwork(BaseModel):
    objectID: int
    isHighlight: bool
    accessionNumber: Optional[str] = None
    accessionYear: Optional[str] = None
    isPublicDomain: bool
    primaryImage: Optional[str] = None
    primaryImageSmall: Optional[str] = None
    additionalImages: Optional[List[HttpUrl]] = []
    constituents: Optional[List[Constituent]] = []
    department: Optional[str] = None
    objectName: Optional[str] = None
    title: Optional[str] = None
    culture: Optional[str] = None
    period: Optional[str] = None
    dynasty: Optional[str] = None
    reign: Optional[str] = None
    portfolio: Optional[str] = None
    artistRole: Optional[str] = None
    artistPrefix: Optional[str] = None
    artistDisplayName: Optional[str] = None
    artistDisplayBio: Optional[str] = None
    artistSuffix: Optional[str] = None
    artistAlphaSort: Optional[str] = None
    artistNationality: Optional[str] = None
    artistBeginDate: Optional[str] = None
    artistEndDate: Optional[str] = None
    artistGender: Optional[str] = None
    artistWikidata_URL: HttpUrl
    artistULAN_URL: HttpUrl
    objectDate: Optional[str] = None
    objectBeginDate: int
    objectEndDate: int
    medium: Optional[str] = None
    dimensions: Optional[str] = None
    dimensionsParsed: Optional[float] = None
    measurements: List[Measurement]
    creditLine: Optional[str] = None
    geographyType: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    county: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    subregion: Optional[str] = None
    locale: Optional[str] = None
    locus: Optional[str] = None
    excavation: Optional[str] = None
    river: Optional[str] = None
    classification: Optional[str] = None
    rightsAndReproduction: Optional[str] = None
    linkResource: Optional[str] = None
    metadataDate: datetime
    repository: Optional[str] = None
    objectURL: HttpUrl
    tags: List[Tag] = []
    objectWikidata_URL: Optional[str] = None
    isTimelineWork: bool
    GalleryNumber: Optional[str] = None


class ArtworkList(BaseModel):
    total: int
    objectIDs: Optional[List[int]] = []