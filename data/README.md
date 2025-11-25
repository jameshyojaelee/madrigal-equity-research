# Data directory

Substructure (to be fleshed out):
- `data/raw/` – original downloaded files (filings, labels, PDFs, etc).
- `data/processed/` – cleaned/tabular data derived from raw sources.
- `data/external/` – manually downloaded external files not fetched by scripts.
- `data/metadata/` – YAML/CSV describing what each data source is.

Raw data should not be committed if large or copyrighted; only small metadata or extracted tables should be added to git.

## Downloading core documents
`data/metadata/sources.yaml` lists tracked documents and their URLs. Run `python data/download_sources.py` to fetch any entries with real URLs; downloads are stored under `data/raw/` and kept out of git.
