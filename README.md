# A Collector's Vault simulation

Statistical simulation of Netmarble's Marvel Future Fight Collector's Vault

Determines typical cost of participation and likely prizes acquired.

[This notebook](Collector's%20Vault.ipynb) is probably what you really want to
read, but it's best [read at nbviewer.org](https://nbviewer.org/github/therealchjones/collector-sim/blob/master/Collector%27s%20Vault.ipynb)

**_This project is no longer under active development and has been archived on GitHub. Dependencies have been updated for any vulnerabilities as of 13 March 2023, but no further updates are expected._**

## Files

- [Collector's Vault.ipynb](Collector's%20Vault.ipynb) - Jupyter Notebook
  describing the experiment and including the code. [Read it at nbviewer.org](https://nbviewer.org/github/therealchjones/collector-sim/blob/master/Collector%27s%20Vault.ipynb) for the best experience; viewing it on GitHub is okay, but internal links don't work.
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

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://github.com/therealchjones">
    <span property="dct:title">Christian Jones</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Simulating the Collector's Vault</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="US" about="https://github.com/therealchjones">
  United States</span>.
</p>
