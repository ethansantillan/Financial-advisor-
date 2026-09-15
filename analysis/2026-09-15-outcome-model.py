import random, statistics as st
random.seed(7)
N=200_000

# --- Portfolio (live, 15 Sep 00:43 ET) ---
XRP=6987.25; OTHER=6221.86; STOCKS=1552.45; ROTH=7611.82; FID=800.0
CASH=3533.81; EVT=329.81
NW=XRP+OTHER+STOCKS+ROTH+FID+CASH+EVT

# --- Node 1: the 2:15pm roll call ---
# Calibrated so implied P(signed into law 2026) reproduces the ~28% market price.
P_PASS, P_FAIL, P_PULL = 0.35, 0.55, 0.10

def xrp_move(branch):
    r=random.random()
    if branch=='pass':
        if r<0.35: return random.uniform(0.20,0.41)   # repricing toward $1.70-2.00
        if r<0.75: return random.uniform(0.09,0.20)   # moderate pop $1.55-1.70
        return random.uniform(-0.01,0.09)             # sell-the-news
    if branch=='fail':
        if r<0.30: return random.uniform(-0.23,-0.15) # $1.10-1.20
        if r<0.75: return random.uniform(-0.15,-0.08) # $1.20-1.30
        return random.uniform(-0.08,0.00)             # "not yet", already priced
    if r<0.70: return random.uniform(-0.07,-0.01)     # pulled: stays alive, mild
    return random.uniform(-0.01,0.02)

def fomc():
    r=random.random()
    if r<0.30: return -0.05, -0.020   # hawkish dots beyond what's priced
    if r<0.85: return  0.00,  0.000   # hike lands as priced
    return 0.03, 0.012                # relatively dovish framing

up=0; tot=0.0; outs=[]; bybranch={'pass':[0,0],'fail':[0,0],'pull':[0,0]}
for _ in range(N):
    r=random.random()
    b='pass' if r<P_PASS else ('fail' if r<P_PASS+P_FAIL else 'pull')
    mx=xrp_move(b)
    fc,fe=fomc()
    mx_t = mx + fc*1.0                    # XRP also takes the macro shock
    mo   = mx*0.45 + fc*1.1               # other crypto: partial CLARITY beta, high macro beta
    me   = fe                             # equities
    d = XRP*mx_t + OTHER*mo + (STOCKS+ROTH+FID)*me
    outs.append(d); tot+=d
    bybranch[b][1]+=1
    if d>0: up+=1; bybranch[b][0]+=1

outs.sort()
def pct(p): return outs[int(p*N)]
print(f"Net worth now: ${NW:,.0f}   (XRP {XRP/NW*100:.1f}%, crypto {(XRP+OTHER)/NW*100:.1f}%, cash {CASH/NW*100:.1f}%)")
print()
print(f"P(portfolio UP by Wednesday close) = {up/N*100:.1f}%")
print(f"P(portfolio DOWN)                  = {(1-up/N)*100:.1f}%")
print(f"Expected change  ${tot/N:+,.0f}   ({tot/N/NW*100:+.2f}% of net worth)")
print()
print("Distribution of the dollar outcome:")
for p,l in [(0.05,'5th  (bad tail)'),(0.25,'25th'),(0.50,'50th  median'),(0.75,'75th'),(0.95,'95th (good tail)')]:
    print(f"  {l:18} ${pct(p):+,.0f}   ({pct(p)/NW*100:+.2f}%)")
print()
print("P(up) conditional on each branch:")
for k,(u,n) in bybranch.items():
    print(f"  {k:5} branch  {n/N*100:4.1f}% of the time   ->  P(up | {k}) = {u/n*100:.1f}%")

# implied P(signed into law 2026), sanity check against the ~28% market price
sign = P_PASS*0.65 + P_PULL*0.25 + P_FAIL*0.05
print(f"\nSanity check -> implied P(H.R.3633 signed in 2026) = {sign*100:.1f}%  (market 25-30%)")
