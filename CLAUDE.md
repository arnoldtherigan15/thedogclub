# CLAUDE.md: The Dog Club client documents

Project documents for The Dog Club Bali's website redesign (freelance project by Arnold, Essential package, IDR 7.5M). The website code is in the sibling repo `../thedogclub-website`; see its CLAUDE.md for the code workflow.

## Working with Arnold

- Reply in casual Indonesian. Everything the client reads (pages in `client/`, sheet replies) is in clear, plain English, except WhatsApp chat templates, which are in Indonesian ("Kak").
- When Arnold only asks a question, answer it. Do not edit files until he asks for the change.
- When writing for the client, say who it is for in one line before the text.

## What lives here

| Path | What |
| --- | --- |
| `client/` | Pages for the client, published to https://arnoldtherigan15.github.io/thedogclub/ by `.github/workflows/pages.yml` on every push to `main` (the root redirects to `progress/`) |
| `client/progress/` | Project progress. Content in `data.js` (phases, needs, payments, dated updates) |
| `client/open-feedback/` | "What we still need": open items from the feedback. Content in `data.js`; set an item's `status` to `done` when it arrives |
| `client/invoice/`, `invoice-1/`, `invoice-2/` | Invoice overview and the invoices (payment 1 and 2 paid; payment 3, IDR 1.5M, before go-live) |
| `client/quotation/`, `seo-audit/`, `onboarding/`, `feedback/` | Signed quotation, audit with fix status, account guides, early design proposals |
| `docs/` | Internal: `PLAN.md`, `TICKETS.md` (TDC-0xx), `WORKFLOW.md`, `tracker.html` (rebuild with `python3 docs/build_tracker.py`) |
| `design/` | Raw client files, git-ignored (3+ GB): Canva exports (`canva-12-nov/` is the latest), `assets/Photo/…` mirrors the client's Google Drive folders |

## Client pages

- Static HTML with Tailwind from the CDN, `assets/tailwind-config.js` (cream, beige, forest, sunshine, softGray) and `assets/site.css`; Inter and Playfair Display; Font Awesome icons. Keep `noindex` on every page.
- Pages with changing content read a `data.js` (`window.PROJECT`, `window.OPEN_ITEMS`). Change the data, not the markup, and check it loads: `node -e "global.window={};require('./client/progress/data.js')"`.
- Before pushing, serve `client/` (`npx serve client -l 4174`) and check the changed pages on laptop and phone widths, links and images included.

## Keeping things in step

When the website changes or the client answers, keep these consistent:
- the Google Sheet (`1vneEA3jCe-mwgoh2xG2bGOXtSEw0FLwKkLqOQDk_S4c`): Status and "Our reply" in Design feedback, answers and new rows in Open questions;
- `client/open-feedback/data.js`: open items, question numbers, counts;
- `client/progress/data.js`: `updated`, feedback done count, needs, payments, a dated entry in `updates`;
- invoices, when a payment arrives.

Question and feedback numbers (Q-xx, #xx) must match the sheet everywhere.

## Git

- Commit straight to `main` here (it is not the website). Conventional Commits in English, e.g. `content(progress): …`, `feat(client): …`, with the Co-Authored-By trailer.
- Commit as `git -c user.email=arnoldtherigan15@gmail.com commit …`.
- Push with Arnold's personal key and retry on network errors:
  ```bash
  export GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -o ConnectTimeout=20 -o BatchMode=yes -i $HOME/.ssh/id_rsa"
  for i in 1 2 3 4 5; do git push -q origin main && break; sleep 5; done
  ```
