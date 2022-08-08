# A Collector's Vault simulation

Statistical simulation of Netmarble's Marvel Future Fight Collector's Vault

Determines typical cost of participation and likely prizes acquired.

[This notebook](Collector's%Vault.ipynb) is probably what you really want to
read.

## Files

- [Collector's Vault.ipynb](Collector's%20Vault.ipynb) - Jupyter Notebook
  describing the experiment and including the code
- [sim.py](sim.py) - Python script exported from the above notebook for
  command-line invocation; generates the data set but does not analyze
- output-_n_ - comma-delimited file output from _n_ runs of the simulation,
  suitable for analysis as in the "Basic results" section of
  [the notebook](Collector's%20Vault.ipynb)
- [README.md](README.md) - this file
- [.python-version](.python-version) - on which the simulations here were last
  tested

## Download

To view locally, change, and/or edit these files,
[download the latest release from GitHub](https://github.com/therealchjones/collector-sim/releases/latest/download/).
This is highly recommended and is significantly faster than cloning the
repository.

Alternatively, you can clone this GitHub repository:

```
git clone https://github.com/therealchjones/collector-sim
```

## Installation / Setup / Usage

To view or develop the notebook locally, [download](#download) the files, and
from the root directory of the unzipped archive or the repository, run:

```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Then, to open the notebook:

```
jupyter notebook "Collector's Vault.ipynb"
```

Developed by @therealchjones / chjones@aleph0.com /
[u/therealchjones](https://www.reddit.com/user/therealchjones)
