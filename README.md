# Dropbox Upload Test

A minimal Python example that uploads a single local file to Dropbox using the official `dropbox` SDK.
It wraps the upload in a small `TransferData` class and overwrites the destination file if it exists.

## Setup

```bash
pip install dropbox
export DROPBOX_TOKEN="your-dropbox-access-token"   # never commit this
```

## Usage

```bash
export SOURCE_FILE="./text.txt"   # local file to upload (default: text.txt)
export DEST_PATH="/test.txt"      # destination path in Dropbox (default: /test.txt)
python dropboxData.py
```

## Notes
- The access token is read from the `DROPBOX_TOKEN` environment variable — see `.env.example`.
- See `SECURITY-NOTE.md` regarding the token that was previously committed here.
