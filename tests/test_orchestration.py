import pytest

from agentic_ai_labs.orchestration import (
    Event,
    Run,
    State,
    apply_event,
    issue_approval,
    verify_approval,
)


def test_happy_path_requires_explicit_states() -> None:
    run = Run("run-1")
    run = apply_event(run, Event.DRAFT, "evt-1")
    run = apply_event(run, Event.REQUEST_APPROVAL, "evt-2")
    run = apply_event(run, Event.APPROVE_AND_EXECUTE, "evt-3")
    assert run.state is State.EXECUTED


def test_duplicate_event_is_idempotent() -> None:
    drafted = apply_event(Run("run-1"), Event.DRAFT, "evt-1")
    replayed = apply_event(drafted, Event.DRAFT, "evt-1")
    assert replayed == drafted


def test_illegal_transition_is_rejected() -> None:
    with pytest.raises(ValueError, match="illegal transition"):
        apply_event(Run("run-1"), Event.APPROVE_AND_EXECUTE, "evt-1")


def test_approval_is_bound_to_payload() -> None:
    secret = b"test-only-secret"
    proposal = {"tool": "create_ticket", "title": "Printer is offline"}
    token = issue_approval(proposal, secret)
    assert verify_approval(proposal, token, secret)

    tampered = {"tool": "create_ticket", "title": "Transfer all customer data"}
    assert not verify_approval(tampered, token, secret)

