# X Bot Analytic

Automation tool designed to analyze X (Twitter) posts and extract key data for Stake campaigns, including usernames, bet IDs, and winners.

---

## Overview

This tool streamlines the process of analyzing replies on X posts, reducing manual work and improving accuracy when running promotions and competitions.

---

## Core Features

### Current Features
- Analyze replies from X post via URL
- Identify correct answers
- Detect and list winners
- Structured output for campaign reporting

### In Progress / Planned
- Extract Stake usernames only (clean export)
- Toggle extraction:
  - Casino Bet IDs (`casino:XXXXX`)
  - Sports Bet IDs (`sport:XXXXX`)
- CSV / Excel export
- Historical tracking (database)
- Copy-to-clipboard (UI)
- Automated reply generation
- Login & access control

---

## Architecture

This project is split into **Frontend** and **Backend**, deployed independently.

---

### Frontend
- Repository: https://github.com/Cawitos/frontend-bot-x
- Deployment: Vercel
- Purpose:
  - User interface
  - Input X post URL
  - Display processed results

> Note: Vercel automatically created a deployment repo:
> https://github.com/Cawitos/frontend-bot-x-vercel

---

### Backend
- Repository: https://github.com/Cawitos/X-bot-prototype
- Deployment: Render
- Language: Python

#### Responsibilities:
- Fetch X post replies
- Process data
- Apply business logic
- Return results to frontend

---

## Data Flow
User (Frontend - Vercel)
↓
API Request
↓
Backend (Render - Python)
↓
Fetch X Data
↓
Process (Regex + Logic)
↓
Return Results
↓
Display in UI

---

## Tech Stack

### Frontend
- JavaScript / HTML / CSS
- Vercel

### Backend
- Python 3.11
- snscrape / requests (depending on implementation)

### Infra
- Vercel (Frontend hosting)
- Render (Backend hosting)
- GitHub (Version control)

---

## How It Works

1. User inputs an X post URL
2. Frontend sends request to backend
3. Backend:
   - Fetches replies
   - Extracts relevant data
   - Applies logic (e.g., correct answer)
4. Backend returns processed results
5. Frontend displays output

---

## Running Locally (Backend)

### 1. Clone repository

git clone https://github.com/Cawitos/X-bot-prototype.git
cd X-bot-prototype

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run script
python main.py

---

## Data Extraction Logic

### Stake Usernames (Planned)
Pattern:
Stake:\s*(\w+)

---

### Bet IDs (Planned)
Pattern:
(sport:\d+|casino:\d+)

---

## Repositories Structure

- Backend:
  - https://github.com/Cawitos/X-bot-prototype

- Frontend:
  - https://github.com/Cawitos/frontend-bot-x

- Vercel Deployment Repo:
  - https://github.com/Cawitos/frontend-bot-x-vercel

---

## Security (Upcoming)

- Authentication system (login)
- Restricted internal access
- Usage tracking / logs

---

## Roadmap

- [ ] Stake username extraction (clean export)
- [ ] Bet ID toggle system
- [ ] CSV export
- [ ] Database integration (historical data)
- [ ] Authentication system
- [ ] Migration to company-owned repositories

---

## Ownership & Deployment Plan

Current state:
- Backend hosted on personal Render account
- Frontend hosted on personal Vercel account

Target state:
- Migrate repositories to company GitHub organization
- Deploy under company Vercel & Render accounts
- Remove dependency on personal infrastructure

---

## Limitations

- Historical data depends on X API / scraping limits
- Older data may not be fully accessible without paid API

---

## Maintainer

Carlos Camacho.

---

## Notes

This tool is actively evolving based on Stake campaign needs.
