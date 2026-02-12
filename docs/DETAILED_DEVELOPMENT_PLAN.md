# Legal SaaS Development Plan (Pan-India Scope)

**Total Estimated Duration**: 18-20 Weeks (4.5 - 5 Months)
**Strategy**: Broad POC first (Phase 0), then Deep Dive into Universal Engine (Phase 1).

---

## Phase 0: Expanded POC - Feasibility Across All Portals (Weeks 1-4)
*Goal: Prove basic connectivity with ALL target systems (Breadth-First).*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0.1** | **Setup** | Repo, Env, API Keys (OpenAI, 2Captcha, IndianKanoon) | Standalone | None | 8 |
| **0.2** | **eCourts Test** | Script to fetch 1 Case Status from `services.ecourts` | Linked | 0.1 | 5 |
| **0.3** | **High Court Test**| Script to poll `hcraj.nic.in` Display Board (10 mins) | Linked | 0.1 | 8 |
| **0.4** | **Revenue/Land** | Script to fetch status from `gcms` & `apnakhata` (Basic) | Linked | 0.1 | 8 |
| **0.5** | **Whatsapp Test** | Send "Hello World" Template via Twilio/Meta Sandbox | Linked | 0.1 | 4 |
| **0.6** | **Voice Test** | Transcribe 1 sample Audio -> JSON via Whisper | Linked | 0.1 | 4 |
| **0.7** | **Legacy API** | Fetch 1 Judgment from Indian Kanoon API | Linked | 0.1 | 3 |
| **0.8** | **Integration** | Combine 0.3 + 0.5 (Live Alert Demo) | Linked | 0.3, 0.5 | 5 |

**POC Total**: ~45 Hours (Weeks 1-4)

---

## Phase 1: Universal Scraper Engine (Weeks 5-8)
*Focus: Robust, Abstract Engine with Multi-State Adapters.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Core Engine** | `BaseScraper` Class + `StateAdapter` Pattern | Standalone | 0.2 | 15 |
| **1.2** | **Proxy Manager** | Rotating Residential IPs + User-Agent Spoofing | Linked | 1.1 | 10 |
| **1.3** | **eCourts Adapter** | Production-grade District Court Scraper | Linked | 1.1 | 20 |
| **1.4** | **State Adapter 1** | Rajasthan (HC + Revenue + Land) - Full Implementation | Linked | 1.1 | 15 |
| **1.5** | **State Adapter 2** | Delhi (HC + District) - Full Implementation | Linked | 1.1 | 10 |

**Phase 1 Total**: ~70 Hours (Weeks 5-8)

---

## Phase 2: Backend Architecture & User Mgmt (Weeks 9-11)
*Focus: Scalable Monolith.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2.1** | **Database** | Postgres Schema (Polymorphic Courts/Cases) | Standalone | None | 10 |
| **2.2** | **Auth System** | JWT + Role Base Access (Admin, Subscriber, Contributor) | Linked | 2.1 | 8 |
| **2.3** | **Subscription** | Stripe/Razorpay (Plans: District vs Pro) | Linked | 2.2 | 10 |
| **2.4** | **Admin Dashboard** | React Panel for System Health & User Mgmt | Linked | 2.2 | 12 |

**Phase 2 Total**: ~40 Hours (Weeks 9-11)

---

## Phase 3: Intelligence & RAG (Weeks 12-15)
*Focus: "The Brain".*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Voice Pipeline** | API Endpoint + Whisper + Gemini "Hinglish" Extractor | Standalone | 2.2 | 15 |
| **3.2** | **Legal RAG** | **Indian Kanoon API** Wrapper | Linked | 2.2 | 5 |
| | | Vector Search (pgvector) for "Similar Cases" | Linked | 3.2 | 12 |
| | | "Outcome Probability" Logic (LLM Analysis) | Linked | 3.2 | 12 |

**Phase 3 Total**: ~44 Hours (Weeks 12-15)

---

## Phase 4: Advocate Dashboard PWA (Weeks 16-19)
*Focus: Mobile Interface.*

| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Case Portfolio** | List View: "My Daily Board" (Unified) | Standalone | 2.1 | 15 |
| **4.2** | **Alerts Hub** | UI to Draft & Approve Client Messages | Linked | 4.1 | 10 |
| **4.3** | **Voice Recorder** | Audio Capture UI + Upload | Linked | 4.1 | 8 |
| **4.4** | **Search UI** | Interface for RAG/Similar Case Search | Linked | 3.2 | 8 |

**Phase 4 Total**: ~41 Hours (Weeks 16-19)

---

## Phase 5: Production & Handoff (Week 20)
| Task ID | Task Name | Sub-task | Type | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5.1** | **Deploy** | Docker Compose + VPS (Nginx, SSL, Redis) | Standalone | None | 10 |
| **5.2** | **Docs** | API Documentation + Video Guide | Linked | None | 8 |

**Phase 5 Total**: ~18 Hours

---

## 6. Risk Management & Contingencies

| Risk Category | Potential Issue | Mitigation Strategy |
| :--- | :--- | :--- |
| **Technical** | `hcraj` changes CAPTCHA / DOM structure | **Auto-Healing Scrapers**: Detect changes -> Pause -> Alert Admin. Fallback to Contributor verification. |
| **Legal** | eCourts bans IP range | **Rotating Proxies**: Use residential IPs. Implement "Ethical Rate Limiting" (1 req/min). |
| **Business** | WhatsApp API Price Hike | **Hybrid Notification**: Switch low-priority alerts to Email/Push Notifications + SMS. |
| **Data** | Stale Case Status | **Crowdsourcing**: Incentivize Junior Advocates to verify status manually. |
