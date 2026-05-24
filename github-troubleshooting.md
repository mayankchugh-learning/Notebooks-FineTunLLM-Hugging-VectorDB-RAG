# GitHub troubleshooting

Notes for common push and security issues in this repository (notebooks, Colab exports, API keys).

## Push blocked: GH013 / Push Protection (secrets in commits)

### Symptom

`git push` (including `git push -f`) fails with:

```text
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote:     - Push cannot contain secrets
remote:       —— Hugging Face User Access Token ————————————————————
remote:          - commit: <sha>
remote:            path: SomeNotebook.ipynb:62
```

GitHub links to [working with push protection](https://docs.github.com/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line#resolving-a-blocked-push).

### Why removing the token from the file is not enough

Push protection scans **every commit** in the push, not only the latest working tree.

Typical notebook case:

1. A cell ran and **saved output** contained a real token (for example a printed `hf_…` string).
2. You later edited the source to use `userdata.get('HF_TOKEN')` or cleared outputs locally.
3. An **older commit** in your branch still contains the secret in the notebook JSON.

New commits do not erase old commits. Force-pushing still sends that history, so the push is rejected again.

### Confirm which commit still has the secret

PowerShell (replace commit SHA and notebook path from the GitHub error):

```powershell
git show <commit-sha>:Huggingface_explore_live_class-25May26.ipynb | Select-String -Pattern "hf_"
```

If matches appear, that commit must leave your push history (or be rewritten).

Check whether **HEAD** is clean:

```powershell
git show HEAD:YourNotebook.ipynb | Select-String -Pattern "hf_[A-Za-z0-9]{15,}"
```

No output on `HEAD` but push still fails → fix history, not just the open file.

### Fix: squash local commits into one clean commit (recommended when ahead of `origin/main`)

Use this when you have a few local commits on top of `origin/main` and only the **current tree** is secret-free.

```powershell
git fetch origin
git status
# Expect: "Your branch is ahead of 'origin/main' by N commits"

git reset --soft origin/main
git commit -m "Add notebook; outputs cleared, no secrets in history"
git push origin main
```

What this does:

- Moves `main` back to match `origin/main` **without** changing your files (soft reset).
- Stages all changes from the discarded local commits as one new commit.
- Replaces the old commit chain (including the commit that contained tokens) with a single new commit GitHub can accept.

**Do not use** `git push -f origin main` to “fix” this unless you have already rewritten history and understand you are overwriting the remote branch.

### If secrets are buried deeper in history

If bad commits are not only “a few commits ahead” of `origin/main` (for example already on the remote, or many commits back), use history rewriting tools:

- [git filter-repo](https://github.com/newren/git-filter-repo) (preferred), or
- BFG Repo-Cleaner

Then force-push only after coordinating with anyone else using the repo. For a personal notebook repo with a short local-only mistake, the soft-reset squash above is usually enough.

### After a blocked push: revoke exposed tokens

Treat any token that appeared in a commit, push error, or chat log as **compromised**:

1. [Hugging Face → Settings → Access Tokens](https://huggingface.co/settings/tokens) — revoke affected tokens.
2. Create new tokens if needed.
3. Store them in Colab **Secrets** / `.env` / environment variables — never in committed notebook output.

Using GitHub’s “allow secret” unblock URL is for emergencies only; it does not remove the secret from git history.

---

## Prevention (notebooks)

Before `git add` / `git commit` / `git push`:

1. **Clear outputs** in Jupyter/VS Code: *Clear All Outputs*, or in Colab before download/export.
2. Prefer source cells like `userdata.get('HF_TOKEN')` without printing the token value.
3. Optional: install [nbstripout](https://github.com/kynan/nbstripout) so outputs are stripped on commit:

   ```powershell
   pip install nbstripout
   nbstripout --install
   ```

4. Never commit `.env` or raw API keys (this repo’s `.gitignore` excludes `.env`).

---

## Quick reference

| Problem | Cause | Fix |
| --- | --- | --- |
| GH013, secret in commit SHA | Token in old commit / notebook output | `git reset --soft origin/main`, recommit, `git push` |
| Push rejected after “I removed the token” | History unchanged | Same as above, or filter-repo for deep history |
| Token was ever pushed or printed | Exposure | Revoke and rotate at provider |

---

## Example resolved in this repo (May 2026)

- **Notebook:** `Huggingface_explore_live_class-25May26.ipynb`
- **Issue:** Hugging Face tokens in saved cell outputs in commit `6794450`; later commits cleared outputs but push still failed.
- **Resolution:** `git reset --soft origin/main`, single new commit `5d71981`, `git push origin main` succeeded.
