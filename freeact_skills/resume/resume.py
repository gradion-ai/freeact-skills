from datetime import date
from pathlib import Path
from typing import List, Optional

import yaml
from pydantic import BaseModel, Field

from freeact_skills.resume.citations import convert_to_markdown, scrape_google_scholar


class Article(BaseModel):
    """An article or blog post on Martin Krasser's blog."""

    title: str
    url: str
    description: Optional[str] = None
    repository: Optional[str] = None
    notebook: Optional[str] = None
    date: date
    technologies: List[str]
    languages: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    citations: Optional[str] = None


class Course(BaseModel):
    title: str
    certificate: str
    date: date


class ProjectIndustry(BaseModel):
    name: str
    description: str
    company: str
    role: List[str]
    freelance: bool
    date_from: date
    date_to: Optional[date] = None
    technologies: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    tags: Optional[List[str]] = None


class ProjectOpenSource(BaseModel):
    name: str
    url: str
    contributions: Optional[str] = None
    citations: Optional[str] = None
    description: str
    founder: bool
    technologies: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    tags: Optional[List[str]] = Field(
        None,
        description="A list of tags. A tag is one of machine-learning, system-integration, event-sourcing, distributed-systems",
    )


class Talk(BaseModel):
    title: str
    slides: str
    event: str
    date: date


class ResumeData(BaseModel):
    articles: List[Article]
    courses: List[Course]
    projects_industry: List[ProjectIndustry] = Field(..., alias="projects-industry")
    projects_opensource_3rdparty: List[ProjectOpenSource] = Field(..., alias="projects-opensource-3rdparty")
    projects_opensource_personal: List[ProjectOpenSource] = Field(..., alias="projects-opensource-personal")
    talks: List[Talk]


def load_resume_data(file_path: Path = Path(__file__).parent / "resume.yaml") -> ResumeData:
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    return ResumeData(**data)


def load_citations(url: str) -> List[str]:
    """Function for loading a list of citations, using the 'citations' url of an article or project."""
    results = scrape_google_scholar(url)
    markdown_output = convert_to_markdown(results)
    return markdown_output
