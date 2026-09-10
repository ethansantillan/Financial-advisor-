# Twenty-One Tickers, One Bet

**Date:** 10 September 2026
**Request:** "Take a long time and research all of these stocks and tell me which ones to invest into with my money in my Robinhood account. If u want me to put it into my Roth IRA as well that is also good."
**Artifact:** https://claude.ai/code/artifact/db8d75f6-6904-4682-8f53-5b065bb56936

---

## 0. Three ticker errors, before anything else

These are in the list as given. Two of them would have bought something other than what was intended.

| As listed | What it actually is | What was probably meant |
|---|---|---|
| **EWI** — "iShares MSCI Italy ETF, noted as a proxy for the Korean market" | iShares MSCI **Italy** ETF. Italy. Milan. Ferrari, Enel, UniCredit. It has no Korean exposure of any kind. | **EWY** — iShares MSCI South Korea ETF (Samsung ~25%, SK Hynix ~12%). That is the memory-cycle proxy. |
| **KOSPI** | An **index**, not a security. There is no US-listed ticker "KOSPI." Nothing to buy. | Again **EWY**, or nothing. |
| **MUU** | Direxion Daily MU Bull **2× Shares** — a leveraged single-stock ETF that resets daily. Not a share class of Micron. | **MU** itself, if the intent was Micron exposure. |

The Italy one matters. A buy order for EWI executes cleanly, shows a normal-looking ETF in the account, and delivers zero of the exposure it was bought for. Nothing about the confirmation screen would flag it.

---

## 1. The finding that matters more than any individual name

All 21 tickers are the same bet.

Power (BE, VST, GEV, VRT) → they sell electricity and cooling **to data centres**.
Chips (INTC, MRVL, AVGO, AMD, SOXL, SMH, SOXX) → they sell silicon **to data centres**.
Data centre (IREN, CIFR, CLSK, WULF, NBIS) → they **are** data centres.
Memory (MU, MUU, DRAM) → they sell HBM **to data centres**.

One demand curve. If AI capital expenditure decelerates, every one of these falls together, because they all get paid out of the same budget line at the same handful of buyers.

And the account is already positioned this way:

| Bucket | Share of net worth |
|---|---|
| Crypto (XRP, BTC, SOL, DOGE, ETH) | 48.7% |
| NVDA | 3.3% |
| META | 2.4% |
| **Total already in the same risk factor** | **~54.4%** |

Crypto belongs in that count. It is not a diversifier here — it is a long-duration, liquidity-sensitive risk asset that sells off in the same weeks these names do. Buying more of this list is not diversification. It is adding to the position that already exists.

That does not mean buy none of it. It means the correct question is not "which of these 21," it is "how much more of this factor, and through what."

---

## 2. Leverage decay, with the actual numbers

SOXL is 3× the daily return of the semiconductor index. Over five years:

| | 5-year return |
|---|---|
| **SOXL** (3× daily) | **+478.93%** |
| **SMH** (1×) | **+403.72%** |

Three times the daily exposure bought about **75 percentage points** over five years — roughly 1.19× the unlevered fund's return, for 3× the leverage and something close to 3× the drawdowns, through one of the best five-year stretches semiconductors have ever had.

Why: the fund resets daily, so the return path compounds, not the return. Drag is approximately `0.5 × L × (L−1) × σ²` per day. At L=3 that is 3σ² daily.

The illustration that makes it concrete — an index that goes nowhere:

| Day | Index | SOXL |
|---|---|---|
| Start | 100.0 | 100.0 |
| +10% | 110.0 | 130.0 |
| −9.09% | 100.0 | 94.5 |
| +10% | 110.0 | 122.9 |
| −9.09% | 100.0 | 89.4 |
| **Net** | **0.0%** | **−10.6%** |

The index is exactly flat. The 3× fund is down. Nobody made a bad call; the structure did it. Same mechanism, worse, applies to MUU on a single stock.

These are day-trading instruments held for hours. In a 42-year retirement account they are a way to lose money while being right.

---

## 3. The screen

### Buy — core

**SMH** (VanEck Semiconductor, 0.35%) or **SOXX** (iShares, 0.34%). Pick one, not both — holdings overlap ~73%. SMH is more concentrated in the top names; SOXX is slightly broader. Either one is the whole chip sector in a single line, and it removes the single-company risk that INTC and AMD each carry individually.

**AVGO** (Broadcom) — the best individual name on the list. Expected to hold roughly **60% of the custom AI accelerator (ASIC) market by 2027**; AI revenue expected around **$100B in FY2027**. This is the pick-and-shovel position on the hyperscalers building their own silicon rather than buying NVIDIA's — which is the direction the largest buyers are actively moving. Trades near **65× earnings**, so it is not cheap; it is a quality-at-a-price position, not a value one.

### Watch — real businesses, wrong entry price or unproven

- **GEV** (GE Vernova) — the strongest fundamentals in the power group. **$176B backlog**, equipment orders **+88%**. Gas turbine slots are sold out into the back half of the decade. But **P/E above 52** already prices most of that. Excellent company, demanding entry.
- **VRT** (Vertiv) — thermal management and power distribution for data centres. Genuine backlog growth. Very high beta to the same capex line.
- **MU** (Micron) — HBM is sold out well into next year and pricing is strong. Memory is the most violently cyclical corner of semis; the stock has already run hard on that cycle. This is a good business at a late-cycle price.
- **NBIS** (Nebius) — real GPU cloud with real contracted revenue, but early and capital-hungry.
- **BE** (Bloom Energy) — fuel cells, on-site power, genuine data-centre deals. Still not consistently profitable.
- **VST** (Vistra) — the cleanest way to own actual generation with nuclear in the mix. Already re-rated substantially on the data-centre-power thesis.
- **MRVL** (Marvell) — custom silicon and optics, but it is the number-two player in AVGO's market and has lost ground on specific programme wins.
- **DRAM** — thin, narrow memory ETF. MU direct is the cleaner expression.
- **CIFR / WULF / IREN** — bitcoin miners pivoting to AI hosting. IREN has the most credible pivot of the three. But this is a **double exposure to risk already owned**: bitcoin price *and* AI capex, in leveraged, capital-intensive, dilution-prone equities. Given crypto is already 48.7% of net worth, these stack risk rather than spread it.

### Pass

- **AMD** — a real second source to NVIDIA, but priced as though the MI-series is already winning. The gap in software ecosystem is the entire question and it is not resolved.
- **INTC** — a turnaround with government money attached. Foundry has not proven it can win external customers at scale. Multi-year, binary, and not a retirement-account core holding.
- **CLSK** — the weakest balance sheet of the miner group and the least developed AI pivot.

### Avoid

- **SOXL** — see section 2.
- **MUU** — 2× daily on a single volatile stock. Worse than SOXL structurally.
- **EWI** — Italy. Not Korea.
- **KOSPI** — not purchasable.

---

## 4. The macro risk, stated plainly

Roughly **$400B a year** is being spent on AI infrastructure against roughly **$100B** of enterprise AI revenue. That gap can close by revenue rising to meet spend, or by spend falling to meet revenue. Both are live.

Index concentration in the largest names is at levels last seen in 2000. And there is a live cautionary example: a hedge fund concentrated in SK Hynix and CoreWeave fell from about **$45B to roughly $10B** — those were correct calls on the theme, held in the wrong size.

The theme being right does not protect a position that is too large.

---

## 5. What to actually do

Available: ~$2,026 Robinhood cash, ~$1,408 HYSA at 3.30%, plus $4,800 of remaining 2026 Roth room ($2,700 of $7,500 already contributed).

**Use the Roth, not the taxable account.** Every one of these is a growth position expected to compound for 42 years. In the Roth that compounding is never taxed. In the taxable account it generates a capital gains bill on every rebalance. Same stocks, same thesis — the Roth is worth materially more over that horizon. Robinhood also matches 1% on Roth contributions with no Gold subscription needed.

**Proposed $2,500 into the Roth:**

| Position | Amount | Share | Why |
|---|---|---|---|
| **VTI or VOO** | $1,500 | 60% | The part that is not a bet. Broad market. This is the diversification the account does not currently have. |
| **SMH** | $600 | 24% | The whole chip sector, one line, no single-company risk. |
| **AVGO** | $400 | 16% | The single best name on the list. |

That leaves roughly **$1,034 liquid** — the Robinhood cash stays as cash, which is what makes it possible to not sell anything in a drawdown.

The 60% index allocation will look boring next to the tickers on this list. That is the point. The account already has 54.4% in the exciting version of this bet. What it does not have is a floor.

---

## 6. Still open

- **Annual income** — asked several times, not yet answered. This determines whether long-term capital gains are taxed at **0%** or 15%, which changes the taxable-account plan entirely.
- **Kraken XRP cost basis** — needed for any tax-loss planning there.
- **The $350 BE order** — intent unclear.
