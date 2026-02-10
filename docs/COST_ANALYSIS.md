# Comprehensive Project Cost & Roadmap Analysis (Bottom-Up Estimation)

## 1. Executive Summary (Revised)
*   **Total Project Estimates**:
    *   **Effort**: ~340 Hours.
    *   **Timeline**: **16 Weeks** (4 Months) @ 20-25 hrs/week (Realistic Freelance Pace).
    *   **Development Cost**: **₹2,10,000 - ₹2,50,000** (Based on hourly breakdown).

---

## 2. Detailed Breakdown: Task, Time & Cost

**Rate Assumptions**:
*   **Backend/Scraper (Standard)**: ₹600/hr.
*   **Frontend (React/PWA)**: ₹500/hr.
*   **AI/Complex Logic**: ₹1,000/hr.
*   **DevOps/System Arch**: ₹800/hr.

### Phase 1: Data Acquisition (The Scrapers)
*Target: 2 Govt Portals + Base Engine*

| Sub-Task | Description | Complexity | Hours | Rate (₹) | Est. Cost (₹) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Engine Core** | Proxy rotation, Retry logic, Captcha handler placeholders. | High | 15 | 800 | 12,000 |
| **Portal 1 Scraper** | Auth (Captcha), Nav, Table Extraction, PDF Download logic. | High | 25 | 600 | 15,000 |
| **Portal 2 Scraper** | Auth (Captcha), Nav, Table Extraction, PDF Download logic. | High | 25 | 600 | 15,000 |
| **Data Normalization**| Cleaning distinct outputs into a single schema. | Med | 10 | 600 | 6,000 |
| **Unit Testing** | Validating scrapers against changing layouts. | Med | 10 | 600 | 6,000 |
| **Phase 1 Total** | | | **85 Hrs** | | **₹54,000** |

### Phase 2: Core Backend & API
*Target: System Architecture, Database, Auth*

| Sub-Task | Description | Complexity | Hours | Rate (₹) | Est. Cost (₹) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DB Design** | Postgres Schema (Users, Tenants, Projects, Logs). | High | 10 | 800 | 8,000 |
| **Auth System** | JWT Implementation, Password Hashing, Role-based Access. | Med | 15 | 600 | 9,000 |
| **CRUD APIs** | Endpoints for Projects, Clients, Scrape triggers. | Med | 20 | 600 | 12,000 |
| **Task Queue** | Setting up Celery/Redis for async scraping jobs. | High | 15 | 800 | 12,000 |
| **Phase 2 Total** | | | **60 Hrs** | | **₹41,000** |

### Phase 3: The Intelligence Layer (AI)
*Target: Voice-to-Data & RAG Search*

| Sub-Task | Description | Complexity | Hours | Rate (₹) | Est. Cost (₹) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Audio Pipeline** | Connect Whisper API, handle audio formats (webm/mp3). | High | 15 | 800 | 12,000 |
| **Extraction Logic** | Prompt Engineering (Gemini) to extract JSON from text. | Very High | 30 | 1000 | 30,000 |
| **RAG Setup** | PDF Parsing (OCR), Vector DB Ingestion (PgVector). | High | 25 | 1000 | 25,000 |
| **Search API** | Implementing Semantic + Keyword hybrid search. | High | 15 | 800 | 12,000 |
| **Phase 3 Total** | | | **85 Hrs** | | **₹79,000** |

### Phase 4: Frontend (Mobile PWA)
*Target: User Interface & Experience*

| Sub-Task | Description | Complexity | Hours | Rate (₹) | Est. Cost (₹) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **UX/UI Shell** | Navigation, Layouts, Mobile Responsiveness. | Med | 20 | 500 | 10,000 |
| **Feature Screens** | Forms, Lists, Details, Audio Recorder Component. | Med | 40 | 500 | 20,000 |
| **Integration** | Connecting UI to APIs, Error Handling, Loading States. | Med | 20 | 500 | 10,000 |
| **Offline Sync** | Service Workers for limited offline capability. | High | 10 | 800 | 8,000 |
| **Phase 4 Total** | | | **90 Hrs** | | **₹48,000** |

### Phase 5: Deployment & QA
*Target: Production Ready*

| Sub-Task | Description | Complexity | Hours | Rate (₹) | Est. Cost (₹) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VPS Setup** | Linux Hardening, Docker, Nginx, SSL, Postgres. | High | 10 | 800 | 8,000 |
| **CI/CD** | Automated key testing and deployment pipelines. | Med | 5 | 800 | 4,000 |
| **UAT / Bug Fixes**| 2 Weeks of buffer for user testing and fixes. | Var | 20 | 600 | 12,000 |
| **Phase 5 Total** | | | **35 Hrs** | | **₹24,000** |

---

## 3. Practical Timeline (Week by Week)

*Assumes 1 Developer working ~20-25 Hours/Week.*

| Week | Phase | Focus Areas | Cost Milestone |
| :--- | :--- | :--- | :--- |
| **1-3** | **Scraping** | Build Base Engine + Portal 1 + Portal 2. | ~₹50k |
| **4-5** | **Backend** | Database, Auth API, Project CRUD. | ~₹30k |
| **6-8** | **AI Core** | Audio Pipeline + Prompt Tuning (Hinglish). | ~₹40k |
| **9-11**| **Frontend** | React UI, Integration, Audio Recorder. | ~₹40k |
| **12-13**| **RAG** | E-Library, PDF Parsing, Vector Search. | ~₹35k |
| **14** | **Deploy** | DevOps, Server Setup. | ~₹10k |
| **15-16**| **Polish** | User Testing, Bug Fixes, Buffer. | ~₹15k |

**Total Duration**: **16 Weeks** (4 Months).

---

## 4. Operational "Running" Costs (Monthly)

**Scenario: 100 Users, ~1000 Scrapes/day.**

| Item | Service | Estimated Cost (INR) |
| :--- | :--- | :--- |
| **Compute** | Hetzner Cloud (CPX31: 4 vCPU, 8GB RAM) | ₹1,500 |
| **Database** | Managed Postgres (DigitalOcean) | ₹1,200 |
| **Storage** | S3 / R2 (100 GB Traffic) | ₹500 |
| **AI (Voice)** | OpenAI Whisper (API) | ₹2,500 |
| **AI (LLM)** | Gemini 1.5 Flash (Affordable) | ₹800 |
| **Scraping** | Residential Proxies + CapSolver | ₹2,000 |
| **WhatsApp** | Meta API (Conversational) | ₹1,500 |
| **Total** | | **~₹10,000 / month** |
