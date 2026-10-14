import re

with open("arizona_bbox.html", encoding="utf-8") as f:
    content = f.read()

# page 4 (0-indexed split) = the "Reading Near Chart" page
page = content.split('<page width="792.000000" height="612.000000">')[4]
word_re = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>')
words = [(float(a), float(b), float(c), float(d), e) for a, b, c, d, e in word_re.findall(page)]

# canonical reading-row triplets, read directly off the chart (unambiguous,
# verified against the chart's own linear text order top to bottom) -- matching
# by word content, not by height-clustering, avoids caption/instruction text
# ("sized and for", "you will", etc.) being mistaken for a genuine row.
rows = [
    ("J16", 200, ("space", "woman", "cycle")),
    ("J15", 170, ("flood", "guard", "relax")),
    ("J14", 140, ("shave", "lunch", "quiet")),
    ("J13", 110, ("world", "stake", "frown")),
    ("J12", 100, ("curve", "paint", "forum")),
    ("J10", 75, ("feast", "elect", "round")),
    ("J8", 60, ("model", "trust", "smile")),
    ("J6", 50, ("plant", "treat", "miner")),
    ("J4", 40, ("mouth", "prize", "water")),
    ("J2", 30, ("bread", "carve", "cabin")),
    ("J1", 20, ("study", "chair", "plane")),
]

print(f"{'J':>4} {'20/N':>5} {'acuity':>7} {'h,pt':>6} {'h*acuity':>9}")
results = []
for j, n, triplet in rows:
    matches = [w for w in words if w[4] in triplet]
    heights = [w[3] - w[1] for w in matches]
    assert len(heights) == 3, f"{j}: expected 3 words, found {len(heights)} -- {matches}"
    h = sum(heights) / len(heights)
    acuity = 20.0 / n
    results.append((j, acuity, h))
    print(f"{j:>4} {n:5d} {acuity:7.4f} {h:6.2f} {h*acuity:9.2f}")

big, small = results[0][2], results[-1][2]
exp_ratio = results[-1][1] / results[0][1]  # size ratio = acuity_big/acuity_small inverted
act_ratio = big / small
print(f"\nExpected size ratio (J16/J1) = {exp_ratio:.2f}")
print(f"Actual size ratio = {act_ratio:.2f}")
print(f"actual/expected = {act_ratio/exp_ratio:.2f}")
