# Client Cost Responsibility Document (Non-Developer Costs)

 This document outlines the **Infrastructure and Operational Costs** that must be paid directly by the client to third-party service providers. These are required to keep the SaaS platform running.

---

## 1. Fixed / One-Time Setup Costs
*Expenses occurred once at the beginning of the project.*

| Item | Description | Estimated Price (INR) | Vendor Options |
| :--- | :--- | :--- | :--- |
| **Domain Name** | Web Address (e.g., `.com` or `.in`) | ₹800 - ₹1,200 / year | GoDaddy, Namecheap, BigRock |
| **SSL Certificate** | Security Encryption (HTTPS) | ₹0 (Free) | Let's Encrypt (Recommended) |
| **Play Store Console** | Developer Account (If publishing Android App) | ₹2,100 ($25) | Google (One-time fee) |
| **Apple App Store** | Developer Account (If publishing iOS App) | ₹8,300 ($99) / year | Apple (Recurring Yearly) |
| **WhatsApp Setup** | Business Verification | ₹0 | Meta (Requires Business Docs) |
| **Total One-Time** | | **~₹3,000** (Web Only) | **~₹13,500** (Web + Mobile Stores) |

---

## 2. Recurring Running Costs (Monthly)
*These scale based on usage (Number of Users & Scrapes).*

### A. Server Infrastructure (The "Computer")
| Item | Description | Est. Cost (INR) | Vendor |
| :--- | :--- | :--- | :--- |
| **VPS Server** | 4 vCPU, 8GB RAM (Required for multiple browser scrapers) | ₹2,000 - ₹3,000 | Hostinger, AWS, Hetzner Cloud (Cheapest) or DigitalOcean |
| **Object Storage** | S3-compatible storage for PDFs/Images (100GB) | ₹500 | DigitalOcean Spaces / AWS S3 |
| **Database Backups** | Automated daily backups | ₹200 - ₹500 | AWS S3 / Snapshots |
| **Subtotal Infra** | | **~₹3,500 / month** | |

### B. Third-Party APIs (The "Brain")
| Item | Usage Estimate | Est. Cost (INR) | Vendor |
| :--- | :--- | :--- | :--- |
| **OpenAI Whisper** | Voice-to-Text (~1000 mins/mo) | ₹500 - ₹1,000 | OpenAI API |
| **Gemini Flash** | Data Extraction (High volume) | ₹500 - ₹800 | Google DeepMind |
| **WhatsApp API** | ~1000 Conversations (Marketing/Utility) | ₹1,000 - ₹2,000 | Meta (First 1k service convos free) |
| **Subtotal APIs** | | **~₹3,000 / month** | |

### C. Scraping Logistics (The "Fuel")
| Item | Description | Est. Cost (INR) | Vendor |
| :--- | :--- | :--- | :--- |
| **Residential Proxies**| To avoid IP Bans (2GB Bandwidth) | ₹1,500 - ₹2,500 | BrightData / SmartProxy |
| **Captcha Solving** | Solving ~5000 Captchas | ₹500 - ₹800 | 2Captcha / CapSolver |
| **Subtotal Scraper** | | **~₹2,500 / month** | |

---

## 3. Total Monthly "Burn" Calculation

| Scenario | Usage Profile | Total Estimated Monthly Cost |
| :--- | :--- | :--- |
| **Low Usage** | 10 Users, 100 Scrapes/day | **₹6,000 - ₹8,000** |
| **Medium Usage** | 50 Users, 1000 Scrapes/day | **₹9,000 - ₹12,000** |
| **High Usage** | 200+ Users, 5000+ Scrapes/day | **₹18,000+** (Need larger server + more proxies) |

**Note**: All payments are typically made via Credit Card directly to the vendors (Hostinger, AWS, DigitalOcean, OpenAI, etc.).
