import pytest

from src.services.prompt import (
    MissingPromptVariableError,
)
from src.services.prompt.renderer import (
    PromptRenderer,
)


def test_render_success():

    renderer = PromptRenderer()

    output = renderer.render(
        "Hello {{ name }}",
        {
            "name": "Maulin",
        },
    )

    assert output == "Hello Maulin"


def test_missing_variable():

    renderer = PromptRenderer()

    with pytest.raises(
        MissingPromptVariableError
    ):

        renderer.render(
            "Hello {{ name }}",
            {},
        )