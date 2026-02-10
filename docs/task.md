# SaaS Dashboard Development Tasks

## Phase 1: Core Scraper & Basic API
- [ ] **Repo Setup**
    - [ ] Initialize FastAPI (Backend).
    - [ ] Initialize React (`mobile-pwa`) with Vite + Tailwind + ShadCN.
- [ ] **Scraper Core**
    - [ ] Playwright script for Government Portal 1.
    - [ ] Extract JSON Data + PDF Download.
- [ ] **Basic API**
    - [ ] Endpoint `POST /scrape {id}`.

## Phase 2: Mobile PWA Foundation (Auth & CRUD)
- [ ] **Mobile UI Shell**
    - [ ] Bottom Navigation Layout.
    - [ ] "Add Record" FAB.
- [ ] **Auth System**
    - [ ] Login Screen (JWT).
    - [ ] Tenant Middleware.
- [ ] **Project Management**
    - [ ] API: Create/Read/Update/Delete Projects.
    - [ ] UI: Forms & Grid View.
- [ ] **Admin Panel**
    - [ ] System Stats Dashboard.
- [ ] **Voice Recorder Component**
    - [ ] Implement `MediaRecorder` API.
    - [ ] Audio Visualization.

## Phase 3: The Intelligence Engine (AI & Drafts)
- [ ] **Audio Pipeline**
    - [ ] Whisper integration (STT).
    - [ ] Gemini extraction (JSON).
- [ ] **Drafts Queue System**
    - [ ] DB Schema for `NotificationDraft`.
    - [ ] "Swipe to Approve" User Interface.
- [ ] **Daily Brief Scheduler**
    - [ ] Cron Job (06:00 AM).
    - [ ] Change Detection Logic.

## Phase 4: E-Library & Search
- [ ] **Document Ingestion**
    - [ ] PDF to Text parser.
- [ ] **Search API**
    - [ ] Postgres Full-Text Search implementation.
- [ ] **Mobile Search UI**
    - [ ] Filter interface (Year, Category).

## Phase 5: Polish & Notification Delivery
- [ ] **WhatsApp Integration**
    - [ ] Approve Button -> Meta API connection.
- [ ] **Offline Support**
    - [ ] Service Worker configuration.
- [ ] **Security Audit**
    - [ ] PII Encryption verification.
