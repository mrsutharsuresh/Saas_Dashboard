# Phase 0: Elaborate Proof of Concept (POC) Plan - Granular Breakdown
*A microscopic, hour-level breakdown of the 9 foundational POC tasks. This aggressively factors in real-world roadblocks (Cloudflare, Web Audio API bugs, Meta Rejections, LLM Tuning) and provides actionable developer checklists.*

**Total Realistic Phase 0 Effort:** 215 hours 0 minutes
**Budget Implication (@ ₹1,000 - ₹1,200/hr):** ₹2,15,000 – ₹2,58,000

---

## 1. Proof of Scraping (Websites, Captcha, Proxies)
*Goal: Prove consistent access to heavily guarded government portals.*
* **Subtotal: 62 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **1.1** | Initialize Playwright stealth architecture | - Setup Headless Chrome environment and Python async bindings (`1h`)<br>- Implement Playwright-stealth to strip `webdriver` flags (`2h`)<br>- Inject custom Canvas/WebGL fingerprint spoofing (`2h`)<br>- Randomize User-Agent, Navigator language, and Viewport arrays (`1h`) | `6 hr 00 min` |
| **1.2** | Integrate Residential Proxy pool | - API integration with proxy provider to fetch active IP nodes/ports (`2h`)<br>- Write middleware to intercept `403 Forbidden` and `429 Too Many Requests` (`3h`)<br>- Implement IP rotation and ban-detection sliding window (`2h`)<br>- Setup logging to monitor and map consumed proxy bandwidth (`1h`) | `8 hr 00 min` |
| **1.3** | Implement 2Captcha API wrappers | - Build async request wrapper to post image payload to 2Captcha API (`2h`)<br>- Write polling logic (10s intervals) to fetch solved text (`1h 30m`)<br>- Handle API timeout, empty responses, and exponential backoff (`1h 30m`)<br>- Implement "Report Incorrect Solution" logic for refunds/retry (`1h`) | `6 hr 00 min` |
| **1.4** | Target 1: `services.ecourts` District Courts | - Analyze network tab to identify invisible session cookies/tokens (`2h`)<br>- Automate capturing the 5-char captcha element as base64 and send to 2Captcha (`2h 30m`)<br>- Inject solution, post JS form, and await DOM table render (`2h`)<br>- Parse HTML tables into structured JSON arrays for Case Data (`2h`) | `8 hr 30 min` |
| **1.5** | Target 1.B: Handle eCourts downtime | - Identify standard HTML structure for "Server Too Busy" custom responses (`1h`)<br>- Implement exponential backoff queue to pause scraper execution (`2h`)<br>- Trigger secure admin alerts (Log/Webhook) on max retries exceeded (`1h`) | `4 hr 00 min` |
| **1.6** | Target 2: `judgments.ecourts` | - Automate site navigation to target Judgment Query page (`2h`)<br>- Extract true PDF link hidden behind iframe viewer structures (`2h`)<br>- Download PDF buffer memory stream and validate byte integrity (`1h 30m`)<br>- Handle reset connections and corrupted 0-byte downloads (`1h`) | `6 hr 30 min` |
| **1.7** | Target 3: `hcraj` Live Display Board | - Inspect WebSocket/polling XHR requests for real-time board updates (`2h`)<br>- Write `aiohttp` loop to poll every 15s without triggering generic DDOS alerts (`2h`)<br>- Implement socket disconnect and auto-reconnect fallback (`2h`) | `6 hr 00 min` |
| **1.8** | Target 4: Revenue (`gcms`) / Land (`apnakhata`) | - Reverse engineer dynamic CSRF tokens injected into initial DOM response (`3h`)<br>- Map required headers (Referer, Origin, strict MIME types) for form posting (`2h`)<br>- Handle multi-step post-back flows (Page 1 -> Submit -> Page 2 -> Scrape) (`4h`) | `9 hr 00 min` |
| **1.9** | End-to-end stress test across 4 targets | - Write `asyncio.gather` pipeline to run all 4 targets simultaneously (`3h`)<br>- Enforce proxy context isolation to prevent cookie cross-contamination (`3h`)<br>- Compile success/failure logs into an execution benchmark report (`2h`) | `8 hr 00 min` |

---

## 2. Integration with WhatsApp APIs
*Goal: Transmit outgoing templates & handle standard incoming events without double-billing.*
* **Subtotal: 21 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **2.1** | Meta Portal setup & Template approval | - Create Meta App, configure test mobile numbers, and generate Permanent Access Tokens (`1h 30m`)<br>- Draft 3 core business template JSONs (Alert, Welcome, Error) (`1h`)<br>- Submit templates for review and handle arbitrary rejection revisions (`1h 30m`) | `4 hr 00 min` |
| **2.2** | Build FastAPI webhook endpoints | - Setup POST endpoint for Meta callback verification challenge (`1h 30m`)<br>- Parse incoming user messages (Status updates vs Text messages) (`1h 30m`)<br>- Implement SHA256 header signature validation to prevent spoofed calls (`1h 30m`) | `4 hr 30 min` |
| **2.3** | Deploy local Redis container | - Scaffold `docker-compose.yml` for Redis Alpine image (`1h`)<br>- Configure persistent volume storage (`1h`)<br>- Set up PyRedis connection pooling within FastAPI dependencies (`1h 30m`) | `3 hr 30 min` |
| **2.4** | Python deduplication logic | - Generate unique hash based on `[Phone_Number + Case_ID + Status]` (`1h 30m`)<br>- Check Redis Key / Execute SETNX before firing WhatsApp Template (`2h`)<br>- Handle race conditions via Redis Locks when two scrapers trigger simulataneously (`1h 30m`) | `5 hr 00 min` |
| **2.5** | End-to-end messaging test | - Trigger mock scenario sending 10 template alerts within 1 minute (`1h 30m`)<br>- Verify Redis successfully drops duplicate hashes (`1h 30m`)<br>- Debug webhook delivery receipts (Sent, Delivered, Read) (`1h`) | `4 hr 00 min` |

---

## 3. Database Creation (DPDP Schema Base)
*Goal: Setup encrypted data store capable of AI Vector Search.*
* **Subtotal: 13 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **3.1** | PostgreSQL + `pgvector` setup | - Initialize local DB container enforcing `pgvector` installation (`1h`)<br>- Configure connection pooling (`pgBouncer` defaults) for FastAPI async (`1h 30m`)<br>- Setup separate schemas (Public vs Auth) for data security (`1h`) | `3 hr 30 min` |
| **3.2** | Draft SQLAlchemy models | - Define User & Subscription tables with strict PII limitations (`1h 30m`)<br>- Define Case table with `JSONB` for unstructured web data (`1h`)<br>- Embed mandatory `consent_given` and `encryption_salt` columns for DPDP (`1h 30m`) | `4 hr 00 min` |
| **3.3** | Initialize Alembic migrations | - Setup dynamic `alembic.ini` configuration connecting to local async DB (`1h`)<br>- Generate initial revision and test up/down migration paths (`1h 30m`) | `2 hr 30 min` |
| **3.4** | Database seeding script | - Generate 50 mock advocates and cases respecting strong Foreign Keys (`1h 30m`)<br>- Optimize script for bulk-inserts rather than row-by-row commits (`1h 30m`) | `3 hr 00 min` |

---

## 4. Basic Dashboard (React Data Viewer)
*Goal: Tangible web portal to verify the scraped and processed data.*
* **Subtotal: 24 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **4.1** | React/Vite scaffolding & Typescript | - Initialize Vite React-TS and strip barebones CSS (`1h`)<br>- Configure TailwindCSS and ShadCN basic UI theme (`1h 30m`)<br>- Write strict TS generic interfaces for Case JSON payloads (`1h 30m`) | `4 hr 00 min` |
| **4.2** | Setup React Router & Context | - Implement browser routing for `/dashboard` and `/login` (mock) (`1h 30m`)<br>- Wrap App in Context API to hold simulated user/auth state (`1h 30m`) | `3 hr 00 min` |
| **4.3** | Build "Case Portfolio" table | - Build UI Table component with dynamic columns based on court type (`2h`)<br>- Integrate `tanstack/react-table` for headless virtualization (`3h`)<br>- Add client-side row sorting and fuzzy-text filtering (`2h`) | `7 hr 00 min` |
| **4.4** | Axios/Fetch integration | - Create modular Axios instance with base URL mappings (`1h 30m`)<br>- Add global request/response interceptors to handle 401s and 500s (`2h`)<br>- Write hook (`useCases`) to fetch data and manage loading/error states (`1h 30m`) | `5 hr 00 min` |
| **4.5** | Mobile-responsive adaptations | - Hide non-essential table columns on small screens (`md:hidden`) (`2h`)<br>- Test layout on Chrome/Safari inspector for layout breakdown anomalies (`1h 30m`)<br>- Implement custom scrollbars for overflowing table div (`1h 30m`) | `5 hr 00 min` |

---

## 5. Voice Input UI Component
*Goal: Enable Advocates to submit field intelligence intuitively.*
* **Subtotal: 16 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **5.1** | UI Component state machine | - Design Mic Button component mapping 5 specific states (Idle, Requesting, Recording, Review, Uploading) (`2h`)<br>- Build pulsating CSS animations for active recording state (`1h 30m`) | `3 hr 30 min` |
| **5.2** | `Web Audio API` cross-browser integration | - Write `navigator.mediaDevices.getUserMedia` wrapper (`1h 30m`)<br>- Handle explicit user denials / browser blocking with graceful UI alerts (`2h`)<br>- Engineer fallback polyfills for strict iOS Safari audio constraints (`2h`) | `5 hr 30 min` |
| **5.3** | Audio constraints & file limits | - Apply client-side auto-gain and noise suppression constraint flags (`1h 30m`)<br>- Track buffer array size in real-time, enforcing a 3-minute hard-stop (`1h 30m`) | `3 hr 00 min` |
| **5.4** | Blob -> FormData transmission | - Convert raw MediaRecorder buffer chunks into `.webm` Blob (`1h 30m`)<br>- Construct `multipart/form-data` payload containing Blob and User ID (`1h`)<br>- Implement upload progress bar intercepting network disconnects (`1h 30m`) | `4 hr 00 min` |

---

## 6. Integration: Speech-to-Text Proof
*Goal: Accurately capture Hinglish legal dictation into strings.*
* **Subtotal: 12 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **6.1** | FastAPI Transcribe Endpoint | - Implement `/api/voice/transcribe` utilizing `UploadFile` (`1h`)<br>- Read incoming file stream in chunks (to prevent RAM spike) and write to `/tmp` (`1h 30m`)<br>- Auto-delete `/tmp` audio securely after processing (`1h`) | `3 hr 30 min` |
| **6.2** | OpenAI `Whisper` API wrapper | - Integrate official OpenAI Python SDK connection (`1h`)<br>- Post Audio buffer strictly selecting `whisper-1` model (`1h`)<br>- Build retry (`tenacity`) loops specifically for `502 Bad Gateway` API errors (`1h 30m`) | `3 hr 30 min` |
| **6.3** | Dictation benchmark tests | - Compile 10 distinct audio files of Hindi/English courtroom phrasing (`2h`)<br>- Process via pipeline and identify systemic hallucination words (`2h`)<br>- Test `ffmpeg` pre-processing (normalize volume) if initial tests fail (`1h`) | `5 hr 00 min` |

---

## 7. Proof of RAG (Indian Kanoon & Judgments)
*Goal: Prove legal precedent similarity search via Vector Database.*
* **Subtotal: 29 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **7.1** | Advanced PDF parsing | - Ingest pure text layer PDFs via `PyMuPDF` (`2h`)<br>- Detect scanned images and pipe to `pytesseract` OCR only if necessary (`3h`)<br>- Strip watermarks, headers, and pagination footers cleanly (`3h`) | `8 hr 00 min` |
| **7.2** | Semantic chunking strategy | - Implement Langchain `RecursiveCharacterTextSplitter` (`2h`)<br>- Tune chunk-overlap limits to prevent splitting legal precedent logic mid-sentence (`2h`)<br>- Append parent case metadata blocks to each isolated chunk (`2h`) | `6 hr 00 min` |
| **7.3** | Connect `text-embedding-3-small` | - Wrap OpenAI Embeddings API request handler (`1h`)<br>- Batch chunks array (max limits) to reduce outbound HTTP handshakes (`2h`)<br>- Detect Token-Limit-Exceeded errors and automatically re-chunk target string (`2h`) | `5 hr 00 min` |
| **7.4** | Store chunks in `pgvector` | - Define Vector SQLAlchemy Column storing Float dimensions (`1h`)<br>- Insert array payload and textual chunks natively into DB table (`2h`)<br>- Implement IVF-Flat/HNSW `pgvector` indexing structure (`2h`) | `5 hr 00 min` |
| **7.5** | Cosine Distance queries | - Write raw SQL `ORDER BY embedding <-> '[query]' LIMIT X` function (`2h`)<br>- Dynamically test threshold cut-offs to reject completely irrelevant matches (`1h 30m`)<br>- Package DB response into JSON format containing Paragraph text & Case source (`1h 30m`) | `5 hr 00 min` |

---

## 8. Basic Logger Module
*Goal: Professional, machine-readable audits for failing scrapers.*
* **Subtotal: 8 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **8.1** | Inject `structlog` & Context | - Override default Python `logging` and setup `structlog` JSON renderer (`1h`)<br>- Generate UUID for each request/scraper job. Bind UUID context globally (`1h 30m`)<br>- Push logs synchronously to StdOut (for Docker consumption) (`30m`) | `3 hr 00 min` |
| **8.2** | Masking Processors (DPDP) | - Write regex processors to sniff and obfuscate 10-digit phone numbers in payload (`1h 30m`)<br>- Write dictionary filter to drop keys like `"password"` or `"token"` from JSON dumps (`1h 30m`) | `3 hr 00 min` |
| **8.3** | Log file rotation | - Add `logging.handlers.RotatingFileHandler` interceptor (`1h`)<br>- Restrict max file size to 50MB and keep max 5 backups (`1h`) | `2 hr 00 min` |

---

## 9. Basic Integration with LLM
*Goal: Convert unstructured text logs into structured JSON Case Objects.*
* **Subtotal: 30 hr 0 min**

| ID | Primary Activity | Granular Sub-tasks | Appx Total |
| :--- | :--- | :--- | :--- |
| **9.1** | Initialize Gemini SDK | - Connect `google-generativeai` package (`1h`)<br>- Setup configuration settings (Temperature 0.0, JSON output mime-types) (`1h`)<br>- Map rate-limit backoffs mapping to GCP free/paid tiers (`1h`) | `3 hr 00 min` |
| **9.2** | Deep Prompt Engineering | - Design strictly typed JSON schema prompt defining `Case`, `Next Date`, etc. (`1h 30m`)<br>- Embed 3 Few-Shot examples (Raw Text -> Desired JSON) into system context (`4h 30m`)<br>- Tune instructions avoiding Markdown backticks in raw API response (`2h`) | `8 hr 00 min` |
| **9.3** | Output Validation (Pydantic) | - Author Python Pydantic classes mirroring the expected Gemini JSON response (`2h`)<br>- Intercept Gemini output, `json.loads()`, and validate via Pydantic (`2h 30m`)<br>- If `ValidationError`, append error to prompt and force Gemini to self-correct (`2h 30m`) | `7 hr 00 min` |
| **9.4** | Mitigation Logic & Integrity | - Regex logic to ensure `Next Date` string parsed by AI matches `YYYY-MM-DD` natively (`2h`)<br>- Cross-check algorithm ensuring AI generated Case Type exists in a known enum list (`2h`)<br>- Abort & flag for manual review if AI hallucinates impossible future years (`3h`) | `7 hr 00 min` |
| **9.5** | Full pipeline stress test | - Pass 20 distinct Whisper transcript excerpts to the logic chain (`2h`)<br>- Verify DB ingestion completes strictly matching the expected schemas (`2h`)<br>- Aggregate JSON validation errors to identify edge-case tuning needs (`1h`) | `5 hr 00 min` |

---
**Total Realistic Phase 0 POC Estimate: 215 Hours.**
