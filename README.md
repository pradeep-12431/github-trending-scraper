# 📊 GitHub Trending Scraper

This is a Python script that scrapes the top 5 trending repositories from [GitHub Trending](https://github.com/trending) and saves them into a CSV file.

## 🚀 What It Does

- Scrapes the top 5 trending repositories from GitHub
- Extracts:
  - Repository name
  - Direct link to the repository
- Saves the results into a file: `trending_repos.csv`

---

## 📦 Tech Stack

- Python 3
- `requests` — for making HTTP requests
- `beautifulsoup4` — for parsing and extracting HTML data
- `csv` — for saving the output to a file

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4
