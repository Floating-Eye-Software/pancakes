# Quality of Life Framework Design Input

Source image: `quality-of-life.png`

Reference: Statistics Canada's Quality of Life Hub, https://www.statcan.gc.ca/hub-carrefour/quality-life-qualite-vie/index-eng.htm

## Purpose

This note translates Canada's Quality of Life Framework into design input for Pancakes.

The framework is useful because it treats well-being as more than income, productivity, or individual health behaviour. It combines economic security, health, relationships, environment, safety, institutional trust, subjective well-being, fairness, and long-term resilience.

For Pancakes, this is a strong public-health and public-policy anchor. It can help prevent the product from collapsing into a narrow habit tracker, chore economy, gig board, or budgeting app.

## Framework Summary

Statistics Canada describes the Quality of Life Framework as a high-level national framework for monitoring key determinants of well-being for people living in Canada. The framework has 92 indicators across five domains and three central indicators. It also applies two cross-cutting lenses across the domains: fairness and inclusion, and sustainability and resilience.

Central indicators:

- Life satisfaction.
- Sense of meaning and purpose.
- Future outlook.

Domains:

- Prosperity.
- Health.
- Society.
- Environment.
- Good governance.

Cross-cutting lenses:

- Fairness and inclusion.
- Sustainability and resilience.

## Design Interpretation

Pancakes should treat quality of life as a multidimensional household and community state, not as a single score.

The product can help people coordinate care, routines, service exchange, budgeting, local support, and reflection. It should not pretend to measure a person's worth, rank households, or prescribe one universal model of a good life.

Better product framing:

```text
What conditions help this person, household, or node live well?
What support is missing?
What can the household or community safely coordinate?
What is improving, worsening, or becoming fragile?
```

Avoid product framing:

```text
Who is winning?
Who is productive enough?
Who has the best lifestyle score?
Which household creates the most platform value?
```

## Pancakes Domain Mapping

### Central Indicators

Central indicators are subjective and should remain self-reported or gently reflected, not inferred from surveillance.

Pancakes uses:

- Lightweight check-ins for life satisfaction.
- Reflection prompts for meaning and purpose.
- Hope/future-outlook prompts for household planning.
- Periodic review of whether routines, services, and covenants are helping.

Guardrails:

- Do not infer mental state from task completion alone.
- Do not expose central indicators to employers, schools, or service providers by default.
- Do not use subjective well-being indicators as eligibility gates for help.

### Prosperity

StatCan's prosperity domain includes income and growth, employment and job quality, skills and opportunity, and economic security and deprivation.

Pancakes uses:

- Household budgeting and cash-flow planning.
- Food, housing, transport, childcare, and internet-access support.
- Skill-building covenants.
- Service exchange that recognizes useful work without forcing all care into wage logic.
- Economic shock planning, such as emergency meals, emergency rides, and short-term household coverage.

Relevant product objects:

- Budget.
- Household account.
- Resource need.
- Service offer.
- Service request.
- Skill.
- Covenant.
- Local credit.
- Emergency plan.

Guardrails:

- Keep Pancakes credits separate from money unless explicitly posted through a financial/accounting boundary.
- Avoid race-to-the-bottom gig pricing.
- Avoid public poverty markers or shame-based budget views.

### Health

StatCan's health domain includes healthy people and health care systems. The image highlights self-rated mental health, self-rated health, physical activity, healthy eating, access to care, unmet needs, home care, and medication affordability.

Pancakes uses:

- Gentle routines for food, movement, rest, medication reminders, and appointments.
- Support requests for rides, meal preparation, home care logistics, and care coordination.
- Household visibility into care tasks where the affected person consents.
- Low-pressure tracking of barriers, not only behaviours.

Relevant product objects:

- Health-adjacent routine.
- Care task.
- Appointment.
- Meal plan.
- Medication reminder.
- Support request.
- Consent boundary.
- Care circle.

Guardrails:

- Pancakes is not a medical device by default.
- Avoid diagnosis, treatment claims, or clinical triage unless deliberately designed and governed for that use.
- Health data should be private by default and separable from service-market data.

### Society

StatCan's society domain includes culture and identity, social cohesion and connections, and time use. The image highlights belonging to local community, someone to count on, trust in others, time use, and satisfaction with time use.

Pancakes uses:

- Mutual aid and service exchange.
- Local groups, guilds, households, and nodes.
- Relationship-aware scheduling.
- Time-use reflection.
- "Someone to count on" support maps.
- Community practices, gatherings, volunteering, recreation, and cultural participation.

Relevant product objects:

- Household.
- Node.
- Guild.
- Care circle.
- Trust relationship.
- Availability.
- Time block.
- Community event.
- Volunteering record.

Guardrails:

- Social connection should not become coercive availability.
- Trust should be contextual, soft, and revocable.
- Avoid public leaderboards for volunteering, care work, or friendship.

### Environment

StatCan's environment domain includes environment and people, ecological integrity, and stewardship. The image highlights air quality, drinking water, climate adaptation, disasters, local environment satisfaction, walkable communities, public transit, greenhouse gas emissions, conserved areas, water quality, natural capital, waste management, and marine/coastal ecosystems.

Pancakes uses:

- Location-aware but privacy-preserving local resources.
- Walking, transit, errands, food, gardening, repair, reuse, and waste-reduction workflows.
- Community preparedness for heat, storms, outages, smoke, and other disruptions.
- Environmental context for service exchange, such as local pickup, shared rides, or neighbourhood repair.

Relevant product objects:

- Local resource.
- Map marker.
- Preparedness plan.
- Repair service.
- Garden task.
- Transit/routing note.
- Climate event.
- Waste/reuse flow.

Guardrails:

- Location sharing must be off by default.
- Use approximate location where possible.
- Avoid exposing home addresses, child locations, or domestic-safety-sensitive places.

### Good Governance

StatCan's good governance domain includes safety and security, democracy and institutions, justice and human rights. The image highlights personal safety, confidence in institutions, discrimination and unfair treatment, neighbourhood safety, emergency preparedness, misinformation/trust in media, and access to justice.

Pancakes uses:

- Clear household and node governance.
- Steward/custodian roles.
- Dispute handling.
- Safety rules for service exchange.
- Transparent credit rules.
- Consent and appeal paths.
- Community moderation and incident records.

Relevant product objects:

- Node policy.
- Role.
- Permission.
- Dispute.
- Incident.
- Moderation action.
- Rule change.
- Consent record.
- Audit trail.

Guardrails:

- Governance should support safety and fairness, not surveillance.
- Moderation and dispute records need privacy controls and retention rules.
- Users need a way to pause, exit, appeal, and export their data.

## Cross-Cutting Lenses

### Fairness and Inclusion

StatCan frames this lens as assessing the distribution of outcomes across different populations to support equity and equality.

Pancakes translation:

- Check who benefits and who carries burden.
- Design for disability, language, age, income, caregiving status, rural/urban context, and digital access.
- Make help discoverable without requiring social status or technical fluency.
- Let households and nodes adapt rules locally while preserving baseline rights.

Design questions:

- Who cannot use this workflow?
- Who is made visible in a risky way?
- Who is asked to provide care without enough power to decline?
- Which users need offline, low-bandwidth, low-literacy, or assisted modes?

### Sustainability and Resilience

StatCan frames this lens as long-term thinking about indicator trajectories, risks, resilience, and future quality of life.

Pancakes translation:

- Track whether routines are sustainable, not just completed.
- Support preparedness for shocks.
- Avoid creating dependence on a single platform operator.
- Let nodes continue local coordination when internet, money, transport, or institutional support is strained.

Design questions:

- Does this workflow still work during stress?
- Does it create burnout?
- Does it preserve local capacity?
- Can a household or node recover after conflict, outage, illness, or financial shock?

## Measurement Approach

Pancakes should not create one global Quality of Life score.

Use a layered model instead:

- Personal reflection: private check-ins and notes.
- Household state: routines, needs, plans, and consented shared tasks.
- Node state: service availability, disputes, resource gaps, and local resilience.
- Public-data context: StatCan indicators, shown as background context rather than personal diagnosis.

Possible status shapes:

- Missing support.
- Stable support.
- Improving support.
- Fragile support.
- Overburdened support.
- Needs review.

This language is safer than ranking, scoring, or optimizing people.

## Integration With Existing Pancakes Ideas

Service exchange:

- Connects most strongly to Society, Prosperity, Good Governance, and Health.
- Needs fairness checks so low-income or high-care-burden users are not pushed into serving others for survival.

Household covenants:

- Can support Health, Society, Prosperity, and central indicators.
- Should include consent, privacy boundary, witness/ratification, and review.

Pancakes Earth:

- Connects to Environment, Society, Health, and Good Governance.
- Must use privacy-preserving location and context-aware safety rules.

Credits:

- Can coordinate service exchange and recognition.
- Should not stand in for money, health outcomes, moral worth, or quality of life.

Pitchfork integration:

- Can make support, routines, and care symbolically meaningful.
- Should cap rewards and avoid turning life problems into grind loops.

## Candidate Feature Set

First slice:

- Quality-of-life domain tags for tasks, services, covenants, and resources.
- Private well-being check-ins for life satisfaction, meaning, and future outlook.
- Household support map: who can help with what, under what boundaries.
- Service requests linked to needs, not only categories.
- Node risk register for safety, privacy, burden, and resilience.

Second slice:

- Public-data reference panels using StatCan Quality of Life indicators.
- Local resource map with approximate location.
- Time-use reflection and overload detection.
- Preparedness planning for household and node disruptions.
- Equity review checklist for new node policies or service categories.

Do later:

- Automated recommendations.
- Cross-node benchmarking.
- Public dashboards.
- Any health-risk, financial-risk, or safety-risk inference.

## Data Model Sketch

```text
QualityOfLifeDomain
  id
  name
  source

QualityOfLifeSubdomain
  id
  domain_id
  name

QualityOfLifeIndicator
  id
  subdomain_id
  name
  headline
  subjective
  source_url

WellbeingCheckIn
  id
  person_id
  indicator_id
  value
  note
  visibility
  created_at

Need
  id
  household_id
  domain_id
  description
  urgency
  privacy_level
  status

SupportAction
  id
  need_id
  service_id
  covenant_id
  task_id
  status

NodeQoLReview
  id
  node_id
  period
  fairness_notes
  resilience_notes
  risks
  decisions
```

## Open Questions

- Should Quality of Life domains be visible UI tags, internal metadata, or both?
- How should Pancakes separate health-adjacent support from regulated medical functionality?
- Can a household opt into central indicators without sharing them with the node?
- Should public StatCan indicators be cached locally, fetched live, or linked only?
- What is the minimum governance model for a node that handles service exchange?
- How should Pancakes represent burden, burnout, and unmet needs without shaming people?

## Recommendation

Use the Quality of Life Framework as a design compass and taxonomy, not as a scoring engine.

The strongest Pancakes fit is:

```text
private reflection
+ household support coordination
+ local service exchange
+ node governance
+ public-data context
```

The framework should help Pancakes ask better questions about well-being, equity, and resilience. It should not become a universal dashboard that ranks people, households, or communities.
