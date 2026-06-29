from pathlib import Path

from .cache import PromptCache
from .loader import PromptLoader
from .models import PromptRole, PromptType
from .renderer import PromptRenderer


class PromptService:
    """
    Public interface for loading and rendering prompts.
    """

    def __init__(
        self,
        prompts_root: Path,
        loader: PromptLoader | None = None,
        renderer: PromptRenderer | None = None,
        cache: PromptCache | None = None,
    ) -> None:

        self._loader = loader or PromptLoader(prompts_root)
        self._renderer = renderer or PromptRenderer()
        self._cache = cache or PromptCache()

    def render(
        self,
        prompt_type: PromptType,
        prompt_role: PromptRole,
        variables: dict[str, object],
    ) -> str:

        template = self._cache.get(
            prompt_type,
            prompt_role,
        )

        if template is None:

            template = self._loader.load(
                prompt_type,
                prompt_role,
            )

            self._cache.set(
                prompt_type,
                prompt_role,
                template,
            )

        return self._renderer.render(
            template,
            variables,
        )

    def get_system_prompt(
        self,
        prompt_type: PromptType,
        variables: dict[str, object],
    ) -> str:

        return self.render(
            prompt_type,
            PromptRole.SYSTEM,
            variables,
        )

    def get_user_prompt(
        self,
        prompt_type,
        variables,
    ) -> str:

        return self.render(
            prompt_type,
            PromptRole.USER,
            variables,
        )