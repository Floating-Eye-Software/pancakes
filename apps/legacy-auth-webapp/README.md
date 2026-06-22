# Legacy Authentication Web App

This directory preserves the original Pancakes Flask authentication and user
profile skeleton. It is not the current Pancakes node implementation.

The application expects a `.env` file containing `SECRET_KEY` and stores its
development SQLite database at `data/pancakes.db`. Run it from this directory
so that its relative database and template paths resolve correctly:

```sh
cp example.env .env
python3 main.py
```

The repository-root `make upload` target still stages this application for the
legacy deployment layout.

The `remote-server/` directory preserves the legacy remote host's Dockerfile,
Makefile, and deployment layout. Generated application staging, backups, and
database files under that directory remain ignored. Repository-root mount,
upload, and download targets use this location.
