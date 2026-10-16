# Agent Instructions

Python library `auth0-ciam-client` (Auth0 CIAM session/JWT handling), used by the Angel Studios Kodi addon.

On a new machine:

```bash
git clone https://github.com/brianpatrickreavey/auth0-ciam-client.git
cd auth0-ciam-client
uv sync   # or pip install -e ".[dev]"
```

Treat questions as read-only. Do not edit unless the user uses explicit action language.

`.github/copilot-instructions.md` is copy-pasted from the Kodi plugin and names the wrong project. Prefer this file. Workflow still: ask-first, 90% coverage target for the plugin that consumes this library.

See `README.md` and `TODO.md`.
