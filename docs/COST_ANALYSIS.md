# Project Cost & Resource Analysis (Indian Market - 2025 Estimates)

## 1. Executive Summary
*   **Revised Timeline**: **12-14 Weeks** (3 - 3.5 Months). *Relaxed to accommodate freelance availability.*
*   **Total Development Cost**: **₹1.8L - ₹2.5L** (Fixed Price) OR **₹60k - ₹80k / month**.
*   **Monthly Running Cost**: ₹4,000 - ₹10,000 (Scales with usage).

---

## 2. Resource Requirements & Rates (Lower Band)

### A. The "Solo Full-Stack" (Risk: Burnout)
*   **Profile**: Python (FastAPI/Scrapy) + React + Basic AI.
*   **Rate**: ₹600 - ₹1,000 / hr.
*   **Monthly**: ₹60,000 - ₹90,000.

### B. The Specialized Team (Recommended)
You need distinct skills. "All-in-one" developers often write poor scrapers or bad React code.

| Role | Responsibility | Hourly Rate (INR) | Monthly (Retainer) |
| :--- | :--- | :--- | :--- |
| **Backend/Scraping Eng.** | FastAPI + Playwright + Captcha Solving | ₹500 - ₹800 | ₹25k - ₹40k |
| **GenAI / API Eng.** | RAG, Vector DB, Whisper, LLM Tuning | ₹800 - ₹1,500 | ₹40k - ₹60k |
| **Frontend (PWA) Eng.** | React, Tailwind, Mobile UX | ₹400 - ₹700 | ₹20k - ₹35k |
| **DevOps** | Deployment (AWS/DO), CI/CD, Docker | ₹600 - ₹1,000 | Project Basis (~₹10k) |

---

## 3. Granular Cost Breakdown (Per Activity)

### A. Scraping (The Foundation)
*Research suggests pricing per site based on complexity.*
*   **Simple Site** (Static HTML, No Captcha): **₹5,000 - ₹8,000** one-time.
*   **Complex Site** (Govt Portal, Captcha, Session Timeouts): **₹15,000 - ₹25,000** per site.
    *   *Note*: Maintenance for complex sites is ~20% of dev cost per month.
*   **Total for 2 Sites**: **~₹40,000**.

### B. AI & RAG Intelligence
*High demand skill. Rates are higher.*
*   **Voice Pipeline**: Whisper integration + Hinge-lish optimization. **₹25,000**.
*   **RAG / E-Library**: Set up Vector DB (Pinecone/PgVector), PDF Parsing, Semantic Search. **₹35,000**.
*   **Total AI Module**: **~₹60,000**.

### C. Frontend & Dashboard (Mobile PWA)
*   **User App**: Auth, Projects Grid, Forms, Offline Sync. **₹40,000**.
*   **Admin Dashboard**: Simple stats view. **₹15,000**.
*   **Total Frontend**: **~₹55,000**.

### D. Deployment (DevOps)
*   **Setup**: Dockerizing, Setting up Nginx, SSL, Postgres on VPS.
*   **Cost**: **₹10,000 - ₹15,000** (One-time Task).

### **Grand Total Dev Estimate**: ~₹1,70,000 - ₹2,00,000

---

## 4. Operational & Running Costs (Monthly)

### A. One-Time Setup
*   **Developer Deployment Fee**: ₹15,000 (Engineer's time to set up cloud).
*   **Domain & SSL**: ₹1,000.

### B. Recurring Monthly "Burn"
| Item | Cost (INR) | Notes |
| :--- | :--- | :--- |
| **VPS (2 vCPU / 4GB RAM)** | ₹1,600 (Hetzner/DO) | Essential for Playwright + Docker. |
| **Managed DB (Optional)** | ₹1,200 | For auto-backups (RDS is expensive, use DO/Supabase). |
| **Object Storage (S3)** | ₹400 | Storing PDFs. |
| **Scraping APIs** | ₹1,000 | 2Captcha + Proxies (Variable). |
| **AI APIs (OpenAI/Gemini)** | ₹2,000+ | Usage based. Increases with user count. |
| **Total Monthly** | **₹6,000 - ₹10,000** | **Bootstrap Budget** |

---

## 5. Revised Roadmap (Relaxed)

*   **Month 1**: **Scraping Core**. Focus ONLY on getting data from 2 portals reliably.
*   **Month 2**: **Backend & AI**. Building the API, Database, and Voice/RAG engines.
*   **Month 3**: **Frontend (PWA)**. Connecting the UI.
*   **Month 3.5**: **QA & Deployment**. Testing on low-end phones. Deploying to Cloud.
*   **Total**: ~14 Weeks.
