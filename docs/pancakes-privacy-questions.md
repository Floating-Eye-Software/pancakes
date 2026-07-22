# Pancakes Privacy Questions

## Status

**Design Note (Provisional)**

This document explores open questions about privacy, observation, inference, care, and AI within the Pancakes ecosystem.

It is intentionally exploratory.

It does not establish policy or architectural requirements.

Instead, it identifies a class of questions that increasingly appear as Pancakes evolves from a collection of applications into a long-lived life computing platform.

Many of these questions cannot be answered using traditional privacy models alone.

---

# Purpose

Traditional privacy discussions focus on questions such as:

* Who owns information?
* Who may access it?
* Who may disclose it?
* Who may copy it?
* Who may delete it?

These questions remain essential.

However, Pancakes introduces another class of questions.

Instead of asking:

> Who may access information?

we increasingly find ourselves asking:

> What kinds of knowledge should humane software help create?

This distinction becomes important because Pancakes is designed to:

* accumulate observations over years,
* assist with reflection,
* recognize long-term patterns,
* help people understand themselves,
* help people understand their relationships,
* incorporate increasingly capable AI assistants.

Even when every individual observation is ethical, the resulting body of knowledge may raise entirely new ethical questions.

This document explores those questions.

---

# Relation to Existing Work

The phenomenology underlying these questions has already been explored from an Informational Experiential Realism perspective in **Informational Personal Space, Opacity, and Future-Space Restriction**.

That document argues that the discomfort associated with "being modeled" is not primarily about privacy violations.

Instead, it arises when interpretations become durable social structures that influence another person's future despite never overcoming the inherent opacity of human experience.
This document assumes that analysis.

Its purpose is different.

Rather than explaining the phenomenon, it asks:

> If informational personal space exists, what responsibilities does that create for software?

---

# A Motivating Example

Abed begins keeping a personal journal in Pancakes.

His goal is not to study anyone else.

He wants to become better at understanding social situations and his own relationships.

Each evening he spends a few minutes reflecting on the day.

His entries contain observations such as:

* Jeff seemed unusually impatient today.
* Annie left the study group early.
* Shirley looked worried about her business.
* Troy was quieter than usual.
* Britta seemed excited after class.
* I interrupted Pierce too often.
* Chang appeared exhausted.
* I felt disconnected from everyone today.
* Annie cancelled movie night.
* Jeff apologized to Britta.
* Dean Pelton seemed unusually energetic.

The notebook is fundamentally about **Abed's own life**.

He is not tracking Annie.

He never accesses Annie's notebook.

He never reads her private records.

He never bypasses permissions.

Years later he asks his AI assistant:

> "Can you help me understand my relationships?"

The assistant reviews thousands of journal entries.

Among many observations it notices that Annie's mood, participation, and energy appear to follow a recurring monthly rhythm.

Eventually it becomes capable of predicting that rhythm with considerable accuracy.

Neither Abed nor the AI ever accessed Annie's private information.

Everything was inferred from years of ordinary public observations recorded for an entirely different purpose.

This raises an uncomfortable question.

Should Pancakes help create that knowledge?

---

# Observation

Observation is an ordinary part of human life.

We constantly notice:

* expressions,
* routines,
* conversations,
* habits,
* friendships,
* moods,
* schedules.

Observation is not surveillance.

Observation is one of the foundations of empathy, friendship, parenting, teaching, and caregiving.

Questions:

* When does observation become recordkeeping?
* When does recordkeeping become modeling?
* When does modeling become surveillance?
* Is observation itself ethically neutral?

---

# Recording

Writing observations changes their character.

Human memory is:

* incomplete,
* selective,
* reconstructive,
* temporary.

Written records become:

* persistent,
* searchable,
* cumulative,
* analyzable.

Questions:

* Is recording ethically different from remembering?
* Should some observations intentionally remain ephemeral?
* Is forgetting sometimes a desirable property?

---

# Inference

Many important conclusions are never directly observed.

They emerge through inference.

Examples:

Observed:

* headaches,
* cancelled plans,
* reduced energy,
* social withdrawal.

Inferred:

* depression,
* pregnancy,
* burnout,
* fertility,
* chronic illness.

Often the inferred conclusion is substantially more sensitive than any individual observation.

Questions:

* Should inferred information receive stronger protection than observed information?
* Is inference itself a form of personal information?

---

# Prediction

Inference naturally enables prediction.

Examples:

* likely burnout,
* probable conflict,
* expected relapse,
* estimated fertility,
* anticipated depressive episode.

Prediction changes relationships.

Prediction changes power.

Prediction changes responsibility.

Questions:

* Should AI predict sensitive characteristics of people who never consented?
* Should systems intentionally avoid certain categories of prediction?

---

# Human Versus Machine Observation

Humans naturally develop models of other people.

AI differs primarily in scale.

Humans:

* forget,
* revise,
* misunderstand,
* forgive,
* become distracted.

AI may:

* remember indefinitely,
* correlate across years,
* aggregate thousands of observations,
* identify subtle statistical patterns,
* generate increasingly accurate predictive models.

The concern may therefore be less about artificial intelligence itself than about persistent, large-scale modeling.

---

# Relational Information

Many observations do not belong exclusively to one individual.

Examples:

* Annie and Jeff argued.
* Troy visited Abed.
* Shirley helped Britta.
* Our household ate dinner together.
* My daughter struggled at school today.

These observations are inherently relational.

Questions:

* Whose information is this?
* Who may delete it?
* Who may export it?
* Who may ask AI questions about it?

---

# Care Versus Surveillance

Observation can arise from care.

Examples include:

* parenting,
* caregiving,
* mentoring,
* teaching,
* friendship,
* partnership.

The same observational techniques can also support:

* coercion,
* manipulation,
* stalking,
* social control.

Technology alone does not distinguish the two.

Questions:

* What makes observation caring?
* What makes it surveillance?
* Does purpose matter?
* Does reciprocity matter?
* Does institutional power matter?

---

# Care Modes

Future Pancakes systems may support:

* caregiving,
* parenting,
* education,
* mentoring,
* household coordination,
* community stewardship.

These domains necessarily involve observing other people.

Should systems distinguish between:

* self-observation,
* mutual observation,
* caregiving,
* professional care,
* institutional care,
* emergency care?

Should these contexts carry different ethical expectations?

---

# Informational Personal Space

People possess physical personal space.

Standing extremely close to another person is often uncomfortable even though it causes no direct physical injury.

Perhaps people also possess informational personal space.

Possible hypothesis:

> Every person deserves a zone of interpretive openness around themselves.

Questions:

* Is ambiguity itself a human good?
* Can a person become "too knowable"?
* Can exhaustive modeling become invasive despite relying entirely on public observations?

---

# Epistemic Boundaries

Perhaps privacy is only one category of boundary.

Perhaps there are also boundaries around knowledge itself.

Possible questions include:

What may be:

* observed,
* recorded,
* remembered,
* inferred,
* predicted,
* surfaced,
* shared,
* acted upon?

These may represent distinct ethical categories rather than different stages of the same process.

---

# Symbolic Projection

Throughout Pancakes, symbolic projection is generally preferred over explicit disclosure.

Instead of:

> Fertility window

an ambient client might display:

> A crimson moon.

Instead of:

> Burnout score

it might display:

> A neglected garden.

Instead of:

> Elevated stress

it might display:

> Storm clouds gathering beyond the hills.

One possible reason is that symbolism preserves ambiguity.

It communicates emotional reality without collapsing lived experience into explicit diagnostic statements.

Perhaps symbolic projection is not merely an aesthetic decision.

Perhaps it is also a privacy technology.

---

# AI Questions

Should AI:

* infer depression?
* infer loneliness?
* infer abuse?
* infer pregnancy?
* infer addiction?
* infer relationship deterioration?

If so:

* for whom?
* under whose authority?
* with what confidence?
* with what explanation?
* with what obligations?

Should an AI ever know something that no human participant has consciously recognized?

---

# Bystanders

Life journals inevitably contain observations about other people.

Examples include:

* conversations,
* shared meals,
* disagreements,
* celebrations,
* family life,
* coworkers,
* classmates,
* strangers.

Should AI treat bystanders differently from users?

Do bystanders possess rights even when they never use Pancakes themselves?

---

# Community Knowledge

Entire communities may become observable over time.

Nodes may reveal:

* flourishing,
* isolation,
* conflict,
* burnout,
* generosity,
* cooperation.

Such knowledge may support stewardship.

It may also enable surveillance.

How should communities preserve dignity while still understanding themselves?

---

# Possible Design Principles

These are hypotheses rather than conclusions.

* Observation and inference are ethically distinct.
* Recording and remembering are ethically distinct.
* Prediction creates new ethical obligations.
* Relational information deserves distinct governance.
* Permission to observe is not permission to infer.
* Permission to infer is not permission to disclose.
* Ambiguity may itself deserve protection.
* Symbolic projection may preserve dignity better than explicit diagnosis.
* AI should practice epistemic humility.
* Systems should avoid unnecessary collapse of interpretive openness.

---

# Open Questions

Some questions remain unresolved.

* Can a system intentionally remain ignorant?
* Should forgetting be considered a feature?
* Can ambiguity be preserved by design?
* Can informational personal space be violated without violating traditional privacy?
* Can someone consent to being modeled?
* Can that consent later be withdrawn?
* What obligations accompany knowledge about another person?
* Should AI answer every question it can answer?
* What constitutes informational trespass?
* What constitutes respectful observation?
* Can humane software require epistemic restraint?

---

# Closing Thoughts

Pancakes began by asking questions about privacy.

Increasingly, it appears to be asking questions about knowledge itself.

Traditional privacy asks:

> Who may access information?

Humane life computing may also need to ask:

> What kinds of knowledge should systems help create?

The goal may not simply be protecting information.

It may be protecting each person's ability to remain partially unknowable.

Not because opacity is a flaw.

But because opacity is one of the conditions that makes human freedom, growth, reinterpretation, and genuine relationships possible.

---

# Appendix A — Everyday Modeling and Epistemic Primacy

The questions explored in this document are often associated with artificial intelligence, surveillance, or large-scale data collection.

However, the underlying phenomenon appears in ordinary human life.

## The Convenience Store

A customer visits the same neighborhood convenience store almost every day.

Each visit is unremarkable.

He purchases the same bag of chips.

The owners gradually recognize him.

Eventually he realizes they refer to him among themselves as:

> "The chip guy."

No private records were accessed.

No surveillance occurred.

No confidential information was disclosed.

The owners simply remembered a repeated pattern of public observations.

Yet the customer experiences discomfort.

Traditional privacy frameworks struggle to explain this reaction.

Nothing secret has been revealed.

Nothing has been stolen.

Nothing has been exposed.

The discomfort instead arises from a different source.

The repeated observations have become a durable model.

The customer is no longer encountered as an open-ended person.

He is encountered through an established interpretation.

The issue is not that the owners know he buys chips.

The issue is that they may now believe they know what kind of person he is.

Repeated observation naturally invites inference.

Observed:

* buys chips almost every day.

Possible inferences:

* unhealthy diet,
* poor self-control,
* lives alone,
* does not cook,
* lacks discipline,
* always follows the same routine.

None of these conclusions necessarily follows from the observation.

They remain interpretations.

Nevertheless, repeated observation tends to increase confidence in those interpretations.

Importantly, the customer's lived experience remains opaque.

Perhaps the chips are shared with coworkers.

Perhaps they replace lunch.

Perhaps they are simply an inexpensive daily pleasure.

The observers cannot know.

Yet their growing familiarity may create the feeling that they do.

This illustrates an important distinction.

Observation is not inherently problematic.

Neighborhood businesses often remember regular customers.

Remembering names, favorite orders, or familiar routines can be an expression of hospitality, belonging, and care.

The discomfort emerges when accumulated observations become perceived knowledge of another person's character.

Repeated exposure produces epistemic confidence that may exceed what the observations actually justify.

## The Library

A second example illustrates a related but distinct phenomenon.

While packing a backpack, someone remarks:

> "You're going to the library."

The prediction is correct.

By itself, this is unremarkable.

The observer has noticed a recurring pattern and successfully anticipated another occurrence.

But the conversation continues.

The observer says:

> "I know you better than you know yourself."

This statement transforms the interaction.

The issue is no longer prediction.

It is authority.

The speaker claims that their accumulated observations entitle them to a more authoritative understanding of the other person than the person's own first-person experience.

This claim cannot be justified by repeated observation alone.

Human behavior may become increasingly predictable while human experience remains fundamentally opaque.

The observer may correctly anticipate where someone is going while still misunderstanding why they are going there, what they are thinking, or how they understand themselves.

Prediction does not overcome opacity.

It merely increases confidence.

This suggests another ethical distinction.

There is a profound difference between saying:

> "I think you're going to the library."

and saying:

> "I know you better than you know yourself."

The first is a prediction.

The second is a claim of epistemic superiority.

## Toward Epistemic Primacy

These examples suggest that humane software should distinguish between increasing predictive capability and increasing epistemic authority.

Accumulating observations may improve a system's ability to recognize patterns.

It does not necessarily justify stronger claims about another person's motives, identity, values, or lived experience.

This document therefore raises a possible question for future work.

Do people possess not only informational personal space, but also a form of **epistemic primacy**?

If so, it would not imply that individuals are always correct about themselves.

Rather, it would recognize that each person's first-person perspective occupies a privileged role that should not be casually displaced by external models, whether human or artificial.

AI systems may help people discover patterns, identify possibilities, or reflect upon their lives.

They should be cautious about presenting those models as more authoritative than the person's own ongoing process of self-understanding.

The concept of epistemic primacy remains provisional.

It may ultimately prove to be an important extension of informational personal space and a useful design principle for humane life computing.

## Summary

These everyday examples illustrate that the ethical questions explored in this document are not unique to artificial intelligence.

They arise whenever repeated observation becomes durable interpretation.

Artificial intelligence magnifies the phenomenon through persistence, scale, and statistical sophistication.

The underlying ethical question, however, remains the same.

How much knowledge should repeated observation be permitted to create?

Humane systems should recognize that repeated observation does not eliminate opacity.

Accumulated evidence may improve prediction while still failing to justify confident conclusions about another person's motives, values, circumstances, or character.

Respect for informational personal space therefore requires more than protecting access to information.

It also requires epistemic humility regarding what observations can legitimately support and respect for each person's ongoing role as the primary interpreter of their own life.
