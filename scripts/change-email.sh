#!/usr/bin/env bash
# This script rewrites Git history to replace a specific email with okigan@gmail.com.
# Usage: ./change-email.sh OLD_EMAIL

# Exit on error
set -e

OLD_EMAIL="${1:?Usage: $0 OLD_EMAIL}"
NEW_EMAIL="okigan@gmail.com"
# Uncomment and set a new name if you also want to update the committer/author name
# NEW_NAME="Your Name"

git filter-branch --env-filter '
if [ "$GIT_COMMITTER_EMAIL" = "'$OLD_EMAIL'" ]; then
    export GIT_COMMITTER_EMAIL="'$NEW_EMAIL'"
    # export GIT_COMMITTER_NAME="'$NEW_NAME'"
fi
if [ "$GIT_AUTHOR_EMAIL" = "'$OLD_EMAIL'" ]; then
    export GIT_AUTHOR_EMAIL="'$NEW_EMAIL'"
    # export GIT_AUTHOR_NAME="'$NEW_NAME'"
fi
' --tag-name-filter cat -- --branches --tags

echo "Rewrote history: all occurrences of $OLD_EMAIL are now $NEW_EMAIL"
