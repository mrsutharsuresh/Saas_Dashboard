# Legal SaaS Development Plan (Rajasthan + Central Pilot)

**Total Estimated Duration**: 32-36 Weeks (8 - 9 Months) - *Hyper-realistic schedule encompassing heavy anti-bot mitigation and AI tuning.*
**Strategy**: Expanded POC first (Phase 0), then Deep Dive into Core Engine & Security (Phase 1).
**Total Estimated Effort**: ~885 Hours

---

## Phase 0: Expanded POC - Feasibility Check (Weeks 1-5)
*Goal: Systematically prove all crucial high-risk technical integrations before building business logic.*

**Detailed POC Breakdown**: The POC Phase has been rigorously broken down into a 36-step, hour-by-hour action plan mapped against actual coding roadblocks (Cloudflare, Web Audio API bugs, Meta Rejections, LLM Tuning). 
Please refer to the separate **[POC_DETAILED_DEVELOPMENT_PLAN.md](POC_DETAILED_DEVELOPMENT_PLAN.md)** for the granular task list.
*   **Total Realistic POC Effort**: **215 Hours**

---

## Phase 1: Core Engine & Proxy / Security (Weeks 6-11)
*Focus: Production-grade scraping immune to aggressive IP bans and DOM mutations.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Scraper Core** | Implement browser fingerprint spoofing (Canvas/WebGL defeners) & Cloudflare Turnstile bypasses. | 0.1 | 35 |
| **1.2** | **Security Layer** | **AES-256-GCM** + AWS KMS integration. Key rotation logic & Secure Enclaves for DB credentials. | 0.3 | 25 |
| **1.3** | **Proxy Manager** | Service to detect contaminated IP subnets, geo-target residential IPs, and map bandwidth costs carefully. | 1.1 | 30 |
| **1.4** | **Central Adapters**| Supreme & District courts. Handle unannounced DOM updates via schema-less fallback parsers. | 1.1 | 25 |
| **1.5** | **State Adapters**| `hcraj` Live Board. Handle massive traffic spikes during court hours without dropping socket connections. | 1.1 | 25 |
| | | **Phase 1 Total** | | **140** |

---

## Phase 2: Backend DB, Subscriptions & Auth (Weeks 12-16)
*Focus: Scalable multi-tenant architecture and strict financial/data compliance.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **DB Partitioning**| Implement horizontal partitioning for Case History tables to prevent index bloat on JSONB blobs. | 1.2 | 20 |
| **2.2** | **Strict Auth** | OAuth 2.0 + Session hijacking prevention. DPDP compliant "Hard Delete" sweeping orphan records. | 2.1 | 20 |
| **2.3** | **Subscriptions** | Razorpay Webhooks. Handle failed recurrent payments, dispute/chargeback logic, and pro-ration. | 2.1 | 35 |
| **2.4** | **Support Module** | Secure AWS S3 uploads for user ticket attachments + SLA timer tracking logic. | 2.1 | 15 |
| **2.5** | **Alerts Engine** | Dead-Letter Queues (DLQ) for failed WABA messages, strict rate-limit backoffs (exponential). | 0.2, 2.1| 20 |
| | | **Phase 2 Total** | | **110** |

---

## Phase 3: Intelligence & RAG Integration (Weeks 17-21)
*Focus: Eliminating LLM hallucinations and handling massive document ingestion.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Verified Voice** | Complex error handling when voice contradicts web state. Human-in-the-loop fallback UI triggers. | 0.6, 0.9| 35 |
| **3.2** | **Kanoon Wrapper** | Cache invalidation strategies, rate-limit pauses, scraping unstructured archaic HTML responses. | - | 15 |
| **3.3** | **RAG Pipeline** | Vector dimension tuning. Handling massive PDFs (500+ pages) without Out-Of-Memory (OOM) errors. | 0.7 | 30 |
| **3.4** | **Semantic Search**| Hybrid search (Keyword + Vector) for precision. Prompt-injection prevention from Advocate inputs. | 3.3 | 30 |
| | | **Phase 3 Total** | | **110** |

---

## Phase 4: Advocate PWA Frontend (Weeks 22-28)
*Focus: Unbreakable mobile interface with offline capabilities.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Case Portfolio** | Infinite scrolling/pagination for 1000s of cases. Service Worker caching for offline viewing. | 2.1 | 35 |
| **4.2** | **Consent UI** | Granular toggles per DPDP Act. Generation of PDF "Consent Receipts" for legal audit trails. | 2.2 | 25 |
| **4.3** | **Integrate UI** | WebSockets for real-time WABA delivery read-receipts. Optimistic UI updates during network drops. | 3.1, 3.4| 60 |
| **4.4** | **Payment Portal** | Handling 3D Secure redirects smoothly inside the PWA without breaking session state. | 2.3 | 25 |
| **4.5** | **UI/UX Polish** | Core Web Vitals optimization to guarantee < 2s LCP. Custom micro-animations. Lighthouse audits. | 4.3 | 25 |
| | | **Phase 4 Total** | | **170** |

---

## Phase 5: Production & Handoff (Weeks 29-34)
*Focus: Hardening the infrastructure for Day-1 public scale.*

| Task ID | Task Name | Sub-task | Dependency | Est. Hrs |
| :--- | :--- | :--- | :--- | :--- |
| **5.1** | **Chaos & Load** | Test 500+ concurrent scrapers. DB failover testing. Redis memory eviction policy tuning. | 1.1 | 35 |
| **5.2** | **CI/CD & Deploy**| Zero-downtime GitHub Actions pipelines. Docker Swarm / Kubernetes setup. Vault for API secrets. | - | 35 |
| **5.3** | **QA & Buffer** | Extensive manual testing. Fixing hyper-specific edge cases across iOS/Android/Windows environments. | All | 50 |
| **5.4** | **Documentation**| Auto-generated Swagger APIs. "Runbooks" for manual Scraper interventions when government portals break. | 5.2 | 20 |
| | | **Phase 5 Total** | | **140** |

---

## 6. Risk Management & Contingencies (Aggressive)

| Risk Category | Potential Issue | Mitigation Strategy |
| :--- | :--- | :--- |
| **Technical** | Complete UI overhaul of Govt Portals | **Schema-less Fallbacks**: Alerts trigger PagerDuty for developers. System falls back to raw HTML snapshot storage until scraper is patched. |
| **Technical** | IP Subnet Blacklisting | Over-provision residential proxies globally. Auto-rotate out entire subnets if `403` rates exceed 5%. |
| **Legal/Compliance** | DPDP Act Audit | **AES-256 Encryption** at rest. Mandatory Boolean `consent_given` in DB schemas. "Delete Account" strictly wipes DB/S3 schemas. |
| **Infrastructure** | Runaway AI/Proxy Costs | Hard billing limits on OpenAI/Meta APIs. Auto-suspend features if thresholds breached. |
| **Data Quality** | Hallucinations in LLMs | Mandatory **Deterministic Verification** (Regex/Rules) applied *after* LLM output before committing to DB. |
