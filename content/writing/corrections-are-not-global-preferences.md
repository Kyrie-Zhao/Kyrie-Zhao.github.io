“Please make this less emotional.”

A personal assistant could interpret that as a revision to one paragraph, a preference for this kind of message, a general writing preference, or a fact about the user's personality.

The sentence alone may not tell us which one is intended. A system eager to learn can become confidently wrong by choosing the broadest interpretation.

This note proposes a way to reason about feedback scope. The examples are synthetic and the checks are design suggestions, not evidence that automatic feedback attribution has been solved.

## First identify what was being corrected

Consider three replies to a family-message draft:

> That did not happen.

> It happened, but do not mention it to my parents.

> You can mention it, but this paragraph sounds like a farewell speech.

The first disputes content. The second limits disclosure. The third concerns expression. Saving all three as negative sentiment toward a topic loses the difference between them.

An update to wording should not quietly erase a factual record. A disclosure restriction should not be treated as evidence that the event never happened. A factual correction should reach later uses of the mistaken claim, not merely soften its next expression.

## Scope is part of the meaning

A useful interpretation of feedback keeps the affected task and circumstances in view. “Do not force a life lesson into a weekly update” does not prohibit lessons in a retrospective. “Not today” does not always revoke a standing preference. “Never share this with my family” is not a request for a different tone.

When the scope is ambiguous, there are several possible responses: ask a focused question, apply the change locally, or preserve a tentative interpretation for later confirmation. Which is appropriate depends on the consequence of getting it wrong and the burden of interrupting the user.

The system should not ask for clarification about every adjective. It also should not silently promote every edit into a durable rule.

## Test the intended effect and the collateral effect

A simple evaluation uses a correction, a related task, and an unrelated task.

| Input | Desired observation |
| --- | --- |
| Another weekly update | The unwanted closing reflection is reduced |
| A requested project retrospective | Useful lessons are still included |
| A factual summary of the original event | The underlying event remains unchanged |
| A later explicit instruction requesting reflection | The current instruction is handled within its scope |

A system that removes reflective language everywhere has learned an effect but not its boundary. A system that only fixes the current paragraph may have respected scope but failed to retain a clearly intended recurring preference.

The evaluator needs to specify which of these interpretations the scenario supports before inspecting model behavior. Otherwise almost any output can be defended afterward as a reasonable personalization choice.

## The user can change the arrangement

A previously accurate preference may no longer apply. This differs from correcting an earlier misunderstanding.

If someone once wanted strict reminders and now asks to pause them, the old arrangement need not become false history. The question is what should govern behavior now. Similarly, withdrawing a use of information does not necessarily mean disputing the information itself.

This distinction helps avoid destructive updates in which one change erases useful context elsewhere. It also makes it possible to explain why the assistant behaves differently without insisting the user has been inconsistent.

A change should have a visible effect on the appropriate future task. “I understand” is not a substitute for that observation.

## Do not confuse writing instructions with a person

A user's style preferences can tell us how they want a particular artifact written. They are not automatically evidence of emotional disposition, relationship quality, or long-term identity.

This is especially important when several task memories share one person model. An instruction from a work report should not become an unexamined premise in a family message. Shared storage does not imply shared applicability.

Builders can make that boundary explicit in evaluation without prescribing a universal set of physical modules. The problem is the authority and scope of an update, regardless of where the implementation stores it.

The success criterion is practical: the next relevant task gets better, unrelated tasks do not get worse, and the person can revise the arrangement again. Learning should reduce the work of managing the assistant, rather than turn every correction into a negotiation with an expanding rulebook.
