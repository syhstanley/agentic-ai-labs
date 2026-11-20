"""A tiny deterministic orchestration core.

This is deliberately not an autonomous agent. It demonstrates the reliable
shell around an agent: explicit states, legal transitions, approval binding,
and idempotent event handling. Chapter 03 asks the learner to place model and
tool calls behind this boundary.
"""

from __future__ import annotations

import hashlib
import hmac
import json
from dataclasses import dataclass, field, replace
from enum import StrEnum
from typing import Any


class State(StrEnum):
    RECEIVED = "received"
    DRAFTED = "drafted"
    WAITING_APPROVAL = "waiting_approval"
    EXECUTED = "executed"
    REJECTED = "rejected"
    FAILED = "failed"


class Event(StrEnum):
    DRAFT = "draft"
    REQUEST_APPROVAL = "request_approval"
    APPROVE_AND_EXECUTE = "approve_and_execute"
    REJECT = "reject"
    FAIL = "fail"


TRANSITIONS: dict[tuple[State, Event], State] = {
    (State.RECEIVED, Event.DRAFT): State.DRAFTED,
    (State.DRAFTED, Event.REQUEST_APPROVAL): State.WAITING_APPROVAL,
    (State.WAITING_APPROVAL, Event.APPROVE_AND_EXECUTE): State.EXECUTED,
    (State.WAITING_APPROVAL, Event.REJECT): State.REJECTED,
    (State.RECEIVED, Event.FAIL): State.FAILED,
    (State.DRAFTED, Event.FAIL): State.FAILED,
    (State.WAITING_APPROVAL, Event.FAIL): State.FAILED,
}


@dataclass(frozen=True)
class Run:
    run_id: str
    state: State = State.RECEIVED
    processed_event_ids: frozenset[str] = field(default_factory=frozenset)


def apply_event(run: Run, event: Event, event_id: str) -> Run:
    """Apply an event once, rejecting illegal state changes.

    Real systems must persist the event ID and state atomically in a database.
    This in-memory example only demonstrates the invariant.
    """

    if event_id in run.processed_event_ids:
        return run
    try:
        next_state = TRANSITIONS[(run.state, event)]
    except KeyError as exc:
        raise ValueError(f"illegal transition: {run.state} + {event}") from exc
    return replace(
        run,
        state=next_state,
        processed_event_ids=run.processed_event_ids | {event_id},
    )


def _canonical_payload(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def issue_approval(payload: dict[str, Any], secret: bytes) -> str:
    """Bind an approval to the exact proposed action."""

    return hmac.new(secret, _canonical_payload(payload), hashlib.sha256).hexdigest()


def verify_approval(payload: dict[str, Any], token: str, secret: bytes) -> bool:
    expected = issue_approval(payload, secret)
    return hmac.compare_digest(expected, token)

