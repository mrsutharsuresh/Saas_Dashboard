# Legal Intelligence & Case Tracking SaaS (Pan-India) - Comprehensive Requirements

## 1. Primary Objective
Building a scalable, AI-powered **Legal Practice Management Platform** for Indian Advocates. The system automates case tracking across federal and state judicial bodies, provides real-time alerts, and leverages crowdsourced intelligence.

## 2. Target Portals (Scope of Integration)

The platform must integrate with the following judicial systems. **Note**: Each portal has unique CAPTCHA and session handling mechanisms.

### A. Federal / Central Systems (Phased)
1.  **eCourts Services** (`services.ecourts.gov.in`):
    *   **Scope**: All District & Sessions Courts across India (Start with Rajasthan/Delhi).
    *   **Data Points**: CNR Number, Case Status, Next Hearing Date, Business.
2.  **Supreme Court of India** (`sci.gov.in`):
    *   **Scope**: Highest appellate cases.
3.  **Tribunals**: NCLT (`nclt.gov.in`), DRT, CAT (Phased rollout).

### B. State-Specific Systems (Pilot Phase)
**1. Rajasthan (Priority)**
*   **High Court**: `https://hcraj.nic.in/hcraj/`
    *   **Critical Feature**: Live Display Board (Real-Time Item Number Tracking).
*   **Revenue Courts**: `https://gcms.rajasthan.gov.in/`
    *   **Scope**: Revenue cases, appeals.
*   **Land Records**: `https://apnakhata.rajasthan.gov.in/`
    *   **Scope**: Jamabandi, Mutation Status.

**2. Delhi (Secondary Pilot)**
*   **High Court**: `https://delhihighcourt.nic.in/`
*   **Revenue**: `https://revenue.delhi.gov.in/`

---

## 3. User Personas & Detailed Workflows

### A. Admin (Superuser)
*   **Responsibility**: Monitor system health and revenue.
*   **Key Features**:
    *   **Scraper Dashboard**: View success rates of scraping jobs per state. (e.g., "Rajasthan HC: 98% Success", "UP Bhulekh: 50% Fail - Captcha Issue").
    *   **User Management**: Approve/Ban Advocates.
    *   **Subscription Plans**: Define tiers (Basic: District Only | Pro: HC + Revenue | Elite: Real-Time Alerts).

### B. Customer Advocate (Subscriber)
*   **Responsibility**: Track their case portfolio.
*   **Workflow**:
    1.  **Onboarding**: Selects State Bar Council ID.
    2.  **Add Case**: Enters CNR Number OR Advocate Name. System auto-populates list.
    3.  **Daily Routine**: Receives "Morning Brief" WhatsApp at 8 AM.
    4.  **Live Tracking**: If enabled, receives "Case Incoming" alert when item number is close.
    5.  **Intelligence**: Uses Search Bar to query "Similar Judgments" (RAG).

### C. Contributor Advocate (Source)
*   **Responsibility**: Provide ground-level intelligence (Crowdsourcing).
*   **Workflow**:
    1.  **Voice Note**: Records "Aaj court 5 mein judge sahab nahi aaye" via App.
    2.  **Verification**: System transcribes and cross-verifies with other inputs.
    3.  **Reward**: Earns credits for accurate, timely updates.

---

## 4. Automated Notification Workflow (Hinglish Standard)
*Channel: WhatsApp Business API (WABA)*

### A. Morning Brief (8:00 - 9:00 AM)
> **Template**:
> 📌 **NyayaTrack: Aaj ki Cause List ({Date})**
> Namaste Adv. {Name} ji, aaj aapke total {Count} cases scheduled hain:
>
> 1. **{Case_Title}** (Item {Item_No}) - {Court_Name}
> 2. **{Case_Title}** (Item {Item_No}) - {Court_Name}
>
> ⚖️ **Tip**: High Court wala case subah 10:30 par priority par hai.
> — Team NyayaTrack

### B. Real-Time Court Room Alert
> **Template**:
> ⚠️ **NYAYATRACK ALERT: Case Incoming!**
> Adv. {Name} ji, aapka case **Item No. {My_Item}** ({Court_Name}) abhi call hone wala hai.
>
> **Current Running Item: {Current_Item}**
> Kripya court room ke bahar ya andar maujood rahein.

### C. Evening Summary (6:00 - 7:00 PM)
> **Template**:
> ✅ **NyayaTrack: Aaj ka Progress Report**
> Aaj ke cases ka status:
>
> * **{Case_Title}**: Next Date - {Next_Date} ({Purpose})
> * **{Case_Title}**: Order Reserved.
>
> 📅 **Kal ke liye Alert**: Kal aapka ek Filing deadline hai "{Next_Day_Case}" case mein.
> Aapki digital file update kar di gayi hai.
> — Powered by NyayaTrack

---

## 5. Non-Functional Requirements (SLA & Compliance)

### A. Performance & Scalability
*   **Latency**: Real-Time Alerts must be delivered within **60 seconds** of change on the Display Board.
*   **Throughput**: System must handle **100 Concurrent Scrapers** without degradation.
*   **Uptime**: Target **99.5% Availability** during Court Hours (10 AM - 5 PM).

### B. Compliance & Legal
*   **Data Residency**: All Case Data & PII must be stored within **India (Mumbai Region)** servers (DPDP Act 2023).
*   **Consent**: Strict opt-in for tracking engaging parties.
*   **Scraping Ethics**: Respect `robots.txt` rate limits; Identify User-Agent as `NyayaTrack-Bot`.
