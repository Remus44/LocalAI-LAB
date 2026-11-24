#!/usr/bin/env bash
set -eu
: "${OLLAMA_API_BASE:?Set OLLAMA_API_BASE to the private LAN address first}"
curl --fail --show-error --max-time 10 "${OLLAMA_API_BASE%/}/api/tags"
