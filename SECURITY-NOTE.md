# Security Note

A Dropbox API access token was previously hard-coded in `dropboxData.py` and committed to this
repository's history. It has since been removed from the code, and the git history has been rewritten
to purge the token string.

**That token should be considered compromised.** If you still have access to the Dropbox account /
app that issued it, revoke it at <https://www.dropbox.com/developers/apps> (open the app → revoke the
generated access token, or delete the app).

The script now reads its token from the `DROPBOX_TOKEN` environment variable instead. See `.env.example`.
