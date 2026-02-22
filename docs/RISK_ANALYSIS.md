# Risk Analysis & Feasibility Report

## 1. Scraping Roadblocks
**Risk**: Government portals often have CAPTCHAs, rate limiting, and IP bans.
*   **Captchas**: We rely on **2Captcha** given its proven ~90% success rate. *Risk*: Success rates may dip due to AI advancements introducing more complex captchas.
*   **IP Bans**: Scraper needs **Residential Proxies** (e.g., BrightData, Smartproxy) if requests > 100/day.
*   **UI/Structure Changes**: Government portal UI changes will result in scraper failure.
    *   **Mitigation**: Implement robust **Health Checks** connected to alert systems.

## 2. Voice AI Accuracy (Hinglish)
**Risk**: Mixed Hindi-English audio is hard for standard models.
*   **Solution**: **OpenAI Whisper (v3)** is currently the SOTA (State of the Art) for Indian accents and code-switching (Hinglish).
*   **Availability**:
    *   **API**: ~ $0.006/minute (Very cheap). Highly accurate.
    *   **Self-Hosted**: Requires GPU. Not recommended for MVP.
*   **Recommendation**: Use **OpenAI Whisper API** for STT. Use **Gemini 1.5 Flash** for extracting the JSON data from that text.

## 3. Database & File Storage
**Risk**: Storing PDFs/Images in PostgreSQL ("BLOBs") bloats the DB and kills performance.
*   **Strategy**: **Hybrid Storage**.
    *   **Structured Data** (Users, Projects, Tables): Goes into **PostgreSQL**.
    *   **Unstructured Data** (PDFs, Images): Goes into **Object Storage** (AWS S3 / DigitalOcean Spaces / MinIO).
    *   **Local MVP**: Save files to a `media/` folder on the disk.
    *   **Why**: S3 is infinitely scalable and cheap ($5/TB). Postgres is expensive to scale.

## 4. Privacy & Logs Deletion
**Risk**: Handling "Delete Account" requests securely.
*   **Fix**: Wipe data from DB + S3 Backups. Modifying logs is explicitly excluded as it's too tedious. Ensure Consent is captured explicitly in DB.

## 5. Scaling Bottlenecks
*   **Bottleneck 1: Database Connections**: usage spikes at 6 AM (Daily Brief).
    *   **Fix**: Use **PgBouncer** (Connection Pooling).
*   **Bottleneck 2: Scraper Memory**: Browser automation (Playwright) eats RAM (~500MB per tab).
    *   **Fix**: Queue system (Celery). Limit concurrent scrapes.

## 6. Hardware & Hosting Requirements
**Choice**: Use APIs (Gemini/OpenAI) to save GPU server costs.
**Recommended Config**:
*   DigitalOcean Droplet with 4-8GB RAM (Playwright needs RAM).
**Recommended Server Config (using APIs):**
*   **Provider**: DigitalOcean Droplet / AWS t3.medium
*   **Specs**:
    *   **CPU**: 2 vCPUs (For async requests)
    *   **RAM**: 4GB - 8GB (Playwright needs RAM)
    *   **Storage**: 50 GB NVMe (For Logs/Temp Files)
*   **Est. Cost**: $20 - $40 / month.
*   **Hostinger VPS**: "KVM 2" or "KVM 4" plans are suitable. Avoid Shared Hosting.
