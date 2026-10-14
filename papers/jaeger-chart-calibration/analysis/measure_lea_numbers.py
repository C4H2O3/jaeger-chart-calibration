from PIL import Image

img = Image.open("lea_page3-3.png").convert("L")
W, H = img.size
px = img.load()
print(f"Image size: {W}x{H}")

DPI = 600
PT_PER_PX = 72.0 / DPI

# center digit-group column band -- present in every row, avoids margin labels
X_LO, X_RIGHT = int(W * 0.40), int(W * 0.58)
THRESH = 150

# scan rows for ink presence in this band
row_has_ink = []
for y in range(H):
    found = False
    for x in range(X_LO, X_RIGHT, 3):
        if px[x, y] < THRESH:
            found = True
            break
    row_has_ink.append(found)

# cluster consecutive ink rows into bands (gap > 5px breaks a cluster)
clusters = []
start = None
gap = 0
for y, has in enumerate(row_has_ink):
    if has:
        if start is None:
            start = y
        gap = 0
    else:
        if start is not None:
            gap += 1
            if gap > 3:
                clusters.append((start, y - gap))
                start = None
                gap = 0
if start is not None:
    clusters.append((start, H - 1))

print(f"Found {len(clusters)} ink clusters (rows) in center band")

labels = [
    ("20/400", 400, 0.05), ("20/320", 320, 0.063), ("20/250", 250, 0.08),
    ("20/200", 200, 0.10), ("20/160", 160, 0.12), ("20/125", 125, 0.16),
    ("20/100", 100, 0.20), ("20/80", 80, 0.25), ("20/63", 63, 0.32),
    ("20/50", 50, 0.40), ("20/40", 40, 0.50), ("20/32", 32, 0.63),
    ("20/25", 25, 0.80), ("20/20", 20, 1.0), ("20/16", 16, 1.25),
    ("20/12.5", 12.5, 1.6), ("20/10", 10, 2.0),
]

print(f"\n{'label':>8} {'decimal':>8} {'h_px':>7} {'h_pt':>8} {'h*decimal':>10}")
results = []
for i, (c_top, c_bot) in enumerate(clusters):
    if i >= len(labels):
        break
    label, n_val, dec = labels[i]
    h_px = c_bot - c_top
    h_pt = h_px * PT_PER_PX
    results.append((label, n_val, dec, h_pt))
    print(f"{label:>8} {dec:8.3f} {h_px:7d} {h_pt:8.2f} {h_pt*dec:10.2f}")

if len(results) >= 2:
    biggest = results[0]   # 20/400, decimal .05 -> largest print
    smallest = results[-1]  # 20/10, decimal 2.0 -> smallest print
    expected_ratio = biggest[3] and (smallest[2] / biggest[2])  # placeholder, fixed below
    exp_r = biggest[1] / smallest[1]  # N ratio, e.g. 400/10 = 40
    act_r = biggest[3] / smallest[3]
    print(f"\nExtremes: {biggest[0]} vs {smallest[0]}")
    print(f"Expected height ratio (by N) = {exp_r:.2f}")
    print(f"Actual measured height ratio = {act_r:.2f}")
    print(f"actual/expected = {act_r/exp_r:.2f}")
