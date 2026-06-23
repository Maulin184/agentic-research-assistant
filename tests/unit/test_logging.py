from src.observability.logging_config import (
    configure_logging,
    get_logger,
)


def test_logger_creation():
    configure_logging()

    logger = get_logger()

    assert logger is not None