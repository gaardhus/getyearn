# getyarn

<!-- [![Actions Status][actions-badge]][actions-link] -->

[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/gaardhus/getyarn/workflows/CI/badge.svg
[actions-link]:             https://github.com/gaardhus/getyarn/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/getyarn
[conda-link]:               https://github.com/conda-forge/getyarn-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/gaardhus/getyarn/discussions
[pypi-link]:                https://pypi.org/project/getyarn/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/getyarn
[pypi-version]:             https://img.shields.io/pypi/v/getyarn
[rtd-badge]:                https://readthedocs.org/projects/getyarn/badge/?version=latest
[rtd-link]:                 https://getyarn.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

Get and merge video clips from https://getyarn.io/

clone the repository and install with pipx:

```bash
git clone git@github.com:gaardhus/getyearn.git
cd getyarn
pipx install .
```

```bash
~ ❯ getyarn --help
usage: getyarn [-h] [--next-clips NEXT_CLIPS] url output

positional arguments:
  url                   Yarn URL
  output                Output file

options:
  -h, --help            show this help message and exit
  --next-clips NEXT_CLIPS
                        Number of next clips to download
```

Then run the CLI

```bash
getyarn https://getyarn.io/yarn-clip/81fa2465-64ec-4e61-b1d9-b778b9a09058 few_words.mp4 --next-clips 1
```
