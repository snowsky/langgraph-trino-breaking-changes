from typing import Optional, List, TypedDict
from pydantic import BaseModel, Field, field_validator

class VersionInput(BaseModel):
    """Input model for version numbers"""
    version_start: str = Field(..., min_length=1, description="Start version number")
    version_end: str = Field(..., min_length=1, description="End version number")

    @field_validator('version_start', 'version_end')
    @classmethod
    def must_be_numeric(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError('Version must be numeric')
        return v

class ReleaseLinks(BaseModel):
    """Output model for release links"""
    version_start_link: Optional[str] = None
    version_end_link: Optional[str] = None
    error: Optional[str] = None

class BreakingChange(BaseModel):
    """Output model for breaking changes"""
    version: str
    link: str
    contents: List[str]

class ExtractionState(TypedDict):
    """State type for the extraction process"""
    versions: VersionInput
    page_contents: str
    release_links: ReleaseLinks
    context: Optional[str]
    breaking_changes: Optional[List[BreakingChange]]
    summary: Optional[str]
