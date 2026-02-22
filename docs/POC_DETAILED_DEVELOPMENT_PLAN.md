# Phase 0: Elaborate Proof of Concept (POC) Plan
*A granular, microscopic breakdown of the 9 foundational POC tasks. Designed to map exactly the actual engineering effort required to de-risk the Legal SaaS platform.*

**Total Estimated Phase 0 Effort:** 125 hours 0 minutes
**Budget Implication (@ ₹1,000 - ₹1,200/hr):** ₹1,25,000 – ₹1,50,000

---

## 1. Proof of Scraping (Websites, Captcha, Proxies)
*Goal: Prove consistent access to heavily guarded government portals.*
* **Subtotal: 35 hr 30 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **1.1** | Initialize Playwright Headless architecture & integrate Python proxy rotation script. | `4 hr 30 min` |
| **1.2** | Implement 2Captcha API wrappers and write failure/latency handling logic. | `5 hr 00 min` |
| **1.3** | Target 1: Script `services.ecourts` District Courts (bypass 5-char captcha). | `6 hr 30 min` |
| **1.4** | Target 2: Script `judgments.ecourts` (fetch & verify sample PDFs). | `5 hr 00 min` |
| **1.5** | Target 3: Implement `aiohttp` fast-polling logic for `hcraj` Live Display Board. | `4 hr 30 min` |
| **1.6** | Target 4: Form-posting scrapers for Revenue (`gcms`) and Land (`apnakhata`). | `7 hr 00 min` |
| **1.7** | End-to-end pipeline test across all 4 targets simultaneously to check proxy ban triggers. | `3 hr 00 min` |

---

## 2. Integration with WhatsApp APIs
*Goal: Transmit outgoing templates & handle standard incoming events without double-billing.*
* **Subtotal: 12 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **2.1** | Meta Developer Portal setup, number verification, and Template application. | `2 hr 30 min` |
| **2.2** | Build FastAPI webhook endpoints to handle incoming WhatsApp payloads. | `3 hr 30 min` |
| **2.3** | Deploy local Redis container specifically for caching recent sent-message hashes. | `2 hr 30 min` |
| **2.4** | Write the Python deduplication logic (check Redis hash before sending Meta request). | `2 hr 00 min` |
| **2.5** | End-to-end messaging test with live phone numbers. | `1 hr 30 min` |

---

## 3. Database Creation (DPDP Schema Base)
*Goal: Setup encrypted data store capable of AI Vector Search.*
* **Subtotal: 9 hr 30 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **3.1** | Local PostgreSQL environment setup with `pgvector` extension enabled. | `2 hr 00 min` |
| **3.2** | Draft SQLAlchemy models (User, Case, Subscription) including `consent_given` booleans. | `3 hr 30 min` |
| **3.3** | Initialize Alembic & run base schema database migrations. | `2 hr 00 min` |
| **3.4** | Write a database seeding script to inject 50 mock Advocate/Case records for UI testing. | `2 hr 00 min` |

---

## 4. Basic Dashboard (React Data Viewer)
*Goal: Tangible web portal to verify the scraped and processed data.*
* **Subtotal: 18 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **4.1** | React/Vite/Tailwind scaffolding & project structure initialization. | `2 hr 00 min` |
| **4.2** | Setup React Router, Context API, and global layout framing. | `3 hr 00 min` |
| **4.3** | Build the "Case Portfolio" data table component with simulated columns. | `5 hr 00 min` |
| **4.4** | Wire Axios/Fetch API calls strictly to the mock FastAPI endpoints. | `4 hr 00 min` |
| **4.5** | Basic responsive design polish (Mobile vs Desktop table adaptations). | `4 hr 00 min` |

---

## 5. Voice Input UI Component
*Goal: Enable Advocates to submit field intelligence intuitively.*
* **Subtotal: 9 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **5.1** | UI Component design (Microphone button, states: Standby/Recording/Review). | `2 hr 00 min` |
| **5.2** | Integration with browser `Web Audio API` (handle mic permissions, stream streaming). | `4 hr 00 min` |
| **5.3** | Blob generation & multipart/form-data upload handlers to transmit audio to Python. | `3 hr 00 min` |

---

## 6. Integration: Speech-to-Text Proof
*Goal: Accurately capture Hinglish legal dictation into strings.*
* **Subtotal: 9 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **6.1** | Create dedicated FastAPI `/api/voice/transcribe` file upload endpoint. | `2 hr 30 min` |
| **6.2** | Integrate OpenAI `Whisper` API client to parse the incoming temporary audio files. | `3 hr 30 min` |
| **6.3** | Run 10 benchmark test cases using deep Hindi + English code-switching. | `3 hr 00 min` |

---

## 7. Proof of RAG (Indian Kanoon & Judgments)
*Goal: Prove legal precedent similarity search via Vector Database.*
* **Subtotal: 17 hr 0 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **7.1** | Design logic to parse eCourts Judgment PDFs into smaller semantic text chunks. | `5 hr 00 min` |
| **7.2** | Integrate `text-embedding-3-small` OpenAI API to generate float arrays from chunks. | `3 hr 00 min` |
| **7.3** | Push generated vectors to PostgreSQL `pgvector` indices. | `4 hr 00 min` |
| **7.4** | Implement Cosine Distance SQL search query & return closest judgment paragraphs. | `5 hr 00 min` |

---

## 8. Basic Logger Module
*Goal: Professional, machine-readable audits for failing scrapers.*
* **Subtotal: 4 hr 30 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **8.1** | Install & inject `structlog` into the main application factory. | `1 hr 30 min` |
| **8.2** | Configure JSON formatting handlers so errors are serialized natively. | `1 hr 30 min` |
| **8.3** | Integrate FastAPI middleware to automatically log request/response cycles. | `1 hr 30 min` |

---

## 9. Basic Integration with LLM
*Goal: Convert unstructured text logs into structured JSON Case Objects.*
* **Subtotal: 10 hr 30 min**

| Subtask ID | Activity | Appx Duration |
| :--- | :--- | :--- |
| **9.1** | Setup primary Google Gemini 1.5 Pro/Flash SDK client. | `2 hr 00 min` |
| **9.2** | Rigorous Prompt Engineering (Zero-Shot & Few-Shot) to force strict JSON Schema outputs. | `4 hr 30 min` |
| **9.3** | Full pipeline test: Audio -> Whisper -> Prompt -> Gemini -> JSON output in Console. | `4 hr 00 min` |

---
**Total Phase 0 POC Estimate: 125 Hours.**
