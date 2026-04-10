"""
AlohaOne Platform Detail Page Generator
----------------------------------------
Generates one detail HTML page per platform from a central data dictionary.
Run from C:\\Source\\Aloha\\AlohaOne\\ : python generate_platforms.py
"""

import os
import pathlib

OUT_DIR = pathlib.Path(__file__).parent / "platforms"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# PLATFORM DATA
# =========================================================
# Each platform has:
#   slug, name, icon, gradient, status ('live'|'coming'|'planned'),
#   tagline, description (paragraphs),
#   overview (single paragraph for overview section),
#   capabilities: list of { title, icon, gradient, items: [...] },
#   integrations: list of { slug, name, icon, gradient, note },
#   cta: optional dict with primary_label, primary_href, secondary_label, secondary_href

PLATFORMS = {

# ---------------- AlohaCommerce ----------------
"commerce": {
    "name": "AlohaCommerce",
    "icon": "fa-shopping-cart",
    "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
    "status": "live",
    "tagline": "Enterprise e-commerce without the enterprise price tag.",
    "description": "A multi-tenant commerce platform with products, orders, payments, shipping, flexible theming, and an AI-powered content studio — built on serverless AWS from day one.",
    "overview": "AlohaCommerce is the storefront and order-management backbone of the AlohaOne ecosystem. It handles the entire retail lifecycle — product catalog, checkout, payments, orders — with a template-first storefront engine that lets you ship a beautiful store in minutes, not months. AlohaInventory, AlohaCRM, AlohaAffiliate, and AlohaConfigurator are already bundled and toggle-able per tenant. Pair it with AlohaDeliver for last-mile fulfillment.",
    "capabilities": [
        {
            "title": "Products & Catalog",
            "icon": "fa-box",
            "gradient": "linear-gradient(135deg,#0891b2,#0e7490)",
            "items": [
                "Simple, configurable, bundle, and digital products",
                "Variants with dependent options and dynamic pricing",
                "Product categories and collections",
                "SEO per product and category",
                "Reviews, ratings, and verified purchase badges",
                "Bulk import with auto-mapping",
                "Deep stock sync with AlohaInventory (optional)",
            ]
        },
        {
            "title": "Checkout & Orders",
            "icon": "fa-receipt",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Session-based carts with guest checkout",
                "Stripe payments + Stripe Connect per-store",
                "Discount codes, BOGO, and scheduled promos",
                "Tax engine with per-region rules",
                "Full order lifecycle with status history",
                "Refunds, cancellations, and partial captures",
            ]
        },
        {
            "title": "Storefront & Theming",
            "icon": "fa-palette",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Template gallery (Artisan, Coastal, Modern, Boutique, and more)",
                "Liquid templating with live preview",
                "Section-based page builder — no coding",
                "CSS variable theming and brand controls",
                "Content pages, blog, and gift finder",
                "Custom domains with managed SSL",
            ]
        },
        {
            "title": "Shipping & Fulfillment",
            "icon": "fa-truck",
            "gradient": "linear-gradient(135deg,#14b8a6,#0d9488)",
            "items": [
                "Configurable methods and zones",
                "White-glove, freight, and local delivery",
                "Carrier integration and tracking numbers",
                "Shipment status timeline",
                "Regional delivery scheduling",
                "Self-pickup and in-store options",
            ]
        },
        {
            "title": "AI Content Studio",
            "icon": "fa-wand-magic-sparkles",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "AI product description generation",
                "Conversational image generation (MidJourney-style)",
                "Background removal and upscaling",
                "Theme palette generation",
                "Credit-based wallet for AI usage",
                "AI-powered gift recommendations",
            ]
        },
        {
            "title": "Platform & Admin",
            "icon": "fa-gauge-high",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "Real-time sales and conversion dashboards",
                "Role-based team permissions",
                "Webhook system with signed payloads",
                "Multi-tenant with PostgreSQL RLS",
                "Ecwid, Etsy, and custom integrations",
                "Full audit logging and activity feeds",
            ]
        },
    ],
    "integrations": [
        {"slug": "inventory", "name": "AlohaInventory", "note": "Warehouses, BOMs, and stock control"},
        {"slug": "deliver", "name": "AlohaDeliver", "note": "Last-mile delivery with photo proof"},
        {"slug": "email", "name": "AlohaEmail", "note": "Order confirmations and transactional mail"},
        {"slug": "marketing", "name": "AlohaMarketing", "note": "Attribution and campaign tracking"},
        {"slug": "social", "name": "AlohaSocial", "note": "Auto-post products across social platforms"},
        {"slug": "affiliate", "name": "AlohaAffiliate", "note": "Commission tracking on orders"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Customers become CRM contacts automatically"},
        {"slug": "data", "name": "AlohaData", "note": "Order and product analytics warehouse"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents for product Q&A and support"},
    ],
    "cta": {
        "primary_label": "Start Free Trial",
        "primary_href": "../../AlohaOneApp/index.html?platform=commerce&intent=register",
        "secondary_label": "See a Live Store",
        "secondary_href": "https://ultimatecraftdesk.com",
    },
    "customers": {
        "label": "Real Stores, Live Today",
        "heading": "Built for complex products, proven on real ones",
        "sub": "From cubbie-by-cubbie custom desks to made-to-order gift crates, AlohaCommerce runs storefronts that off-the-shelf platforms can't handle.",
        "items": [
            {
                "name": "UltimateCraftDesk.com",
                "url": "https://ultimatecraftdesk.com",
                "description": "Flagship custom-desk store with 3D configurator, component-level inventory, and full production workflow integration.",
                "tags": ["3D Configurator", "Configurable", "BOM"],
            },
            {
                "name": "NoodleBoards.com",
                "url": "https://noodleboards.com",
                "description": "Custom stovetop covers and serving trays with size, wood, and finish options.",
                "tags": ["Made-to-Order", "Variants"],
            },
            {
                "name": "UltimateDogBeds.com",
                "url": "https://ultimatedogbeds.com",
                "description": "Customizable dog beds with size, fabric, and fill options.",
                "tags": ["Configurable", "Pet"],
            },
            {
                "name": "SecretArms.com",
                "url": "https://secretarms.com",
                "description": "Furniture and wall pieces with built-in firearm storage compartments.",
                "tags": ["Furniture", "Niche"],
            },
            {
                "name": "Bodyjunk.com",
                "url": "https://bodyjunk.com",
                "description": "Body lotions, lip balms, and soaps with scent variants and bundles.",
                "tags": ["Variants", "Bundles"],
            },
            {
                "name": "OceanStyled.com",
                "url": "https://oceanstyled.com",
                "description": "Ocean and beach apparel with standard size and color variants.",
                "tags": ["Apparel"],
            },
            {
                "name": "GiftedCrate",
                "description": "Customizable gift baskets with a visual crate builder.",
                "tags": ["Configurator", "Gifting"],
            },
            {
                "name": "UltimateWeddingRentals.com",
                "url": "https://ultimateweddingrentals.com",
                "description": "Wedding rentals with inventory-based reservation model.",
                "tags": ["Rental", "Inventory"],
            },
        ],
    },
    "pricing": {
        "label": "Pricing",
        "heading": "First store free. Grow from there.",
        "sub": "No credit card required to start. You only pay for additional stores as you launch them.",
        "tiers": [
            {
                "name": "Starter",
                "price": "$0",
                "period": "first store free",
                "cta_label": "Start Free",
                "cta_href": "../../AlohaOneApp/index.html?platform=commerce&intent=register",
                "features": [
                    "1 storefront",
                    "Unlimited products",
                    "Unlimited orders",
                    "Bundled CRM, Affiliate, Inventory, Configurator",
                    "$20 AI Image Studio credit",
                    "Template gallery + page builder",
                ],
            },
            {
                "name": "Multi-Store",
                "price": "$9.99",
                "period": "per additional store · monthly",
                "featured": True,
                "cta_label": "Start Free, Pay Later",
                "cta_href": "../../AlohaOneApp/index.html?platform=commerce&intent=register",
                "features": [
                    "Everything in Starter",
                    "Add stores on demand",
                    "Stripe Connect payouts",
                    "Custom domains with managed SSL",
                    "Priority email support",
                    "Billed per active store",
                ],
            },
            {
                "name": "Enterprise",
                "price": "Custom",
                "period": "white-glove onboarding",
                "cta_label": "Contact Us",
                "cta_href": "../index.html#cta",
                "features": [
                    "Everything in Multi-Store",
                    "Dedicated onboarding",
                    "SLA and support agreement",
                    "Custom integrations",
                    "Production workflow integration (AlohaFlow)",
                    "Delivery integration (AlohaDeliver)",
                ],
            },
        ],
    },
    "final_cta": {
        "heading": "Launch your store in minutes.",
        "sub": "Sign up, pick a template, and your storefront is live. No credit card required — your first store is free, and you can configure custom products, run affiliate programs, and manage component inventory from day one.",
        "primary_label": "Start Free Trial",
        "primary_href": "../../AlohaOneApp/index.html?platform=commerce&intent=register",
        "secondary_label": "See a Live Store",
        "secondary_href": "https://ultimatecraftdesk.com",
    },
},

# ---------------- AlohaDocument ----------------
"document": {
    "name": "AlohaDocument",
    "icon": "fa-file-alt",
    "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
    "status": "live",
    "tagline": "Intelligent document management with OCR, search, and workflow.",
    "description": "Upload, organize, and find any document. Built-in OCR, full-text search, custom metadata, versioning, and a complete audit trail — trusted by regulated industries.",
    "overview": "AlohaDocument is a modern document management system built for organizations that need to store, find, and control access to critical files. Every document is indexed, every action is audited, and every field is configurable.",
    "capabilities": [
        {
            "title": "Capture & Process",
            "icon": "fa-upload",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Drag-and-drop upload of any file type",
                "Automatic OCR for scanned PDFs and images",
                "Audio and video transcription",
                "PDF conversion for standardized viewing",
                "ZIP decompression and batch import",
                "Bulk classification on upload",
            ]
        },
        {
            "title": "Search & Discovery",
            "icon": "fa-magnifying-glass",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Full-text search across all content",
                "Relevance-ranked results with context snippets",
                "AND/OR query syntax",
                "Metadata-based advanced search",
                "AI-assisted natural language queries",
                "Creator, date, and status filters",
            ]
        },
        {
            "title": "Dynamic Metadata",
            "icon": "fa-tags",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Custom fields per document type",
                "Text, date, numeric, dropdown, and cascading lists",
                "Required-field and regex validation",
                "Color-coded list values",
                "Field-level change history",
                "Reusable field library",
            ]
        },
        {
            "title": "Versioning & Audit",
            "icon": "fa-code-branch",
            "gradient": "linear-gradient(135deg,#14b8a6,#0d9488)",
            "items": [
                "Unlimited version history with notes",
                "Immutable activity timeline",
                "Every view, download, and edit tracked",
                "Soft deletes for recovery",
                "Performance metrics on every query",
                "Compliance-ready audit exports",
            ]
        },
        {
            "title": "Relationships & Notes",
            "icon": "fa-link",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Paperclip documents to other documents",
                "Append-only comments with timestamps",
                "Auto-generated document indexes",
                "Quick navigation between related files",
                "Barcode and external-ID tracking",
                "Bulk download of document families",
            ]
        },
        {
            "title": "Permissions & Security",
            "icon": "fa-lock",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "Document-level read/edit/delete permissions",
                "Security classifications (Public, Internal, Restricted)",
                "Role-based security groups",
                "Project and organization isolation",
                "Microsoft Entra / Azure AD SSO",
                "Encrypted storage with S3 server-side encryption",
            ]
        },
    ],
    "integrations": [
        {"slug": "case", "name": "AlohaCase", "note": "Attach documents to cases and dockets"},
        {"slug": "search", "name": "AlohaSearch", "note": "Full-text and semantic search across every file"},
        {"slug": "support", "name": "AlohaSupport", "note": "Link docs to tickets as reference"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Attach files to customer records"},
        {"slug": "project", "name": "AlohaProject", "note": "Specs and design docs on issues"},
        {"slug": "agent", "name": "AlohaAgent", "note": "Agents can search and summarize your documents"},
    ],
},

# ---------------- AlohaCase ----------------
"case": {
    "name": "AlohaCase",
    "icon": "fa-gavel",
    "gradient": "linear-gradient(135deg,#6366f1,#4338ca)",
    "status": "live",
    "tagline": "Case and docket management for legal, compliance, and regulatory teams.",
    "description": "Every case is a living record — documents, metadata, comments, and a full audit trail. Purpose-built for commissions, agencies, law firms, and regulated industries.",
    "overview": "AlohaCase models any case-driven workflow — legal matters, regulatory dockets, compliance investigations, insurance claims. Cases have structured metadata, attached documents, searchable content, and a complete history of who did what and when.",
    "capabilities": [
        {
            "title": "Case Lifecycle",
            "icon": "fa-folder-open",
            "gradient": "linear-gradient(135deg,#6366f1,#4338ca)",
            "items": [
                "Configurable case types per practice area",
                "Auto-generated case numbers with prefixes",
                "Custom status workflows",
                "Duplicate detection on creation",
                "Case templates and standardized intake",
                "Bulk case operations",
            ]
        },
        {
            "title": "Documents in Context",
            "icon": "fa-paperclip",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Attach unlimited documents to a case",
                "Auto-generated case index on first upload",
                "Full-text search within a case",
                "Bulk document upload and classification",
                "Detach with audit trail",
                "Download the entire case as a ZIP",
            ]
        },
        {
            "title": "Case Metadata",
            "icon": "fa-list-ul",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Custom fields per case type",
                "Parties, jurisdictions, utilities, docket numbers",
                "Required-field validation",
                "Field-level change history",
                "Metadata-based search and filter",
                "Color-coded status and priority",
            ]
        },
        {
            "title": "Collaboration",
            "icon": "fa-comments",
            "gradient": "linear-gradient(135deg,#14b8a6,#0d9488)",
            "items": [
                "Append-only case comments",
                "Unified activity timeline across case and documents",
                "User and group assignments",
                "Notifications on case events",
                "Cross-team visibility with permission gates",
                "Internal notes separate from external record",
            ]
        },
        {
            "title": "Reporting & Export",
            "icon": "fa-file-export",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "CSV export of any case list",
                "Column selection and custom views",
                "Exports respect all filters",
                "Bulk download of case documents",
                "Performance and activity reports",
                "Retention and disposition policies",
            ]
        },
        {
            "title": "Access Control",
            "icon": "fa-user-shield",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "Case-level permissions",
                "Project and organization isolation",
                "Multi-organization tenancy",
                "Role-based security groups",
                "Microsoft Entra / Azure AD SSO",
                "Every action attributed and auditable",
            ]
        },
    ],
    "integrations": [
        {"slug": "document", "name": "AlohaDocument", "note": "Powers the case document store"},
        {"slug": "search", "name": "AlohaSearch", "note": "Semantic search within and across cases"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Link cases to parties and contacts"},
        {"slug": "support", "name": "AlohaSupport", "note": "Escalate tickets into formal cases"},
        {"slug": "project", "name": "AlohaProject", "note": "Track case work as project tasks"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents summarize and research cases"},
    ],
},

# ---------------- AlohaConfigurator ----------------
"configurator": {
    "name": "AlohaConfigurator",
    "icon": "fa-cube",
    "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
    "status": "live",
    "tagline": "3D product configuration with real-time rendering.",
    "description": "Let customers design their own product in 3D — with real-time visuals, live pricing, and automatic bill-of-materials generation that flows straight into your commerce cart. Already prototyped on Three.js and integrating into AlohaCommerce for UltimateCraftDesk.com.",
    "overview": "AlohaConfigurator is a 3D configuration engine for made-to-order products. A working Three.js prototype already drives the Ultimate Craft Desk storefront, and the template-first architecture makes it trivial to spin up new configurators for other AlohaCommerce stores. Every configuration turns into a ready-to-fulfill order with full BOM.",
    "capabilities": [
        {
            "title": "3D Engine",
            "icon": "fa-cube",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Real-time 3D rendering in the browser",
                "Mobile-optimized WebGL viewer",
                "Drag-to-rotate, zoom, and AR preview",
                "Material and color swapping",
                "Component-level geometry swaps",
                "Photorealistic lighting presets",
            ]
        },
        {
            "title": "Template-First",
            "icon": "fa-layer-group",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Gallery of configuration templates",
                "Clone and customize per product",
                "Rule engine for option dependencies",
                "Constraint validation",
                "Visual option preview",
                "No-code template editor",
            ]
        },
        {
            "title": "Pricing & BOM",
            "icon": "fa-calculator",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Live pricing as customer configures",
                "Dynamic bill-of-materials generation",
                "Option-level price adjustments",
                "Volume and tier pricing",
                "Automatic component allocation",
                "Cost and margin tracking",
            ]
        },
        {
            "title": "Commerce Integration",
            "icon": "fa-cart-arrow-down",
            "gradient": "linear-gradient(135deg,#14b8a6,#0d9488)",
            "items": [
                "One-click add to AlohaCommerce cart",
                "Configuration snapshot saved with order",
                "Production-ready BOM export",
                "Reorder past configurations",
                "Save and share configurations",
                "Quote-to-order workflow",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Configurations become cart line items"},
        {"slug": "inventory", "name": "AlohaInventory", "note": "BOM resolves against component stock"},
        {"slug": "document", "name": "AlohaDocument", "note": "Spec sheets and technical drawings"},
        {"slug": "project", "name": "AlohaProject", "note": "Production tasks from custom orders"},
    ],
    "cta": {
        "primary_label": "See It Live",
        "primary_href": "https://ultimatecraftdesk.com",
        "secondary_label": "Enable in AlohaOne",
        "secondary_href": "../../AlohaOneApp/index.html?platform=configurator&intent=register",
    },
},

# ---------------- AlohaBackup ----------------
"backup": {
    "name": "AlohaBackup",
    "icon": "fa-shield-alt",
    "gradient": "linear-gradient(135deg,#14b8a6,#0d9488)",
    "status": "live",
    "tagline": "Every file. Every device. Always safe.",
    "description": "Continuous encrypted backup across Windows, macOS, Linux, iOS, and Android. Restore anywhere, anytime. Free tier includes 1 device and 5 GB — no credit card required.",
    "overview": "AlohaBackup runs silently on every device you own. Filesystem watchers catch every change the instant it happens, content-addressed chunking deduplicates automatically across your whole account, and AES-256 encryption keeps everything safe before it leaves your machine. Lose a device, break a laptop, get hit by ransomware — pull any file from any point in history onto any other registered device in seconds.",
    "capabilities": [
        {
            "title": "Continuous Backup",
            "icon": "fa-sync",
            "gradient": "linear-gradient(135deg,#14b8a6,#0d9488)",
            "items": [
                "Filesystem watchers — no scheduled jobs",
                "Content-addressed chunking (SHA-256 dedup)",
                "Smart 4-8 MB chunks to minimize bandwidth",
                "Include and exclude glob patterns",
                "Cross-platform: Windows, macOS, Linux, iOS, Android",
                "Daemon and CLI modes for servers",
            ]
        },
        {
            "title": "Security & Encryption",
            "icon": "fa-lock",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "AES-256 at rest via AWS KMS per-tenant",
                "TLS encryption in transit",
                "Hardware-ID device binding",
                "Per-device UUID in OS secure storage",
                "Device revocation from any browser",
                "Presigned URLs for direct S3 upload",
            ]
        },
        {
            "title": "Restore Anywhere",
            "icon": "fa-download",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Restore files to any registered device",
                "File-level or folder-level restore",
                "Version history (7-365 days by tier)",
                "Priority restore on Pro and Enterprise",
                "Browse all backed-up files online",
                "Download single files or ZIP exports",
            ]
        },
        {
            "title": "Tiers & Account",
            "icon": "fa-user-tag",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Free tier — get started in 60 seconds",
                "Family, Pro, and Enterprise tiers",
                "Progressive device and storage limits",
                "Promotional discount codes",
                "Per-device storage quotas",
                "SSO and SLAs on Enterprise",
            ]
        },
    ],
    "integrations": [
        {"slug": "document", "name": "AlohaDocument", "note": "Backup your document repository"},
        {"slug": "search", "name": "AlohaSearch", "note": "Find backed-up files across every device"},
        {"slug": "agent", "name": "AlohaAgent", "note": "Agents can search backed-up files"},
    ],
    "cta": {
        "primary_label": "Start Free",
        "primary_href": "../../AlohaOneApp/index.html?platform=backup&intent=register",
        "secondary_label": "Sign In",
        "secondary_href": "../../AlohaOneApp/index.html?platform=backup",
    },
    "platform_matrix": {
        "label": "Every Device",
        "heading": "Works everywhere you do",
        "sub": "One account, all your devices. Sign in once and new installs register automatically.",
        "items": [
            {"name": "Windows",  "detail": "10/11 · 79 MB",        "icon": "fab fa-windows",
             "href": "http://aloha-dev-web-f4d6fd.s3-website-us-east-1.amazonaws.com/downloads.html"},
            {"name": "macOS",    "detail": "Apple Silicon + Intel","icon": "fab fa-apple",
             "href": "http://aloha-dev-web-f4d6fd.s3-website-us-east-1.amazonaws.com/downloads.html"},
            {"name": "Linux",    "detail": "Ubuntu / Fedora · 40 MB","icon": "fab fa-linux",
             "href": "http://aloha-dev-web-f4d6fd.s3-website-us-east-1.amazonaws.com/downloads.html"},
            {"name": "Android",  "detail": "7.0+ · 35 MB",         "icon": "fab fa-android",
             "href": "http://aloha-dev-web-f4d6fd.s3-website-us-east-1.amazonaws.com/downloads.html"},
            {"name": "iOS",      "detail": "15+",                  "icon": "fab fa-app-store-ios",
             "soon": True},
        ],
    },
    "pricing": {
        "label": "Pricing",
        "heading": "Simple pricing. Fair limits.",
        "sub": "Start free and upgrade only when you outgrow it. No credit card to sign up.",
        "tiers": [
            {
                "name": "Free",
                "price": "$0",
                "period": "forever",
                "cta_label": "Start Free",
                "cta_href": "../../AlohaOneApp/index.html?platform=backup&intent=register&tier=free",
                "features": [
                    "1 device",
                    "5 GB total storage",
                    "7-day version history",
                    "Email support",
                    "No credit card required",
                ],
            },
            {
                "name": "Family",
                "price": "$9.99",
                "period": "per month",
                "featured": True,
                "cta_label": "Start Family Plan",
                "cta_href": "../../AlohaOneApp/index.html?platform=backup&intent=register&tier=family",
                "features": [
                    "5 devices",
                    "500 GB total storage",
                    "100 GB per device",
                    "30-day version history",
                    "Priority email support",
                ],
            },
            {
                "name": "Pro",
                "price": "$19.99",
                "period": "per month",
                "cta_label": "Start Pro",
                "cta_href": "../../AlohaOneApp/index.html?platform=backup&intent=register&tier=pro",
                "features": [
                    "10 devices",
                    "2 TB total storage",
                    "500 GB per device",
                    "90-day version history",
                    "Priority restore",
                    "Chat support",
                ],
            },
        ],
    },
    "final_cta": {
        "heading": "Never lose a file again.",
        "sub": "Install AlohaBackup on every device, sign in once, and let it run. The free tier is enough for most single-device users — you only pay when you actually need more.",
        "primary_label": "Start Free",
        "primary_href": "../../AlohaOneApp/index.html?platform=backup&intent=register",
        "secondary_label": "Download the App",
        "secondary_href": "http://aloha-dev-web-f4d6fd.s3-website-us-east-1.amazonaws.com/downloads.html",
    },
    "integration_note": "Register for AlohaOne to enable AlohaBackup on your account. Downloads for Windows, macOS, Linux, and Android are hosted on the AlohaBackup download page linked below — sign in once on any device and your whole fleet syncs.",
},

# ---------------- AlohaCRM ----------------
"crm": {
    "name": "AlohaCRM",
    "icon": "fa-users",
    "gradient": "linear-gradient(135deg,#10b981,#059669)",
    "status": "live",
    "tagline": "The single source of truth for every customer relationship.",
    "description": "Contacts, companies, deals, pipelines, landing pages, lead capture, and scoring — already bundled inside AlohaCommerce and ready to toggle on per-tenant.",
    "overview": "AlohaCRM is the customer database for the entire AlohaOne ecosystem. The contacts, companies, leads, landing pages, and scoring engines are already running inside AlohaCommerce — activate them for any tenant with a single feature flag. Every other AlohaOne platform (Marketing, Email, Support) reads from and writes to the same source of truth.",
    "capabilities": [
        {
            "title": "Contacts & Companies",
            "icon": "fa-address-book",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Unified contact database",
                "Company hierarchies and subsidiaries",
                "Custom fields and tags",
                "Activity timeline per contact",
                "Merge duplicates with history preservation",
                "Bulk import and export",
            ]
        },
        {
            "title": "Landing Pages",
            "icon": "fa-browser",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Drag-and-drop landing page builder",
                "Template gallery with industry layouts",
                "Mobile-responsive by default",
                "Custom domains and SSL",
                "A/B split testing",
                "Conversion tracking built-in",
            ]
        },
        {
            "title": "Lead Capture & Scoring",
            "icon": "fa-filter",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Forms with conditional logic",
                "Progressive profiling",
                "AI-powered lead scoring",
                "Automatic lead routing",
                "Duplicate detection on capture",
                "Source attribution from any channel",
            ]
        },
        {
            "title": "Pipelines & Deals",
            "icon": "fa-chart-line",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Multiple configurable pipelines",
                "Kanban and list views",
                "Stage automation rules",
                "Weighted forecasting",
                "Win/loss tracking",
                "Activity and quota dashboards",
            ]
        },
        {
            "title": "Segmentation",
            "icon": "fa-layer-group",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Dynamic audience segments",
                "Behavioral and demographic filters",
                "Segments power Marketing and Email",
                "Saved views for every team",
                "Segment change notifications",
                "Exportable to any other platform",
            ]
        },
        {
            "title": "Unified Customer View",
            "icon": "fa-eye",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "Commerce orders on the contact timeline",
                "Support tickets in the same view",
                "Email engagement history",
                "Survey responses attached",
                "Document attachments per contact",
                "One-click context for any team member",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Customers sync as contacts automatically"},
        {"slug": "marketing", "name": "AlohaMarketing", "note": "Segments power campaign audiences"},
        {"slug": "email", "name": "AlohaEmail", "note": "Drip recipients come from CRM"},
        {"slug": "support", "name": "AlohaSupport", "note": "Full customer context on every ticket"},
        {"slug": "survey", "name": "AlohaSurvey", "note": "Responses attach to contacts"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents work the pipeline for you"},
    ],
    "cta": {
        "primary_label": "Enable AlohaCRM",
        "primary_href": "../../AlohaOneApp/index.html?platform=crm&intent=register",
        "secondary_label": "Learn About Commerce",
        "secondary_href": "commerce.html",
    },
},

# ---------------- AlohaAffiliate ----------------
"affiliate": {
    "name": "AlohaAffiliate",
    "icon": "fa-handshake",
    "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
    "status": "live",
    "tagline": "Turn partners into your sales force.",
    "description": "A complete affiliate and referral program — partner portal, tracking links, commission rules, automated payouts, and fraud prevention. Already bundled inside AlohaCommerce and ready to toggle on per-tenant.",
    "overview": "AlohaAffiliate is already running inside AlohaCommerce — partner applications, commission payouts, tracking, and fraud detection are all implemented. Activate the feature flag and your tenant instantly has a full affiliate program: partners get their own portal with performance dashboards and marketing collateral; you get automation and attribution on every order.",
    "capabilities": [
        {
            "title": "Partner Portal",
            "icon": "fa-user-tie",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Branded signup and application flow",
                "Approval workflow with status",
                "Performance dashboard per affiliate",
                "Click, lead, and conversion analytics",
                "Commission and payout history",
                "Marketing collateral library (banners, copy, docs)",
            ]
        },
        {
            "title": "Tracking & Attribution",
            "icon": "fa-link",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Unique tracking codes per affiliate",
                "Click tracking with IP and device logs",
                "Cookie-based and fingerprint attribution",
                "Affiliate-specific discount codes",
                "Campaign organization and tagging",
                "Landing URL tracking",
            ]
        },
        {
            "title": "Commissions & Payouts",
            "icon": "fa-money-bill-wave",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Percentage, flat, and tiered commissions",
                "Per-product or per-category rules",
                "Stripe Connect automated payouts",
                "Payout schedules and holds",
                "Tax form collection (W-9, W-8)",
                "1099 generation at year-end",
            ]
        },
        {
            "title": "Fraud Prevention",
            "icon": "fa-shield-halved",
            "gradient": "linear-gradient(135deg,#ef4444,#dc2626)",
            "items": [
                "Self-referral detection",
                "Click-spam filtering",
                "Velocity and pattern monitoring",
                "Suspicious activity alerts",
                "Manual review queue",
                "Fingerprint-based duplicate blocking",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Commissions on every order"},
        {"slug": "marketing", "name": "AlohaMarketing", "note": "Campaign attribution and UTMs"},
        {"slug": "email", "name": "AlohaEmail", "note": "Partner notifications and payout alerts"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Partners are contacts with a role"},
    ],
    "cta": {
        "primary_label": "Enable AlohaAffiliate",
        "primary_href": "../../AlohaOneApp/index.html?platform=affiliate&intent=register",
        "secondary_label": "Learn About Commerce",
        "secondary_href": "commerce.html",
    },
},

# ---------------- AlohaMarketing ----------------
"marketing": {
    "name": "AlohaMarketing",
    "icon": "fa-bullhorn",
    "gradient": "linear-gradient(135deg,#f97316,#ea580c)",
    "status": "coming",
    "tagline": "Campaigns, automation, and growth — unified.",
    "description": "Design campaigns, build audiences from CRM segments, send through Email, and measure everything. The growth engine for the entire AlohaOne suite.",
    "overview": "AlohaMarketing is the campaign orchestration layer. It pulls audiences from AlohaCRM, delivers through AlohaEmail, attributes conversions from AlohaCommerce, and tracks everything end-to-end. You design the journey; the ecosystem runs it.",
    "capabilities": [
        {
            "title": "Campaign Builder",
            "icon": "fa-wand-magic-sparkles",
            "gradient": "linear-gradient(135deg,#f97316,#ea580c)",
            "items": [
                "Visual campaign designer",
                "Multi-channel orchestration (email, SMS, push)",
                "Trigger-based and scheduled campaigns",
                "A/B and multivariate testing",
                "Goal setting and tracking",
                "Template library and cloning",
            ]
        },
        {
            "title": "Drip & Automation",
            "icon": "fa-diagram-project",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Drag-and-drop journey builder",
                "Delays, branches, and conditions",
                "Trigger events from any platform",
                "Exit criteria and goal completion",
                "Live journey analytics",
                "Enrollment and progression tracking",
            ]
        },
        {
            "title": "Audiences",
            "icon": "fa-users-viewfinder",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Pull segments directly from AlohaCRM",
                "Behavioral filters (purchased, opened, clicked)",
                "Lookalike and predictive segments",
                "Real-time segment updates",
                "Exclusion rules and suppression lists",
                "Frequency capping",
            ]
        },
        {
            "title": "Attribution & Analytics",
            "icon": "fa-chart-column",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Multi-touch attribution",
                "Revenue tracking from Commerce",
                "Open, click, and conversion dashboards",
                "Cohort analysis",
                "Campaign ROI reporting",
                "Export to BI tools",
            ]
        },
    ],
    "integrations": [
        {"slug": "crm", "name": "AlohaCRM", "note": "Audiences come from CRM segments"},
        {"slug": "email", "name": "AlohaEmail", "note": "Delivery engine for every campaign"},
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Revenue attribution and product promos"},
        {"slug": "data", "name": "AlohaData", "note": "Warehouse for campaign analytics"},
        {"slug": "affiliate", "name": "AlohaAffiliate", "note": "Campaign attribution for partners"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents write and optimize campaigns"},
    ],
},

# ---------------- AlohaEmail ----------------
"email": {
    "name": "AlohaEmail",
    "icon": "fa-envelope",
    "gradient": "linear-gradient(135deg,#fb923c,#f97316)",
    "status": "coming",
    "tagline": "Transactional and drip email that actually lands.",
    "description": "The delivery engine for every AlohaOne platform. Build templates once, send from anywhere, and track deliverability, bounces, and engagement in real time.",
    "overview": "AlohaEmail is the shared email infrastructure for the whole ecosystem. Transactional mail from Commerce, drip sequences from Marketing, ticket updates from Support, partner alerts from Affiliate — all flow through one deliverability-optimized pipeline.",
    "capabilities": [
        {
            "title": "Template Builder",
            "icon": "fa-brush",
            "gradient": "linear-gradient(135deg,#fb923c,#f97316)",
            "items": [
                "Drag-and-drop MJML editor",
                "Responsive by default",
                "Liquid variable interpolation",
                "Template library and sharing",
                "Inline testing and preview",
                "Dark mode compatibility checks",
            ]
        },
        {
            "title": "Transactional",
            "icon": "fa-paper-plane",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "High-throughput transactional API",
                "Order, shipping, and receipt emails",
                "Password reset and verification",
                "Per-tenant sender domains",
                "DKIM and SPF automation",
                "Webhook delivery events",
            ]
        },
        {
            "title": "Drip Sequences",
            "icon": "fa-clock",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Multi-step sequence builder",
                "Triggered by any ecosystem event",
                "Time delays and conditional branches",
                "Auto-unsubscribe on unsubscribe intent",
                "Re-engagement and win-back flows",
                "Recipient progression tracking",
            ]
        },
        {
            "title": "Deliverability",
            "icon": "fa-gauge-high",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Bounce and complaint handling",
                "Reputation monitoring",
                "Suppression list management",
                "List hygiene and validation",
                "Send-time optimization",
                "Inbox placement analytics",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Order and shipping notifications"},
        {"slug": "marketing", "name": "AlohaMarketing", "note": "Campaign delivery backbone"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Contacts as recipients"},
        {"slug": "support", "name": "AlohaSupport", "note": "Ticket notifications and replies"},
        {"slug": "affiliate", "name": "AlohaAffiliate", "note": "Partner and payout emails"},
    ],
},

# ---------------- AlohaSurvey ----------------
"survey": {
    "name": "AlohaSurvey",
    "icon": "fa-poll",
    "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
    "status": "coming",
    "tagline": "Surveys, forms, and feedback that scale.",
    "description": "A SurveyMonkey-class survey platform with branching logic, rich question types, real-time analytics, and responses that land straight in your CRM.",
    "overview": "AlohaSurvey lets you design beautiful surveys and forms, distribute them anywhere, and analyze results in context. Every response becomes part of the contact record in AlohaCRM, so insights drive actual actions.",
    "capabilities": [
        {
            "title": "Survey Builder",
            "icon": "fa-pen-ruler",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "15+ question types",
                "Branching and skip logic",
                "Question piping and variables",
                "Template gallery",
                "Mobile-first design",
                "Custom themes and branding",
            ]
        },
        {
            "title": "Distribution",
            "icon": "fa-share-nodes",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Shareable links and QR codes",
                "Embed on any website",
                "Send via AlohaEmail",
                "SMS distribution",
                "Kiosk mode for in-person",
                "Anonymous and identified responses",
            ]
        },
        {
            "title": "Analytics",
            "icon": "fa-chart-pie",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Real-time response dashboards",
                "Cross-tab analysis",
                "NPS and CSAT scoring",
                "Sentiment analysis on open text",
                "Response exports (CSV, Excel)",
                "Trend reports over time",
            ]
        },
        {
            "title": "Response Handling",
            "icon": "fa-inbox",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Auto-save to CRM contact records",
                "Trigger workflows on response",
                "Email alerts on new responses",
                "Response-level notifications",
                "Partial response capture",
                "Duplicate prevention",
            ]
        },
    ],
    "integrations": [
        {"slug": "crm", "name": "AlohaCRM", "note": "Responses become contact attributes"},
        {"slug": "email", "name": "AlohaEmail", "note": "Survey distribution and invitations"},
        {"slug": "marketing", "name": "AlohaMarketing", "note": "Segment audiences by responses"},
        {"slug": "support", "name": "AlohaSupport", "note": "Post-ticket satisfaction surveys"},
    ],
},

# ---------------- AlohaSupport ----------------
"support": {
    "name": "AlohaSupport",
    "icon": "fa-headset",
    "gradient": "linear-gradient(135deg,#38bdf8,#0284c7)",
    "status": "coming",
    "tagline": "Helpdesk that speaks every channel.",
    "description": "Tickets, live chat, unified inbox, SLA management, and customer context from every AlohaOne platform — all in one pane of glass.",
    "overview": "AlohaSupport unifies email, chat, SMS, and social into a single ticketing system. Every conversation is backed by complete customer context from CRM, Commerce, and Documents, so your team answers questions with the full picture.",
    "capabilities": [
        {
            "title": "Ticketing",
            "icon": "fa-ticket",
            "gradient": "linear-gradient(135deg,#38bdf8,#0284c7)",
            "items": [
                "Email-to-ticket conversion",
                "Priorities, statuses, and queues",
                "Round-robin and skill-based routing",
                "Macros and canned responses",
                "Internal notes and @mentions",
                "Merge, split, and link tickets",
            ]
        },
        {
            "title": "Agent Workspace",
            "icon": "fa-toolbox",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Powered by AlohaMessage for multi-channel conversations",
                "Customer context sidebar on every ticket",
                "Order and document attachments",
                "Side-by-side ticket comparisons",
                "Agent collision detection",
                "Keyboard shortcuts and hotkeys",
            ]
        },
        {
            "title": "SLAs & Automation",
            "icon": "fa-stopwatch",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Configurable SLA policies",
                "First-response and resolution timers",
                "Escalation rules and alerts",
                "Business-hours calendars",
                "Automation triggers and actions",
                "Auto-tagging and categorization",
            ]
        },
        {
            "title": "Knowledge & Self-Serve",
            "icon": "fa-circle-question",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Suggested articles from AlohaKnowledge",
                "In-ticket article insertion",
                "Customer-facing help center",
                "Search deflection analytics",
                "Article feedback loop",
                "AI-powered reply drafts",
            ]
        },
    ],
    "integrations": [
        {"slug": "message", "name": "AlohaMessage", "note": "Multi-channel inbox behind every ticket"},
        {"slug": "assistant", "name": "AlohaAssistant", "note": "Calls can be escalated to tickets"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Customer context on every ticket"},
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Order details for support agents"},
        {"slug": "knowledge", "name": "AlohaKnowledge", "note": "Suggested articles and deflection"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents handle tier-1 tickets"},
    ],
},

# ---------------- AlohaKnowledge ----------------
"knowledge": {
    "name": "AlohaKnowledge",
    "icon": "fa-book-open",
    "gradient": "linear-gradient(135deg,#a78bfa,#7c3aed)",
    "status": "coming",
    "tagline": "Your team's second brain.",
    "description": "A modern knowledge base and wiki with rich editing, powerful search, granular permissions, and content that powers AI agents and support deflection.",
    "overview": "AlohaKnowledge is the documentation layer for your organization. Write articles once, reference them everywhere — embedded in Support tickets, referenced by AlohaAgent, and surfaced in customer-facing help centers.",
    "capabilities": [
        {
            "title": "Rich Editing",
            "icon": "fa-pen-to-square",
            "gradient": "linear-gradient(135deg,#a78bfa,#7c3aed)",
            "items": [
                "WYSIWYG and markdown side-by-side",
                "Embeds: video, images, code blocks, diagrams",
                "Mermaid and flowchart support",
                "Collaborative editing with presence",
                "Version history with diff viewer",
                "Templates and reusable blocks",
            ]
        },
        {
            "title": "Organization",
            "icon": "fa-folder-tree",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Nested categories and spaces",
                "Tags and custom metadata",
                "Quick-access favorites",
                "Internal and external article types",
                "Cross-linking with backlinks",
                "Table of contents generation",
            ]
        },
        {
            "title": "Search",
            "icon": "fa-magnifying-glass",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Full-text search across all content",
                "Typo tolerance and synonyms",
                "Semantic search powered by embeddings",
                "Search-in-context from any platform",
                "Analytics on searches with no results",
                "Popular and trending articles",
            ]
        },
        {
            "title": "Permissions",
            "icon": "fa-key",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Per-space and per-article permissions",
                "Public and private articles",
                "Role-based access control",
                "External viewer links",
                "Approval workflows",
                "Content expiration and review reminders",
            ]
        },
    ],
    "integrations": [
        {"slug": "support", "name": "AlohaSupport", "note": "Article suggestions on tickets"},
        {"slug": "search", "name": "AlohaSearch", "note": "Semantic search across every article"},
        {"slug": "training", "name": "AlohaTraining", "note": "Source content for courses"},
        {"slug": "document", "name": "AlohaDocument", "note": "Link formal documents to articles"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents answer from your knowledge"},
    ],
},

# ---------------- AlohaTraining ----------------
"training": {
    "name": "AlohaTraining",
    "icon": "fa-graduation-cap",
    "gradient": "linear-gradient(135deg,#4ade80,#16a34a)",
    "status": "coming",
    "tagline": "Courses, quizzes, and certifications.",
    "description": "A learning management system for employee onboarding, customer education, and certification programs — built on shared identity and content from AlohaKnowledge.",
    "overview": "AlohaTraining turns your knowledge base into structured learning paths. Build courses, track progress, issue certifications, and integrate with CRM so you know exactly who's trained on what.",
    "capabilities": [
        {
            "title": "Course Builder",
            "icon": "fa-chalkboard",
            "gradient": "linear-gradient(135deg,#4ade80,#16a34a)",
            "items": [
                "Modular course structure",
                "Video, text, quiz, and assignment lessons",
                "Pull content from AlohaKnowledge",
                "Prerequisites and learning paths",
                "Drip content release",
                "Reusable lesson library",
            ]
        },
        {
            "title": "Assessments",
            "icon": "fa-clipboard-question",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Multiple-choice, open-ended, and coding quizzes",
                "Question banks and randomization",
                "Time limits and proctoring options",
                "Auto-grading with manual review",
                "Retake policies",
                "Certification thresholds",
            ]
        },
        {
            "title": "Tracking",
            "icon": "fa-chart-line",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Per-learner progress dashboards",
                "Completion and time-on-task reports",
                "Cohort and team analytics",
                "Manager reporting views",
                "xAPI and SCORM support",
                "Integration with HR systems",
            ]
        },
        {
            "title": "Certifications",
            "icon": "fa-certificate",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Branded certificates on completion",
                "Expiration and renewal tracking",
                "Public verification URLs",
                "Digital badge integration",
                "CEU and CPE credit tracking",
                "Automated reminder workflows",
            ]
        },
    ],
    "integrations": [
        {"slug": "knowledge", "name": "AlohaKnowledge", "note": "Source content for lessons"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Track who's trained on what"},
        {"slug": "email", "name": "AlohaEmail", "note": "Reminders and completion notices"},
        {"slug": "support", "name": "AlohaSupport", "note": "Surface training gaps from ticket patterns"},
    ],
},

# ---------------- AlohaProject ----------------
"project": {
    "name": "AlohaProject",
    "icon": "fa-diagram-project",
    "gradient": "linear-gradient(135deg,#6366f1,#4f46e5)",
    "status": "coming",
    "tagline": "Project management that developers actually use.",
    "description": "Issues, boards, sprints, roadmaps, and time tracking — the JIRA-class project tool built for teams that already live in AlohaOne.",
    "overview": "AlohaProject is a full project management system for engineering, operations, and cross-functional teams. Boards, sprints, backlogs, and roadmaps — with deep integration into Documents, Knowledge, and Support for context you can't get anywhere else.",
    "capabilities": [
        {
            "title": "Issues & Tasks",
            "icon": "fa-list-check",
            "gradient": "linear-gradient(135deg,#6366f1,#4f46e5)",
            "items": [
                "Custom issue types and workflows",
                "Rich text descriptions with embeds",
                "Subtasks, dependencies, and epics",
                "Custom fields and labels",
                "Bulk edit and multi-select",
                "Keyboard-first navigation",
            ]
        },
        {
            "title": "Boards & Sprints",
            "icon": "fa-columns",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Kanban and scrum boards",
                "Sprint planning and velocity tracking",
                "Burndown and burnup charts",
                "Backlog grooming views",
                "Swimlanes and WIP limits",
                "Multi-project boards",
            ]
        },
        {
            "title": "Roadmaps & Planning",
            "icon": "fa-map",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Timeline and Gantt views",
                "Dependencies across teams",
                "Milestone tracking",
                "Portfolio-level roadmaps",
                "Capacity planning",
                "Release planning",
            ]
        },
        {
            "title": "Tracking & Automation",
            "icon": "fa-robot",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Time tracking and worklogs",
                "Custom workflow rules",
                "Auto-assignment and transitions",
                "Webhooks and REST API",
                "GitHub/GitLab integration",
                "SLA tracking on issues",
            ]
        },
    ],
    "integrations": [
        {"slug": "document", "name": "AlohaDocument", "note": "Attach specs and design files"},
        {"slug": "knowledge", "name": "AlohaKnowledge", "note": "Link articles to issues"},
        {"slug": "support", "name": "AlohaSupport", "note": "Escalate tickets to engineering"},
        {"slug": "case", "name": "AlohaCase", "note": "Track case work as tasks"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents triage and draft tickets"},
    ],
},

# ---------------- AlohaInventory ----------------
"inventory": {
    "name": "AlohaInventory",
    "icon": "fa-warehouse",
    "gradient": "linear-gradient(135deg,#0891b2,#0e7490)",
    "status": "live",
    "tagline": "Component-level inventory control, built in.",
    "description": "Multi-warehouse stock management with deep support for components and configurable products — BOMs, assemblies, cycle counts, and real-time reservations. Already bundled inside AlohaCommerce and ready to toggle on per-tenant.",
    "overview": "AlohaInventory is already running inside AlohaCommerce — it handles components and configurable components natively, so a product's inventory can be tracked down to the individual parts that make it up. When a customer configures a made-to-order product via AlohaConfigurator, the BOM is resolved against component stock in real time. Toggle it on for any tenant and every SKU gets component-level traceability, multi-location reservations, and assembly workflows.",
    "capabilities": [
        {
            "title": "Multi-Warehouse",
            "icon": "fa-warehouse",
            "gradient": "linear-gradient(135deg,#0891b2,#0e7490)",
            "items": [
                "Unlimited warehouse locations",
                "Per-location stock levels and policies",
                "Bin and aisle-level precision",
                "Location-based pick and pack rules",
                "Transfers between locations with in-transit tracking",
                "Per-location reorder points",
            ]
        },
        {
            "title": "BOM & Assemblies",
            "icon": "fa-sitemap",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "Bill-of-materials with nested components",
                "Component-level stock tracking",
                "Dynamic BOM modification on customer options",
                "Assembly and kitting workflows",
                "Disassembly and rework orders",
                "Phantom and reference BOMs",
            ]
        },
        {
            "title": "Stock Control",
            "icon": "fa-boxes-stacked",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Real-time available quantity calculations",
                "Reservations for pending orders",
                "Low-stock alerts and reorder automation",
                "Safety stock and min/max levels",
                "Lot, serial, and expiration tracking",
                "FIFO, LIFO, and FEFO picking strategies",
            ]
        },
        {
            "title": "Receiving & Shipping",
            "icon": "fa-truck-ramp-box",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Purchase order workflows",
                "Inbound receipts with QC holds",
                "Barcode scanning for pick and pack",
                "Wave and batch picking",
                "Shipping integration with AlohaDeliver",
                "Cross-docking support",
            ]
        },
        {
            "title": "Counting & Audit",
            "icon": "fa-clipboard-list",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Cycle count schedules",
                "Full physical inventory workflows",
                "Variance tracking and approval",
                "Adjustment reason codes",
                "Full audit trail of every stock move",
                "Shrinkage and loss reporting",
            ]
        },
        {
            "title": "Integrations",
            "icon": "fa-plug",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Real-time stock feed to AlohaCommerce",
                "Supplier catalogs and price lists",
                "EDI for enterprise suppliers",
                "Webhook events on stock changes",
                "REST API for WMS integrations",
                "Forecasting and demand planning",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Real-time stock and BOM for every product"},
        {"slug": "deliver", "name": "AlohaDeliver", "note": "Hand off shipments from warehouse to delivery"},
        {"slug": "data", "name": "AlohaData", "note": "Stock turns, shrinkage, and forecasting analytics"},
        {"slug": "project", "name": "AlohaProject", "note": "Track assembly and rework as projects"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents forecast demand and flag anomalies"},
    ],
    "cta": {
        "primary_label": "Enable AlohaInventory",
        "primary_href": "../../AlohaOneApp/index.html?platform=inventory&intent=register",
        "secondary_label": "Learn About Commerce",
        "secondary_href": "commerce.html",
    },
},

# ---------------- AlohaDeliver ----------------
"deliver": {
    "name": "AlohaDeliver",
    "icon": "fa-truck-fast",
    "gradient": "linear-gradient(135deg,#f97316,#c2410c)",
    "status": "coming",
    "tagline": "Last-mile delivery with photo and video proof.",
    "description": "Route planning, driver apps, pickup and delivery notifications, and photo or video proof at every stop. Purpose-built for white-glove, freight, and local delivery operations.",
    "overview": "AlohaDeliver handles the last mile — route optimization, driver mobile apps, real-time tracking, and visual proof of every pickup and delivery. Customers get live updates; you get a defensible record of every handoff with photos and video.",
    "capabilities": [
        {
            "title": "Route Planning",
            "icon": "fa-route",
            "gradient": "linear-gradient(135deg,#f97316,#c2410c)",
            "items": [
                "AI-powered route optimization",
                "Multi-stop and multi-driver planning",
                "Time window and capacity constraints",
                "Drag-and-drop route editor",
                "Dynamic rerouting on traffic and delays",
                "Depot, return, and break scheduling",
            ]
        },
        {
            "title": "Driver Mobile App",
            "icon": "fa-mobile-screen-button",
            "gradient": "linear-gradient(135deg,#0891b2,#0e7490)",
            "items": [
                "Turn-by-turn navigation",
                "Stop list with priorities and notes",
                "Barcode scanning on pickup and delivery",
                "Signature capture on delivery",
                "Offline mode for dead zones",
                "Hands-free voice updates",
            ]
        },
        {
            "title": "Photo & Video Proof",
            "icon": "fa-camera",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Required photos at pickup and delivery",
                "Video walkthroughs for white-glove delivery",
                "Damage documentation with annotations",
                "Timestamped and geo-tagged media",
                "Customer-visible delivery photos",
                "Full media history per order",
            ]
        },
        {
            "title": "Notifications",
            "icon": "fa-bell",
            "gradient": "linear-gradient(135deg,#fbbf24,#d97706)",
            "items": [
                "SMS and email on pickup scheduled",
                "Live ETA updates as driver approaches",
                "Arrival and in-progress notifications",
                "Delivery completion with photo",
                "Missed delivery and reschedule flows",
                "Customer rating requests post-delivery",
            ]
        },
        {
            "title": "Live Tracking",
            "icon": "fa-location-crosshairs",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Real-time driver GPS on customer map",
                "Dispatcher command center view",
                "Fleet-wide status dashboard",
                "Live ETA updates with traffic",
                "Geofence-triggered events",
                "Historical route playback",
            ]
        },
        {
            "title": "Operations",
            "icon": "fa-clipboard-check",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Driver performance and on-time metrics",
                "Delivery exception workflows",
                "Proof-of-delivery archive",
                "Claims and disputes with evidence",
                "Dispatcher assignment and overrides",
                "Third-party driver network support",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Deliveries linked to orders automatically"},
        {"slug": "inventory", "name": "AlohaInventory", "note": "Pickups from warehouse locations"},
        {"slug": "email", "name": "AlohaEmail", "note": "Delivery notification emails"},
        {"slug": "document", "name": "AlohaDocument", "note": "Photo and video proof archive"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Customer delivery history on contact timeline"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents resolve delivery disputes with evidence"},
    ],
},

# ---------------- AlohaSocial ----------------
"social": {
    "name": "AlohaSocial",
    "icon": "fa-share-nodes",
    "gradient": "linear-gradient(135deg,#ec4899,#be185d)",
    "status": "coming",
    "tagline": "One composer. Every social platform.",
    "description": "Plug into every major social media API and post across platforms from one unified composer. Schedule, publish, monitor engagement, and respond — all from inside AlohaOne.",
    "overview": "AlohaSocial is the social media control center for the entire AlohaOne ecosystem. Compose once, publish everywhere — Facebook, Instagram, X, LinkedIn, TikTok, YouTube, Pinterest, Threads, Bluesky — with scheduling, engagement tracking, and AI-assisted content creation.",
    "capabilities": [
        {
            "title": "Unified Composer",
            "icon": "fa-pen-fancy",
            "gradient": "linear-gradient(135deg,#ec4899,#be185d)",
            "items": [
                "One editor, every platform",
                "Platform-specific previews",
                "Per-platform tweaks from a single draft",
                "Media library with reusable assets",
                "Hashtag and mention autocomplete",
                "Character-limit enforcement per network",
            ]
        },
        {
            "title": "Connected Networks",
            "icon": "fa-network-wired",
            "gradient": "linear-gradient(135deg,#0891b2,#0e7490)",
            "items": [
                "Facebook Pages and Groups",
                "Instagram feed, Reels, and Stories",
                "X (Twitter) posts and threads",
                "LinkedIn company and personal pages",
                "TikTok and YouTube Shorts",
                "Pinterest, Threads, Bluesky, and more",
            ]
        },
        {
            "title": "Scheduling & Queues",
            "icon": "fa-calendar-check",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Visual content calendar",
                "Best-time-to-post suggestions",
                "Evergreen content queues",
                "Timezone-aware scheduling",
                "Bulk import from CSV",
                "Approval workflows for teams",
            ]
        },
        {
            "title": "Engagement",
            "icon": "fa-comments",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Unified inbox for comments and DMs",
                "Mention and keyword monitoring",
                "Auto-response rules",
                "Sentiment analysis",
                "Reply from any channel in one view",
                "Escalate issues to AlohaSupport",
            ]
        },
        {
            "title": "Analytics",
            "icon": "fa-chart-line",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Engagement metrics per post and network",
                "Audience growth and demographics",
                "Top-performing content reports",
                "Competitor benchmarking",
                "Attribution to AlohaCommerce revenue",
                "Export to AlohaData warehouse",
            ]
        },
        {
            "title": "AI Content",
            "icon": "fa-wand-magic-sparkles",
            "gradient": "linear-gradient(135deg,#a855f7,#7e22ce)",
            "items": [
                "AI-generated captions and hashtags",
                "Post-variation generation for A/B testing",
                "Auto-post AlohaCommerce product launches",
                "AI image generation via Commerce Studio",
                "Tone and brand-voice enforcement",
                "Agent-driven social campaigns",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Auto-post product launches and promotions"},
        {"slug": "marketing", "name": "AlohaMarketing", "note": "Social as a campaign channel"},
        {"slug": "support", "name": "AlohaSupport", "note": "Escalate social complaints to tickets"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Social engagement on contact timelines"},
        {"slug": "data", "name": "AlohaData", "note": "Social analytics in your warehouse"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents write, schedule, and respond"},
    ],
},

# ---------------- AlohaAssistant ----------------
"assistant": {
    "name": "AlohaAssistant",
    "icon": "fa-phone-volume",
    "gradient": "linear-gradient(135deg,#a855f7,#7e22ce)",
    "status": "coming",
    "tagline": "Your voice-enabled AI executive assistant.",
    "description": "A 24/7 virtual exec assistant that answers your phone, books appointments, takes messages, and handles calls with natural voice AI. Never miss a customer again.",
    "overview": "AlohaAssistant is a voice-first AI that acts as your business's virtual executive assistant. It answers phone calls, schedules appointments on your calendar, routes urgent matters to the right person, takes detailed messages, and logs every conversation — all in a natural-sounding voice that represents your brand, 24/7.",
    "capabilities": [
        {
            "title": "Voice Reception",
            "icon": "fa-phone-volume",
            "gradient": "linear-gradient(135deg,#a855f7,#7e22ce)",
            "items": [
                "24/7 phone answering with natural voice",
                "Multiple voice personas and accents",
                "Custom greeting and business script",
                "Barge-in and interruption handling",
                "Spam and robocall screening",
                "Warm transfer to human staff",
            ]
        },
        {
            "title": "Appointment Booking",
            "icon": "fa-calendar-check",
            "gradient": "linear-gradient(135deg,#0891b2,#0e7490)",
            "items": [
                "Natural language calendar booking",
                "Live availability lookup",
                "Confirmation via SMS and email",
                "Reschedule and cancel by voice",
                "Multi-staff and multi-location support",
                "Buffer times and business hours",
            ]
        },
        {
            "title": "Messages & Transcripts",
            "icon": "fa-sticky-note",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Detailed message capture",
                "Full conversation transcription",
                "Caller intent summary",
                "Urgency detection and priority flagging",
                "Voicemail → email with transcript",
                "Searchable call history",
            ]
        },
        {
            "title": "Smart Routing",
            "icon": "fa-sitemap",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Department and staff routing rules",
                "After-hours escalation",
                "VIP caller recognition",
                "Language detection and routing",
                "Queue management and callbacks",
                "On-call schedule integration",
            ]
        },
        {
            "title": "Customer Context",
            "icon": "fa-id-card",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Caller ID lookup in AlohaCRM",
                "Personalized greetings for known contacts",
                "Order history awareness",
                "Open ticket context from AlohaSupport",
                "Previous call summary for returning callers",
                "Auto-log to contact record",
            ]
        },
        {
            "title": "Call Intelligence",
            "icon": "fa-chart-line",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Call volume and pattern analytics",
                "Common question categorization",
                "After-hours vs business-hours breakdown",
                "Caller sentiment tracking",
                "Missed opportunity reports",
                "AI-generated daily call summaries",
            ]
        },
    ],
    "integrations": [
        {"slug": "message", "name": "AlohaMessage", "note": "Every call logged in the unified inbox"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Caller ID lookup and contact auto-update"},
        {"slug": "support", "name": "AlohaSupport", "note": "Convert calls to tickets"},
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Order status over the phone"},
        {"slug": "agent", "name": "AlohaAgent", "note": "Powered by AlohaAgent's voice AI stack"},
    ],
},

# ---------------- AlohaMessage ----------------
"message": {
    "name": "AlohaMessage",
    "icon": "fa-comments",
    "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
    "status": "coming",
    "tagline": "Every customer conversation, one inbox.",
    "description": "The unified message center for your business — email, phone, SMS, Facebook, Instagram, Etsy, WhatsApp, live chat, and more. Reply from one screen no matter which channel the customer used.",
    "overview": "AlohaMessage is the conversation layer for the whole AlohaOne ecosystem. Every message from every channel lands in one unified inbox — email, phone transcripts from AlohaAssistant, Facebook and Instagram DMs, Etsy messages, SMS, WhatsApp Business, live chat. Your team replies from one screen; customers get seamless conversations regardless of how they reach out.",
    "capabilities": [
        {
            "title": "Every Channel",
            "icon": "fa-tower-broadcast",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "Email (IMAP, SES, Gmail, Outlook)",
                "Phone and voicemail via AlohaAssistant",
                "SMS and MMS (Twilio and friends)",
                "Facebook Messenger and Instagram DMs",
                "Etsy messages and Etsy order conversations",
                "WhatsApp Business",
                "Live chat from AlohaCommerce storefronts",
                "Web forms and contact pages",
            ]
        },
        {
            "title": "Unified Inbox",
            "icon": "fa-inbox",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "All channels in one threaded view",
                "Conversations grouped by customer, not channel",
                "Unread, assigned, and priority filters",
                "Shared team inbox with assignments",
                "Internal notes and @mentions",
                "Full-text search across every message",
            ]
        },
        {
            "title": "Reply From One Place",
            "icon": "fa-reply-all",
            "gradient": "linear-gradient(135deg,#ec4899,#db2777)",
            "items": [
                "Reply in the original channel seamlessly",
                "Switch channels mid-conversation",
                "Canned responses and templates",
                "Rich media and file attachments",
                "Typing indicators and read receipts",
                "Keyboard shortcuts for fast handling",
            ]
        },
        {
            "title": "Team Collaboration",
            "icon": "fa-people-group",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Assignment rules and round-robin",
                "Agent collision detection",
                "Status indicators (online, busy, away)",
                "Handoff with full context preservation",
                "Tag, categorize, and filter conversations",
                "SLA timers with escalation",
            ]
        },
        {
            "title": "AI & Automation",
            "icon": "fa-wand-magic-sparkles",
            "gradient": "linear-gradient(135deg,#a855f7,#7e22ce)",
            "items": [
                "AI-suggested replies in your brand voice",
                "Auto-categorization and tagging",
                "Sentiment analysis on every message",
                "Language detection and auto-translation",
                "Auto-responses for FAQs",
                "Escalation triggers based on intent",
            ]
        },
        {
            "title": "Customer Context",
            "icon": "fa-address-card",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Full CRM profile beside every conversation",
                "Order history from AlohaCommerce",
                "Open tickets from AlohaSupport",
                "Past conversations across all channels",
                "Customer lifetime value at a glance",
                "Attach documents from AlohaDocument",
            ]
        },
    ],
    "integrations": [
        {"slug": "assistant", "name": "AlohaAssistant", "note": "Phone calls flow into the inbox as transcripts"},
        {"slug": "support", "name": "AlohaSupport", "note": "Escalate conversations to formal tickets"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Every message attached to a contact record"},
        {"slug": "email", "name": "AlohaEmail", "note": "Outbound email via deliverability pipeline"},
        {"slug": "social", "name": "AlohaSocial", "note": "Social DMs and comments captured as messages"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI drafts and auto-responses"},
    ],
},

# ---------------- AlohaData ----------------
"data": {
    "name": "AlohaData",
    "icon": "fa-database",
    "gradient": "linear-gradient(135deg,#0ea5e9,#0369a1)",
    "status": "coming",
    "tagline": "Data warehouse as a service — Redshift-class without the overhead.",
    "description": "A fully-managed columnar data warehouse for the AlohaOne ecosystem. ELT pipelines from every platform, SQL workbench, scheduled transforms, BI connectors, and time-travel snapshots.",
    "overview": "AlohaData is the analytics backbone of AlohaOne. Every other platform auto-streams its data in — orders from Commerce, tickets from Support, leads from CRM, activity from Document — so you can run SQL, build dashboards, and feed BI tools without writing a single pipeline.",
    "capabilities": [
        {
            "title": "Managed Warehouse",
            "icon": "fa-database",
            "gradient": "linear-gradient(135deg,#0ea5e9,#0369a1)",
            "items": [
                "Columnar storage optimized for analytics",
                "Elastic compute — scale up for queries, down for cost",
                "Automatic compression and partitioning",
                "Time-travel snapshots and point-in-time recovery",
                "Zero-copy cloning for dev and staging",
                "Serverless billing — pay per query",
            ]
        },
        {
            "title": "Auto ELT from AlohaOne",
            "icon": "fa-arrow-right-arrow-left",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "One-click sync from every AlohaOne platform",
                "CDC-based near-real-time replication",
                "Schema evolution handled automatically",
                "Historical backfills on enable",
                "Tenant-scoped data isolation",
                "Raw and conformed layers out of the box",
            ]
        },
        {
            "title": "SQL Workbench",
            "icon": "fa-terminal",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Browser-based SQL editor",
                "Query history and saved queries",
                "Shareable dashboards and charts",
                "AI-assisted query generation",
                "Query explain plans and optimization hints",
                "Per-user workspace and drafts",
            ]
        },
        {
            "title": "Transforms & Modeling",
            "icon": "fa-diagram-project",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Scheduled materialized views",
                "dbt-compatible transform layer",
                "Dependency graph and lineage",
                "Incremental and full refresh modes",
                "Data quality tests",
                "Semantic layer for metrics definitions",
            ]
        },
        {
            "title": "BI & Export",
            "icon": "fa-chart-column",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Tableau, Power BI, Looker, Metabase connectors",
                "JDBC and ODBC drivers",
                "Embedded dashboards via API",
                "CSV, Parquet, and JSON export",
                "Reverse ETL back to operational platforms",
                "Scheduled report email via AlohaEmail",
            ]
        },
        {
            "title": "Governance",
            "icon": "fa-user-shield",
            "gradient": "linear-gradient(135deg,#06b6d4,#0891b2)",
            "items": [
                "Column-level access control",
                "Row-level security policies",
                "PII tagging and masking",
                "Full audit log of every query",
                "Data retention and GDPR deletion",
                "SOC 2 / HIPAA-ready controls",
            ]
        },
    ],
    "integrations": [
        {"slug": "commerce", "name": "AlohaCommerce", "note": "Orders, products, and revenue warehouse"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Customer and pipeline analytics"},
        {"slug": "marketing", "name": "AlohaMarketing", "note": "Campaign performance and attribution"},
        {"slug": "support", "name": "AlohaSupport", "note": "Ticket and SLA analytics"},
        {"slug": "search", "name": "AlohaSearch", "note": "Index warehouse tables for unified search"},
        {"slug": "agent", "name": "AlohaAgent", "note": "AI agents write and run SQL for you"},
    ],
},

# ---------------- AlohaSearch ----------------
"search": {
    "name": "AlohaSearch",
    "icon": "fa-magnifying-glass",
    "gradient": "linear-gradient(135deg,#0d9488,#115e59)",
    "status": "live",
    "tagline": "Full-text and semantic search across everything you own.",
    "description": "One search box for every document, case, file, record, and row in AlohaOne. Full-text search is already live and integrated with AlohaCase and AlohaDocument; semantic and vector search extend the same index across every other platform.",
    "overview": "AlohaSearch is the unified search layer for the entire AlohaOne ecosystem. Its full-text engine is already running in production, integrated directly into AlohaCase and AlohaDocument — users search across case documents, document content, and metadata with relevance-ranked results and snippets. The platform is expanding to add semantic and vector search and to index every other platform (CRM contacts, Commerce products, Backup files, Knowledge articles, warehouse tables) into a single cross-ecosystem search surface.",
    "capabilities": [
        {
            "title": "Hybrid Search",
            "icon": "fa-magnifying-glass",
            "gradient": "linear-gradient(135deg,#0d9488,#115e59)",
            "items": [
                "Full-text (BM25) and vector search together",
                "Hybrid ranking with tunable weights",
                "Typo tolerance and stemming",
                "Synonyms and custom dictionaries",
                "Phrase, boolean, and proximity queries",
                "Highlighted snippets with context",
            ]
        },
        {
            "title": "Semantic & AI",
            "icon": "fa-brain",
            "gradient": "linear-gradient(135deg,#8b5cf6,#7c3aed)",
            "items": [
                "Natural language queries",
                "Embeddings-based semantic retrieval",
                "AI-generated answers with citations",
                "Auto-suggested follow-up questions",
                "Query rewriting and expansion",
                "Multilingual support",
            ]
        },
        {
            "title": "Unified Index",
            "icon": "fa-layer-group",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Indexes AlohaDocument files and OCR text",
                "Indexes AlohaCase metadata and attachments",
                "Indexes AlohaBackup file contents",
                "Indexes AlohaKnowledge articles",
                "Indexes AlohaData warehouse tables",
                "Indexes CRM contacts, Commerce products, Support tickets",
            ]
        },
        {
            "title": "Permissions & Security",
            "icon": "fa-user-shield",
            "gradient": "linear-gradient(135deg,#ef4444,#dc2626)",
            "items": [
                "Permission-aware result filtering",
                "Per-tenant index isolation",
                "Respects source-platform ACLs at query time",
                "PII redaction in snippets",
                "Audit log of every query",
                "Encrypted index storage",
            ]
        },
        {
            "title": "Developer & UX",
            "icon": "fa-code",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "REST and GraphQL APIs",
                "Drop-in search widget for any page",
                "Faceted search and filters",
                "Saved searches and alerts",
                "Typeahead and instant search",
                "Search analytics and click-through tracking",
            ]
        },
        {
            "title": "Feeds AlohaAgent",
            "icon": "fa-robot",
            "gradient": "linear-gradient(135deg,#a855f7,#7e22ce)",
            "items": [
                "Retrieval-augmented generation (RAG) out of the box",
                "Citation-backed agent answers",
                "Tool interface for agents to query search",
                "Chunking and vectorization pipeline",
                "Automatic re-embedding on content change",
                "Source attribution for every result",
            ]
        },
    ],
    "integrations": [
        {"slug": "document", "name": "AlohaDocument", "note": "Primary source of unstructured content"},
        {"slug": "case", "name": "AlohaCase", "note": "Search within and across cases"},
        {"slug": "backup", "name": "AlohaBackup", "note": "Find backed-up files across every device"},
        {"slug": "knowledge", "name": "AlohaKnowledge", "note": "Semantic article retrieval"},
        {"slug": "data", "name": "AlohaData", "note": "Structured warehouse content"},
        {"slug": "agent", "name": "AlohaAgent", "note": "RAG layer for every AI agent"},
    ],
},

# ---------------- AlohaAgent ----------------
"agent": {
    "name": "AlohaAgent",
    "icon": "fa-robot",
    "gradient": "linear-gradient(135deg,#a855f7,#7e22ce)",
    "status": "coming",
    "tagline": "AI agents that work across every platform.",
    "description": "Build, deploy, and manage AI agents that read your documents, answer your customers, triage your tickets, and automate workflows across the entire AlohaOne ecosystem.",
    "overview": "AlohaAgent is the AI layer for the whole AlohaOne suite. Agents have read and write access (subject to permissions) to every connected platform — Documents, CRM, Commerce, Support, Project, Knowledge — so they can actually get work done, not just chat about it.",
    "capabilities": [
        {
            "title": "Agent Builder",
            "icon": "fa-wand-magic-sparkles",
            "gradient": "linear-gradient(135deg,#a855f7,#7e22ce)",
            "items": [
                "No-code agent configuration",
                "Natural language instructions and goals",
                "Tool selection (which platforms the agent can touch)",
                "Permission scoping per agent",
                "Prompt templates and starter agents",
                "Conversation memory and context windows",
            ]
        },
        {
            "title": "Cross-Platform Tools",
            "icon": "fa-plug",
            "gradient": "linear-gradient(135deg,#3b82f6,#2563eb)",
            "items": [
                "Search AlohaDocument and AlohaKnowledge",
                "Create and update CRM contacts",
                "Draft Commerce product descriptions",
                "Triage Support tickets",
                "File AlohaProject issues",
                "Send emails via AlohaEmail",
            ]
        },
        {
            "title": "Deployment",
            "icon": "fa-rocket",
            "gradient": "linear-gradient(135deg,#10b981,#059669)",
            "items": [
                "Embed in any AlohaOne UI",
                "Expose as a chat widget on your site",
                "Slack and Teams integrations",
                "Scheduled and event-triggered runs",
                "REST API for custom invocation",
                "Agent marketplace (share and install)",
            ]
        },
        {
            "title": "Safety & Control",
            "icon": "fa-shield-halved",
            "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
            "items": [
                "Granular per-tool permissions",
                "Human-in-the-loop approval steps",
                "Full audit log of every action",
                "Token and cost budgets per agent",
                "PII redaction and filtering",
                "Model selection (Claude, GPT, local)",
            ]
        },
    ],
    "integrations": [
        {"slug": "search", "name": "AlohaSearch", "note": "Retrieval-augmented generation for every agent"},
        {"slug": "data", "name": "AlohaData", "note": "Agents write SQL and analyze warehouse data"},
        {"slug": "document", "name": "AlohaDocument", "note": "Agents read and summarize documents"},
        {"slug": "knowledge", "name": "AlohaKnowledge", "note": "Ground answers in your knowledge base"},
        {"slug": "support", "name": "AlohaSupport", "note": "Tier-1 ticket automation"},
        {"slug": "crm", "name": "AlohaCRM", "note": "Agents work the pipeline"},
    ],
},

}  # end PLATFORMS


# =========================================================
# HTML TEMPLATE
# =========================================================
STATUS_BADGES = {
    "live": ('badge-live', 'Live'),
    "coming": ('badge-coming', 'Coming Soon'),
    "planned": ('badge-coming', 'Planned'),
}

def render_capabilities(caps):
    out = []
    for cap in caps:
        items = "\n".join(f"                        <li>{it}</li>" for it in cap["items"])
        out.append(f"""            <div class="col-md-6 col-lg-4 fade-up">
                <div class="capability-group">
                    <div class="capability-group-icon" style="background: {cap['gradient']}">
                        <i class="fas {cap['icon']}"></i>
                    </div>
                    <h5>{cap['title']}</h5>
                    <ul>
{items}
                    </ul>
                </div>
            </div>""")
    return "\n".join(out)


def render_integrations(ints):
    out = []
    for i in ints:
        target = PLATFORMS.get(i["slug"], {})
        gradient = target.get("gradient", "var(--ao-gradient)")
        icon = target.get("icon", "fa-circle")
        name = i.get("name", target.get("name", i["slug"]))
        out.append(f"""            <div class="col-md-6 col-lg-4 fade-up">
                <a href="{i['slug']}.html" class="integration-card">
                    <div class="integration-card-icon" style="background: {gradient}">
                        <i class="fas {icon}"></i>
                    </div>
                    <div class="integration-card-body">
                        <strong>{name}</strong>
                        <span>{i['note']}</span>
                    </div>
                </a>
            </div>""")
    return "\n".join(out)


def render_cta(p):
    cta = p.get("cta")
    if cta:
        return f"""            <a href="{cta['primary_href']}" class="btn btn-hero btn-primary-custom me-2 mb-2">{cta['primary_label']}</a>
            <a href="{cta['secondary_href']}" class="btn btn-hero btn-outline-light mb-2">{cta['secondary_label']}</a>"""
    return """            <a href="../index.html#cta" class="btn btn-hero btn-primary-custom me-2 mb-2">Request Early Access</a>
            <a href="../index.html#platforms" class="btn btn-hero btn-outline-light mb-2">See All Platforms</a>"""


def render_integration_note(p):
    note = p.get("integration_note")
    if not note:
        return ""
    return f"""
        <div class="alert alert-info mt-4" style="max-width:780px;margin:2rem auto 0;background:#eef2ff;border:1px solid #c7d2fe;color:#3730a3;border-radius:var(--ao-radius);padding:1.25rem 1.5rem;">
            <i class="fas fa-info-circle me-2"></i> {note}
        </div>"""


def render_platform_matrix(p):
    pm = p.get("platform_matrix")
    if not pm:
        return ""
    cards = []
    for item in pm.get("items", []):
        classes = "platform-support-card"
        if item.get("soon"):
            classes += " soon"
        href_attr = f'href="{item["href"]}"' if item.get("href") and not item.get("soon") else 'href="#"'
        cards.append(f"""            <div class="col-6 col-md-4 col-lg">
                <a {href_attr} class="{classes}">
                    <i class="{item['icon']}"></i>
                    <strong>{item['name']}</strong>
                    <span>{item.get('detail', '')}</span>
                </a>
            </div>""")
    items_html = "\n".join(cards)
    return f"""
<section class="platform-matrix-section">
    <div class="container">
        <div class="text-center">
            <p class="section-label">{pm.get('label', 'Every Device')}</p>
            <h2 class="section-heading">{pm.get('heading', 'Works everywhere you do')}</h2>
            <p class="section-sub">{pm.get('sub', '')}</p>
        </div>
        <div class="row g-3 justify-content-center">
{items_html}
        </div>
    </div>
</section>"""


def render_customers(p):
    cs = p.get("customers")
    if not cs:
        return ""
    cards = []
    for item in cs.get("items", []):
        tags_html = ""
        if item.get("tags"):
            tags_html = '<div class="customer-tags">' + "".join(
                f'<span class="customer-tag">{t}</span>' for t in item["tags"]
            ) + '</div>'
        name_html = item["name"]
        if item.get("url"):
            name_html = f'<a href="{item["url"]}" target="_blank" rel="noopener">{item["name"]}</a>'
        cards.append(f"""            <div class="col-md-6 col-lg-4 fade-up">
                <div class="customer-card">
                    <strong>{name_html}</strong>
                    <p>{item['description']}</p>
                    {tags_html}
                </div>
            </div>""")
    items_html = "\n".join(cards)
    return f"""
<section class="customers-section">
    <div class="container">
        <div class="text-center">
            <p class="section-label">{cs.get('label', 'Customers')}</p>
            <h2 class="section-heading">{cs.get('heading', 'Trusted by real businesses')}</h2>
            <p class="section-sub">{cs.get('sub', '')}</p>
        </div>
        <div class="row g-4">
{items_html}
        </div>
    </div>
</section>"""


def render_pricing(p):
    pr = p.get("pricing")
    if not pr:
        return ""
    cards = []
    for tier in pr.get("tiers", []):
        classes = "pricing-card"
        if tier.get("featured"):
            classes += " featured"
        features_html = "\n".join(f"                        <li>{f}</li>" for f in tier.get("features", []))
        cards.append(f"""            <div class="col-md-6 col-lg-4 fade-up">
                <div class="{classes}">
                    <h5>{tier['name']}</h5>
                    <div class="price">{tier['price']}</div>
                    <p class="period">{tier.get('period', '')}</p>
                    <ul>
{features_html}
                    </ul>
                    <a href="{tier['cta_href']}" class="btn">{tier['cta_label']}</a>
                </div>
            </div>""")
    items_html = "\n".join(cards)
    return f"""
<section class="pricing-section">
    <div class="container">
        <div class="text-center">
            <p class="section-label">{pr.get('label', 'Pricing')}</p>
            <h2 class="section-heading">{pr.get('heading', 'Simple pricing')}</h2>
            <p class="section-sub">{pr.get('sub', '')}</p>
        </div>
        <div class="row g-4 justify-content-center">
{items_html}
        </div>
    </div>
</section>"""


def render_final_cta(p):
    fc = p.get("final_cta")
    if not fc:
        return ""
    buttons = []
    if fc.get("primary_label"):
        buttons.append(f'<a href="{fc["primary_href"]}" class="btn btn-hero btn-primary-custom">{fc["primary_label"]}</a>')
    if fc.get("secondary_label"):
        buttons.append(f'<a href="{fc["secondary_href"]}" class="btn btn-hero btn-outline-light">{fc["secondary_label"]}</a>')
    btn_html = "\n            ".join(buttons)
    return f"""
<section class="final-cta-section">
    <div class="container final-cta-content">
        <h2>{fc['heading']}</h2>
        <p>{fc.get('sub', '')}</p>
        <div class="d-flex gap-3 justify-content-center flex-wrap">
            {btn_html}
        </div>
    </div>
</section>"""


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — AlohaOne</title>
    <meta name="description" content="{tagline}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/platform-detail.css">

    <style>
        .fade-up {{ opacity: 0; transform: translateY(24px); transition: opacity .6s ease, transform .6s ease; }}
        .fade-up.visible {{ opacity: 1; transform: translateY(0); }}
    </style>
</head>
<body>

<!-- NAV -->
<nav class="navbar navbar-expand-lg fixed-top bg-transparent">
    <div class="container">
        <a class="navbar-brand" href="../index.html">
            <span class="brand-gradient">AlohaOne</span>
        </a>
        <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navMain">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navMain">
            <ul class="navbar-nav ms-auto me-3">
                <li class="nav-item"><a class="nav-link" href="../index.html#platforms">Platforms</a></li>
                <li class="nav-item"><a class="nav-link" href="../index.html#why">Why AlohaOne</a></li>
                <li class="nav-item"><a class="nav-link" href="../index.html#how">How It Works</a></li>
            </ul>
            <a href="../index.html#cta" class="btn btn-sm btn-outline-primary rounded-pill px-3">Get Early Access</a>
        </div>
    </div>
</nav>

<!-- DETAIL HERO -->
<section class="detail-hero">
    <div class="container detail-hero-content">
        <a href="../index.html#platforms" class="back-link">
            <i class="fas fa-arrow-left"></i> All Platforms
        </a>
        <div class="row align-items-center">
            <div class="col-lg-9">
                <div class="detail-hero-icon" style="background: {gradient}">
                    <i class="fas {icon}"></i>
                </div>
                <div>
                    <span class="platform-badge {badge_class}">{badge_label}</span>
                </div>
                <h1>{name}</h1>
                <p class="tagline">{tagline}</p>
                <p class="description">{description}</p>
                <div class="d-flex flex-wrap gap-2">
{cta_buttons}
                </div>
            </div>
        </div>
    </div>
</section>

<!-- OVERVIEW -->
<section class="overview-section">
    <div class="container">
        <p>{overview}</p>
{integration_note}
    </div>
</section>

<!-- CAPABILITIES -->
<section class="capabilities-section">
    <div class="container">
        <div class="text-center">
            <p class="section-label">Capabilities</p>
            <h2 class="section-heading">Everything {name} Can Do</h2>
            <p class="section-sub">Deep feature set, but only pay for what you enable. Each capability can be turned on per-org as your needs grow.</p>
        </div>
        <div class="row g-4">
{capabilities}
        </div>
    </div>
</section>

{platform_matrix}
{customers_section}
{pricing_section}

<!-- INTEGRATIONS -->
<section class="integrations-section">
    <div class="container">
        <div class="text-center">
            <p class="section-label">Connects With</p>
            <h2 class="section-heading">Better Together</h2>
            <p class="section-sub">{name} is powerful alone — but it's designed to share data and context with every other AlohaOne platform.</p>
        </div>
        <div class="row g-3">
{integrations}
        </div>

        <div class="ecosystem-callout mt-5">
            <h4>One Platform, Pay For What You Use</h4>
            <p>AlohaOne is a single platform with capabilities you enable and pay for as you need them. Start with {name}, add more when you're ready.</p>
            <a href="../index.html#cta" class="btn">Request Early Access</a>
        </div>
    </div>
</section>

{final_cta_section}

<!-- FOOTER -->
<footer class="footer">
    <div class="container">
        <div class="row g-4">
            <div class="col-lg-4 mb-3">
                <h4 class="text-white mb-3" style="font-weight:800">
                    <span style="background:var(--ao-gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">AlohaOne</span>
                </h4>
                <p class="mb-0" style="max-width:280px">
                    One platform, every tool your business needs.
                </p>
            </div>
            <div class="col-6 col-lg-2">
                <h6>Platforms</h6>
                <a href="commerce.html">Commerce</a>
                <a href="document.html">Document</a>
                <a href="case.html">Case</a>
                <a href="project.html">Project</a>
                <a href="crm.html">CRM</a>
            </div>
            <div class="col-6 col-lg-2">
                <h6>More</h6>
                <a href="marketing.html">Marketing</a>
                <a href="email.html">Email</a>
                <a href="support.html">Support</a>
                <a href="knowledge.html">Knowledge</a>
                <a href="agent.html">Agent</a>
            </div>
            <div class="col-lg-4">
                <h6>Get Started</h6>
                <a href="../index.html#cta">Request Early Access</a>
                <a href="../index.html#platforms">Browse All Platforms</a>
            </div>
        </div>
        <div class="footer-bottom d-flex flex-wrap justify-content-between align-items-center">
            <p class="text-muted">&copy; <span id="footer-year"></span> AlohaOne. All rights reserved.</p>
            <a href="../index.html" class="text-muted">&larr; Back to home</a>
        </div>
    </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>
"""


# =========================================================
# GENERATE
# =========================================================
def main():
    count = 0
    for slug, p in PLATFORMS.items():
        badge_class, badge_label = STATUS_BADGES[p["status"]]
        html = TEMPLATE.format(
            name=p["name"],
            tagline=p["tagline"],
            description=p["description"],
            overview=p["overview"],
            icon=p["icon"],
            gradient=p["gradient"],
            badge_class=badge_class,
            badge_label=badge_label,
            cta_buttons=render_cta(p),
            integration_note=render_integration_note(p),
            capabilities=render_capabilities(p["capabilities"]),
            integrations=render_integrations(p["integrations"]),
            platform_matrix=render_platform_matrix(p),
            customers_section=render_customers(p),
            pricing_section=render_pricing(p),
            final_cta_section=render_final_cta(p),
        )
        (OUT_DIR / f"{slug}.html").write_text(html, encoding="utf-8")
        count += 1
        print(f"  [OK] {slug}.html")
    print(f"\nGenerated {count} platform detail pages in {OUT_DIR}")


if __name__ == "__main__":
    main()
