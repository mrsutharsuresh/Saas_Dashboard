# SaaS Dashboard Development Tasks

## Phase 1: Data Acquisition (Scrapers)
- [ ] **Portal Scraper Core**
    - [x] Base Scraper Engine (Stealth + Retry).
    - [ ] Portal 1 Script (Blocked on URL).
    - [ ] Portal 2 Script (Blocked on URL).

## Phase 2: Core Backend & API
- [/] **System Architecture**
    - [x] Database Models (User, Project, Client).
    - [x] Auth API (JWT, Register, Login).
    - [x] Project CRUD API.
    - [ ] Celery Task Queue Setup.

## Phase 3: AI Intelligence Layer
- [ ] **Voice Pipeline**
    - [ ] Whisper Integration (Audio -> Text).
    - [ ] Gemini Extract Logic (Text -> JSON).
- [ ] **RAG Engine**
    - [ ] PDF Parsing.
    - [ ] Vector Search Basic.

## Phase 4: Frontend (Mobile PWA)
- [/] **Core UI**
    - [x] Vite + Tailwind Setup.
    - [x] Auth Context & Private Routes.
    - [x] Login & Register Screens.
    - [x] Dashboard & Project List.
    - [ ] Audio Recorder Component.

## Phase 5: Deployment & QA
- [ ] **Infrastructure**
    - [ ] Docker Compose Setup.
    - [ ] Nginx Reverse Proxy.
    - [ ] CI/CD Pipeline.