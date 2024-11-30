
# Intelligent Data Analysis Application "Media Flayer"

## Project Overview

This application is an open-source intelligent system that features a graphical user interface built with Streamlit and integrates multiple data sources for comprehensive data analysis.

## Features

- User-friendly GUI built with Streamlit
- Integration with multiple data sources/APIs
- 4 Unique Custom Tailored Social Media Scrapers
- Real-time data processing and analysis
- Interactive data visualization
- AI Powered analysis 

## Technical Requirements

- Python 3.12.4
- Kivy
- pandas
- requests
- matplotlib
- numpy
- Ollama LLM

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Exxxa/Open_Source_Intelligent_Application
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```
4. Install ollama
   go to https://ollama.com/ and install to appropriate OS
   when done installing run this command in terminal:
   ```bash
   ollama run llama3.2
   ```
## Project Structure

```
OPEN_SOURCE_INTELLIGENT_APPLICATION/
├── docs/
│   ├── project_plan.md
├── src/
│   ├── main.py
│   ├── gui/
│   ├── data_sources/
│   └── utils/
├── requirements.txt
└── README.md
```

## Development Guidelines

1. Document all functions and classes
3. Create feature branches for new development
4. Submit pull requests for code review

## Data Sources

The application integrates with the following APIs:

1. [Twttr API] - "A powerful Twttr API with endpoints to help you access valuable Twttr data."
   - https://rapidapi.com/davethebeast/api/twitter241/playground/apiendpoint_eab00723-ecc9-4fd0-994e-698d471075e5
2. [Instagram Scraper API] - "The most stable and fastest Instagram API online"
   - https://rapidapi.com/social-api1-instagram/api/instagram-scraper-api2/playground/apiendpoint_59cb4f4c-55c0-41b5-807d-e39967e66c1d
3. [Reddit Scraper] - "Reddit Unofficial API is a fast, reliable and comprehensive tool for extracting data from Reddit."
   - https://rapidapi.com/fkal094tiokg09w3vi095i/api/reddit-scraper2/playground/apiendpoint_6dae487b-0fef-4350-9017-c323a57ad278
4. [TikTok API] - "Lightweight and complete TikTok API"
   - https://rapidapi.com/Lundehund/api/tiktok-api23/playground/apiendpoint_c1dca90d-a452-4ec8-9ac8-5d6fe43c9d62

## Team Members and Roles

- Pierre LOPEZ
- Thailer Simmons
- Abel Castilla
- Trent Kauflin
- Jorge Martinez JR
- Rabia Ahmed
- Joseph Barron
- Michal Pruszynski
