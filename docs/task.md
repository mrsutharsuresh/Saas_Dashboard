# SaaS Dashboard Development Tasks

## Phase 1: Proof of Concept (POC) - The "Vertical Slice"
- [ ] **Scraper Prototype**
    - [ ] Set up Python/Playwright environment.
    - [ ] Implement robust login/nav logic for the target government portal.
    - [ ] handle CAPTCHA (manual intervention or solver integration for POC).
    - [ ] Extract raw data for a single record ID.
- [ ] **Basic API & DB**
    - [ ] Initialize FastAPI project with PostgreSQL connection.
    - [ ] Create basic `Project` model.
    - [ ] Create endpoint to trigger scraper and return JSON.
- [ ] **Simplified UI**
    - [ ] Initialize React/Vite project.
    - [ ] Create a simple input form (Record ID) and result display.

## Phase 2: MVP Foundation & Multi-Tenancy
- [ ] **Authentication System**
    - [ ] Implement JWT Auth (Login, Register, Password Reset).
    - [ ] Middleware for Tenant Isolation (Row Level Security logic).
- [ ] **Database Schema Refinement**
    - [ ] Design comprehensive schemas: `Tenant`, `EndClient`, `Project`, `AuditLog`.
    - [ ] Run migrations.
- [ ] **Project Management CRUD**
    - [ ] API endpoints for Create, Read, Update, Delete Projects.
    - [ ] UI for "My Projects" grid view.

## Phase 3: The "Daily Brief" Engine (Workers)
- [ ] **Task Queue Infrastructure**
    - [ ] Set up Redis and Celery (or ARQ).
    - [ ] Configure Worker Docker container.
- [ ] **Change Detection Logic**
    - [ ] Implement `DiffService` to compare new scrape vs. old DB state.
    - [ ] Event emission: `UpdateDetected`.
- [ ] **Scheduler**
    - [ ] Configure cron for 6:00 AM daily run.
    - [ ] Implement batching (e.g., process 10 records at a time to respect rate limits).

## Phase 4: Intelligence & Notifications
- [ ] **AI Summarizer**
    - [ ] Integrate Google Gemini API.
    - [ ] Implement prompt engineering for "3-bullet summary".
    - [ ] Handle PDF text extraction.
- [ ] **WhatsApp Integration**
    - [ ] Set up Meta Graph API client.
    - [ ] Create Message Templates and get approval.
    - [ ] Implement "Send Notification" worker task.

## Phase 5: Dashboard Polish & Admin
- [ ] **UI/UX Refinement**
    - [ ] Implement "Premium" Glassmorphism design system.
    - [ ] Add loading states, toasts, and error handling.
- [ ] **Admin Panel**
    - [ ] Super-Admin view for system stats (Total Projects, Scraper Success Rate).
- [ ] **Client Visibility**
    - [ ] (Optional) Read-only view for end-clients if they click a link.

## Phase 6: Production Readiness
- [ ] **Security Review**
    - [ ] Audit PII encryption.
    - [ ] Penetration testing (basic).
- [ ] **DevOps**
    - [ ] Docker Compose for production.
    - [ ] CI/CD pipeline (GitHub Actions).
    - [ ] Load Testing (Simulate 1000 concurrent tasks).
