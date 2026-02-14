# Project Plan: Legal SaaS (Rajasthan + Central Pilot)

## Executive Summary
**Project Name**: NyayaTrack (Pilot Edition)
**Goal**: Automate case tracking for **Rajasthan & Central Courts** with Real-Time Alerts, Secure Data, and Subscription Management.
**Strategy**: **Broad POC First** (Validate all portals) -> **Secure Core Engine** (DPDP Compliant Scrapers).
**Timeline**: **18-20 Weeks** (4.5 - 5 Months).
**Budget**: **₹2.6L - ₹3.0L** (Development) + **~₹15k/mo** (Operational).

## Key Modules
1.  **Core Scrapers**: Rajasthan High Court (Live Board), eCourts (District), Revenue, Land, Supreme Court.
2.  **Security**: AES-256 Encryption for Case/User Data (DPDP Act).
3.  **Payments**: Razorpay Integration for Recurring Subscriptions.
4.  **Support**: Feedback Ticket System.
5.  **Ops**: Centralized Logger & Residential Proxy Manager.

## Roadmap Overview

| Phase | Duration | Focus Area | Deliverables |
| :--- | :--- | :--- | :--- |
| **Phase 0** | **Weeks 1-4** | **Broad POC** | Connectivity Proofs for eCourts, HC, Revenue, Land, WhatsApp, Payment, Encryption. |
| **Phase 1** | **Weeks 5-8** | **Secure Engine** | `AbstractScraper` Core + AES Encryption + Proxy Manager. |
| **Phase 2** | **Weeks 9-11** | **Backend Biz Logic**| Subscription (Razorpay), Auth (Consent Log), Support Module. |
| **Phase 3** | **Weeks 12-15**| **Intelligence** | Voice-to-Text Pipeline + Indian Kanoon RAG. |
| **Phase 4** | **Weeks 16-19**| **Frontend (PWA)** | Advocate Dashboard, Decrypted View, Ticket UI. |
| **Phase 5** | **Week 20**    | **Release** | Production Deploy (Docker/SSL), User Manuals. |
