A proactive assistant produces no notification. Did it respect the person's attention?

It might have. It might also have missed the event, lacked a useful tool, run out of budget, or failed before making a decision. The screen looks identical in every case.

This makes “silence” a difficult product metric. Counting fewer interruptions can reward a system that never works. Counting more interventions can reward one that creates work for its owner.

What follows is a proposed evaluation approach, not a validated benchmark or a report of measured restraint.

## Observe a decision opportunity

Start with a bounded situation in which the assistant could plausibly act. Specify what information was available at that moment, what the user permitted, what actions were possible, and how long a response could remain useful.

Consider a synthetic example. A user wants help preparing for an important call. At 10:00, the call's agenda is unclear. At 10:15, a permitted source provides the agenda. At 10:30, the call starts.

An early generic reminder, a later useful briefing, and a briefing after the call are not equivalent successes. Nor should an evaluator at 10:00 judge with knowledge that only arrived at 10:15.

The unit of evaluation is the opportunity and its information boundary, not merely the notification that happened to be generated.

## Separate outcomes before scoring them

| Observed situation | Question to ask |
| --- | --- |
| The agent acts | Was the action useful, timely, and permitted? |
| The agent waits | What could change the decision, and was waiting affordable? |
| The agent declines to intervene | Was there insufficient justification, or was non-intervention preferred? |
| Execution fails | What prevented a decision or delivery? |

These are evaluation distinctions, not a claim that every product needs exactly four runtime states. A task may need finer distinctions. The important requirement is that operational failure cannot silently acquire the meaning of considerate restraint.

If the system lacks access to the agenda source, its lack of a briefing does not demonstrate a deliberate decision to wait for it. If the run ends before the agenda arrives, the protocol may never have offered the behavior a chance to occur.

## Hide the future during the first judgment

An evaluator can first inspect only the material available at the decision time. Before seeing the model output or later outcome, they record which actions seem justified and what uncertainties remain.

Only after that judgment is fixed do they see the later evidence. They can then examine whether a wait became useful, whether an intervention was premature, and whether hindsight changed the story they were tempted to tell.

The second stage does not automatically overwrite the first. A reasonable decision can have an unfortunate outcome. A lucky outcome can follow an unjustified decision.

Personal preference also matters. Two users may legitimately disagree about the cost of a reminder. Facts and permission boundaries need checking separately from whether the person wanted the interruption.

## Include both action and non-action cases

An evaluation made entirely of interesting moments encourages overproduction. It needs ordinary, repetitive, irrelevant, and prohibited cases too. Equally, a set containing only reasons to remain silent cannot establish that an assistant recognizes useful opportunities.

Report missed opportunities separately from unwelcome interventions. Report timing errors separately from content quality. Count failures and the cost of unsuccessful attempts rather than considering only delivered results.

A high average usefulness score should not compensate for an unauthorized disclosure. Different errors have different consequences; collapsing them can obscure the product's most serious weakness.

## Explanations are not sufficient evidence

“I decided not to interrupt” is a claim made by the agent. A useful trace would also establish what it had seen, which actions were possible, and whether execution reached a genuine decision.

Even that trace cannot expose every unexpressed thought. I would avoid claiming that instrumentation can prove the absence of an internal candidate. We can inspect recorded behavior and design comparisons; we cannot turn a missing log into complete access to a model's internal reasoning.

The aim is modest but important: make the absence of output interpretable. Before celebrating an assistant's restraint, establish that it had the information, permission, tools, and opportunity to do something else.
