**How to Calculate a Jaeger Chart When No Standard Exists**

# Introduction

I got a request from a client to make a Jaeger chart (a near-vision reading test) for a commercial kit of near vision tests. That requires three numbers for each line – typeface, point size, line spacing. To my request the client replied with an unexpected answer: no exact data existed. Instead of a specification, I got from him a few competitor references as examples.

Measuring those references showed that letter size on adjacent lines doesn't follow any single mathematical pattern that could simply be copied and used in my own chart.

Looking into the literature, it turned out that the Jaeger chart had no metrological standard at all. The Jaeger notation (J1...J16) historically has never been tied to the physical size of the sign. In 1854, Eduard Jaeger numbered the samples by the typefaces of one specific Viennese print shop, not by the angular size of the letter. This gap between the historical numbering and the physical size was never closed. The lack of a single Jaeger-notation standard remains an open problem, actively discussed in the industry.

I asked myself: if there's nothing to copy, can the Jaeger chart be calculated correctly at all? And if so, on what basis?

There's no standard, but there is physics. The size of an optotype at a fixed working distance is set by the angular size of the sign. From this follows an invariant, checkable with a ruler on any printout: the product "sign height × visual acuity" stays constant across the whole scale.

The kit I had to build wasn't limited to one chart. Besides the Jaeger chart, it included a duochrome test and eight more tests of a different kind: for fixation, accommodation, phoria, and astigmatism. Calculating the Jaeger chart turned out to be only the first step. It immediately raised the question of whether the same angular principle applies to the rest of the kit's tests. Checking that boundary became a separate part of the work.

I couldn't find a ready-made calculation. So, I had to derive it from first principles, build a full near-vision test kit on it, and separately check how well real charts available from the open sources match their own stated scale. To do this I had to:

1. Derive the optotype size formula from the angular principle of visual acuity (5 arcminutes at the working distance) and build the full acuity scale 1.0–0.1 for the Jaeger chart.
2. Transfer the method to a Cyrillic optotype (Golovin-Sivtsev letters) for the duochrome test in the same kit.
3. Test the invariant "height × acuity = const" against existing commercial charts available publicly.
4. Classify the kit's remaining tests by the type of sizing principle (acuity / free dimension / distance-locked), so as not to apply the invariant where it doesn't apply.
5. Record the methodological and copyright limitations encountered while building the kit.

The object of this study is the process of calibrating optotypes for near-vision tests. The subject is how well real charts, as actually used, match their own stated size scale.

Methodologically, I relied on deriving the formula from optics (existing charts turned out to be unusable as a source), direct programmatic measurement of real third-party sources (PDF text layer where possible; raster measurement with a ratio test that doesn't require knowing the scale, where not), and reproducing the found discrepancies independently across several sources.

I managed to show the absence of a metrological standard in a universally used method, to derive and describe a reproducible way to replace it, and to measure and compare the calibration of several independent real near-vision products in a comparable way, including an assessment of which of them actually hold their stated scale and which don't.

# Existing Research

Even though the Jaeger chart has no unified standard, there is methodological literature around this problem. The foundational work is F. W. Law's "Standardization of Reading Types" (British Journal of Ophthalmology, 1951), which justifies a serif typeface for reading charts and the idea of standardization through the physical size of the sign. N-notation is built on it (a practical semi-standard for near vision): Times New Roman typeface, a fixed series of point sizes (5, 6, 8, 10, 12, 14, 18, 24, 36, 48 pt).

M-notation also exists separately – a physically defined, reproducible angular size – along with modern research tools such as Radner reading charts, built on a strictly logarithmic step between lines (unlike Jaeger's arbitrary step). Publications specializing in ophthalmic equipment openly call the lack of a unified Jaeger-notation standard a known, industry-discussed problem ("The Jaeger Notation Debate").

Separately, Russian-language ophthalmology has its own, independent tradition of measuring near visual acuity – a standard working distance of 33 cm (not 40, as with Jaeger and N-notation), with charts based on the Golovin-Sivtsev typeface (the classic optotype of Russian ophthalmology for distance vision). This convention was not tested instrumentally in the present work. A different working distance requires a separate derivation of the formula and remains an explicitly flagged direction for future checking, not part of the measurements already done.

# The Calculation Method

The basic principle isn't new: visual acuity (or "VA") of 1.0 corresponds to a sign that subtends 5 arcminutes at the working distance. For a working distance of 40 cm, this directly gives the reference value – the height of a lowercase letter (x-height) at VA = 1.0:

    5' = 0.00145444 rad
    400 mm × 0.00145444 = 0.582 mm

Everything after that rests on one invariant: size is inversely proportional to acuity, so the product stays constant across the whole scale – `sign height × acuity = const`. The specific invariants for a 40 cm working distance:

- by lowercase letter (any typeface): `x-height × VA = 0.582 mm`
- by capital letter (Times New Roman): `cap-height × VA = 0.860 mm`
- by point size (Times New Roman): `point size × VA = 3.68`
- by point size (duochrome, Golovin-Sivtsev typeface): `point size × VA = 2.06`

This principle gives both a formula and a ready verification tool: any finished chart can be checked with a ruler or calipers.

Point size doesn't carry over between typefaces directly. Letter height at the same point size depends on the typeface. For example, for Times New Roman: x-height = 0.448·em, cap-height = 0.662·em (cap-height = 1.478 × x-height). For Myriad Pro: x-height ≈ 0.484·em, cap-height ≈ 0.674·em. The Golovin-Sivtsev typeface (optotype): letter height = 0.80·em (measured from the source file), stroke = 1/5 of the height.

The common clinical rule "1 M-unit ≈ 8 pt" is assumed to be universal, independent of typeface, and it doesn't hold even for Times New Roman, because it gives the wrong number. The correct value, derived from x-height 0.448, is approximately 9.2 pt, not 8.

Table 1. Jaeger chart for Latin script, Times New Roman, 40 cm

| VA | Point size, pt | em, mm | x-height, mm | Cap-height, mm |
|----|-----------------|--------|--------------|-----------------|
| 1.0 | 3.68 | 1.30 | 0.582 | 0.860 |
| 0.9 | 4.09 | 1.44 | 0.646 | 0.955 |
| 0.8 | 4.60 | 1.62 | 0.727 | 1.075 |
| 0.7 | 5.26 | 1.86 | 0.831 | 1.228 |
| 0.6 | 6.14 | 2.16 | 0.970 | 1.433 |
| 0.5 | 7.36 | 2.60 | 1.164 | 1.720 |
| 0.4 | 9.20 | 3.25 | 1.454 | 2.149 |
| 0.3 | 12.27 | 4.33 | 1.939 | 2.866 |
| 0.2 | 18.40 | 6.49 | 2.909 | 4.298 |
| 0.1 | 36.81 | 12.99 | 5.818 | 8.597 |

Formulas: `x-height = 0.582/VA`, `point size = 3.68/VA`, `cap-height = 0.860/VA`. Print check: the capital letter in the 0.1 line should be 8.60 mm.

A counterintuitive but checkable result: VA 1.0 at 40 cm needs a sub-millimeter letter (x-height 0.582 mm; cap-height 0.86 mm). Independent verification: a standard 20/20 optotype at a 6 m distance ≈ 8.7 mm; scaled to 40 cm – 8.7 × (0.4/6) = 0.58 mm, which matches the derived formula.

# Transferring the Method to Cyrillic

Transferring the size to Cyrillic and printing the chart would have been too easy. But since no strict Cyrillic analog of the Latin Sloan optotype exists (Sloan is a standard Latin set of optotype letters – C, D, H, K, N, O, R, S, V, Z – which is used in modern distance acuity charts such as ETDRS; the letter is inscribed in a 5×5 square, stroke is 1/5 of the side), I had to dig into the theory again. The Russian standard is the Golovin-Sivtsev typeface, seven letters: Б, И, К, М, Н, Ш, Ы (Cyrillic letters, construction equivalent to B, I, K, M, N, Sh, Y). Construction is the same as Sloan: the letter is inscribed in a 5×5 square, stroke thickness is 1/5 of the side. The Golovin-Sivtsev chart was historically meant for distance vision (5 m), but since the optotype is defined by angular size and not the distance, it's legitimate to use it for near vision too, by recalculating the height for a 40 cm working distance. This gives the following values:

Table 2. Jaeger chart for Golovin-Sivtsev Cyrillic script, 40 cm

| VA | Letter height, mm | Stroke thickness, mm | Point size, pt |
|----|---------------------|------------------------|-----------------|
| 1.0 | 0.582 | 0.116 | 2.06 |
| 0.9 | 0.647 | 0.129 | 2.29 |
| 0.8 | 0.728 | 0.146 | 2.58 |
| 0.7 | 0.831 | 0.166 | 2.94 |
| 0.6 | 0.970 | 0.194 | 3.44 |
| 0.5 | 1.164 | 0.233 | 4.12 |
| 0.4 | 1.455 | 0.291 | 5.16 |
| 0.3 | 1.940 | 0.388 | 6.87 |
| 0.2 | 2.910 | 0.582 | 10.31 |
| 0.1 | 5.820 | 1.164 | 20.62 |

Formula: `point size = 2.06/VA` (under the metric "letter = 0.80·em"). Check: the letter in the 0.1 line – 5.82 mm, point size 10 pt – 2.82 mm.

The duochrome test and the Jaeger chart turn out to share one metric logic – a common invariant of 0.582 mm by letter height, despite different optotypes and different typeface origins. The whole kit is tied to one working distance.

# Findings on Third-Party Charts

Once I had my own tables, I decided to apply the method "in reverse" and measure actual letter sizes in publicly available charts unrelated to my project, to verify whether the invariant holds. I managed to verify seven independent sources: commercial products, publicly available materials, and one professional academic source.

The only thing in common for all seven sources is that they are near visual acuity tests, and the same physics applies to all of them (angular sign size at a fixed distance). However, they set different tasks for the person being tested. Sources based on continuous text (reading paragraphs) require literacy, reading fluency, and involve a crowding effect between neighboring letters and words – an objectively harder task than sources based on isolated, well-spaced symbols (individual digits or letters), some of which are specifically designed for children and illiterate patients. I compared the sources by one common criterion – whether the stated size calibration holds.

Two independent tests were used for each chart in the comparison. The invariant was used where the real print scale is known (a PDF text layer with a stated page size): `sign height / stated value (M or acuity) = const` across the whole scale. In the ratio test, which works without knowing the scale (including on raster images), you compare the measured ratio of the longest line to the shortest with the ratio that follows from their stated values.

**Shamir Optical Industries,** a large Israeli manufacturer of ophthalmic lenses, one of the world's industry leaders (measured from a PDF with a text layer). The invariant holds exactly in the acuity range 0.4–0.9, but fails on the large lines (0.3 / 0.2 / 0.1). The ratio of point sizes at the extreme lines is 6.3× instead of a strict decimal 10×. The large lines are therefore undersized (apparently to fit the chart on the page).

**Bausch+Lomb,** a large American manufacturer of eye care products and contact lenses, one of the industry's oldest brands (measured from a raster sheet). Holds exactly in the working range, fails on the largest line (VA=0.1). The ratio of the extreme lines is 6.2×, nearly identical to Shamir. Manufacturers, it appears, reproduce one and the same approximate size series rather than calibrating independently.

**A scan of a chart proposed by a practicing ophthalmologist** (low quality, only relative values were measured). The ratio of the extreme lines is 6.75×, and the spread of the invariant within the scale is noticeably larger than Shamir's – the least regular of all the sources.

**AllAboutVision** (allaboutvision.com, a large specialized resource). An M-notation chart, text layer, page size stated. The invariant drops almost 2.7-fold from the small end of the scale to the middle. Ratio test: stated 2.50M/0.37M = 6.76×, actual 3.13× – almost half of what's needed.

**visionexpert.tv** (a Russian-language source, text layer, A4 format stated, gives both the acuity and an internal "font NN" label for each line). Comparing by the stated "font NN" looked perfectly stable – but that's a false positive: the manufacturer's internal numbering isn't required to be a linear scale. The real check, by the formula "height × acuity = const," shows the invariant dropping almost 3.2-fold toward the small end of the scale. Ratio test: stated 10×, actual 3.34× – the worst result of all seven sources (actual/expected = 0.33).

**Lea Numbers Pocket Card** (#271000, Good-Lite / Lea-Test, developed by Lea Hyvärinen, M.D.). Measurements were made from a high-resolution photo of the packaging, since on the official answer-key PDF the digits are vector outlines rather than selectable text, so programmatic text-based measurement was not possible. The invariant holds within ±5% across the whole acuity range 0.05–0.80 (a 16-fold difference in line size). Ratio test: stated 16.00×, actual 16.38× (actual/expected = 1.02) – nearly perfect. The three smallest lines in this photo are physically smaller than 1–2 pixels and couldn't be measured, due to the resolution limit of the photo.

**Banner Eye Care, University of Arizona.** Measured from the guide "Guide to In-Home Vision Testing," developed by this academic ophthalmology department for vision monitoring during the COVID-19 pandemic. Made of words to read, not isolated symbols, and by task type closest to the Jaeger chart. Uses genuine Jaeger notation (J16...J1) with a Snellen equivalent (the classic acuity fraction notation such as 20/20, used for distance charts) at 14 inches, and includes a built-in print-scale self-check – it asks the reader to compare a printed 25 mm coin image with a real coin before testing. The invariant holds in a narrow range of 3.70–4.23 across the whole 10-fold acuity scale. Ratio test: stated 10.00×, actual 9.65× (actual/expected = 0.97) – the second source that passed the check.

Table 3. Summary table of sources

| Source | actual/expected (ratio test) | Task type |
|---|---|---|
| Shamir | ~0.63 | reading (paragraph) |
| Bausch+Lomb | edge ratio 6.2× instead of 10× | reading (paragraph) |
| Scan proposed by a practicing ophthalmologist | edge ratio 6.75× instead of 10×, less regular | reading (paragraph) |
| AllAboutVision | 0.46 | reading (paragraph) |
| visionexpert.tv | 0.33 (worst) | reading (paragraph) |
| Lea Numbers (Good-Lite) | 1.02 | isolated symbols |
| Banner Eye Care / University of Arizona | 0.97 | reading (words) |

Five of the seven sources don't hold their own stated scale, distorting size at the edges of the chart. Both sources that passed the check come from a serious professional context – a licensed clinical brand with a named developer, and an academic university ophthalmology department. All five sources with a discrepancy come from the general public web, without clear clinical verification. The sample is far too small for any statistical conclusions or generalizations.

# Preparing the Rest of the Kit's Tests

The Jaeger chart and the duochrome test aren't the only elements of the kit, and it would be a direct repeat of an already-discussed mistake to automatically extend the same angular principle to the rest of the tests. The parameters of these other tests weren't derived by the same method. They're taken from existing specialized sources. What matters here isn't where the numbers come from, but where the invariant stops applying. The tests fall into three groups by the principle that sets their size.

The grouping is determined by what the test actually measures and how size affects the result. Where the sign's size is itself the measured quantity (can the person tell apart a mark of this size), the angular invariant applies. Where the overall size of the target doesn't matter and only one specific element inside it matters (a dot, a stroke, a gap), what's critical isn't the target's size but that element. And where a test encodes an angle or a deviation through fixed geometry (a displacement in millimeters equals so many prism diopters), the test's result depends on the distance and the sizes staying exactly as specified, and they can't be scaled.

**Group A – acuity charts** (size set by the invariant "acuity × size = const"): the Jaeger chart, the duochrome test.

**Group B – single targets** (free overall size, what matters is a functional element, not the overall size):

Table 4. Summary table for Group B

| Test | Overall size | Functional element |
|---|---|---|
| Radiant figure | Ø 30–60 mm | stroke 0.3–0.5 mm |
| Cross test with central fixation | 18–28 mm | equal lines ~0.3–0.5 mm; central point |
| Cross test without central fixation | 18–28 mm | equal lines ~0.3–0.5 mm; open center |
| Granularity test (Jackson cross-cylinder target, JCC) | 12–20 mm | dots Ø ~0.5 mm |
| Push-up test (measuring amplitude of accommodation) | 30–40 mm | dark rectangle with two white squares |

**Group C – size changes the result** (rigidly tied to the working distance):

- **Schober test**: outer ring Ø 35 mm (5°), inner ring Ø 17.5 mm (2.5°), cross smaller than the inner ring (≈8–9 mm, with a gap for reading), lines 0.5–1 mm. Cross displacement of 4 mm = 1 prism diopter (Δ); touching the inner ring ≈ 2.2 Δ, the outer ring ≈ 4.4 Δ. Red cross, green rings.
- **Howell test** (phoria scale): a step of 4 mm = 1 Δ at 40 cm; number N is positioned at 4·N mm from the arrow; range ±15 Δ, scale width ≈ 125 mm. Can't be scaled – the scale is rigidly tied to the working distance.
- **Worth test**: figure span 35 mm edge to edge, each element ≈ 6 mm. Red rhombus, green crosses, white circle.

A separate note on the Amsler grid (not included in the final kit): its standard working distance is 30 cm, a 5 mm cell corresponds to 1°. For a 40 cm working distance, keeping the same 1°-per-cell angular step, the cell should be 7 mm, not 5. This is an example of the fact that not all tests, even within one kit, "live" at the same working distance.

# Errors and Misconceptions

In the course of this work, I identified the following common errors:

1. No standard exists. Copying someone else's chart reproduces their unverified error and doesn't give a correct size.
2. The same point size in different typefaces gives a different letter height at identical font sizes. What matters is the sign's height in millimeters.
3. **"1 M-unit ≈ 8 pt."** The common clinical rule "1 M-unit ≈ 8 pt" is assumed to be universal, independent of typeface, and it doesn't hold even for Times New Roman, because it gives the wrong number. The correct value, derived from x-height 0.448, is approximately 9.2 pt, not 8.
4. The em, x-height, and cap-height values are three different quantities for the same line (for the 0.1 acuity line: em 12.99 mm, x-height 5.82 mm, cap-height 8.60 mm).
5. You can't just "compress" individual lines of an acuity chart. You can only scale the whole chart proportionally, recalculated for a specific working distance.
6. The acuity invariant only applies to Group A charts. For Group B targets, what matters is the functional element; for Group C phoria tests, it's the rigid tie to distance.
7. When copying someone else's chart with the same nominal point sizes but in a different typeface, the letters in practice come out roughly 7% smaller or larger than stated. That gives neither an exact copy nor a correct calculation.

# Copyright Aspect of the Optotype Text

The reading text in the Jaeger chart isn't a random set of words, but a meaningful excerpt. I chose a fragment of "Through the Looking-Glass" by Lewis Carroll (1871, public domain). The canonical Russian translation by N. Demurova is under copyright (the translator died in 2021; protection lasts until approximately 2091) and couldn't be used.

To resolve this, I translated the fragment independently from the original, not reproducing the protected text. Carroll's characteristic wordplay around "Nobody" was reworked from scratch, without borrowing Demurova's translation choices.

Methodologically this points to a more general principle: an optotype chart can be set in any meaningful public-domain text, or an original one. The content of the text doesn't affect the measurement of visual acuity – only the size of the sign matters.

# Limitations

**Absolute sizes taken from raster images and scans are only reliable in relative terms.** Where a source has no text layer with an explicitly stated page scale, measurements rely on the ratio test (a ratio of sizes), not absolute millimeters. For several sources checked in this work, this is noted separately.

**Font metrics are nominal.** The x-height/em and cap-height/em values depend on the specific typeface version and the rendering software. For each measurement, the specific file it was measured from is stated.

**The method is reproducible and isn't a monopoly.** The paper claims the uniqueness of the finished product and of the fact that "no one had checked these sources this explicitly before," not exclusivity of the calculation itself. The calculation is derived from publicly available optics and published methodological literature.

**The clinical part went through a separate review.** The interpretation of the tests (phoria, accommodation) and the finished kit as a whole were approved by the client's ophthalmologist without objections before use. This isn't a mathematical check, and its result is stated in the paper as a fact, not re-evaluated here.

**The sample of third-party sources isn't sufficient for representative statistics.** Although the seven sources showed that professional sources hold the scale better than the general public web, this isn't enough to call it an established pattern.

# Conclusion

1. The Jaeger chart has no metrological standard and never has had one. This is a documented historical fact (Eduard Jaeger, 1854, the typefaces of one specific Viennese print shop).
2. The correct optotype size is derived from elementary angular optics and checked with a ruler on any finished printout. The invariant "sign height × acuity = const" holds constant across the whole scale.
3. An empirical check of seven independent real sources showed: five of seven don't hold their own stated scale, distorting size at the edges of the chart (actual/expected from 0.33 to 0.63).
4. The method transfers to a Cyrillic optotype (Golovin-Sivtsev letters) without losing the shared metric logic. The duochrome test and the Jaeger chart rest on the same invariant, despite the different origins of the typefaces.
5. Not all of the kit's tests follow the same sizing principle. The three-group classification (acuity / free dimension / distance-locked) prevents applying the invariant where it's physically inapplicable.
6. Respecting copyright matters even for a detail as small as the reading text in a chart.
7. The correctness of my clinical interpretation was checked and confirmed without objections by the client's ophthalmologist.

# Data and Code

**Published:** the derived formulas and calculation tables (the "Calculation Method" and "Transferring the Method to Cyrillic" sections of this paper, in a generalized form not tied to any specific commercial product), and the code used to check the seven third-party sources – `measure_allaboutvision.py`, `measure_visionexpert.py`, `measure_lea_numbers.py`, `measure_arizona_reading_near.py`. Each script reproduces the figures given in the text when run on the source file of the corresponding source.

**Not published:** materials specific to the commercial test kit (layout, branded files, client-specific instructions). This work didn't use any patient data.

# References

1. Law, F.W. (1951). Standardization of Reading Types. *British Journal of Ophthalmology*.
2. Precision Vision. The Jaeger Notation Debate (materials on the lack of a Jaeger-notation standard; needs an exact citation confirmed before publication).
3. Radner reading charts – a modern research instrument built on a strictly logarithmic step between lines (needs an exact citation confirmed before publication).
4. Comparative validation studies of handheld near-acuity charts (Ophthalmology Science / ScienceDirect, 2025) – needs the exact citation checked before publication; flagged by the author in the working materials as unverified.
5. Carroll, L. (1871). Through the Looking-Glass, and What Alice Found There. Public domain.
6. Worth four-dot test – parameters: MDPI (Life, 2023, 13/9/1900); PMC7396169 – needs final citation checks before publication.

Sources checked for the findings (section "Findings on Third-Party Charts"):

1. Shamir – a commercial near-vision chart, measured from a PDF with a text layer.
2. Bausch+Lomb – a commercial near-vision chart, measured from a raster sheet.
3. allaboutvision.com – https://cdn.allaboutvision.com/images/jaeger-chart.pdf
4. visionexpert.tv – https://visionexpert.tv/pl/fileservice/user/file/download/h/b3b82ea62c09f317875e7da1b3e918a0.pdf
5. Good-Lite / Lea-Test – LEA NUMBERS® Pocket Near Vision Card, #271000, developed by Lea Hyvärinen, M.D. https://store.good-lite.com/products/271000
6. University of Arizona, Ophthalmology and Vision Science / Banner Eye Care – Guide to In-Home Vision Testing, 2020. https://eyes.arizona.edu/sites/default/files/eyechart.pdf
