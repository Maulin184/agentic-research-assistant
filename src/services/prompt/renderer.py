"""
Prompt renderer.

Responsibilities
----------------
- Render templates using Jinja2.
- Validate variables.
- Produce final prompt text.

This module must never:
- Read files.
- Cache templates.
"""

from jinja2 import (
    Environment,
    StrictUndefined,
    TemplateError,
)

from .exceptions import (
    MissingPromptVariableError,
    PromptRenderingError,
)

from jinja2 import UndefinedError


class PromptRenderer:
    """
    Renders markdown prompt templates.
    """

    def __init__(self) -> None:
        self._environment = Environment(
            undefined=StrictUndefined,
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(
        self,
        template: str,
        variables: dict[str, object],
    ) -> str:
        """
        Render a template.
        """

        try:

            compiled = self._environment.from_string(
                template
            )

            return compiled.render(
                **variables
            )

        except UndefinedError as exc:
            raise MissingPromptVariableError(str(exc)) from exc

        except TemplateError as exc:
            raise PromptRenderingError(str(exc)) from exc

            raise