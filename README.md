# AlohaOne

Marketing site for the AlohaOne ecosystem — a single AI-native business
platform with commerce, documents, cases, CRM, projects, and more, all
sharing a single identity and enabled on demand.

Intended to deploy to **alohaone.ai**.

## Stack

Plain HTML / CSS / vanilla JS with Bootstrap 5.3.3 and Font Awesome 6.5.1.
No build step, no framework, no server-side rendering. Drop on any static
host (S3 + CloudFront, Netlify, Vercel, GitHub Pages).

## Structure

```
AlohaOne/
├── index.html                  # Home — hero with AI brain viz, platform grid, CTA
├── platforms/                  # Per-platform detail pages (22 pages)
│   ├── commerce.html
│   ├── document.html
│   ├── backup.html
│   └── ... (one per platform)
├── css/
│   ├── style.css               # Site-wide styles, tropical palette, navbar, footer
│   └── platform-detail.css     # Detail page sections (hero, capabilities, pricing, etc.)
├── js/
│   └── main.js                 # Nav scroll, fade-in, form handling, brain viz renderer
├── generate_platforms.py       # Generator for all platform detail pages
└── README.md
```

## Adding or editing a platform

All 22 platform detail pages are generated from a central dict in
`generate_platforms.py`. To add a new platform or update an existing one:

1. Edit the `PLATFORMS` dict in `generate_platforms.py`
2. Run `python generate_platforms.py`
3. All 22 pages rebuild

The hero's floating neural-network brain viz pulls from a separate array in
`js/main.js` — keep that roughly in sync with the generator dict.

## Tropical palette

Colors are CSS variables in `css/style.css`:

```
--ao-primary    #0891b2   ocean teal
--ao-accent     #ec4899   hibiscus pink
--ao-secondary  #f97316   sunset orange
--ao-tropical   #22c55e   palm green
--ao-sunshine   #fbbf24   plumeria yellow
--ao-dark       #083344   deep ocean (dark sections)
--ao-light      #fff8ec   warm cream (light sections)
--ao-gradient   ocean → hibiscus → sunset (primary brand gradient)
```

## Related projects

- **[AlohaOneApp](../AlohaOneApp/)** — the application layer where CTAs land
  after users click "Start Free Trial" or "Register Now"
- Other platforms in the ecosystem live in sibling directories under
  `C:\Source\Aloha\`

## Deploy

Static site, no build step. Sync to any S3 + CloudFront distribution:

```bash
aws s3 sync . s3://<bucket>/ --exclude "*.py" --exclude ".git/*" --exclude "__pycache__/*"
```

The CTAs use relative paths to the sibling `AlohaOneApp/` directory. At
production deploy time those need to be rewritten to absolute URLs pointing
at the app subdomain (e.g., `https://app.alohaone.ai/...`).
