# Risk Analysis & Feasibility Report

## 1. Scraping Roadblocks
**Risk**: Government portals often have CAPTCHAs, rate limiting, and IP bans.
*   **Captchas**: Simple text captchas can sometimes be solved by OCR (Tesseract). Complex ones (ReCaptcha/Cloudflare) require paid services like **2Captcha** or **CapSolver** (~$0.50 per 1000 solutions).
*   **IP Bans**: Scraper needs **Residential Proxies** (e.g., BrightData, Smartproxy) if requests > 100/day.
*   **Structure Changes**: If the Govt portal changes HTML, scraper fails.
    *   **Mitigation**: "Canary Tests" runs daily. If it fails, Admin gets an SMS/Email immediately.

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

## 4. Scaling Bottlenecks
*   **Bottleneck 1: Database Connections**: usage spikes at 6 AM (Daily Brief).
    *   **Fix**: Use **PgBouncer** (Connection Pooling) to handle 1000s of connections.
*   **Bottleneck 2: Scraper Memory**: Browser automation (Playwright) eats RAM (~500MB per tab).
    *   **Fix**: Queue system (Celery). Limit concurrent scrapes to `CPU_CORES * 2`.

## 5. Hardware & Hosting Requirements
**Decision**: Self-Host Models vs Use APIs?
*   **Choice**: **Use APIs** (Gemini/OpenAI).
    *   *Reason*: Running Whisper-Large + LLM requires ~24GB VRAM GPU ($500/mo server). APIs cost pay-as-you-go (~$10/mo).

**Recommended Server Config (using APIs):**
*   **Provider**: DigitalOcean Droplet / AWS t3.medium
*   **Specs**:
    *   **CPU**: 2 vCPUs (For async requests)
    *   **RAM**: 4GB - 8GB (Playwright needs RAM)
    *   **Storage**: 50 GB NVMe (For Logs/Temp Files)
*   **Est. Cost**: $20 - $40 / month.
*   **Hostinger VPS**: "KVM 2" or "KVM 4" plans are suitable. Avoid Shared Hosting.
