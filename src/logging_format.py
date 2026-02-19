from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any, Dict, Optional


class JsonFormatter(logging.Formatter):
    """
    Minimal JSON logger with room for structured fields.
    Emits one JSON object per line.
    """

    def format(self, record: logging.LogRecord) -> str:
        base: Dict[str, Any] = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }

        # Include exception info if present
        if record.exc_info:
            base["exc_info"] = self.formatException(record.exc_info)

        # Pull any structured fields from `extra=...`
        # (logging stores them directly on the record object)
        reserved = {
            "name", "msg", "args", "levelname", "levelno", "pathname", "filename",
            "module", "exc_info", "exc_text", "stack_info", "lineno", "funcName",
            "created", "msecs", "relativeCreated", "thread", "threadName",
            "processName", "process", "message"
        }
        for k, v in record.__dict__.items():
            if k not in reserved and k not in base:
                base[k] = v

        return json.dumps(base, ensure_ascii=False)


def configure_logging(
    log_level: str = "INFO",
    json_logs: bool = False,
    log_file: Optional[str] = None,
) -> None:
    """
    Configure root logging.
    - If log_file is provided, logs go there; else to stderr.
    - If json_logs=True, emit JSON lines.
    """
    level = getattr(logging, log_level.upper(), None)
    if not isinstance(level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    handler: logging.Handler
    if log_file:
        handler = logging.FileHandler(log_file, encoding="utf-8")
    else:
        handler = logging.StreamHandler(sys.stderr)

    if json_logs:
        handler.setFormatter(JsonFormatter())
    else:
        handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s %(levelname)s %(name)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level)


def log_extra(**kwargs: Any) -> Dict[str, Any]:
    """
    Helper to build `extra` dicts. Keeps callsites tidy:
        logger.info("...", extra=log_extra(path=..., n=...))
    """
    return kwargs
