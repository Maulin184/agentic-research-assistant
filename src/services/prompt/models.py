"""
Prompt domain models.

This module defines the supported prompt categories used throughout
the application.

Using enums instead of raw strings improves:

- Readability
- IDE auto-completion
- Type safety
- Refactoring safety

Each enum value maps directly to a folder under the `prompts/`
directory.
"""

from enum import Enum


class PromptType(str, Enum):
    """Supported prompt categories."""

    PLANNER = "planner"
    RESEARCHER = "researcher"
    REVIEWER = "reviewer"
    WRITER = "writer"
    FINAL_REVIEWER = "final_reviewer"

class PromptRole(str, Enum):
    SYSTEM = "system"
    USER = "user"