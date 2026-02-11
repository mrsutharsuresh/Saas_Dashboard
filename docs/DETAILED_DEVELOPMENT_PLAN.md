# Detailed Development Plan & Timeline (Indian Market - Relaxed)

**Total Estimated Duration**: 16-18 Weeks (4 - 4.5 Months)
**Work Mode**: Freelance / Contract (Part-time or Relaxed Full-time)

---

## Phase 0: Extended POC + LLM (Weeks 1-4)
*Goal: Deep Dive Feasibility (Portal 1) + Basic AI Processing.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0.1** | **Setup & Analysis** | Repo Setup + Network Analysis (Portal 1) | Standalone | None | 8 |
| **0.2** | **Portal 1 Script** | Navigation + Captcha Handling (Manual/Simple) | Linked | 0.1 | 15 |
| **0.3** | **Data Extraction** | HTML Table to JSON Parsing | Linked | 0.2 | 8 |
| **0.4** | **Basic LLM Setup** | Integrate Gemini API (Flash Model) | Linked | 0.1 | 6 |
| **0.5** | **AI Data Cleaning** | **Evaluate LLM for parsing messy addresses/names** | Linked | 0.4, 0.3 | 12 |
| **0.6** | **Demo Output** | Unified JSON + AI Summary Field | Linked | 0.5 | 5 |

**POC Total**: ~54 Hours (Allocated over 4 Weeks)
**POC Cost**: **₹35,000** (Fixed)

---

## Phase 1: Full Data Acquisition Scrapers (Weeks 5-6)
*Focus: Scaling to Portal 2, automating Captchas, and hardening Portal 1 for production.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Scraper Engine** | Global Retry Logic + Proxy Rotation | Standalone | 0.2 | 10 |
| **1.2** | **Portal 1 Polish** | Refactors for stability (PDFs, Error Handling) | Linked | 0.2 | 10 |
| **1.3** | **Portal 2 Automation** | Analyze + Script Navigation | Standalone | 1.1 | 20 |
| | | **Data Extraction** (Table -> JSON) | Linked | 1.3 | 8 |
| | | PDF Download & Storage Logic | Linked | 1.3 | 5 |
| **1.4** | **Data Pipeline** | Normalize Data (Schema Unification) | Linked | 0.3, 1.3 | 8 |
| | | **Validation Scripts** (Null checks, Type alerts) | Linked | 1.4 | 5 |
| **1.5** | **Hardening** | Integrate 2Captcha API for both Portals | Linked | 1.1 | 6 |

**Phase 1 Total**: ~72 Hours (Allocated over 2 Weeks)

---

## Phase 2: Backend Core & Database (Weeks 7-9)
*Focus: Security, Tenant Isolation, and API Structure.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2.1** | **Database Design** | Schema Design (ER Diagram) | Standalone | None | 8 |
| | | Migration Setup (Alembic) | Linked | 2.1 | 4 |
| **2.2** | **Auth System** | User Model & Password Hashing | Standalone | 2.1 | 6 |
| | | JWT Token Implementation | Linked | 2.2 | 6 |
| | | Role Based Access (Admin vs Pro) | Linked | 2.2 | 8 |
| **2.3** | **Core APIs** | Project CRUD (Create/Read/Upd/Del) | Linked | 2.1 | 12 |
| | | Client CRUD | Linked | 2.1 | 8 |
| | | Scraper Trigger API (Async Task) | Linked | 1.4, 2.3 | 10 |
| **2.4** | **Infrastructure** | Redis + Celery Setup (Queue) | Linked | 2.3 | 12 |

**Phase 2 Total**: ~74 Hours (Allocated over 3 Weeks)

---

## Phase 3: AI Intelligence Layer (Weeks 10-12)
*Focus: High Accuracy Voice Processing & Document RAG.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Voice Pipeline** | Audio Upload API (Blob storage) | Standalone | 2.3 | 8 |
| | | OpenAI Whisper Integration | Linked | 3.1 | 6 |
| | | **Hinglish Optimization** (Prompting) | Linked | 3.1 | 10 |
| **3.2** | **Generative Extraction** | Gemini JSON Extraction Logic | Linked | 3.1 | 12 |
| | | "Pre-fill Form" Data Structure | Linked | 3.2 | 6 |
| **3.3** | **E-Library RAG** | PDF Parsing (OCR Tesseract/LlamaParse)| Standalone | None | 12 |
| | | Vector DB Setup (PgVector) | Linked | 2.1 | 8 |
| | | Semantic Search API | Linked | 3.3 | 10 |

**Phase 3 Total**: ~72 Hours (Allocated over 3 Weeks)

---

## Phase 4: Frontend Mobile PWA (Weeks 13-16)
*Focus: User Experience, Offline Mode, Responsiveness.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Shell Architecture** | Router & Auth Context | Standalone | 2.2 | 8 |
| | | Layouts (Mobile Bottom Nav) | Linked | 4.1 | 8 |
| **4.2** | **Modules UI** | Project List & Details View | Linked | 2.3 | 12 |
| | | **Voice Recorder Component** | Linked | 3.1 | 12 |
| | | Form Pre-fill & Edit UI | Linked | 3.2 | 10 |
| | | E-Library Search UI | Linked | 3.3 | 8 |
| **4.3** | **PWA Features** | Service Worker (Caching) | Linked | 4.1 | 10 |
| | | Manifest & Installability | Linked | 4.3 | 4 |
| **4.4** | **Admin Dashboard** | Stats & User Management UI | Linked | 2.2 | 10 |

**Phase 4 Total**: ~82 Hours (Allocated over 4 Weeks)

---

## Phase 5: QA, Deployment & Handoff (Weeks 17-18+)
*Focus: Stability and Documentation.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5.1** | **Production Env** | VPS Setup (Docker, Nginx, SSL) | Standalone | None | 12 |
| | | CI/CD Pipeline (GitHub Actions) | Linked | 5.1 | 8 |
| **5.2** | **Testing** | End-to-End Scraper Tests | Linked | 1.4 | 10 |
| | | Mobile Responsiveness Audit | Linked | 4.1 | 8 |
| **5.3** | **Handoff** | User Manual & Admin Guide | Linked | None | 8 |

**Phase 5 Total**: ~46 Hours (Allocated over 2 Weeks)
