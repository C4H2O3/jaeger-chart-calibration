# Jaeger Chart Calibration

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23377064.svg)](https://doi.org/10.5281/zenodo.23377064)

Independent research on how to correctly size a Jaeger near-vision reading
chart when the chart has no real metrological standard, and an empirical
audit of whether real commercial and public near-vision charts hold their
own stated scale.

This started as a practical commission: build a branded kit of near-vision
ophthalmic tests, including a Jaeger chart, for a client. Getting the font
size and line spacing right turned out to require deriving the calibration
from first principles, since no usable standard exists for the Jaeger chart
at all.

## Paper

- [How to Calculate a Jaeger Chart When No Standard Exists](papers/jaeger-chart-calibration/paper.md).
  Derives optotype size from the angular-acuity principle, transfers it to a
  Cyrillic (Golovin-Sivtsev) optotype, and empirically checks seven
  independent near-vision charts against their own stated scale, five of
  seven don't hold it.

## Data

This work does not publish body scans, patient data, or any materials
specific to the commissioned commercial kit. The `analysis/` folder has the
code used to check the seven third-party sources discussed in the paper,
but not the source files themselves (several are copyrighted commercial
products or third-party web content). See the paper's "Data and Code"
section for exactly what each script reproduces and where the public
sources can be found.

## License

Two separate licenses apply:
- **Code** (`analysis/` folders): MIT, see [LICENSE](LICENSE).
- **Paper** (text, figures, tables): CC BY 4.0, see [papers/LICENSE](papers/LICENSE).

Both are free to reuse, the condition is attribution.

## Declaration of AI Use

The author used Claude (Anthropic) to verify third-party sources, write the
scripts used to measure them, and proofread drafts. The physics derivation,
the original finding, and all conclusions are the author's own work. The
tool was used under the author's direction, and the author takes full
responsibility for the content of this work.

## Contact

I'm open to questions and ideas for collaboration. Open an issue in this repository.
