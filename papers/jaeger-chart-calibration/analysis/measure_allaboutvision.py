import re

with open("aav_bbox.html", encoding="utf-8") as f:
    content = f.read()

page2 = content.split('<page width="792')[1]

word_re = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>')
words = [(float(a), float(b), float(c), float(d), e) for a, b, c, d, e in word_re.findall(page2)]

is_marker = lambda t: bool(re.match(r"^[.\d]+M$", t))
is_no = lambda t: t == "No."

for col_name, xlo, xhi in [("left", 0, 400), ("right", 400, 800)]:
    col = [w for w in words if xlo <= w[0] < xhi]
    col.sort(key=lambda w: w[1])
    markers = [w for w in col if is_marker(w[4])]
    markers.sort(key=lambda w: w[1])
    print(f"\n=== Column: {col_name} ===")
    for i, (mx0, my0, mx1, my1, mlabel) in enumerate(markers):
        y_start = my1
        y_end = markers[i + 1][1] if i + 1 < len(markers) else 1e9
        body = [w for w in col if y_start < w[1] < y_end and not is_marker(w[4]) and not is_no(w[4])
                and not re.match(r"^\d+\.$", w[4])]
        # plain lowercase words, 3-7 letters, no punctuation -- cleanest for height comparison
        clean = [w for w in body if re.match(r"^[a-z]{3,7}$", w[4])]
        heights = [w[3] - w[1] for w in clean]
        if heights:
            heights.sort()
            med = heights[len(heights) // 2]
            sample_words = [w[4] for w in clean[:4]]
            print(f"{mlabel:>7}  median word height = {med:6.3f} pt   n={len(heights):2d}  e.g. {sample_words}")
        else:
            print(f"{mlabel:>7}  (no clean body words found)")
