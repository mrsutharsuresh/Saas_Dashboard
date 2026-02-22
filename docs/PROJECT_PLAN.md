# Project Plan: Legal SaaS (Rajasthan + Central Pilot)

## Executive Summary
**Project Name**: NyayaTrack (Pilot Edition)
**Goal**: Automate case tracking for **Rajasthan & Central Courts** with Real-Time Alerts, Secure Data, and Subscription Management.
**Strategy**: **Broad POC First** (Validate all portals) -> **Secure Core Engine** (DPDP Compliant Scrapers).
**Timeline**: **32-36 Weeks** (8 - 9 Months) based on a completely reality-adjusted ~885-hour dev cycle.
**Budget**: **₹8.8L - ₹10.6L** (Development - Mid-Level Freelance Pod) + **~₹15k-₹20k/mo** (Operational / AI APIs).

## Key Modules
1.  **Core Scrapers**: Rajasthan High Court (Live Board), eCourts (District), Revenue, Land, Supreme Court.
2.  **Security**: AES-256 Encryption for Case/User Data (DPDP Act).
3.  **Payments**: Razorpay Integration for Recurring Subscriptions.
4.  **Support**: Feedback Ticket System.
5.  **Ops**: Centralized Logger & Residential Proxy Manager.

## Roadmap Overview

| Phase | Duration | Focus Area | Deliverables |
| :--- | :--- | :--- | :--- |
| **Phase 0** | **Weeks 1-5** | **Expanded POC (215 Hrs)** | 1. Scraping Proof (HC/Central/RJ) |
| | | | 2. WhatsApp API (w/ Deduplication) |
| | | | 3. Database Schema (pgvector) |
| | | | 4. Basic Dashboard UI |
| | | | 5. Voice Input UI Component |
| | | | 6. Whisper Speech-to-Text Proof |
| | | | 7. RAG Proof (Kanoon/Judgments) |
| | | | 8. Central Logger (`structlog`) |
| | | | 9. LLM Integration Proof (Gemini JSON) |
| **Phase 1** | **Weeks 6-11** | **Secure Engine** | Cloudflare Bypasses + KMS Proxy Manager + Auto-Healing. |
| **Phase 2** | **Weeks 12-16**| **Backend Core**| Strict Auth (Hard Delete), DB Partitions, DLQ WABA Alerts. |
| **Phase 3** | **Weeks 17-21**| **Intelligence** | Hallucination Mitigation + Hybrid RAG Search (Vector+Keyword). |
| **Phase 4** | **Weeks 22-28**| **Frontend PWA** | WebSockets UI, Infinite Scroll Portfolio, Offline Caching Service Workers. |
| **Phase 5** | **Weeks 29-34**| **Release/QA** | Kubernetes/Swarm CI/CD, Chaos Engineering Tests (500 Scrapers). |
