# Project Development Plan & Roadmap

## Overview
This document breaks down the development of the SaaS Dashboard into distinct, verifiable phases. The goal is to reach a "Proof of Concept" (POC) quickly to validate the core value proposition (Scraping + Updates), followed by a robust MVP build.

---

## Phase 1: Proof of Concept (POC) - The "Vertical Slice"
**Goal**: Validate we can scrape the target portal, extract data, and display it.
**Timeline**: Week 1-2

### Tasks
1.  **Repo Setup**: Initialize FastAPI (Backend) and React/Vite (Frontend).
2.  **Scraper Core**: Write the Python Playwright script to login and scrape *one* specific record from the Government Portal.
    *   *Verifiable Output*: A script that outputs JSON + PDFs for a given ID.
3.  **Basic API**: Create an endpoint `POST /scrape {id}` that triggers the script and returns the result.
4.  **Minimal UI**: A single page app where you input an ID and see the Scraped Data + Link to PDF.

---

## Phase 2: MVP Foundation & Multi-Tenancy
**Goal**: Turn the POC into a real SaaS linking Professionals to Projects.
**Timeline**: Week 3-4

### Tasks
1.  **Auth System**: Implement JWT Authentication.
    *   *Roles*: Super Admin, Professional.
2.  **Database Design**:
    *   Implement `Tenants` (Professionals).
    *   Implement `Projects` (The records being tracked).
    *   Implement `EndClients` (The people receiving updates).
3.  **CRUD Dashboard**: A "Grid View" for Professionals to see all their tracked projects.

---

## Phase 3: The "Daily Brief" Engine
**Goal**: Automate the checking process at scale.
**Timeline**: Week 5

### Tasks
1.  **Task Queue**: Set up Celery + Redis.
2.  **Scheduler**: Configure the 06:00 AM Cron Job.
3.  **Diff Logic**: Implement the "Change Detector".
    *   *Logic*: `if new_status != old_status: mark_as_changed()`.
4.  **Worker Scaling**: Ensure we can run 50+ scrapes in parallel without crashing.

---

## Phase 4: Intelligence & Notifications
**Goal**: Close the loop with the End-Client.
**Timeline**: Week 6

### Tasks
1.  **AI Summary**: Send scraped PDF text to Google Gemini -> Get 3-bullet summary.
2.  **WhatsApp API**: Connect Meta Graph API.
3.  **Pipeline**:
    *   *Trigger*: Change Detected.
    *   *Action*: Generate Summary -> Format WhatsApp Msg -> Send.

---

## Phase 5: Polish & Launch Readiness
**Goal**: Make it look and feel like a premium SaaS.
**Timeline**: Week 7

### Tasks
1.  **UI Polish**: Apply "Glassmorphism" design, loading skeletons, and responsive mobile view.
2.  **Security Audit**: Verify PII encryption.
3.  **Deployment**: Dockerize everything (Web, Worker, DB, Redis) and deploy to Staging.

---

## Summary Roadmap

| Phase | Duration | Key Deliverable |
| :--- | :--- | :--- |
| **1. POC** | 2 Weeks | Working Scraper + Raw Data JSON |
| **2. MVP Core** | 2 Weeks | User Login + Project List |
| **3. Automation** | 1 Week | Daily Auto-Updates working |
| **4. AI + Notif** | 1 Week | WhatsApp messages flowing |
| **5. Polish** | 1 Week | Production-ready Design |
| **Total** | **~7 Weeks** | **Version 1.0 Launch** |
