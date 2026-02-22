# Project Plan: Legal SaaS (Rajasthan + Central Pilot)

## Executive Summary
**Project Name**: NyayaTrack (Pilot Edition)
**Goal**: Automate case tracking for **Rajasthan & Central Courts** with Real-Time Alerts, Secure Data, and Subscription Management.
**Strategy**: **Broad POC First** (Validate all portals) -> **Secure Core Engine** (DPDP Compliant Scrapers).
**Timeline**: **24-28 Weeks** (6 - 7 Months) based on a ~485-hour dev cycle.
**Budget**: **₹4.7L - ₹5.9L** (Development - Mid-Level Freelance Pod) + **~₹12k-₹15k/mo** (Operational).

## Key Modules
1.  **Core Scrapers**: Rajasthan High Court (Live Board), eCourts (District), Revenue, Land, Supreme Court.
2.  **Security**: AES-256 Encryption for Case/User Data (DPDP Act).
3.  **Payments**: Razorpay Integration for Recurring Subscriptions.
4.  **Support**: Feedback Ticket System.
5.  **Ops**: Centralized Logger & Residential Proxy Manager.

## Roadmap Overview

| Phase | Duration | Focus Area | Deliverables |
| :--- | :--- | :--- | :--- |
| **Phase 0** | **Weeks 1-5** | **Expanded POC (125 Hrs)** | 1. Scraping Proof (HC/Central/RJ) |
| | | | 2. WhatsApp API (w/ Deduplication) |
| | | | 3. Database Schema (pgvector) |
| | | | 4. Basic Dashboard UI |
| | | | 5. Voice Input UI Component |
| | | | 6. Whisper Speech-to-Text Proof |
| | | | 7. RAG Proof (Kanoon/Judgments) |
| | | | 8. Central Logger (`structlog`) |
| | | | 9. LLM Integration Proof (Gemini JSON) |
| **Phase 1** | **Weeks 6-9** | **Secure Engine** | `AbstractScraper` Core + AES Encryption + Proxy Manager + Auto-Healing. |
| **Phase 2** | **Weeks 10-12**| **Backend Core**| Subscription (Razorpay), Auth (Consent Schema), Support Tickets. |
| **Phase 3** | **Weeks 13-16**| **Intelligence** | Verified Voice-to-JSON Pipeline + Full RAG Search. |
| **Phase 4** | **Weeks 17-21**| **Frontend PWA** | Advocate Dashboard, Decrypted View, UI Polish. |
| **Phase 5** | **Weeks 22-23**| **Release/QA** | Production Deploy (Docker/SSL), Documentation & Handover. |
