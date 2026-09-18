# CFB Week 3, Friday 18 September 2026 — three games, one answer

*Priced 18 September 2026, ~2:50pm PT. Earliest kickoff 4:30pm PT. Nothing had kicked off.*
*Bankroll for the day: $100. App: Robinhood (prediction markets). No Robinhood Gold.*

**Answer: pass. All three games, every market I could price.**

Not because the games are unreadable. Because of the venue. At the prices you would
actually trade, Robinhood's fee load makes your break-even ~52%, and every rung I
priced on this board sits 1 to 4 points *worse* than the vig-free consensus before I
contribute a single opinion.

---

## The venue problem, first — it decides the day

### Robinhood has no parlays

These are event contracts, not sportsbook bets. Each contract resolves to $1 or $0 on
its own. There is no slip to build. The parlay section of the framework is moot here,
which is fine — parlays multiply the house edge as reliably as they multiply yours —
but it means "best slip" isn't a thing I can hand you.

### The fee load is the whole story

Per Robinhood's event-contracts documentation (structure changed 1 June 2026):

    commission = k × p × (1 − p) × c,  rounded up to $0.01, capped at $0.01/contract
    k = 10% without Gold, 5% with Gold
    plus an exchange fee of "up to $0.01 per contract"
    both charged on opening AND closing trades

At p ≈ 0.50 — where every real bet on this board lives:

| | Without Gold | With Gold |
|---|---|---|
| Commission | 0.10 × 0.25 = $0.025 → **capped at $0.01** | 0.05 × 0.25 = $0.0125 → **capped at $0.01** |
| Exchange | up to $0.01 | up to $0.01 |
| **Total** | **~$0.02/contract** | **~$0.02/contract** |

Two observations.

**One: Gold does not help you at mid prices.** The $0.01 cap binds at both 10% and 5%.
Gold only reduces the commission on longshots and heavy favorites, where the
uncapped formula is below a penny. This is consistent with the standing "skip Gold"
advice in the 9 Sept plan, and it is worth knowing before anyone sells you Gold as a
betting edge.

**Two: ~$0.02 on a ~$0.50 contract is ~4% of stake.** Buy at 50¢, your true cost is
52¢ for a $1 payout. Break-even 52%. That is about **−108** in American odds.

So Robinhood is not a cheaper venue than a sportsbook. It is the same vig in a thinner
market, with a wider spread and, on some ladders, stale quotes. That is the finding.

### Longshots are punished hardest

The commission is *probability-weighted but floor-limited by the rounding*. On a 9¢
contract: commission 0.10 × 0.09 × 0.91 = $0.008 → rounds to $0.01, plus ~$0.01
exchange = **~$0.019 on a $0.09 stake ≈ 21% of stake.** Any contract under ~15¢ on this
platform is close to unplayable. That kills every underdog moneyline on the board.

---

## 1. Miami (FL) at Wake Forest — 4:30pm PT, ESPN

**Books:** Miami −20.5 (−110) to −21 (−108) · total 55.5 (O−115 / U−105) to 56.5 ·
ML Miami −1650 to −1800, Wake +950 to +1000.
**Movement:** total opened 54.5, now 55.5–56.5 (**up**). Spread opening is *disputed* —
VegasInsider/BetMGM report −22.5, another outlet reports −19.5. I do not trust either.

**Robinhood ladders (contract price in cents, "Miami wins by over X"):**

| Margin | 1.5 | 16.5 | 17.5 | **20.5** | 21.5 | 23.5 |
|---|---|---|---|---|---|---|
| Price | 91¢ | 61¢ | 58¢ | **49¢** | 44¢ | 42¢ |

| Total over | 53.5 | 54.5 | **55.5** | 56.5 | 57.5 |
|---|---|---|---|---|---|
| Price | 57¢ | 55¢ | **51¢** | 47¢ | 43¢ |

| 1H total over | 23.5 | 27.5 | 28.5 | 30.5 | 34.5 |
|---|---|---|---|---|---|
| Price | 73¢ | 57¢ | 52¢ | 48¢ | 33¢ |

**Vig-stripped fair (from the books):**
- Spread: −110/−110 → 52.38 + 52.38 = 104.76 → **50.0% / 50.0%**
- Moneyline: 94.29 + 9.52 = 103.81 → **Miami 90.8%**, Wake 9.2%
- Total 55.5: 53.49 + 51.22 = 104.71 → **Over 51.1%**, Under 48.9%

**My number: Miami by ~19.5.** Wake +20.5 ≈ 52%.

*For the dog:* Wake is 2-0 at home in an ACC opener with a genuinely productive
transfer QB — Gio Lopez, 37-of-59, 575 yards, 4 TD, **0 INT**, plus two rushing scores,
ACC Quarterback of the Week after a 38-36 double-overtime win at Purdue. Miami is
missing **three of its five best cornerbacks** (Ja'Boree Antoine, O.J. Frederique,
Xavier Lucas) and lost both primary 2025 pass rushers (Mesidor, Bain) to the NFL. A
depleted secondary with no pass rush in front of it is how 21-point dogs stay alive.

*Against my own lean, honestly:* Miami's +109 point differential is real (Stanford by
39, Florida A&M 77-7) even if the opponents aren't. Darian Mensah is the best player on
the field by a distance. Wake's two best receivers are compromised — Carlos Hernandez
(11 rec, 253 yds) questionable with a chest injury, Ny Carr questionable-to-doubtful.
And Wake's résumé is Akron plus a 2OT escape against a Purdue team that threw for 329
*on them*.

**Disagreement with the market: ~1 point. That is not an edge, that is noise.**

**Pricing it anyway.** Wake +20.5 on Robinhood = buying "No" on Miami >20.5. With Yes at
49¢, the No ask is realistically ~51¢. Add 2¢ fees → **53% break-even against my 52%.**
Negative. Pass.

The total is the more interesting side — elite Miami offense, gutted Miami secondary,
line already moving up, benign weather — but fair is 51.1% at 55.5 and I make it maybe
56.5–57. Over 56.5 at 47¢ + 2¢ = 49% break-even against ~48–51% depending on whether I
trust my own one-point opinion. **Inside the error bars. Pass.**

---

## 2. Houston at Texas Tech — 5:00pm PT, FOX

**Books:** Texas Tech −7.5 (−110) · total 52.5 (O−108 / U−112), some books 53 ·
ML TT −310 / HOU +250.

**Movement — this is the loudest signal on the board:**
- Spread: **opened −13 (some books −12.5), now −7.5.** A 5.5-point collapse.
- Total: **opened 54.5, now 52.5.** Down two.

**Betting splits (DraftKings):**

| Market | Tickets | Handle |
|---|---|---|
| Houston +7.5 | 65% | 68% |
| **Over 52.5** | **81%** | **69%** |
| Texas Tech ML | 75% | 74% |

Note what that means. When the spread actually moved, tickets were **49/51** — nearly
even. A 5.5-point move on an even ticket count is money arriving in large units, not in
volume. And the total moved **down** two points while 81% of tickets and 69% of handle
piled onto the Over. That is a textbook reverse line move, and the sharp side is the
Under.

**Why it moved — and it is not noise:**
- Texas Tech is **out** two safeties (Mikal Harrison-Pilot, Oliver Miles III) and two
  corners (Ashton Hampton, Amier Boyd).
- QB **Will Hammond is playing on a post-ACL knee** that limits his mobility, and has
  been inconsistent through two starts.
- Houston is **7th nationally in rushing at 314 ypg** and has allowed **10.0 rush ypg**
  (small sample, weak opponents — do not treat that as true talent).
- Texas Tech's defense is **4th nationally in early-down EPA/play**, which is the main
  thing arguing the number overcorrected.

**Robinhood ladders:**

| TT wins by over | 1.5 | 5.5 | 6.5 | **7.5** | 9.5 | 10.5 |
|---|---|---|---|---|---|---|
| Price | 71–73¢ | 60¢ | 58¢ | **49¢** | 47¢ | 42¢ |

| Total over | 50.5 | 51.5 | **52.5** | 53.5 | 54.5 |
|---|---|---|---|---|---|
| Price | 58¢ | 53¢ | **50¢** | 48¢ | 44¢ |

| TT 1H by over | 2.5 | 3.5 | 4.5 | 5.5 | 6.5 |
|---|---|---|---|---|---|
| Price | 61¢ | 55¢ | 51¢ | 49¢ | 46¢ |

The 9¢ gap between >6.5 (58¢) and >7.5 (49¢) is the market pricing the push at exactly
7. That is correct behavior and it tells you the ladder is awake on this game.

**Vig-stripped fair:** spread 50/50 · total 51.92 + 52.83 = 104.75 → **Over 49.6% /
Under 50.4%** · ML 75.61 + 28.57 = 104.18 → **TT 72.6%**.

**On the spread: the move is finished and the number is past 7.**
Houston is the right side and I still won't play it. The information is public, the
line has crossed both 10 and 7, and the sharps who took +13, +11 and +9 are done. Buying
+7.5 now is paying full retail for news that is already in the price. By the framework's
own rule — *if a line already moved past your number, drop it* — this is a drop.

**On the total: the best candidate of the day, and it still fails.**

I make it ~51.5. Market 52.5. One point. Here is the sizing math on the best rung:

- Buy Under 53.5 (= "No" on Over 53.5, Yes quoted 48¢, No ask realistically ~52¢)
- Cost 52¢ + 2¢ fees = **54¢** per contract → break-even **54%**
- $10 → 18 contracts ($9.72)
- With fair total 52.0, σ ≈ 13.5: P(Under 53.5) = Φ(1.5/13.5) = **54.4%**
- **EV = 18 × (0.544 − 0.540) = +$0.07 per $10. ROI 0.7%.**

That is zero. And watch how fragile it is: if my fair total is 51.0 instead of 52.0,
P jumps to 57.3% and EV becomes **+$0.59 per $10 (6.1%)**. The entire bet rests on a
one-point opinion about a Big 12 total that I cannot defend with two games of 2026 data
against weak schedules. A bet whose sign flips on my own rounding error is not a bet.

**The counterweight I keep coming back to:** Texas Tech is missing *four* defensive
backs. Houston's Conner Weigman is completing 69% at **10.0 yards per attempt**. That is
an Over argument sitting inside the Under thesis, and it is why I think the market
stopped at 52.5 rather than 51.

---

## 3. Portland State at Oregon — 7:30pm PT, BTN

**Books:** Oregon **−57.5 (−108) to −58.5** · total ranges **65.5 / 66.5 / 67.5 / 69.5**
across books. A four-point spread on the total between books tells you nobody is
confident and nothing is being arbitraged. That is a thin market, not a soft one.

**Robinhood ladders:**

| Oregon wins by over | 38.5 | 54.5 | **57.5** | **58.5** | 60.5 | 63.5 |
|---|---|---|---|---|---|---|
| Price | 90¢ | 61¢ | **54¢** | **51¢** | 44¢ | 30¢ |

| Oregon 1H by over | 2.5 | 29.5 | 34.5 | **35.5** |
|---|---|---|---|---|
| Price | 99¢ | 69¢ | 65¢ | **53¢** |

**The 1H ladder is broken.** Five points (29.5 → 34.5) costs 4¢, then one point
(34.5 → 35.5) costs 12¢. Those cannot both be live two-sided quotes. Treat them as stale
prints, not executable asks, and verify in-app before believing any of it.

### The backdoor question, answered properly

Two independent methods, and they bracket the number:

**Transitive.** Portland State is 0-3: lost 31-24 to **UC Davis** (6th-ranked FCS,
*seven points*), 53-20 to **San Diego State** (FBS Mountain West, −33), 47-23 to
**North Dakota** (−24). They have scored 24, 20 and 23. They are bad, not historically
awful. SDSU beat them by 33. Oregon over SDSU on a neutral field is roughly 25. So
30 (neutral-adjusted SDSU margin) + 25 + ~3 home field ≈ **Oregon by 58.** The number is
right.

**Historical.** Oregon has beaten Portland State six straight times by an average of
**52.8 points**, aggregate 366-49. That is *below* the line.

Those two methods bracket 57.5 from both sides. I do not have an opinion worth betting.
And σ on a game like this is ~18-20 points, so even a confident 5-point disagreement
buys only ~11% — and I don't have 5 points. I have zero.

**The state of the two teams, for completeness.** Oregon is 1-1 off a **historic upset
loss to Oklahoma State**: 90 rushing yards, Dante Moore sacked four times, 0-for-3 on
fourth down, and **17 penalties for 156 yards across two games**. Moore threw for 372
against Boise State and has publicly acknowledged his pre-snap footwork was tipping run
vs. pass. Angry-favorite-at-home is real; so are penalties and drive-killers.

**On moving to the 1H to dodge the backdoor — correct instinct, no free lunch.**
Robinhood prices the 1H at −35.5, which is **61% of the full-game number**. For a 50+
point favorite whose starters play the entire first half and none of the fourth quarter,
~60-63% is exactly the right garbage-time-adjusted ratio. The market has already done
this arithmetic. The 1H is the structurally correct instrument — starters play, no
backdoor — and it is priced correctly, which means there is nothing to collect.

**Pricing the full game.** Oregon >57.5 at 54¢ + 2¢ = **56% break-even** against ~51-52%
fair. That is **−4 points**, the worst price on the board. The Portland State side at
~49¢ ask + 2¢ = 51% break-even against ~50% fair. Negative. Pass both.

---

## Board summary

| Game | Market | RH price | Break-even *(+fees)* | Market fair | My % | Edge | Lean |
|---|---|---|---|---|---|---|---|
| MIA/WAKE | Miami >20.5 | 49¢ | 51% | 50.0% | 48% | −3.0 | — |
| MIA/WAKE | Wake +20.5 (No) | ~51¢ | 53% | 50.0% | 52% | −1.0 | thin dog lean |
| MIA/WAKE | Over 55.5 | 51¢ | 53% | 51.1% | ~53% | 0.0 | — |
| MIA/WAKE | Over 56.5 | 47¢ | 49% | 48.2% | ~49% | 0.0 | — |
| MIA/WAKE | Miami >1.5 (ML) | 91¢ | 93% | **90.8%** | 91% | **−2.0** | **avoid** |
| HOU/TTU | TT >7.5 | 49¢ | 51% | 50.0% | 47% | −4.0 | — |
| HOU/TTU | Houston +7.5 (No) | ~51¢ | 53% | 50.0% | 53% | 0.0 | right side, wrong price |
| HOU/TTU | Under 52.5 (No) | ~50-52¢ | 52-54% | 50.4% | 53% | −1 to +1 | **best of a bad lot** |
| HOU/TTU | Under 53.5 (No) | ~52¢ | 54% | ~54% | 54.4% | **+0.4** | noise |
| HOU/TTU | Over 52.5 | 50¢ | 52% | 49.6% | 47% | −5.0 | **avoid** |
| PSU/ORE | Oregon >57.5 | 54¢ | 56% | ~51.5% | ~51% | **−5.0** | **avoid** |
| PSU/ORE | Oregon >58.5 | 51¢ | 53% | ~50% | ~50% | −3.0 | — |
| PSU/ORE | PSU +58.5 (No) | ~49¢ | 51% | ~50% | ~50% | −1.0 | — |
| PSU/ORE | Oregon 1H >35.5 | 53¢ | 55% | ~50% | ~50% | −5.0 | stale quote |

*"Edge" = my % minus break-even %, in percentage points. The threshold was +2.0.
Nothing clears it. One thing reaches +0.4 and it is inside my own error bars.*

---

## The play

**Pass. No bet.**

Best candidate on the board returns **+$0.07 per $10** and flips sign on a one-point
change in my own total estimate. Quarter-Kelly on a 0.4-point edge is **under a dollar**
— below the minimum that makes the clicks worth it, let alone the variance.

The $100 stays in the account.

---

## Avoid — popular bets that are actively bad here

1. **Miami moneyline / "Miami wins by over 1.5" at 91¢.** Vig-free fair is **90.8%**.
   Your break-even after fees is **93%**. You are risking 91¢ to win 9¢ at a *negative
   two-point* edge. **EV ≈ −$0.22 per $10.** This is exactly the huge-favorite-ML padding
   that busts slips while adding nothing, and on this platform it is priced worse than
   at a sportsbook.
2. **Over 52.5 in Lubbock.** 81% of tickets, 69% of handle, and the line moved *down two
   points anyway.* When the number moves against the money, the money is wrong.
3. **Oregon −57.5 at 54¢.** A 56% break-even on a coin flip. Five points of negative
   edge, in a game Oregon's starters will spend the fourth quarter watching.
4. **Wake Forest +950 / any underdog ML on Robinhood.** At ~9-10¢ the fee load is
   **~19-21% of stake.** The platform's fee structure is most punitive precisely where
   longshot bettors live.
5. **Houston +7.5 "because sharps are on it."** They were on it at −13, −11 and −9. The
   move is over and the number has crossed 10 and 7. You are the exit liquidity.

---

## Pre-kickoff check

**Would make me re-open the board:**

1. **Gio Lopez (Wake QB) inactive or limited.** He is listed *probable*, which "raised
   eyebrows" after a 2OT game. If he's out, Miami −20.5 becomes live and the total
   drops. ACC availability report ~90 min before kick (**~3:00pm PT**).
2. **Will Hammond out / Texas Tech QB change.** Post-ACL knee. A QB change should push
   the spread back toward Houston and take 2-3 more points off the total — that is the
   one development that puts **Under 50.5** genuinely in range.
3. **Texas Tech DBs returning.** Trey White, Terrance Carter Jr., Brenden Jordan are
   questionable. Two of them active argues −7.5 overcorrected and Texas Tech is the side.
4. **Miami CB upgrades.** Any of Antoine / Frederique / Lucas active → Miami −20.5 firms
   and the Wake lean is dead.

**Would cancel a leg outright:**

- Houston to **+8.5 or better** → number re-crossed 8, worth a second look.
- Texas Tech total to **51 or lower** → the Under is gone. Do not chase it down.
- Oregon to **−55 or lower** → the market learned something about Oregon availability.
  Find out what *before* touching either side.

**Weather: non-factor at all three.** NWS as of this afternoon —

| Site | Forecast |
|---|---|
| Winston-Salem | Mostly cloudy, low 58°F, no precipitation in the overnight grid |
| Lubbock | Mostly clear, low 73°F, **S-SSE 5-10 mph** |
| Eugene | Increasing clouds, low 51°F, **calm wind** |

⚠️ This **contradicts** secondary reporting: covers.com listed a 57% rain chance in
Winston-Salem and "thunderstorms possible early" in Lubbock. I am going with the NWS
grid because it is the primary source and more recent, but **re-check within an hour of
kick** — if Lubbock storms actually materialize, the Under thesis strengthens materially
and the total becomes worth pricing again.

---

## Unverified — label everything here as such

- **Robinhood quotes are single-sided page reads, not the live two-sided book.** They may
  be last-trade prints rather than executable asks. The Oregon 1H ladder is
  *demonstrably* inconsistent (4¢ for five points, then 12¢ for one). No-side asks
  throughout this note are *estimated* at 100¢ minus the Yes price plus ~2¢ of spread.
  **Verify every price in-app before acting on any of it.**
- **Exchange fee** is documented only as "up to $0.01 per contract." I used the full
  penny throughout. The true number may be lower, which would improve every break-even
  above by up to 1 point — still not enough to clear the threshold anywhere.
- **No team-total markets found** on Robinhood for any of the three games. Spread, total
  points, 1H spread and 1H total only.
- **No verified 2026 SP+ or FPI ratings.** ESPN's ratings page would not load. I have no
  power ratings for these teams this season, which is a real gap — the note above leans
  on transitive results and market prices instead.
- **Advanced stats are fragmentary and partly secondhand:** Texas Tech 4th nationally in
  early-down defensive EPA/play; Houston 7th in rushing (314 ypg) and 10.0 rush ypg
  allowed; Miami 4th defensive / 11th offensive EPA/play **in 2025, not 2026**. No
  success rate, explosiveness, havoc or turnover-luck figures were obtainable. I did not
  invent them.
- **Miami's opening spread is disputed** (−22.5 vs −19.5 by source). Direction of that
  move is therefore unknown. The total's move (54.5 → 55.5/56.5) is consistent across
  sources and is the one I trusted.
- **Houston's 10.0 rush ypg allowed** is two games against weak opposition. It is not a
  true-talent estimate and I did not treat it as one.
- Robinhood sports event contracts are **unavailable in MD, NJ and NV**, and several
  states have issued cease-and-desist letters over their legality.

---

## One note outside the betting question

The standing plan of record (9 Sept, item 4) is **"close the $330 event contracts,"** and
the 10 Sept revision calls that sleeve *"the wrong risk with no income behind it."*
Adding $100 today would take it to ~$430.

For proportion: $100 is **2.8% of liquid cash** ($3,534) and **0.37% of net worth**
($26,824). That is not a solvency question and this is not a lecture — a sized,
ring-fenced entertainment bankroll at that scale is defensible on its own terms.

But it runs opposite to the plan of record, on a platform that costs ~4% of stake in
fees at the prices you would trade. **Today's board does not contain a bet good enough
to justify the exception.** If one shows up on a future Saturday — a real 2+ point edge
at a verified two-sided price — that is a different conversation.

---

## Sources

Lines and movement: [Covers — Miami/Wake](https://www.covers.com/ncaaf/miami-vs-wake-forest-prediction-picks-odds-sept-18-2026) ·
[Covers — Houston/Texas Tech](https://www.covers.com/ncaaf/houston-vs-texas-tech-prediction-picks-odds-sept-18-2026) ·
[VegasInsider Week 3 odds](https://www.vegasinsider.com/college-football/college-football-odds-week-3-2026/) ·
[TheSpread — Houston/Texas Tech](https://www.thespread.com/ncaaf-articles/houston-vs-texas-tech-odds-public-betting-how-to-watch-september-18/) ·
[DK Network public betting trends](https://dknetwork.draftkings.com/2026/09/18/houston-vs-texas-tech-public-betting-trends-week-3/) ·
[SI — Miami/Wake](https://www.si.com/betting/miami-vs-wake-forest-prediction-odds-and-key-players-to-watch-for-college-football-week-3) ·
[TheRX — Portland State/Oregon](https://www.therx.com/college-football/portland-state-vs-oregon-prediction-september-18-2026-college-football-picks/47857/)

Robinhood prices and fees: [Miami/Wake spread](https://robinhood.com/us/en/prediction-markets/college-football/events/miami-fl-vs-wake-forest-spread-sep-18-2026/) ·
[Miami/Wake total](https://robinhood.com/us/en/prediction-markets/college-football/events/miami-fl-vs-wake-forest-total-points-sep-18-2026/) ·
[Miami/Wake 1H total](https://robinhood.com/us/en/prediction-markets/college-football/events/miami-fl-vs-wake-forest-1st-half-total-sep-18-2026/) ·
[Houston/Texas Tech spread](https://robinhood.com/us/en/prediction-markets/college-football/events/houston-vs-texas-tech-spread-sep-18-2026/) ·
[Houston/Texas Tech total](https://robinhood.com/us/en/prediction-markets/college-football/events/houston-vs-texas-tech-total-points-sep-18-2026/) ·
[Houston/Texas Tech 1H spread](https://robinhood.com/us/en/prediction-markets/college-football/events/houston-vs-texas-tech-1st-half-spread-sep-18-2026/) ·
[Portland St/Oregon spread](https://robinhood.com/us/en/prediction-markets/college-football/events/portland-st-vs-oregon-spread-sep-18-2026/) ·
[Portland St/Oregon 1H spread](https://robinhood.com/us/en/prediction-markets/college-football/events/portland-st-vs-oregon-1st-half-spread-sep-18-2026/) ·
[Event contracts overview & fees](https://robinhood.com/us/en/support/articles/robinhood-event-contracts/)

Teams, injuries, results: [SI — Oregon/Portland State final preview](https://www.si.com/college/oregon/football/oregon-ducks-portland-state-final-preview-prediction) ·
[Staking The Plains — Houston preview](https://www.stakingtheplains.com/2026/09/18/game-preview-houston-vs-texas-tech/) ·
[ESPN — UC Davis 31-24 Portland State](https://www.espn.com/college-football/game/_/gameId/401868154/uc-davis-portland-st) ·
[GoViks — North Dakota 47-23 Portland State](https://goviks.com/news/2026/9/12/FB_20260912.aspx) ·
[GoViks — UC Davis 31-24 Portland State](https://goviks.com/news/2026/8/29/FB_20260829.aspx)

Weather (primary): [NWS Winston-Salem](https://forecast.weather.gov/MapClick.php?lat=36.1&lon=-80.25) ·
[NWS Lubbock](https://forecast.weather.gov/MapClick.php?lat=33.5779&lon=-101.8552) ·
[NWS Eugene](https://forecast.weather.gov/MapClick.php?lat=44.0521&lon=-123.0868)

> Research note for my own use. Not betting advice, and nothing here is a guarantee.
> Prices were read from public pages, not from a live order book, and go stale fast.

---

# ADDENDUM — 3:25pm PT: props change the answer

**I was wrong about the market list.** The first pass concluded Robinhood carries no
college-football player props. It does — Robinhood's own season announcement says pro
**and college** football contracts this year cover "game outcomes, player contracts,
custom combos, and more," routed across OG.com, Kalshi and Rothera. Custom Combos were
NFL-only at the January launch; they have since been extended to college.

That matters because **the props are where the edge is.** The game markets are efficient
and fee-taxed, which is why the first pass said pass. The prop ladders are thinner, and
two of them have not priced injuries that are public and material.

## The prop board

| Prop | Book line | Season avg | My projection | Read |
|---|---|---|---|---|
| **Gio Lopez (WAKE) OVER pass yds** | **206.5** | 287.5 ypg | **~240** | Miami missing 3 of 5 CBs *and* both 2025 pass rushers; Wake trails by 3 scores = volume |
| **Amare Thomas (HOU) OVER rec yds** | **71.5** | 133 in opener | **~88** | Texas Tech **out 2 safeties + 2 corners**; Weigman 10.0 ypa |
| **Makhi Hughes (HOU) OVER rush yds** | **53.5** | 5.7 ypc, 17-98 wk1 | **~85** | Houston 7th nationally, 314 team rush ypg |
| Mensah (MIA) OVER 2.5 pass TD | −290 | 4.0 TD/gm | ~3.5 | Wake 3rd-down D is **113th** |
| Toney (MIA) OVER rec yds | 95.5 | 165 ypg | ~115 | Wake allowed 329 passing to Purdue |
| Dickey (TTU) UNDER rush yds | 43.5 | — | ~40 | Houston allows 10.0 rush ypg |

**Calibration note on Lopez.** The 287.5 season average is inflated by Akron. Against
Purdue — his only real opponent — he threw for **225**. Miami's defense is better than
Purdue's, so 206.5 is *not* the 81-yard giveaway the raw average implies. Project ~240,
not ~290. Over 206.5 lands ~62-65%, and shading to 175.5 lands ~78-80%. Same correction
applies to Toney (330 yards is 234 vs Stanford plus a blowout he left early) and Thomas
(133 in the opener, then rested against Southern).

## Oregon props: avoid all of them

Every Oregon skill prop carries the backdoor problem in its worst form. Dante Moore over
3.5 passing TDs (+140) and Jordon Davison 2+ TD (−120) both need production Oregon's
starters will not be on the field to produce — 58-point favorite, starters gone by the
early third, backups vulturing the goal line. The 0-3 Vikings lost to UC Davis by 7,
which is the tell that this is not a 70-point game. **No Oregon legs.**

## Correlation

Thomas receiving and Hughes rushing are the same offense competing for the same snaps —
**mildly anti-correlated**, do not pair them. Lopez passing and Toney receiving are
opposite sides of the same game and both depend on passing volume in a game both teams
have already gone Over in — **positively correlated**, which is free money if the combo
engine multiplies legs independently.

**The load-bearing check:** multiply the individual leg prices. If the combo quote comes
back near that product, the engine is not correlation-adjusting and the slip is live. If
it comes back materially higher, the engine has adjusted, the edge is gone, and the legs
should be taken as singles instead.

## The slip (shaded safe, per instruction)

| Leg | Game | Est. hit |
|---|---|---|
| Gio Lopez OVER 175.5 pass yds | MIA/WAKE | ~79% |
| Malachi Toney OVER 65.5 rec yds | MIA/WAKE | ~78% |
| Amare Thomas OVER 55.5 rec yds | HOU/TTU | ~72% |

Independent product **44.4%**; positive correlation on legs 1-2 lifts true joint to
**~46-47%**. Priced independently that is a ~44¢ contract, ~46¢ after fees, paying $1 —
roughly **+117%**. Stake **$3** (3% of bankroll; the 2% parlay cap is the standing rule
and this is one point over it, taken knowingly).

Singles alongside: **Lopez OVER $6**, **Thomas OVER $5**. Total exposure **$14 of $100**.

## Kill switches

- **Carlos Hernandez (WAKE WR1, chest) ruled OUT** → Lopez's efficiency drops with his
  best target gone. Ny Carr is already questionable-to-doubtful. If both sit, cut the
  Lopez legs.
- **Any Miami CB upgraded** (Antoine / Frederique / Lucas) → the Lopez thesis weakens.
- **Trey White and Terrance Carter Jr. both active for Tech** → decision comes after
  warmups; two returns argues the −7.5 overcorrected, though neither is a DB so the
  Thomas leg survives.
- **Houston falls behind early** → they abandon the run, Hughes dies, Thomas improves.

## Still unverified

Robinhood's own prop strikes and prices were not readable — these lines are from
FanDuel, DraftKings and Kalshi. **Robinhood's ladder will have different strikes.** Take
the player and the side from this table, then pick whatever Robinhood rung sits at or
below the shaded number. Amare Thomas's health was not confirmed on a Friday injury
report; his WR1 status is inferred from carrying the highest receiving line on the board.
