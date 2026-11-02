# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.2] - 2026-11-01

### Fixed
- Read the `angel_jwt_v3` cookie set by the current Angel login callback.
- Keep `angel_jwt_v2` and `angel_jwt` as fallbacks.

## [0.2.0] - 2026-01-30

### Changed
- Switched from PyJWT to python-jose for improved portability across Python environments
- Removed dependency on cryptography library to avoid PyO3 compatibility issues
- Updated setup.py install_requires to match requirements.txt

## [0.1.0] - 2026-01-30

### Added
- Initial release with Auth0 CIAM authentication support
- Core authentication logic for web scraping-based Auth0 flows
- Session management and token storage
- Configuration system for Auth0 settings