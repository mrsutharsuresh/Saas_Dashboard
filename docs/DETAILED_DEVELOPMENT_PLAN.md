# Legal SaaS Development Plan (Rajasthan + Central Pilot)

**Total Estimated Duration**: 24-28 Weeks (6 - 7 Months) - *Relaxed schedule to accommodate advanced complexities.*
**Strategy**: Expanded POC first (Phase 0), then Deep Dive into Core Engine & Security (Phase 1).
**Total Estimated Effort**: ~485 Hours

---

## Phase 0: Expanded POC - Feasibility Check (Weeks 1-5)
*Goal: Systematically prove all crucial high-risk technical integrations before building business logic.*

**Detailed POC Breakdown**: The POC Phase has been rigorously broken down into a 36-step, hour-by-hour action plan. 
Please refer to the separate **[POC_DETAILED_DEVELOPMENT_PLAN.md](POC_DETAILED_DEVELOPMENT_PLAN.md)** for the granular task list.
*   **Total POC Effort**: **125 Hours**

---

## Phase 1: Core Engine & Proxy / Security (Weeks 6-10)
*Focus: Robust Scraper Engine with strict Data Privacy (DPDP Act).*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Scraper Core** | Build `AbstractScraper` + implements **Auto-Healing / Health Checks**. | 0.1 | 20 |
| **1.2** | **Security Layer** | **AES-256-GCM** encryption utilities for all DB writes/reads (PII mask). | 0.3 | 15 |
| **1.3** | **Proxy Manager** | Service to rotate IPs on `429/403` and handle 2Captcha load balancing. | 1.1 | 15 |
| **1.4** | **Central Adapters**| Production-grade scrapers: Supreme Court, eCourts District, eCourts Judgments. | 1.1 | 15 |
| **1.5** | **State Adapters**| Production-grade scrapers: `hcraj` Live Board polling, `apnakhata`, `gcms`. | 1.1 | 15 |
| | | **Phase 1 Total** | | **80** |

---

## Phase 2: Backend DB, Subscriptions & Auth (Weeks 11-14)
*Focus: Multi-tenant business logic and Consent Schemas.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **DB Schema Final**| Finalize Advocate, Case, Subscription tables with mandatory `consent_given` Boolean. | 1.2 | 10 |
| **2.2** | **Auth System** | JWT logins + **Delete Account API** (Explicitly wipes DB/S3, skips tedious logs). | 2.1 | 10 |
| **2.3** | **Subscriptions** | Razorpay Recurrent Mandates APIs + Tiered limit logic. | 2.1 | 20 |
| **2.4** | **Support Module** | Ticket APIs for users to report mismatched web vs parsed data. | 2.1 | 10 |
| **2.5** | **Alerts Engine** | Celery + Redis queues. Trigger WABA API safely preventing duplicates. | 0.2, 2.1| 10 |
| | | **Phase 2 Total** | | **60** |

---

## Phase 3: Intelligence & RAG Integration (Weeks 15-18)
*Focus: verified parsing and semantic search.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Verified Voice** | Web Audio -> Whisper -> **Cross-verify text vs DB state** -> Gemini JSON. | 0.6, 0.9| 20 |
| **3.2** | **Kanoon Wrapper** | API limits handling for fetching older precedents via Indian Kanoon. | - | 10 |
| **3.3** | **RAG Pipeline** | eCourts PDFs -> `text-embedding-3-small` -> `pgvector` index storage. | 0.7 | 15 |
| **3.4** | **Semantic Search**| API endpoint to take Advocate query, fetch vectors, and return Gemini LLM summary. | 3.3 | 15 |
| | | **Phase 3 Total** | | **60** |

---

## Phase 4: Advocate PWA Frontend (Weeks 19-24)
*Focus: Mobile-First interface (Vite + React).*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Case Portfolio** | Decrypted "Daily Board" View UI. | 2.1 | 20 |
| **4.2** | **Consent UI** | Onboarding screens ensuring DPDP Opt-In explicit logging. | 2.2 | 15 |
| **4.3** | **Integrate UI** | Hook up Web Audio Recorder (4.3), Support Tickets (4.4), RAG Search UI (4.5), and WABA opt-ins to APIs. | 3.1, 3.4| 40 |
| **4.4** | **Payment Portal** | Secure Razorpay client-side integration and Subscription history. | 2.3 | 15 |
| **4.5** | **UI/UX Polish** | PWA Manifest (`manifest.json`), Offline caching, Mobile responsiveness. | 4.3 | 10 |
| | | **Phase 4 Total** | | **100** |

---

## Phase 5: Production & Handoff (Weeks 25-28)
*Focus: Buffer time for complex testing, scaling, and deployment.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **5.1** | **Sys Load Tests** | Test 100 concurrent scrapers + PgBouncer setup. | 1.1 | 15 |
| **5.2** | **Deploy Strategy**| Docker Compose + DigitalOcean VPS (Nginx, SSL, Redis). | - | 15 |
| **5.3** | **QA & Buffer** | Fix edge cases across WA dedupe, Proxy blocks, or UI bugs. | All | 20 |
| **5.4** | **Documentation**| Finalize API swagger, Architecture handover docs. | 5.2 | 10 |
| | | **Phase 5 Total** | | **60** |

---

## 6. Risk Management & Contingencies (Synced)

| Risk Category | Potential Issue | Mitigation Strategy |
| :--- | :--- | :--- |
| **Technical** | `hcraj` DOM changes | **Auto-Healing/Health Checks**: Detect structural changes -> Pause -> Alert Admin immediately via `structlog`. |
| **Technical** | 2Captcha success drops due to new AI | Implement rapid fallback to AI solvers (Capsolver) for high-priority alerts. |
| **Legal/Compliance** | DPDP Act Audit | **AES-256 Encryption** at rest. Mandatory Boolean `consent_given` in DB schemas. "Delete Account" strictly wipes DB/S3 schemas. |
| **Notification** | WABA Rate Limits & Duplicates | Strict Redis caching checks before triggering a Meta API Template to prevent double-billing. |
| **Data Quality** | Hallucinations in Voice AI | Implement logic to **Cross-verify** Whisper extracted case names/dates against the available scraped website state. |
