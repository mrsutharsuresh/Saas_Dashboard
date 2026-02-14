# Legal SaaS Tasks (Rajasthan + Central Pilot)

## Phase 0: Expanded POC - Feasibility Check
- [ ] **Setup & Config**
    - [ ] Repo Initialization (FastAPI + Playwright).
    - [ ] API Keys: OpenAI, 2Captcha, Razorpay.
    - [ ] **Logger Module**: `structlog` setup (Local File).
- [ ] **Integration Tests (Strict Scope)**
    - [ ] **eCourts Services**: Fetch 1 Rajasthan District Case.
    - [ ] **eCourts Judgments**: Fetch 1 Judgment PDF (`judgments.ecourts`).
    - [ ] **Supreme Court**: Fetch 1 SC Case Status.
    - [ ] **Rajasthan HC**: Poll Live Display Board (Client-Side).
    - [ ] **Revenue/Land**: Fetch 1 `gcms` + 1 `apnakhata` Record.
    - [ ] **Payment**: Create 1 Test Order on Razorpay.
    - [ ] **WhatsApp**: Send "Hello World" Template.
    - [ ] **Voice**: Transcribe 1 Sample Audio -> JSON.
    - [ ] **Legacy**: Fetch 1 Judgment from Indian Kanoon.
- [ ] **Demo**
    - [ ] End-to-End Flow (Mocked Data -> WhatsApp Alert).

## Phase 1: Core Engine & Security
- [ ] **Scraper Architecture**
    - [ ] `AbstractScraper` + `ProxyManager` (Residential IP Rotation).
- [ ] **Security Layer (DPDP Compliance)**
    - [ ] AES-256 Encryption Utility for DB.
- [ ] **Production Adapters**
    - [ ] **eCourts**: Universal District Scraper.
    - [ ] **Central**: Supreme Court Scraper.
    - [ ] **Rajasthan**: HC + Revenue + Land Scrapers.

## Phase 2: Backend, Payments & Support
- [ ] **Database Design**
    - [ ] Models: `Advocate`, `Case`, `Subscription`, `SupportTicket`.
- [ ] **Auth & Role Management**
    - [ ] Role Logic (Admin / Subscriber / Contributor).
    - [ ] JWT + Opt-in Consent Log.
    - [ ] **Data Erasure API** (DPDP Compliance).
    - [ ] Admin Dashboard API.
- [ ] **Subscription Module**
    - [ ] **Razorpay Integration** (Recurring Plans).
    - [ ] Invoice Generation Logic.
- [ ] **Support Module**
    - [ ] Ticket Creation API.
    - [ ] Admin Ticket View.

## Phase 3: Legal Intelligence
- [ ] **Voice Pipeline**
    - [ ] Audio Upload + Whisper + Gemini "Hinglish" Extractor.
- [ ] **RAG Engine**
    - [ ] Indian Kanoon API Wrapper.
    - [ ] Vector Search Logic.

## Phase 4: Frontend (Advocate PWA)
- [ ] **App Structure**
    - [ ] Mobile-First Layout (React/Vite).
- [ ] **Key Features**
    - [ ] "My Daily Board" (Decrypted View).
    - [ ] Support Ticket UI.
    - [ ] Subscription Management UI.

## Phase 5: Production & Docs
- [ ] **Deploy**
    - [ ] Docker Compose + Nginx + SSL.
- [ ] **Documentation**
    - [ ] Developer Guide.
    - [ ] User Manual (English/Hindi).