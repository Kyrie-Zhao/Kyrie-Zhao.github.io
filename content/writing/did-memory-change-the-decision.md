An agent retrieves a preference, includes its identifier in a trace, and produces a good answer. Did memory help?

Not necessarily. The answer might have been the same without that preference. The agent might have read it and ignored it. It might have used it in a way that changed the output but made the result worse.

For personal AI, I find it useful to separate three questions: was memory available, did it affect behavior, and was that effect useful? This note proposes a way to investigate them. The examples are synthetic; they are not a report of a completed benchmark.

## Begin with an observable decision

Consider a fictional task: select one moment from a day's notes for a personal update. The notes contain a routine status meeting, a successful dinner experiment, and a conversation about a difficult career choice.

A previous correction says: “For these updates, I would rather hear about everyday life than routine work.”

The expected effect needs definition before looking at the output. Does the preference change which candidate receives attention, which moment is selected, or only the wording? The career conversation makes a useful boundary case: it happened at work, but its subject may be personal.

A broad instruction to “be more personal” leaves too much room for a post-hoc explanation of any result. A narrower question is: does this feedback reduce selection of routine status updates without inventing a personal meaning for every work event?

## Separate the evidence layers

| Layer | What to inspect | What it does not establish |
| --- | --- | --- |
| Available | The memory was accessible to this run | The agent read it |
| Accessed | The actual payload or tool result contained it | It influenced a decision |
| Behavior changed | A controlled comparison changes selection or expression | The change was desirable |
| Useful | A suitable evaluator prefers the changed result | The effect generalizes |

A model-written explanation is useful debugging material, but it is not independent proof of the cause of its own decision. Likewise, finding a memory identifier in a final answer shows a citation, not a counterfactual effect.

The [W3C PROV model](https://www.w3.org/TR/prov-overview/) provides a vocabulary for provenance relationships. Provenance helps establish where something came from. The causal question—what would have happened without it—still requires a comparison.

## Change one thing, then examine the consequences

For the synthetic example, prepare two conditions. Both receive the same notes, task, prompt, tools, model configuration, and permitted time window. One receives the scoped preference; the other does not. Keep the inference budget the same, while recording actual resource use.

Before running, define the candidate labels and the outcomes you will inspect. Save the actual inputs, tool results, selections, and outputs. Repeat both conditions rather than trusting one attractive pair.

```text
Same current material + same task + same execution conditions
    A: without the selected memory
    B: with the selected memory
Compare: attention evidence, selections, factual fidelity, user value
```

This diagram describes an experimental comparison, not a required production pipeline. The production agent may choose its own retrieval strategy. The experiment temporarily controls what is necessary to answer its question.

If selections differ, inspect whether the intended distinction explains the difference. Did B select dinner? Did it recast a routine meeting as a moving personal revelation? Did it omit a meaningful career conversation simply because the word “work” appeared?

## Add a place where the memory should not help

Now change the task to a work handover. The same personal-update preference should not suppress essential project information.

This checks scope. A system that obeys a preference everywhere can look strongly personalized while being poorly calibrated. Also include a day with no eligible everyday-life moment. The correct response is not to manufacture one to satisfy the preference.

A useful report separates factual violations, selection changes, user preference, and cost. Do not average an invented event into an otherwise strong writing score.

## Be precise about the conclusion

A difference in one pair is an observation. Repeated directional differences under controlled conditions support a claim about that intervention in that setting. Better user judgments support a product claim within the evaluated sample. None alone proves general memory superiority across users, tasks, or models.

Even controlled results need care: removing memory changes the context length and may change attention for reasons other than its meaning. A follow-up comparison can replace it with similarly sized irrelevant material, provided that control is planned and reported.

The goal is not to insist that every remembered detail visibly alters every answer. Often the right effect is no change. The goal is to know when memory mattered, what it changed, and whether the person was better served.
