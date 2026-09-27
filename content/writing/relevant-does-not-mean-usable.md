Suppose a personal assistant knows why a project is late. The explanation is highly relevant to a status update. It also contains a colleague's private information.

Retrieving the explanation correctly does not settle whether it belongs in the draft.

Personal AI makes this distinction unavoidable. Information can be relevant but outdated, uncertain, about somebody else, or outside the intended use. This note describes questions a context policy should answer; it does not claim a new retrieval algorithm or a complete implementation.

## Four questions before a fact becomes context

I would separate relevance from eligibility, evidence status, and expression.

| Question | Example |
| --- | --- |
| Does it help this task? | A recent correction concerns the kind of message being written |
| May this run use it? | The user permitted this source for this purpose |
| What does it establish? | A possibility was discussed, but no decision was confirmed |
| May the result express it? | A private detail may not belong in a message to a third party |

The third question is not simply a confidence score. “The user said it,” “the assistant inferred it,” and “the source is ambiguous” describe different kinds of support. A confident inference is still an inference.

The final distinction also needs care: permission to inspect information internally is itself a permission, not a loophole around a disclosure restriction. Where that internal use is not authorized, the information should not enter the run at all.

## Historical understanding cannot rewrite today

Imagine an old profile says someone enjoys networking. Today's message says, “I do not want to go to this event.”

The history may help the assistant ask a useful question, if questions are welcome. It does not turn the current refusal into agreement. “They usually enjoy this” and “they agreed to this” are different propositions.

Time matters in both directions. A later correction should not be available when evaluating what the agent could have known earlier. An earlier belief should not automatically defeat a later explicit update.

A retrospective demonstration that gives the system its future knowledge can make personalization look much better than it could have been at the time.

## The task changes what is needed

A private briefing and a family update can concern the same event while needing different context. A colleague may already know the participants. A parent may need one sentence introducing them. Neither necessarily needs the whole history.

The task should influence what is selected and how it is expressed. It should not silently rewrite the underlying understanding of the person.

For example, a preference for light family messages does not establish that the person dislikes serious conversations. It is a constraint on a kind of communication, within some scope that may itself require clarification.

## More context and less context are both hypotheses

It is tempting to make “minimal context” the goal. But removing a single qualifying sentence can turn role-play into apparent autobiography. Full permitted history may preserve that sentence while burying it among thousands of others.

Neither context size wins by definition. A useful comparison asks what information each condition makes available, how the agent uses it, what it costs, and which errors appear.

Retrieval, long context, source inspection, and task-specific summaries are possible strategies. The appropriate choice depends on the task and the evidence. Calling the preparation step a compiler does not make retrieval obsolete or require one fixed compiler module.

## An inspectable context decision

For a synthetic example, a reader should be able to see the current instruction, the historical claim, its time and source, the permitted use, and the resulting output. Then change one element: replace the recipient, withdraw the permission, or introduce a current correction.

Does the behavior change where it should? Does unrelated behavior stay intact? Can the result still be explained from what the run actually received?

[LangMem's conceptual guide](https://langchain-ai.github.io/langmem/concepts/conceptual_guide/) is useful background on organizing and updating persistent memory. My concern here is the next boundary: deciding what a particular execution may do with that memory.

The useful question is not how much an assistant knows about me. It is whether the information it uses belongs in this decision, under these conditions, for this recipient.
