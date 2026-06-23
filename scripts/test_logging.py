from src.observability.logging_config import (
    configure_logging,
    get_logger,
)

configure_logging()

logger = get_logger()

logger.info(
    "logging_system_initialized",
    component="test_script",
)