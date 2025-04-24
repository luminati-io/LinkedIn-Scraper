# Linkedin Scraper

[![Promo](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/Proxies%20and%20scrapers%20GitHub%20bonus%20banner.png)](https://brightdata.com/products/web-scraper/linkedin) 

This repository provides two methods for collecting data from LinkedIn:
1. **Free**: A great option for small-scale projects, experiments, and learning purposes.
2. **LinkedIn Scraper API**: Designed for large-scale, reliable, and real-time data extraction.

Want to skip scraping? Purchase the full [LinkedIn dataset](https://brightdata.com/products/datasets/linkedin).

## Table of Contents
- [Method 1: Free LinkedIn Scraper](#method-1-free-linkedin-scraper)
    - [Jobs Scraper](#1-jobs-scraper)
    - [Profile Checker](#2-profile-checker)
    - [Quick Start](#quick-start)
    - [Usage Examples](#usage-examples)
- [Common Scraping Challenges with Free Method](#common-scraping-challenges-with-free-method)
- [Method 2: Bright Data LinkedIn Scraper API](#method-2-bright-data-linkedin-scraper-api)
    - [Key Benefits](#key-benefits)
- [Getting Started with the LinkedIn Scraper API](#getting-started-with-the-linkedin-scraper-api)
  - [1. Company Information Scraper](#1-company-information-scraper)
  - [2. Profile by URL](#2-profile-by-url)
  - [3. Profile Discovery](#3-profile-discovery)
  - [4. Posts by URL](#4-posts-by-url)
  - [5. Posts Discovery by URL](#5-posts-discovery-by-url)
  - [6. Posts Discovery by Profile](#6-posts-discovery-by-profile)
  - [7. Posts Discovery by Company](#7-posts-discovery-by-company)
  - [8. Job Listings Collection by URL](#8-job-listings-collection-by-url)
  - [9. Job Listings Discovery by Keyword](#9-job-listings-discovery-by-keyword)
  - [10. Job Listings Discovery by URL](#10-job-listings-discovery-by-url)
- (More info) [Data Collection Approaches](#data-collection-approaches)

## Method 1: Free LinkedIn Scraper
This free tool provides two primary functionalities:
1. **LinkedIn Jobs Scraper**: Collection of job listings with comprehensive metadata
2. **LinkedIn Profile Validator**: Verification of LinkedIn profile and company URLs

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin-jobs" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin-jobs.png" />

### 1. Jobs Scraper
Collects job listings from LinkedIn's job search.

**Key features**:
- Scrapes detailed job listings (title, company, location, URL, posting date)
- Built-in rate limiting & error handling
- Clean JSON output

### 2. Profile Checker
Verify whether LinkedIn profiles or company pages exist.

**Key features**:
- Checks profile/company URLs
- Retries failed requests automatically
- Shows detailed status for each URL
- Can check multiple URLs at once

### Quick Start
Let's get you up and running in minutes:

#### Prerequisites
- Python 3.9 or newer
- Required packages listed in [requirements.txt](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/requirements.txt)

#### Installation
Three simple steps to get started:
```bash
git clone https://github.com/luminati-io/LinkedIn-Scraper.git
cd LinkedIn-Scraper
pip install -r requirements.txt
```
### Usage Examples
Here's how to put the scrapers to work:

#### 1. Jobs Scraper
Configure search parameters:
```python
# In jobs_scraper.py
params = {
    "keywords": "AI/ML Engineer",  # Job title/keywords to search
    "location": "London",          # Location to search in
    "max_jobs": 100               # Maximum number of jobs to collect
}

# Run: python jobs_scraper.py
```

The scraper creates a JSON file with job details:
```json
{
    "title": "Research Engineer, AI/Machine Learning",
    "company": "Google",
    "location": "London, England, United Kingdom",
    "job_link": "https://uk.linkedin.com/jobs/view/research-engineer-ai-machine-learning-at-google-4086259724",
    "posted_date": "3 weeks ago",
}
```

#### 2. Profile Checker
Configure URLs for validation:
```python
# In profile_checker.py
test_urls = [
    "https://www.linkedin.com/company/bright-data/",
    "https://www.linkedin.com/company/aabbccdd/"
]

# Run: python profile_checker.py
```

You'll get clear status indicators for each URL:
```bash
✓ linkedin.com/company/bright-data - Status: 200
✗ linkedin.com/company/aabbccdd - Status: 400
```

## Common Scraping Challenges with Free Method
When collecting data from LinkedIn, you'll encounter various anti-scraping measures. Here's what you need to know:
1. **Rate Limiting**: LinkedIn strictly monitors request frequency per IP address. Exceeding these limits leads to temporary or permanent IP blocks.
2. **CAPTCHA Detection**: LinkedIn presents CAPTCHA challenges when it detects unusual browsing patterns, blocking automated access.
3. **Authentication Barriers**: Most valuable LinkedIn data requires authentication. The platform easily detects and blocks automated login attempts.
4. **Technical Challenges**: Additional barriers include handling pagination, dynamic content loading, incomplete data points, and navigating through LinkedIn ads.

While manual web scraping works for small projects, it becomes increasingly challenging at scale. For reliable, efficient, and scalable LinkedIn data collection, **Bright Data** provides a superior solution that saves time and resources while delivering higher-quality results.

[![Promo](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/Proxies%20and%20scrapers%20GitHub%20bonus%20banner.png)](https://brightdata.com/products/web-scraper/linkedin) 

## Method 2: Bright Data LinkedIn Scraper API
For a robust and scalable LinkedIn scraping solution, consider the [Bright Data LinkedIn Scraper API](https://brightdata.com/products/web-scraper/linkedin). Here's why it's worth considering:

### Key Benefits
- **No Infrastructure Setup:** Handles proxies, CAPTCHAs, and throttling automatically.
- **Scalable and Reliable:** Optimized for high-volume and real-time data extraction.
- **Comprehensive Coverage:** Extract data from profiles, jobs, companies, and posts.
- **Global Access:** Supports all regions and languages.
- **Privacy Compliance:** Fully adheres to GDPR and CCPA standards.
- **Pay-as-You-Go:** Only pay for successful responses.
- **Free Trial:** Includes 20 free API calls to get started.

## Getting Started with the LinkedIn Scraper API
The Bright Data LinkedIn Scraper API allows developers to programmatically extract public data from LinkedIn profiles, companies, job listings, and posts. This enterprise-grade solution handles complex infrastructure requirements including proxy management, request throttling, and data parsing.

Before getting started, you'll need:
- Bright Data Account
    - [Start a free trial](https://brightdata.com/) and log in.
    - Activate your account by adding a payment method under the **Billing** page.
- API Token
    - [Follow this guide](https://docs.brightdata.com/general/account/api-token) to obtain your API token.

### 1. Company Information Scraper
Extract detailed data about companies using their LinkedIn URLs.

<img width="797" alt="linkedin-scraper-bright-data-screenshot-linkedin-company-information-by-url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin-company-information-by-url.png" />


#### Input Parameters
| Field    | Type   | Required | Description                      |
|----------|--------|----------|----------------------------------|
| `url`      | string | Yes      | LinkedIn company URL to extract information from |

#### Sample Response
```json
{
    "name": "Kraft Heinz",
    "about": "The Kraft Heinz Company is one of the largest food and beverage companies in the world, with eight $1 billion+ brands and global sales of approximately $25 billion. We're a globally trusted producer of high-quality, great-tasting, and nutritious foods for over 150 years.",
    "key_info": {
        "headquarters": "Chicago, IL",
        "founded": 2015,
        "company_size": "10,001+ employees",
        "organization_type": "Public Company",
        "industries": "Food and Beverage Services",
        "website": "https://www.careers.kraftheinz.com/",
    },
    "metrics": {"linkedin_followers": 1557451, "linkedin_employees": 25254},
    "stock_info": {
        "ticker": "KHC",
        "exchange": "NASDAQ",
        "price": "$30.52",
        "last_updated": "December 21, 2024",
    },
    "specialties": "Food, Fast Moving Consumer Packaged Goods, CPG, and Consumer Packaged Goods",
    "locations": ["200 E. Randolph St. Suite 7600 Chicago, IL 60601, US"],
    "slogan": "Let's make life delicious!",
}
```

👉 Only key fields are shown here. For the full dataset, refer to the [JSON response sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/linkedin_company_info.json).

#### Code Example
Modify the company URLs in the list to extract data:
```python
companies = [
    {"url": "https://il.linkedin.com/company/ibm"},
    {"url": "https://www.linkedin.com/company/stalkit"},
    {
        "url": "https://www.linkedin.com/organization-guest/company/the-kraft-heinz-company"
    },
    {"url": "https://il.linkedin.com/company/bright-data"},
]
```

👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_company_info_by_url.py)

### 2. Profile by URL
Retrieves detailed information from individual LinkedIn profiles.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin-people-profiles-by-url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin-people-profiles-by-url.png" />

#### Input Parameters
| Parameter   | Type   | Required | Description                           |
|-------------|--------|----------|---------------------------------------|
| `url`       | string | Yes      | LinkedIn profile URL to extract data from|

#### Sample Response
```json
{
    "name": "Richard Branson",
    "profile_info": {
        "position": "Founder at Virgin Group",
        "followers": 18730516,
        "connections": 2,
        "avatar": "https://media.licdn.com/dms/image/v2/C4D03AQHh6_Wth5f3rQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1625181963183?e=2147483647&v=beta&t=oiGK2oBQ3r3COkRR0z62i7CbnqXKw_1ujZ9X4-SKheo",
    },
    "experience": [
        {
            "title": "Founder",
            "company": "Virgin Group",
            "duration": "Jan 1968 - Present (57 years)",
            "description": "Tie-loathing adventurer and thrill seeker, who believes in turning ideas into reality. Otherwise known as Dr Yes at Virgin!",
        }
    ],
    "current_company": {"name": "Virgin Group", "title": "Founder at Virgin Group"},
    "url": "https://www.linkedin.com/in/rbranson/",
}
```

👉 Only key fields are shown here. For the full dataset, refer to the [JSON response sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/profiles_by_url.json).

#### Code Example
Replace the URLs with the LinkedIn profiles you wish to analyze.
```python
profiles = [
    {"url": "https://www.linkedin.com/in/williamhgates"},
    {"url": "https://www.linkedin.com/in/rbranson/"},
    {"url": "https://www.linkedin.com/in/justinwelsh/"},
    {"url": "https://www.linkedin.com/in/simonsinek/"},
]
```

👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_profile_by_url.py)

### 3. Profile Discovery
Searches for LinkedIn profiles using name-based queries.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin-people-profiles-by-name" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin-people-profiles-by-name.png" />

#### Input Parameters
| Parameter     | Type   | Required | Description                                         |
|---------------|--------|----------|-----------------------------------------------------|
| `first_name`  | string | Yes      | Person's first name                         |
| `last_name`   | string | Yes      | Person's last name                       |

#### Sample Response
```json
{
    "profile_info": {
        "id": "richard-branson-8a38866",
        "name": "Richard Branson",
        "location": {"city": "Cincinnati", "state": "Ohio", "country": "US"},
        "about": "Respiratory therapist with 40 years of experience. Over 300 peer-reviewed publications...",
        "metrics": {"followers": 868, "connections": 500, "recommendations": 1},
    },
    "professional": {
        "current_position": {
            "company": "University of Cincinnati",
            "company_link": "https://www.linkedin.com/school/university-of-cincinnati",
        },
        "education": {
            "school": "The George Washington University School of Medicine and Health Sciences",
            "years": "2001-2003",
        },
    },
    "recommendations": [
        "Tracy OConnell Well known pro active valuable assett to the professon of respiratory care."
    ],
    "similar_professionals": [
        {
            "name": "Walter J. Jones, PhD, MHSA",
            "title": "Professor at Medical University of South Carolina",
            "location": "Mount Pleasant, SC",
        },
        {
            "name": "Vincent Arlet",
            "title": "Professor of Orthopaedic Surgery",
            "location": "Philadelphia, PA",
        },
    ],
    "url": "https://www.linkedin.com/in/richard-branson-8a38866",
}
```
👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/profiles_by_name.json)

#### Code Example
Modify the first and last name fields to find profiles.
```python
people = [
    {"first_name": "Richard", "last_name": "Branson"},
    {"first_name": "Bill", "last_name": "Gates"},
]
```
👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_profile_by_name.py)

### 4. Posts by URL
Collects detailed information about specific LinkedIn posts.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin-posts-by-url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin-posts-by-url.png" />

#### Input Parameters
| Parameter | Type   | Required | Description              |
|-----------|--------|----------|--------------------------|
| `url`     | string | Yes      | LinkedIn post URL        |

#### Sample Response
```json
{
    "post_info": {
        "id": "7176601589682434049",
        "url": "https://www.linkedin.com/posts/karin-dodis_web-data-collection-for-businesses-bright-activity-7176601589682434049-Aakz",
        "date_posted": "2024-03-21T15:32:33.770Z",
        "post_type": "post",
        "engagement": {"num_likes": 12, "num_comments": 4},
    },
    "content": {
        "title": "Karin Dodis on LinkedIn: Web data collection for Businesses. Bright Data",
        "text": "Hey data enthusiasts, Bright Data has an awesome collection of free datasets waiting for you to dive into. Whether you're a seasoned analyst or just starting out, these datasets are a goldmine of potential for your projects. From Wikipedia to ESPN and beyond, there's something here for everyone. Use them to fuel your next big idea, hone your skills, and add some serious value to your resume",
    },
    "author": {
        "user_id": "karin-dodis",
        "profile_url": "https://il.linkedin.com/in/karin-dodis",
        "followers": 4131,
        "total_posts": 28,
    },
    "repost_info": {
        "original_author": "Or Lenchner",
        "original_author_id": "orlenchner",
        "original_text": "Free Datasets! Not just samples, but complete datasets with millions of records. Before investing in acquiring specific large-scale data to train your LLM, start with free datasets. Wikipedia dataset, ESPN dataset, Goodreads, IMDB, and more.. Check it out -->",
        "original_date": "2024-03-27T15:39:54.497Z",
        "original_post_id": "7176470998987214848",
    },
}
```

👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/linkedin_posts_url.json)

#### Code Example
Replace the URLs with the LinkedIn post links you want to analyze.

```python
posts = [
    {
        "url": "https://www.linkedin.com/pulse/ab-test-optimisation-earlier-decisions-new-readout-de-b%C3%A9naz%C3%A9?trk=public_profile_article_view"
    },
    {
        "url": "https://www.linkedin.com/posts/orlenchner_scrapecon-activity-7180537307521769472-oSYN?trk=public_profile"
    },
    {
        "url": "https://www.linkedin.com/posts/karin-dodis_web-data-collection-for-businesses-bright-activity-7176601589682434049-Aakz?trk=public_profile"
    },
    {
        "url": "https://www.linkedin.com/pulse/getting-value-out-sunburst-guillaume-de-b%C3%A9naz%C3%A9?trk=public_profile_article_view"
    },
]
```
👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_posts_by_url.py)

### 5. Posts Discovery by URL
Find detailed data on LinkedIn articles authored or interacted with by users.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin-posts-discover-by-url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin-posts-discover-by-url.png" />

#### Input Parameters
| Parameter | Type   | Required | Description                     |
|-----------|--------|----------|---------------------------------|
| `url`     | string | Yes      | LinkedIn author/article URL |
| `limit`   | number | No       | Maximum number of articles to retrieve |

#### Sample Response
```json
{
    "article_info": {
        "id": "fare-business-con-la-propria-identità-cristian-brunori",
        "url": "https://it.linkedin.com/pulse/fare-business-con-la-propria-identità-cristian-brunori",
        "title": "Fare Business con la propria Identità",
        "date_posted": "2017-03-01T17:27:26.000Z",
        "post_type": "article",
        "engagement": {"num_likes": 18, "num_comments": 0},
    },
    "author": {
        "user_id": "cristianbrunori",
        "profile_url": "https://it.linkedin.com/in/cristianbrunori",
        "followers": 5205,
    },
    "content": {
        "headline": "Quali sono i fattori che permettono ad un prodotto, ad un servizio e ad un'azienda di distinguersi nei nuovi scenari di mercato dove quasi tutto è tecnicamente e facilmente riproducibile? Mai come in questo momento storico, l'identità di Marca è un valore imprescindibile per tutelare il proprio lavo",
        "text": "Quali sono i fattori che permettono ad un prodotto, ad un servizio e ad un'azienda di distinguersi nei nuovi scenari di mercato dove quasi tutto è tecnicamente e facilmente riproducibile? Mai come in questo momento storico, l' identità di Marca è un valore imprescindibile per tutelare il proprio lavoro e per aprire nuovi scenari economici ideali per la propria attività...",
    },
    "related_articles": [
        {
            "headline": "La differenza tra Marketing e Branding",
            "date_posted": "2017-06-29T00:00:00.000Z",
        },
        {
            "headline": "Ecco perché un contenuto diventa virale",
            "date_posted": "2017-03-24T00:00:00.000Z",
        },
    ],
}
```
👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/discovered_posts_by_url.json)

#### Code Example
Update the `url` and `limit` fields to retrieve articles from specific LinkedIn profiles.
```python
authors = [
    {
        "url": "https://www.linkedin.com/today/author/cristianbrunori?trk=public_post_follow-articles",
        "limit": 50,
    },
    {
        "url": "https://www.linkedin.com/today/author/stevenouri?trk=public_post_follow-articles"
    },
]
```
👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_posts_discover_by_url.py)


### 6. Posts Discovery by Profile
Discover all posts authored or interacted with by a specific LinkedIn profile.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin_posts_by_profile_url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin_posts_by_profile_url.png" />

#### Input Parameters
| Parameter    | Type   | Required | Description                                                             |
|--------------|--------|----------|-------------------------------------------------------------------------|
| `url`        | string | Yes      | LinkedIn profile URL                                                   |
| `start_date` | date   | No       | Start date to filter posts (ISO 8601 format) |
| `end_date`   | date   | No       | End date to filter posts (ISO 8601 format) |

#### Sample Response
```json
{
    "article_info": {
        "id": "fare-business-con-la-propria-identità-cristian-brunori",
        "url": "https://it.linkedin.com/pulse/fare-business-con-la-propria-identità-cristian-brunori",
        "title": "Fare Business con la propria Identità",
        "date_posted": "2017-03-01T17:27:26.000Z",
        "post_type": "article",
        "engagement": {"num_likes": 18, "num_comments": 0},
    },
    "author": {
        "user_id": "cristianbrunori",
        "profile_url": "https://it.linkedin.com/in/cristianbrunori",
        "followers": 5205,
    },
    "content": {
        "headline": "Quali sono i fattori che permettono ad un prodotto, ad un servizio e ad un'azienda di distinguersi nei nuovi scenari di mercato dove quasi tutto è tecnicamente e facilmente riproducibile? Mai come in questo momento storico, l'identità di Marca è un valore imprescindibile per tutelare il proprio lavo",
        "text": "Quali sono i fattori che permettono ad un prodotto, ad un servizio e ad un'azienda di distinguersi nei nuovi scenari di mercato dove quasi tutto è tecnicamente e facilmente riproducibile? Mai come in questo momento storico, l' identità di Marca è un valore imprescindibile per tutelare il proprio lavoro e per aprire nuovi scenari economici ideali per la propria attività...",
    },
    "related_articles": [
        {
            "headline": "La differenza tra Marketing e Branding",
            "date_posted": "2017-06-29T00:00:00.000Z",
        },
        {
            "headline": "Ecco perché un contenuto diventa virale",
            "date_posted": "2017-03-24T00:00:00.000Z",
        },
    ],
}
```
👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/posts_by_profile.json)

#### Code Example
Modify the profile URLs and date ranges to collect posts from specific LinkedIn profiles.
```python
profiles = [
    {
        "url": "https://www.linkedin.com/in/luca-rossi-0aa497bb",
        "start_date": "2024-10-01T00:00:00.000Z",
        "end_date": "2024-10-09T00:00:00.000Z",
    },
    {
        "url": "https://www.linkedin.com/in/srijith-gomattam-401059214",
        "start_date": "2024-09-01T00:00:00.000Z",
        "end_date": "2024-10-01T00:00:00.000Z",
    },
    {
        "url": "https://www.linkedin.com/in/anna-clarke-0a342513",
        "start_date": "2024-10-01T00:00:00.000Z",
    },
]
```
👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_posts_by_profile_url.py)

### 7. Posts Discovery by Company
Collect posts and updates from company pages.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin_posts_by_company_url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin_posts_by_company_url.png" />

#### Input Parameters
| Parameter    | Type   | Required | Description                                                             |
|--------------|--------|----------|-------------------------------------------------------------------------|
| `url`        | string | Yes      | LinkedIn company URL                                                   |
| `start_date` | date   | No       | Start date to filter posts (ISO 8601 format) |
| `end_date`   | date   | No       | End date to filter posts (ISO 8601 format) |

#### Sample Response
```json
{
    "post_info": {
        "id": "7254476883906482179",
        "url": "https://it.linkedin.com/posts/lanieri_lanieri-torna-in-lussemburgo-siamo-lieti-activity-7254476883906482179-8dW8",
        "date_posted": "2024-10-22T13:01:10.754Z",
        "post_type": "post",
    },
    "content": {
        "title": "Lanieri on LinkedIn: Lanieri torna in Lussemburgo. Siamo lieti di annunciare che dal 7 al 9…",
        "text": "Lanieri torna in Lussemburgo. Siamo lieti di annunciare che dal 7 al 9 novembre il nostro Trunk Show Su Misura fa tappa in Lussemburgo. Crea il tuo pezzo unico insieme ai nostri Style Advisor: scegli il tessuto, i dettagli e la vestibilità del tuo capo: noi lo realizzeremo per te in sole quattro settimane. Ci vediamo all'Hotel Le Royal, Boulevard Royal 12. Prenota il tuo appuntamento qui https://bit.ly/4hgYgyk",
        "images": [
            "https://media.licdn.com/dms/image/v2/D4D22AQHbmc9Vn-NP5Q/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1729602070140?e=2147483647&v=beta&t=gt-rNjUJR_ZMVDjNfwmtx3mwBpR3UjCdtVjoj2ZsAv0"
        ],
    },
    "engagement": {"likes": 12, "comments": 0},
    "company_info": {
        "name": "Lanieri",
        "followers": 5768,
        "account_type": "Organization",
        "profile_url": "https://it.linkedin.com/company/lanieri",
    },
}
```

👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/linkedin_posts_company_url.json)

#### Code Example
Customize the company URLs and date ranges to retrieve posts from specific company pages.
```python
companies = [
    {"url": "https://www.linkedin.com/company/green-philly"},
    {"url": "https://www.linkedin.com/company/lanieri"},
    {"url": "https://www.linkedin.com/company/effortel"},
]
```

👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_posts_by_company_url.py)

### 8. Job Listings Collection by URL
Extract complete information about specific job listings using their URLs.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin_jobs_by_url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin_jobs_by_url.png" />

#### Input Parameters
| Parameter | Type   | Required | Description                  |
|-----------|--------|----------|------------------------------|
| `url`     | string | Yes      | LinkedIn job listing URL    |

#### Sample Response
```json
{
    "job_info": {
        "id": "4073552631",
        "title": "Data Platform Engineer",
        "location": "Tel Aviv-Yafo, Tel Aviv District, Israel",
        "posted_date": "2024-11-22T09:41:10.107Z",
        "posted_time": "1 month ago",
        "employment_type": "Full-time",
        "function": "Engineering and Information Technology",
        "seniority_level": "Not Applicable",
        "industries": "Computer and Network Security",
        "applicants": 85,
        "apply_link": "https://www.linkedin.com/jobs/view/externalApply/4073552631?url=https%3A%2F%2Fcycode%2Ecom%2Fcareers%2Fposition%2F%3Fpos_title%3Ddata-platform-engineer%26pos_id%3D53%2ED48%26coref%3D1%2E11%2Ep9D_4217&urlHash=c1hm",
    },
    "company": {
        "name": "Cycode | Complete ASPM",
        "id": "40789623",
        "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQFsSsfzqEVWtw/company-logo_100_100/company-logo_100_100/0/1689682315729/cycode_logo?e=2147483647&v=beta&t=h91f6XM-5MGHa5FDhMCVtXy7Me0S8YQIPRAYUc4UVC0",
        "url": "https://www.linkedin.com/company/cycode",
    },
    "description": {
        "summary": "This is a unique opportunity to join an exciting early-stage startup experiencing hypergrowth in a white-hot segment of the cybersecurity space. Cycode is a fast-growing cybersecurity startup and the creator of the first comprehensive software supply chain security solution...",
        "requirements": [
            "Bachelor's degree in a relevant field such as Statistics, Mathematics, Computer Science, or Economics",
            "Proven experience in building, deploying, and monitoring of ETLs",
            "Proficiency in data analysis tools such as SQL, Python, Pandas, Apache Spark / Beam",
            "Good understanding of data modeling principles",
            "Familiarity with data visualization tools",
        ],
        "advantages": ["MongoDB", "AWS Cloud", "CICD, Docker Kubernetes"],
    },
}
```

👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/linkedin_jobs_url.json)

#### Code Example
Update the job URLs to collect information about specific job listings.
```python
job_searches = [
    {"url": "https://www.linkedin.com/jobs/view/4073552631"},
    {"url": "https://www.linkedin.com/jobs/view/4073729630"},
]
```

👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_jobs_by_url.py)


### 9. Job Listings Discovery by Keyword
Extract job listings using advanced search criteria and filters to find relevant opportunities.

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin_jobs_by_keyword" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin_jobs_by_keyword.png" />

#### Input Parameters
| Parameter          | Type    | Required | Description                                                                                      |
|--------------------|---------|----------|--------------------------------------------------------------------------------------------------|
| `location`         | string  | Yes      | Collect jobs in a specific location                                                             |
| `keyword`          | string  | No       | Search for jobs by keyword or title (e.g., "Product Manager"). Use quotation marks for exact matches. |
| `country`          | string  | No       | 2-letter country code (e.g., US or FR)                                                   |
| `time_range`       | string  | No       | Time range of job posting (e.g., past 24 hours, past week)                      |
| `job_type`         | string  | No       | Filter by job type (e.g., full-time, part-time, contract)                                        |
| `experience_level` | string  | No       | Filter by required experience level (e.g., entry, mid, senior)                                  |
| `remote`           | string  | No       | Filter jobs by remote work options                                                              |
| `company`          | string  | No       | Search jobs at a specific company                                                               |
| `selective_search` | boolean | No       | When set to `true`, excludes titles that do not contain the specified keywords                  |


#### Sample Response
```json
{
    "job_info": {
        "id": "4096670538",
        "title": "Remote Part-Time Focus Group Participants (Up To $750/Week)",
        "posted_date": "2024-12-15T09:16:55.932Z",
        "posted_time": "1 week ago",
        "location": {"city": "Bronx", "state": "NY", "country": "US"},
        "type": {
            "employment": "Part-time",
            "level": "Entry level",
            "function": "Other",
            "industry": "Market Research",
            "remote": true,
        },
        "applicants": 25,
        "apply_link": "https://www.linkedin.com/jobs/view/externalApply/4096670538?url=https%3A%2F%2Fwww%2Ecollegerecruiter%2Ecom%2Fjob%2F1447234465%3Fr%3D1%26source%3D101%26ids%3D513&urlHash=Nagt",
    },
    "company": {
        "name": "Apex Focus Group",
        "id": "89885194",
        "logo": "https://media.licdn.com/dms/image/v2/C560BAQHmbh3iXrrrEA/company-logo_100_100/company-logo_100_100/0/1670524954585?e=2147483647&v=beta&t=n2mnVpQTNpofk7mrixyy7aBax0fXqhY031fijCPtp14",
        "url": "https://www.linkedin.com/company/apex-focus-group",
    },
    "compensation": {
        "per_session": "$75-$150 (1 hour)",
        "multi_session": "$300-$750",
        "frequency": "weekly",
    },
    "requirements": {
        "technical": [
            "Smartphone with working camera or desktop/laptop with webcam",
            "High speed internet connection",
        ],
        "responsibilities": [
            "Show up 10 mins before discussion start time",
            "Complete written and oral instructions",
            "Complete surveys for each panel",
            "Use and discuss provided products/services",
        ],
    },
    "search_parameters": {
        "keyword": "data analyst",
        "location": "New York",
        "job_type": "Part-time",
        "experience": "Entry level",
        "remote": "Remote",
        "country": "US",
    },
}
```

👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/linkedin_jobs_keyword.json)

#### Code Example
Customize these search criteria to find specific job opportunities across different locations and requirements.
```python
search_criteria = [
    {
        "location": "New York",
        "keyword": "data analyst",
        "country": "US",
        "time_range": "Any time",
        "job_type": "Part-time",
        "experience_level": "Entry level",
        "remote": "Remote",
        "company": "",
    },
    {
        "location": "paris",
        "keyword": "product manager",
        "country": "FR",
        "time_range": "Past month",
        "job_type": "Full-time",
        "experience_level": "Internship",
        "remote": "On-site",
        "company": "",
    },
    {
        "location": "New York",
        "keyword": '"python developer"',
        "country": "",
        "time_range": "",
        "job_type": "",
        "experience_level": "",
        "remote": "",
        "company": "",
    },
]
```

👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_jobs_by_keyword.py)

### 10. Job Listings Discovery by URL
Extract job listings using direct LinkedIn search URLs

<img width="700" alt="linkedin-scraper-bright-data-screenshot-linkedin_jobs_by_search_url" src="https://github.com/luminati-io/LinkedIn-Scraper/blob/main/LinkedIn%20Images/linkedin-scraper-bright-data-screenshot-linkedin_jobs_by_search_url.png" />

#### Input Parameters
| Parameter          | Type    | Required | Description                                                                                       |
|--------------------|---------|----------|---------------------------------------------------------------------------------------------------|
| `url`              | string  | Yes      | Direct LinkedIn search URL (e.g., company search or keyword-based search)                        |
| `selective_search` | boolean | No       | When set to `true`, excludes titles that do not contain the specified keywords                 |

> **Note:** To implement a time range filter, calculate the desired range in seconds (`hours * 3600`) and update the `&f_TPR` parameter in the LinkedIn search URL.
>
> - Use `f_TPR=r3600` for past hour  
> - Use `f_TPR=r86400` for past 24 hours  
> - Use `f_TPR=r604800` for past week

#### Sample Response
```json
{
    "job_info": {
        "id": "4107998267",
        "title": "Software Engineer, Professional Services",
        "location": "Tel Aviv District, Israel",
        "posted": {"date": "2024-12-22T08:39:21.666Z", "time_ago": "1 hour ago"},
        "type": {
            "employment": "Full-time",
            "level": "Entry level",
            "function": "Information Technology",
            "industry": "Software Development",
        },
        "applicants": 25,
        "apply_link": "https://www.linkedin.com/jobs/view/externalApply/4107998267?url=https%3A%2F%2Fwww%2Efireblocks%2Ecom%2Fcareers%2Fcurrent-openings%2F4426623006%3Fgh_jid%3D4426623006",
    },
    "company": {
        "name": "Fireblocks",
        "id": "14824547",
        "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQEyT6gpuwTpPg/company-logo_100_100/company-logo_100_100/0/1630561416766/fireblocks_logo?e=2147483647&v=beta&t=MNcf2cPIzbPMdPDbsidFZBlEVWQHcHK-QimzqSaimww",
        "url": "https://www.linkedin.com/company/fireblocks",
    },
    "requirements": {
        "core": [
            "2+ years of software development experience",
            "Proficiency in JavaScript, TypeScript, and Python",
            "Strong understanding of frontend and backend technologies",
            "Experience with SQL and NoSQL databases",
            "Familiarity with Docker and Kubernetes",
            "Knowledge of blockchain and crypto development",
            "Understanding of security protocols",
        ],
        "nice_to_have": [
            "Experience with Fireblocks or similar crypto platforms",
            "Knowledge of cloud platforms (AWS, GCP, Azure)",
        ],
    },
    "responsibilities": [
        "Collaborate with clients on technical requirements",
        "Build custom tools and integrations",
        "Work on frontend and backend components",
        "Assist with API integration",
        "Provide technical training",
        "Stay updated on blockchain trends",
    ],
}
```

👉 View [Full JSON Response Sample](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_data/linkedin_jobs_search_url.json)

#### Code Example
Modify these search URLs to collect job listings from specific companies or search results.
```python
search_urls[
    {
        "url": "https://www.linkedin.com/jobs/search?keywords=Software&location=Tel%20Aviv-Yafo&geoId=101570771&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&f_TPR=r3600"
    },
    {"url": "https://www.linkedin.com/jobs/semrush-jobs?f_C=2821922"},
    {"url": "https://www.linkedin.com/jobs/reddit-inc.-jobs-worldwide?f_C=150573"},
]
```

👉 View [Full Python Code](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/linkedin_scraper_api_codes/linkedin_jobs_by_search_url.py)


## Data Collection Approaches
You can use the following parameters to fine-tune your results:
| **Parameter**       | **Type**   | **Description**                                            | **Example**                  |
|---------------------|------------|------------------------------------------------------------|------------------------------|
| `limit`             | `integer`  | Max results per input                                   | `limit=10`                   |
| `include_errors`    | `boolean`  | Get error reports for troubleshooting                     | `include_errors=true`        |
| `notify`            | `url`      | Webhook notification URL to be notified upon completion  | `notify=https://notify-me.com/` |
| `format`            | `enum`     | Output format (e.g., JSON, NDJSON, JSONL, CSV)         | `format=json`                |

💡 **Pro Tip:** You can also select whether to deliver the data to an [external storage](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview#via-deliver-to-external-storage) or to deliver it to a [webhook](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview#via-webhook).

----

Need more details? Check the [official API docs](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview).
