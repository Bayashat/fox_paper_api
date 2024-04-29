from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer not to say"  


class UserRole(Enum):
    USER = "User"
    MODERATOR = "Moderator"


class Status(Enum):
    SUBMITTED = "Submitted"
    UNDER_REVIEW = "Under Review"
    REJECTED = "Rejected"
    PUBLISHED = "Published"


class ResearchAction(str, Enum):
    review = "Review"
    publish = "Publish"
    reject = "Reject"