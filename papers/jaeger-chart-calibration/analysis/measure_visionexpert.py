import re

with open("visionexpert_bbox.html", encoding="utf-8") as f:
    content = f.read()

word_re = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>')
words = [(float(a), float(b), float(c), float(d), e) for a, b, c, d, e in word_re.findall(content)]

# find each "№ N (острота зрения X.X) шрифт YY" header and its y/x position
header_re = re.compile(r"№")
headers = []
for i, w in enumerate(words):
    if w[4].startswith("№"):
        # collect the rest of this header line (same y, within next ~8 words)
        line_words = [w]
        for w2 in words[i+1:i+9]:
            if abs(w2[1] - w[1]) < 2:
                line_words.append(w2)
            else:
                break
        text = " ".join(x[4] for x in line_words)
        m = re.search(r"(\d+\.\d+)\).*?шрифт\s*(\d+)", text)
        if m:
            headers.append((w[0], w[1], w[3], float(m.group(1)), int(m.group(2)), text))

headers.sort(key=lambda h: (h[1], h[0]))
print(f"Found {len(headers)} headers\n")

for i, (hx, hy0, hy1, acuity, font_n, text) in enumerate(headers):
    # paragraph body: same column (x within +-20 of header x), y below this header,
    # above the next header in same column or +60pt fallback
    col_candidates = [h for h in headers if abs(h[0] - hx) < 20 and h[1] > hy1]
    y_end = min([h[1] for h in col_candidates], default=hy1 + 70)
    body = [w for w in words if hx - 5 <= w[0] <= hx + 260 and hy1 < w[1] < y_end
            and not w[4].startswith("№") and w[4] not in ("шрифт",) and not re.match(r"^\(?остр", w[4])
            and not re.match(r"^\d+\.\d+\)?$", w[4]) and not re.match(r"^\d+$", w[4])]
    heights = sorted(w[3] - w[1] for w in body if len(w[4]) >= 3)
    if heights:
        med = heights[len(heights) // 2]
        ratio = med / font_n
        print(f"№{i+1:2d}  acuity={acuity:.1f}  шрифт={font_n:2d}  "
              f"measured_h={med:5.2f}pt  h/font={ratio:.4f}  n={len(heights)}")
    else:
        print(f"№{i+1:2d}  acuity={acuity:.1f}  шрифт={font_n:2d}  NO BODY WORDS FOUND")
