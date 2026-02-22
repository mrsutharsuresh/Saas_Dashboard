# Phase 0: Elaborate Proof of Concept (POC) Plan
*A granular, microscopic breakdown of the 9 foundational POC tasks, aggressively adjusted for real-world roadblocks, anti-bot mechanisms, API rate limits, and cross-browser quirks. This is not an idealistic timeline; this is a battle-tested schedule.*

**Total Realistic Phase 0 Effort:** 215 hours 0 minutes
**Budget Implication (@ ₹1,000 - ₹1,200/hr):** ₹2,15,000 – ₹2,58,000

---

## 1. Proof of Scraping (Websites, Captcha, Proxies)
*Goal: Prove consistent access to heavily guarded government portals.*
*Roadblocks Accounted For: Request fingerprinting, Cloudflare Turnstile, IP bans, latent captchas, dynamic DOM structures.*
* **Subtotal: 62 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **1.1** | Initialize Playwright stealth architecture (hide webdriver flags, randomize user-agents). | `6 hr 00 min` |
| **1.2** | Integrate Residential Proxy pool. Implement detection & rotation logic for `403 Forbidden` / `429 Too Many Requests`. | `8 hr 00 min` |
| **1.3** | Implement 2Captcha API wrappers + advanced retry logic for timeout/failure/wrong-solution scenarios. | `6 hr 00 min` |
| **1.4** | Target 1: `services.ecourts` District Courts. Reverse-engineer session cookies & handle 5-char captchas. | `8 hr 30 min` |
| **1.5** | Target 1.B: Handle unexpected eCourts downtime & "Server Too Busy" HTML responses via exponential backoff. | `4 hr 00 min` |
| **1.6** | Target 2: `judgments.ecourts`. Fetch PDFs, handle corrupted PDF responses and connection resets. | `6 hr 30 min` |
| **1.7** | Target 3: `hcraj` Live Display Board. `aiohttp` fast-polling logic + handle random socket closures. | `6 hr 00 min` |
| **1.8** | Target 4: Revenue (`gcms`) / Land (`apnakhata`). Handle hidden form tokens (CSRF) and strict referer checks. | `9 hr 00 min` |
| **1.9** | End-to-end stress test across all 4 targets simultaneously to uncover parallelization/proxy cross-contamination bugs. | `8 hr 00 min` |

---

## 2. Integration with WhatsApp APIs
*Goal: Transmit outgoing templates & handle standard incoming events without double-billing.*
*Roadblocks Accounted For: Meta review rejections, strict 24-hr window rules, sandbox rate limits, webhook delivery failures.*
* **Subtotal: 21 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **2.1** | Meta Portal setup, identity verification roadblocks, and initial Template approval (often rejected once/twice). | `4 hr 00 min` |
| **2.2** | Build FastAPI webhook endpoints + implement strict Meta SHA256 signature verification to prevent spoofing. | `4 hr 30 min` |
| **2.3** | Deploy local Redis + configure persistent volume. Setup connection pooling. | `3 hr 30 min` |
| **2.4** | Python deduplication logic: Handle race conditions where 2 scrapers trigger the same alert simultaneously (Redis Locks). | `5 hr 00 min` |
| **2.5** | End-to-end messaging test. Debug missing delivery receipts & webhook timeout retries. | `4 hr 00 min` |

---

## 3. Database Creation (DPDP Schema Base)
*Goal: Setup encrypted data store capable of AI Vector Search.*
*Roadblocks Accounted For: Connection drops, async PG pooling limits, vector index bloat.*
* **Subtotal: 13 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **3.1** | PostgreSQL + `pgvector` setup. Configure `pgBouncer` / connection pooling limits for async FastAPI. | `3 hr 30 min` |
| **3.2** | Draft SQLAlchemy models with strict nullable constraints, string length limits, and `consent_given` audits. | `4 hr 00 min` |
| **3.3** | Initialize Alembic migrations. Troubleshoot asynchronous DB upgrade conflicts. | `2 hr 30 min` |
| **3.4** | Database seeding script handling foreign-key constraints and bulk-insert optimization. | `3 hr 00 min` |

---

## 4. Basic Dashboard (React Data Viewer)
*Goal: Tangible web portal to verify the scraped and processed data.*
*Roadblocks Accounted For: CORS issues, massive data-table render lags, state hydration errors.*
* **Subtotal: 24 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **4.1** | React/Vite scaffolding + Strict TypeScript strict typings for complex incoming JSON payloads. | `4 hr 00 min` |
| **4.2** | Setup React Router, Context API, and global layout framing. | `3 hr 00 min` |
| **4.3** | Build "Case Portfolio" table. Implement virtualization (e.g., `tanstack/react-table`) to prevent lag with 1000+ rows. | `7 hr 00 min` |
| **4.4** | Axios/Fetch integration + global interceptors for handling 401 Auth and 500 Server errors gracefully. | `5 hr 00 min` |
| **4.5** | Mobile-responsive adaptations and fixing Safari/Chrome CSS discrepancies. | `5 hr 00 min` |

---

## 5. Voice Input UI Component
*Goal: Enable Advocates to submit field intelligence intuitively.*
*Roadblocks Accounted For: iOS Safari preventing auto-play/mic access, background noise, `MediaRecorder` codec formats (WebM vs MP4).*
* **Subtotal: 16 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **5.1** | UI Component state machine (Standby, Requesting Permission, Recording, Paused, Review, Uploading). | `3 hr 30 min` |
| **5.2** | `Web Audio API` cross-browser integration. Implement explicit fallback for strict iOS Safari mic permissions. | `5 hr 30 min` |
| **5.3** | Implement basic client-side noise suppression constraints and enforce max-file-size limits. | `3 hr 00 min` |
| **5.4** | Blob -> base64/FormData conversion and multipart upload handlers. Handle network interruptions during upload. | `4 hr 00 min` |

---

## 6. Integration: Speech-to-Text Proof
*Goal: Accurately capture Hinglish legal dictation into strings.*
*Roadblocks Accounted For: Whisper API timeouts on large files, heavy Hindi dialect errors, out-of-memory on large buffer parsing.*
* **Subtotal: 12 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **6.1** | FastAPI `/api/voice/transcribe` endpoint with chunked streaming to prevent server RAM overload. | `3 hr 30 min` |
| **6.2** | OpenAI `Whisper` API wrapper. Implement fallback retry loops for `502 Bad Gateway` OpenAI errors. | `3 hr 30 min` |
| **6.3** | Benchmark tests on highly garbled "Courtroom environment" audio. Implement pre-processing (ffmpeg normalization) if needed. | `5 hr 00 min` |

---

## 7. Proof of RAG (Indian Kanoon & Judgments)
*Goal: Prove legal precedent similarity search via Vector Database.*
*Roadblocks Accounted For: Scanned PDFs without text layers, token limits exceeded, poor vector similarity matches.*
* **Subtotal: 29 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **7.1** | Advanced PDF parsing: Handle multi-column layouts, watermarks, and determine if simple OCR fallback is required for older judgments. | `8 hr 00 min` |
| **7.2** | Semantic chunking strategy (LangChain text splitters) to ensure chunks don't cut legal arguments in half. | `6 hr 00 min` |
| **7.3** | OpenAI `text-embedding-3-small` API integration + handling API rate limits for batch embedding generation. | `5 hr 00 min` |
| **7.4** | Store in `pgvector`. Implement and tune HNSW/IVFFlat indexes for fast query speeds as vector count grows. | `5 hr 00 min` |
| **7.5** | Cosine Distance queries + tuning the threshold cut-off to prevent irrelevant "hallucinated" judgment matches. | `5 hr 00 min` |

---

## 8. Basic Logger Module
*Goal: Professional, machine-readable audits for failing scrapers.*
*Roadblocks Accounted For: Concurrent write locks on log files, exposing PII in logs, async context loss.*
* **Subtotal: 8 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **8.1** | Inject `structlog`. Configure context variables (correlation IDs) to track a single request across Async tasks. | `3 hr 00 min` |
| **8.2** | Write custom processors to explicitly mask PII (Phone numbers, Names) before logs are written to disk. | `3 hr 00 min` |
| **8.3** | Setup log rotation (e.g., 50MB limits) to prevent server disk space exhaustion. | `2 hr 00 min` |

---

## 9. Basic Integration with LLM
*Goal: Convert unstructured text logs into structured JSON Case Objects.*
*Roadblocks Accounted For: Gemini ignoring JSON schema, hallucinating dates, outputting invalid markdown blocks.*
* **Subtotal: 30 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **9.1** | Initialize Gemini SDK. Handle authentication and API region quota limits. | `3 hr 00 min` |
| **9.2** | Deep Prompt Engineering: Define absolute strict JSON schemas. Use few-shot prompting with raw legal text examples. | `8 hr 00 min` |
| **9.3** | Output Validation: Implement `Pydantic` models to strictly validate the LLM output. Automatically re-prompt the LLM if validation fails. | `7 hr 00 min` |
| **9.4** | Mitigation Logic: Write business rules to cross-check LLM hallucinated dates/names against known facts. | `7 hr 00 min` |
| **9.5** | Full pipeline end-to-end stress test across 20 distinct voice transcriptions. | `5 hr 00 min` |

---
**Total Realistic Phase 0 POC Estimate: 215 Hours.**
