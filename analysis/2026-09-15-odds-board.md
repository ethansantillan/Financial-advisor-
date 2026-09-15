# The Cloture Odds Board

**Written:** 15 September 2026, 00:43 ET (~13h before the roll call)
**Question:** "What's the percentage we make money after the bill tmr."
**Artifact:** https://claude.ai/artifact/GTt2C3ApmLG4YA52Ykux2R
**Model code:** `analysis/2026-09-15-outcome-model.py`

---

## The answer

**~35% chance the portfolio is worth more on Wednesday night than it is now.**
Expected change **−$256 (−0.95%)**. Median **−$597**. 200,000-run Monte Carlo.

| Percentile | Change |
|---|---|
| 5th | −$2,352 (−8.70%) |
| 25th | −$1,432 |
| 50th | **−$597 (−2.21%)** |
| 75th | +$728 |
| 95th | +$2,985 (+11.04%) |

Right-skewed but negatively centred — the signature of a lottery ticket.

---

## The board

| Branch | Probability | P(portfolio up) |
|---|---|---|
| Cloture clears (60+) | **35%** | 91% |
| Cloture fails | **55%** | 3% |
| Thune pulls the vote | **10%** | 23% |

P(make money) ≈ P(cloture) + 1pt. **The whole thing collapses to one question.**

---

## Correction: where my "~33%" last night was wrong

I gave him "~33%" and described it as the cloture probability. **That was a category error.**
Polymarket's 25–30% prices **H.R. 3633 being signed into law by 31 Dec 2026**; Kalshi's
24–32% prices market-structure law before 2027. Both are *strictly harder* than clearing
cloture. Cloture is the first of several gates, so **P(cloture) must exceed the headline
number, not equal it.**

Reverse-engineering from the 28% midpoint:

| Path | Chance | × becomes law 2026 | Contribution |
|---|---|---|---|
| Cloture clears today | 35% | 65% | 22.8% |
| Vote pulled, revived | 10% | 25% | 2.5% |
| Cloture fails, revived | 55% | 5% | 2.8% |
| **Implied P(signed 2026)** | | | **28.0%** ✓ |

Reproduces the market price. **The model is a decomposition of the market's view, not an
independent one** — if the market is wrong, so is this.

---

## The whip count, by name

- **53 Republicans.** Paul and Hawley reliable no → **51**.
- **Tillis has probably flipped back to yes.** He said it fails *"if there's no interest in
  the White House in trying to bridge the gap on the ethics language."* The White House
  bridged it over the weekend (~80% of the Democratic ask). **His stated condition for a no
  has been removed. I had him as a defection on 15 Sept — that looks wrong.**
- **9–10 Democrats needed.** Seven said publicly the bill falls short: **Alsobrooks, Booker,
  Cortez Masto, Gallego, Hickenlooper, Warner, Warnock.** These are the negotiating bloc,
  not opponents; their stated objection was ethics.
- **Gillibrand's condition:** enforceable prohibition on presidents/senior officials
  profiting from crypto. New language: divest or blind trust, $500k penalties, state-AG
  enforcement.
- **The binding constraint is the clock, not the substance.** 635 pages, <48 hours. "I
  haven't read it" is an easy no — and a *procedural* one, not permanent.

---

## Sensitivity — the only assumption that matters

| If P(cloture) is… | P(make money) | Expected | Implied P(law 2026) |
|---|---|---|---|
| 20% | 22% | −$683 | 19% |
| 30% | 31% | −$397 | 25% |
| **35% (estimate)** | **36%** | **−$252** | **28%** |
| 45% | 45% | +$43 | 34% |
| 60% | 58% | +$458 | 43% |

**Cloture must beat a coin flip before tomorrow is positive-EV.** No published whip count
supports that.

---

## The reframe: even the bull case barely gets him back

Robinhood XRP basis $1.9340, spot $1.42, 2,287.4935 coins.

| XRP reaches | Move | Sleeve P/L |
|---|---|---|
| $1.55 | +9% | −$878 |
| $1.70 | +20% | −$535 |
| $2.00 (analyst upside) | +41% | **+$151** |

**The single best realistic outcome tomorrow leaves him $151 ahead on that position.**
This vote was never the thing that fixes his XRP. Worth saying plainly — he has been
treating 15 September as the recovery event for a month.

## Second correction: "dead until 2029" was too strong

I have repeated that line for weeks. **Kalshi prices ~53% that market-structure law
arrives before October 2027.** If the likeliest failure is "635 pages, 48 hours, not yet"
rather than "never," a failed cloture kills the 2026 window, not the bill. Overstated.

---

## Recommendation

- **Don't buy into it.** 35% with negative EV.
- **Don't sell either.** Same math backwards — a 35% chance of a sharp gap up is exactly
  what selling hands away, and the horizon is 2029.
- **At these odds neither action has an edge, so the one with no tax bill wins.** Hold.
- Expected −$256 is 0.95% of net worth. Worth understanding, not worth losing sleep over.

## Weakest link, stated

Branch probabilities are disciplined (calibrated to a live market). **The price-reaction
magnitudes within each branch are my judgement and are the weak part of the model.**

## Sources

- [DeFiRate — CLARITY fact sheet and market odds](https://defirate.com/clarity-act-fact-sheet/)
- [Bitcoin.com — Rounds and Tillis on the odds](https://news.bitcoin.com/regulation-and-legal/clarity-act-republican-senators-fail-white-house-ethics/)
- [The Hill — White House ethics language](https://thehill.com/policy/technology/6087405-white-house-accepts-clarity-act-ethics/)
- [CryptoPotato — XRP downside if the vote fails](https://cryptopotato.com/what-happens-to-xrp-if-the-clarity-act-vote-fails-on-september-15-ai-maps-the-downside/)
- [CBS News — Fed hike odds after CPI](https://www.cbsnews.com/news/fed-rate-hike-september-likelihood-cpi/)
