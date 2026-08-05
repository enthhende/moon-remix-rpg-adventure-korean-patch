#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 apply_patch.py
printf '\nPress Enter to close…'
read answer
