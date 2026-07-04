from pydantic import BaseModel, Field, RootModel


# ==========================
# LLM CONFIGURATION
# ==========================

class LLMConfig(BaseModel):
    """
    Configuration for a single LLM.
    """

    provider: str
    model: str

    temperature: float = Field(
        ge=0.0,
        le=2.0,
    )

    max_tokens: int = Field(
        gt=0,
    )


class ModelsConfig(BaseModel):
    """
    Configuration for all agent models.
    """

    planner: LLMConfig
    researcher: LLMConfig
    reviewer: LLMConfig
    writer: LLMConfig
    final_reviewer: LLMConfig


# ==========================
# RESEARCH CONFIGURATION
# ==========================

class PlanningConfig(BaseModel):
    max_sections: int = Field(gt=0)


class ResearchConfig(BaseModel):
    max_search_results: int = Field(gt=0)
    max_sources_per_section: int = Field(gt=0)


class ReviewConfig(BaseModel):
    max_revision_iterations: int = Field(ge=0)


class ReportConfig(BaseModel):
    default_type: str


class ResearchWorkflowConfig(BaseModel):
    planning: PlanningConfig
    research: ResearchConfig
    review: ReviewConfig
    report: ReportConfig


# ==========================
# LOGGING CONFIGURATION
# ==========================

class EnvironmentLoggingConfig(BaseModel):
    renderer: str


class LoggingConfig(BaseModel):
    development: EnvironmentLoggingConfig
    production: EnvironmentLoggingConfig

# ==========================
# PROVIDER CONFIGURATION
# ==========================

class ProviderConfig(BaseModel):
    """
    Configuration for an LLM provider.
    """

    api_base: str

    timeout: int = Field(
        gt=0,
    )

    max_retries: int = Field(
        ge=0,
    )


class ProvidersConfig(RootModel):
    root: dict[str, ProviderConfig]