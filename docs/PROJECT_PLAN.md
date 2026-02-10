# Project Development Plan & Roadmap (Mobile PWA + AI + SaaS)

## Phase 1: Core Scraper & Basic API
**Goal**: Validate we can scrape the target portal, extract data, and display it.
**Timeline**: Week 1-2

### Tasks
1.  **Repo Setup**: Initialize FastAPI (Backend) and React `mobile-pwa` (Frontend).
2.  **Scraper Core**: Playwright script for Government Portal 1.
    *   *Output*: JSON Data + PDF Download.
3.  **Basic API**: Endpoint `POST /scrape {id}`.

## Phase 2: Mobile PWA Foundation (Auth & CRUD)
**Goal**: A usable mobile app for the Professional + basic Admin tools.
**Timeline**: Week 3

### Tasks
1.  **Mobile UI Shell**: Bottom Navigation, "Add Record" FAB, "My Projects" List.
2.  **Auth System**: Login (JWT), Pin Code, Tenant Middleware.
3.  **Project Management**:
    *   API: Create/Read/Update/Delete Projects & Clients.
    *   UI: Forms for manual entry and list views.
    *   Conflict Logic: Compare new manual data vs old scraped data.
4.  **Admin Panel**: Basic view for System Stats (Total Users/Projects).
5.  **Voice Recorder Component**:
    *   Implement `MediaRecorder` API in React.
    *   Visualizer for audio input.
    *   Upload to Backend -> Save to Disk.

## Phase 3: The Intelligence Engine (AI & Drafts)
**Goal**: Process voice notes into data, automate scrapes, and manage notifications.
**Timeline**: Week 4-5

### Tasks
1.  **Audio Pipeline**: Connect Whisper (STT) + Gemini (Extraction).
2.  **Daily Brief Scheduler**: Cron Job (06:00 AM) to run scrapers.
3.  **Drafts Queue System**:
    *   DB Schema for `NotificationDraft` (Pending/Approved/Rejected).
    *   UI for Professional to "Swipe to Approve".
4.  **AI Summary**: Generate 3-bullet summary from Scraped PDFs.

## Phase 4: E-Library & Search
**Goal**: Manage documents.
**Timeline**: Week 6

### Tasks
1.  **Document Ingestion**: Parse PDFs to text.
2.  **Search API**: Implement Full-Text Search (Postgres `tsvector`).
3.  **Mobile Search UI**: Filters for Year, Category, ID.

## Phase 5: Polish & Notification Delivery
**Goal**: Production ready.
**Timeline**: Week 7

### Tasks
1.  **WhatsApp Integration**: Hook up "Approve" button to Meta API.
2.  **Offline Support**: Service Workers for PWA capabilities.
3.  **Security Audit**: Verify detailed PII encryption.

## Summary Roadmap (Detailed Schedule)

| Phase | Duration | Key Deliverable |
| :--- | :--- | :--- |
| **1. Scrapers** | 3 Weeks | Robust Portal Automations (Portals 1 & 2). |
| **2. Backend** | 2 Weeks | Secure API + Tenant DB Architecture. |
| **3. AI Core** | 3 Weeks | Voice Pipeline + Hinglish Tuning. |
| **4. Frontend** | 3 Weeks | Mobile PWA UI + Offline Config. |
| **5. E-Library** | 2 Weeks | RAG Search + PDF Processing. |
| **6. Deploy/QA** | 3 Weeks | Cloud Setup + UAT + Buffer. |
| **Total** | **~16 Weeks** | **Production Release** |

