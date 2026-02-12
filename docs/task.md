# Legal SaaS Tasks (Pan-India)

## Phase 0: Expanded POC - Feasibility Check
- [ ] **Setup & Config**
    - [ ] Repo Initialization (FastAPI + Playwright).
    - [ ] API Keys: OpenAI, 2Captcha, IndianKanoon.
    - [ ] WhatsApp Sandbox (Twilio/Meta).
- [ ] **Broad Integration Tests**
    - [ ] **eCourts (District)**: Fetch 1 Case Status.
    - [ ] **High Court (Rajasthan)**: Poll Live Display Board (Client-Side).
    - [ ] **Revenue/Land**: Fetch 1 `gcms` Case + 1 `apnakhata` Record.
    - [ ] **WhatsApp**: Send "Hello World" Template.
    - [ ] **Voice**: Transcribe 1 Sample Audio -> JSON.
    - [ ] **Legacy**: Fetch 1 Judgment from Indian Kanoon.
- [ ] **Demo**
    - [ ] End-to-End Flow (Mocked Data -> WhatsApp Alert).

## Phase 1: Universal Scraper Engine
- [ ] **Core Architecture**
    - [ ] `AbstractScraper` & `StateAdapter` Pattern.
    - [ ] Residential Proxy Manager.
- [ ] **Production Adapters**
    - [ ] **eCourts**: Universal District Scraper.
    - [ ] **Rajasthan**: Full implementation (HC + Revenue + Land).
    - [ ] **Delhi**: Full implementation (HC + District).

## Phase 2: Core Backend (User & Data)
- [ ] **Database Design**
    - [ ] Models: `Advocate`, `Case`, `Court` (Polymorphic).
- [ ] **Auth & Role Management**
    - [ ] Contributor vs Subscriber Logic.
    - [ ] Admin Dashboard API.
- [ ] **Subscription Module**
    - [ ] Payment Gateway Integration.

## Phase 3: Legal Intelligence
- [ ] **Voice Pipeline**
    - [ ] Audio Upload Endpoint.
    - [ ] Whisper Transcribe Service.
    - [ ] Gemini "Hinglish" Extractor.
- [ ] **RAG Engine**
    - [ ] Indian Kanoon API Wrapper.
    - [ ] "Similar Case" Search Logic.

## Phase 4: Frontend (Advocate PWA)
- [ ] **App Structure**
    - [ ] Mobile-First Layout (React/Vite).
- [ ] **Key Features**
    - [ ] "My Daily Board" (Unified List).
    - [ ] Client Alert Approval Flow.

## Phase 5: Deployment
- [ ] **Production Ops**
    - [ ] Docker Compose (App + Workers + DB).
    - [ ] Nginx & SSL.