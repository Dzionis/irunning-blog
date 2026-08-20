# iRunning Website

Marketing site + blog for the [iRunning iOS app](https://apps.apple.com/us/app/id6770997508), served at **https://irunning.app**.

Built with Jekyll, styled with the app's "Trail calm" design system (see `DESIGN_SYSTEM.md`). Structure mirrors the `tts-blog` project.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Site runs at http://localhost:4000.

## Deployment (GitHub Pages)

1. Create a GitHub repo and push this directory
2. Settings → Pages → deploy from branch (`main`, root) — the `CNAME` file points GitHub Pages at `irunning.app`
3. At your DNS provider, point `irunning.app`:
   - `A` records → GitHub Pages IPs (`185.199.108.153`, `.109.`, `.110.`, `.111.`)
   - or `ALIAS`/`ANAME` → `<username>.github.io`
4. Enable "Enforce HTTPS" once the certificate is issued

## Adding a blog post

Create `_posts/YYYY-MM-DD-slug.md`:

```markdown
---
title: "Post Title"
description: "One-sentence summary used for SEO and the card excerpt."
categories: [features]   # features | events | news | releases
---

Content in Markdown…
```

Categories are color-coded on the site (green / amber / neutral / coral). The post layout appends the App Store CTA automatically.

## Analytics

GA4 is wired but disabled until a real Measurement ID replaces `G-XXXXXXXXXX` in `_config.yml`. Event tracking is data-attribute driven — see `SITE_CONTEXT.md`.

## Key docs

- `SITE_CONTEXT.md` — content, SEO, analytics, and structure reference
- `DESIGN_SYSTEM.md` — the Trail calm design system (source of truth for colors/type)
