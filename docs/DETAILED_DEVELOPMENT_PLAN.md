# Legal SaaS Development Plan (Rajasthan + Central Pilot)

**Total Estimated Duration**: 18-20 Weeks (4.5 - 5 Months)
**Strategy**: Broad POC first (Phase 0), then Deep Dive into Core Engine & Security (Phase 1).

---

## Phase 0: Expanded POC - Feasibility Check (Weeks 1-4)
*Goal: Prove basic connectivity with ALL target systems (Breadth-First).*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0.1** | **Setup** | Repo, Env, API Keys (Razorpay, OpenAI, 2Captcha) | Standalone | None | 8 |
| **0.2** | **Logger Module** | Basic `structlog` setup (File/Console) | Linked | 0.1 | 4 |
| **0.3** | **eCourts (District)** | Fetch 1 Case from `services.ecourts` (RJ District) | Linked | 0.2 | 5 |
| **0.4** | **eCourts Judgments** | Fetch 1 Judgment PDF from `judgments.ecourts` | Linked | 0.2 | 4 |
| **0.5** | **High Court Test**| Script to poll `hcraj.nic.in` Display Board (10 mins) | Linked | 0.1 | 8 |
| **0.5** | **Revenue/Land** | Script to fetch status from `gcms` & `apnakhata` (Basic) | Linked | 0.1 | 8 |
| **0.6** | **Whatsapp Test** | Send "Hello World" Template via Twilio/Meta Sandbox | Linked | 0.1 | 4 |
| **0.7** | **Voice Test** | Transcribe 1 sample Audio -> JSON via Whisper | Linked | 0.1 | 4 |
| **0.8** | **Legacy API** | Fetch 1 Judgment from Indian Kanoon API | Linked | 0.1 | 3 |
| **0.9** | **Central Test** | Fetch 1 Case from Supreme Court (`sci.gov.in`) | Linked | 0.2 | 6 |
| **0.10** | **Rajasthan Test** | Poll `hcraj` Live Board + Fetch `apnakhata` | Linked | 0.2 | 10 |
| **0.11** | **Payment Test** | Create Razorpay Order + Verify Signature | Linked | 0.1 | 4 |
| **0.12** | **Integration** | Live Alert Demo (Mocked Data -> WhatsApp) | Linked | 0.5, 0.6 | 5 |

**POC Total**: ~45 Hours (Weeks 1-4)

---

## Phase 1: Core Engine, Security & Proxy (Weeks 5-8)
*Focus: Robust Scraper Engine with Security & Compliance.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Scraper Core** | `BaseScraper` Class + `StateAdapter` Pattern | Standalone + `AbstractScraper` + `ProxyManager` Implementation | Standalone | 0.2 | 15 |
| **1.2** | **Security Layer** | **AES-256 Encryption** Utility for DB Storage | Linked | 1.1 | 8 |
| **1.3** | **Proxy Manager** | Rotating Residential IPs + User-Agent Spoofing | Linked | 1.1 | 10 |
| **1.4** | **eCourts Adapter** | Production District Court Scraper (Rajasthan) | Linked | 1.1 | 15 |
| **1.5** | **Central Adapter** | Supreme Court Scraper (Full Implementation) | Linked | 1.1 | 12 |
| **1.6** | **State Adapter** | Rajasthan HC + Revenue + Land Scrapers | Linked | 1.1 | 15 |

**Phase 1 Total**: ~70 Hours (Weeks 5-8)

---

## Phase 2: Backend, Payments & Support (Weeks 9-11)
*Focus: Scalable Monolith & Business Logic.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2.1** | **Database** | Postgres Schema (Encrypted Columns) | Standalone | None | 10 |
| **2.2** | **Auth System** | JWT + Opt-in Audit Log + **Delete Account API** | Linked | 2.1 | 8 |
| **2.3** | **Subscription** | **Razorpay Integration** (Recurring/One-time) | Linked | 2.2 | 12 |
| **2.4** | **Admin Dashboard** | React Panel for System Health & User Mgmt | Linked | 2.2 | 12 |
| **2.5** | **Support Module** | Ticket API + Admin Dashboard for Issues | Linked | 2.2 | 10 |

**Phase 2 Total**: ~40 Hours (Weeks 9-11)

---

## Phase 3: Intelligence & RAG (Weeks 12-15)
*Focus: "The Brain".*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Voice Pipeline** | API Endpoint + Whisper + Gemini "Hinglish" Extractor | Standalone | 2.2 | 15 |
| **3.2** | **Legal RAG** | **Indian Kanoon API** Wrapper | Linked | 2.2 | 5 |
| | | Ingest **eCourts Judgments** (PDF -> Text -> Vector) | Linked | 3.2 | 10 |
| | | Vector Search (pgvector) for "Similar Cases" | Linked | 3.2 | 12 |
| | | "Outcome Probability" Logic (LLM Analysis) | Linked | 3.2 | 12 |

**Phase 3 Total**: ~44 Hours (Weeks 12-15)

---

## Phase 4: Advocate Dashboard PWA (Weeks 16-19)
*Focus: Mobile Interface.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Case Portfolio** | Decrypted View: "My Daily Board" | Standalone | 2.1 | 15 |
| **4.2** | **Alerts Hub** | UI to Draft & Approve Client Messages | Linked | 4.1 | 10 |
| **4.3** | **Voice Recorder** | Audio Capture UI + Upload | Linked | 4.1 | 8 |
| **4.4** | **Search UI** | Interface for RAG/Similar Case Search | Linked | 3.2 | 8 |
| **4.5** | **Support UI** | "Report Issue" Form + Ticket Status View | Linked | 2.4 | 8 |
| **4.6** | **Subscription UI** | Payment Gateway Integration + History | Linked | 2.3 | 8 |

**Phase 4 Total**: ~41 Hours (Weeks 16-19)

---

## Phase 5: Production & Handoff (Week 20)
| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5.1** | **Deploy** | Docker Compose + VPS (Nginx, SSL, Redis) | Standalone | None | 10 |
| **5.2** | **Docs** | API Documentation + Video Guide | Linked | None | 8 |

**Phase 5 Total**: ~18 Hours

---

## 6. Risk Management & Contingencies (Merged Research)

| Risk Category | Potential Issue | Mitigation Strategy |
| :--- | :--- | :--- |
| **Technical** | `hcraj` changes CAPTCHA / DOM structure | **Auto-Healing Scrapers**: Detect changes -> Pause -> Alert Admin. Fallback to Contributor verification. |
| **Legal** | eCourts bans IP range | **Rotating Proxies**: Use residential IPs. Implement "Ethical Rate Limiting" (1 req/min). |
| **Business** | WhatsApp API Price Hike | **Hybrid Notification**: Switch low-priority alerts to Email/Push Notifications + SMS. |
| **Data** | Stale Case Status | **Crowdsourcing**: Incentivize Junior Advocates to verify status manually. |
| **Compliance** | DPDP Act Audit | **AES-256 Encryption**: All PII encrypted at rest. strict Opt-in logs maintained. |
