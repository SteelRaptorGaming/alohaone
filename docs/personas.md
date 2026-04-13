# AlohaOne Ecosystem — Personas & Activities

_Last updated: 2026-04-12_

A reference for every major kind of user who interacts with the AlohaOne
ecosystem, what they do, and which platform (or platform feature) serves
that activity. Use this as the source of truth when designing new flows,
writing docs, or deciding which platform a new capability belongs in.

"Platform" in the last column refers to the product that owns the
experience — even when it's reached *through* the AlohaOne shell
(`app.alohaone.ai`), the underlying platform is what's listed, because
that's where the code lives and where changes should be made.

---

## Persona definitions

| Persona | Who they are | Auth home |
|---|---|---|
| **System Admin** | Visual Data Software staff who operate AlohaOne (e.g., Keith as `kmason`). Full cross-tenant visibility, configures pricing, impersonates to troubleshoot, manages infra. | `app.alohaone.ai` (unified) with `PlatformAdmin` security group |
| **Web Designer** | Professional who builds and runs Commerce storefronts — either for themselves or on behalf of a Website Owner. Pays AlohaOne per launched site. `StoreAdmin` role on one or more stores. | `app.alohaone.ai` → redirected to AlohaCommerce admin |
| **Website Owner** | The person or brand the storefront represents. Holds final authority over the store, may or may not do day-to-day work. `StoreOwner` role. Often the paying account holder if the site wasn't set up by an agency. | `app.alohaone.ai` → AlohaCommerce admin |
| **Website Customer** | The end shopper buying products on a Commerce-powered storefront. Has a customer record in the store's database; does **not** have an AlohaOne platform account. | The public storefront URL; optional store-level login only |
| **AlohaBackup User** | Individual or household using AlohaBackup to back up their devices. Starts on the free tier, may upgrade. | `app.alohaone.ai` (unified) → AlohaOneApp Backup tile + desktop/mobile client |
| **AlohaBrowser User (Parent)** | Adult who sets up the kid-safe browser and curates allowlists, views activity, manages child profiles. | `app.alohaone.ai` → AlohaOneApp Browser tile |
| **AlohaBrowser User (Child)** | Minor using the browser itself on iOS or Windows. No AlohaOne login — the child profile is owned by the parent. | Device-local child profile |
| **AlohaDocument User** | Someone storing, searching, and collaborating on documents. _(The Utah PSC deployment of AlohaDocument is a separate Aloha DMS install outside the shared ecosystem — this persona covers tenants in the shared AlohaOne cluster.)_ | `app.alohaone.ai` → AlohaOneApp Document tile |
| **Affiliate / Partner** | Third party who promotes a store (or the AlohaOne platform itself) in exchange for commission on referrals. | `app.alohaone.ai` → AlohaAffiliate portal |

---

## Activity matrix

| Persona | Expected activity | Platform (or platform feature) |
|---|---|---|
| **System Admin** | Set the monthly per-launched-store rate that web designers pay | AlohaCommerce — `Platform → Pricing Tiers` (Phase D.1) |
| System Admin | Add / rename / archive pricing tiers; each change round-trips to Stripe Prices | AlohaCommerce — `Platform → Pricing Tiers` |
| System Admin | Monitor platform MRR, active / past-due / canceled subscription counts | AlohaCommerce — `Platform → Billing` |
| System Admin | View every organization and store across all tenants | AlohaCommerce — `Platform → Organizations & Stores` |
| System Admin | Impersonate a web designer or owner to troubleshoot | AlohaCommerce admin — "Impersonate" action (existing) |
| System Admin | Read cross-tenant audit log | AlohaCore — `shared.audit_log` surfaced in AlohaOneApp |
| System Admin | Configure platform-scope email templates (welcome, receipts, etc.) | AlohaCommerce — `Content → Email Templates (platform)` |
| System Admin | Manage the platform media library | AlohaCommerce — `Content → Media Library (platform)` |
| System Admin | Approve affiliate applications and set global commission rates | AlohaAffiliate |
| System Admin | Configure AlohaBackup tier pricing (free / family / pro / enterprise) | AlohaBackup — `backup.account_tiers` (admin UI TBD) |
| System Admin | Manage cross-platform identity (unified auth, Cognito user pool) | AlohaOneApp — unified auth routes via Cognito |
| System Admin | Run database migrations, deploy Lambdas, manage infra | `AlohaCommerce/alohacommerce-infra-dev`, `AlohaOne/alohaone-infra-dev`, etc. |
| **Web Designer** | Sign up once at `app.alohaone.ai/register.html` — creates the org + first store automatically | AlohaOne — unified auth → AlohaCommerce `/api/auth/sync` provisioner |
| Web Designer | Pick which pricing tier each store is billed at | AlohaCommerce — `Store Settings → Platform Tier` |
| Web Designer | Build the storefront: products, categories, parts, pricing | AlohaCommerce admin — Store section |
| Web Designer | Configure a payment provider (Stripe) — required before publishing | AlohaCommerce — `Store Settings → Payment Processing` |
| Web Designer | Publish (or unpublish, or archive) a store and see the live status | AlohaCommerce — `Store Settings → Store Status` (Phase D.1) |
| Web Designer | Design themes, page builder layouts, custom domains | AlohaCommerce — `Design` section |
| Web Designer | Run marketing: campaigns, discounts, drip sequences, newsletters | AlohaCommerce — `Marketing` section |
| Web Designer | Manage their own AlohaOne account (profile, password, audit) | AlohaOneApp — `Account Settings` |
| Web Designer | See what they owe AlohaOne this month and past invoices | AlohaOneApp — `Billing` tile (Phase D.2, in progress) |
| Web Designer | Manage a Stripe Customer Portal session to change payment method | AlohaCommerce — `/api/billing/manage` → Stripe |
| Web Designer | Define subscription plans they sell to **their own clients** (site management fees) | AlohaCommerce — Client Plans UI (Phase D.3, planned) |
| Web Designer | Track which clients subscribe to their plans and when payment is due | AlohaCommerce — Client Subscriptions UI (Phase D.3, planned) |
| Web Designer | Optionally also use AlohaInventory / AlohaCRM for the store they run | AlohaInventory, AlohaCRM (live per platforms-data.js) |
| **Website Owner** | Sign in and see store health, orders, and sales | AlohaCommerce — `Store → Dashboard` |
| Website Owner | Approve pricing tier changes / downgrade / upgrade | AlohaCommerce — `Store Settings → Platform Tier` |
| Website Owner | Invite and remove web designers and staff for their store | AlohaCommerce — `Store Settings → Users` (existing `user_store_roles`) |
| Website Owner | View and export orders, customers, revenue reports | AlohaCommerce — `Store → Orders / Customers` |
| Website Owner | Request an archived store be restored (platform-admin action) | Contact System Admin — no self-serve yet |
| Website Owner | Manage billing payment method and see invoices | AlohaOneApp Billing tile → Stripe Customer Portal |
| Website Owner | Read product release notes and ecosystem news | AlohaOneApp home dashboard |
| **Website Customer** | Browse product catalog, configure 3D products | AlohaCommerce storefront Lambda + AlohaConfigurator (bundled) |
| Website Customer | Put items in cart and check out with Stripe | AlohaCommerce — storefront `/cart`, `/checkout` |
| Website Customer | Create optional customer account for order history | AlohaCommerce — store-level `customers` table (NOT an AlohaOne login) |
| Website Customer | Receive order confirmations, shipping updates, payment receipts | AlohaCommerce — `TemplatedEmailService` (SES) |
| Website Customer | Subscribe to the store's newsletter or drip sequence | AlohaCommerce — `Marketing → Newsletter / Sequences` |
| Website Customer | Leave a product review | AlohaCommerce — `Store → Reviews` |
| Website Customer | Contact the store owner for support | Store's configured contact channel; future: AlohaSupport portal |
| **AlohaBackup User** | Sign up via unified auth — provisions a free-tier `backup.accounts` row | AlohaOne unified auth → `AlohaBackup.Api /api/auth/sync` |
| AlohaBackup User | Install the desktop client (Avalonia) or MAUI mobile client | AlohaBackup — desktop / mobile clients |
| AlohaBackup User | Pick folders to back up and set schedule | AlohaBackup client UI — `Folders` page |
| AlohaBackup User | See backup progress, pause, cancel, clean up chunks | AlohaBackup client UI — byte-based progress (landed 2026-04-05) |
| AlohaBackup User | View backup status and storage usage at a glance | AlohaOneApp shell — Backup tile |
| AlohaBackup User | Upgrade from free tier to family / pro / enterprise | AlohaOneApp Billing tile (Phase D.4, not yet wired) |
| AlohaBackup User | Restore a file or whole device to another device | AlohaBackup client — `Restore` |
| AlohaBackup User | Manage their AlohaOne account (password, delete account, audit) | AlohaOneApp — `Account Settings` |
| **AlohaBrowser User (Parent)** | Sign up and create child device profiles | AlohaOne unified auth → AlohaOneApp Browser tile |
| AlohaBrowser User (Parent) | Curate per-child allowlist of sites | AlohaOneApp — Browser dashboard tile |
| AlohaBrowser User (Parent) | Review child's browsing activity | AlohaOneApp — Browser dashboard tile |
| AlohaBrowser User (Parent) | Approve one-off allowlist additions (requests from the child) | AlohaOneApp — pending-approvals view |
| **AlohaBrowser User (Child)** | Launch the kid-safe browser and visit allowlisted sites | AlohaBrowser — iOS (Expo/RN) or Windows (RN-Windows) client |
| AlohaBrowser User (Child) | Request that a new site be added to the allowlist | AlohaBrowser client → relays to parent via AlohaOneApp |
| **AlohaDocument User** | Sign up and land in a shared-schema AlohaDocument tenant | AlohaOne unified auth → AlohaDocument provisioner |
| AlohaDocument User | Upload, OCR, tag, and search documents | AlohaDocument — upload + full-text search |
| AlohaDocument User | Apply custom metadata fields per document type | AlohaDocument — dynamic fields |
| AlohaDocument User | Review version history and audit activity | AlohaDocument — versioning & audit |
| AlohaDocument User | Share or collaborate on documents with team members | AlohaDocument |
| **Affiliate / Partner** | Apply to become an affiliate for a store (or platform) | AlohaAffiliate — partner portal signup |
| Affiliate / Partner | Get a tracking link / code | AlohaAffiliate — tracking & attribution |
| Affiliate / Partner | See clicks, conversions, pending commission | AlohaAffiliate — partner dashboard |
| Affiliate / Partner | Receive commission payouts | AlohaAffiliate — Stripe Connect payouts (default off) |
| Affiliate / Partner | Pull marketing collateral and creative assets | AlohaAffiliate / AlohaCommerce — `Marketing → Collateral` |

---

## Notes and conventions

- **Single sign-on.** Every persona above (except Website Customer and
  AlohaBrowser Child) logs in exactly once at `app.alohaone.ai`. Each
  platform either hosts its experience inside AlohaOneApp as a tile, or
  trampolines the user over with a short-lived cross-origin token.
- **Website Customer is deliberately outside AlohaOne.** They are a
  customer *of the web designer's store*, not of AlohaOne. No AlohaOne
  login, no audit log row, no quota. Only the store-level `customers`
  table knows they exist.
- **Two-tier billing (Phase D).** AlohaOne charges the Web Designer a
  flat per-launched-store monthly fee (Tier 1, D.1 — shipped). The Web
  Designer charges the Website Owner whatever they want as a managed
  service fee (Tier 2, D.3 — planned). AlohaOne takes no % of Tier 2
  revenue — Tier 2 is entirely the designer's to keep.
- **"Other platform" personas look like AlohaBackup.** Any new platform
  that gets added (AlohaDrive, AlohaCMS, AlohaSurvey, AlohaMessage, etc.)
  follows the same shape: unified auth at `app.alohaone.ai`, a tile in
  AlohaOneApp, an optional paid tier managed through the shared billing
  flow, and an optional client app that calls the platform's API.
- **Platform ownership.** When a capability could belong to multiple
  platforms, route it to the one that owns the data. Example: a
  designer's own client-subscription tracking stays in AlohaCommerce
  because the data is scoped per-store and the UI lives in the store
  admin. It is **not** a feature of AlohaOneApp, which is
  cross-platform-shell-only.
