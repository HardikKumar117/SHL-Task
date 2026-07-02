from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class HiringRequirements(BaseModel):

    role: Optional[str] = Field(
        default=None,
        description="Primary role being hired for."
    )

    seniority: Optional[
        Literal[
            "Entry-Level",
            "Junior",
            "Mid-Level",
            "Senior",
            "Executive"
        ]
    ] = None

    purpose: Optional[
        Literal[
            "Selection",
            "Development",
            "Benchmarking",
            "Promotion",
            "Succession Planning"
        ]
    ] = None

    technical_skills: Optional[list[str]] = Field(
        default_factory=list,
        description="List of technical skills. "
    )

    job_family: Optional[str] = Field(
        default=None,
        description="Broad category such as Software Engineering, Sales, Leadership, Customer Service."
    )

    leadership_required: Optional[bool] = None

    communication_required: Optional[bool] = None

    personality_assessment_required: Optional[bool] = None

    cognitive_assessment_required: Optional[bool] = None

    years_experience: Optional[int] = Field(
        default=None,
        description="Years of experience if explicitly mentioned."
    )

    notes: Optional[str] = Field(
        default=None,
        description="Any additional hiring constraints."
    )