# Kotlin Education Landscape 🌍

A data-driven analysis of how Kotlin is taught across universities worldwide.

---

## Overview

This project aims to build a structured dataset and extract meaningful insights about Kotlin adoption in academic environments.

It focuses on understanding:
- Where Kotlin is being taught (countries, regions, institutions)
- How it is taught (course structure, teaching style)
- What topics are covered (Android, Software Engineering, etc.)

---

## Objectives

- Build a clean and structured dataset of universities teaching Kotlin
- Analyze trends in Kotlin adoption across regions
- Identify dominant teaching patterns and subject areas
- Provide insights that can help improve Kotlin education strategies

---

## Dataset Description

The dataset includes the following fields:

- university_name: Name of the institution
- country: Country of the university
- region: Geographic region (Asia, Europe, etc.)
- course_title: Name of the course
- course_level: Beginner / Intermediate / Advanced
- primary_language: Main language used
- secondary_language: Supporting language (if any)
- course_url: Source link
- year_verified: Year of verification
- subject_area: Domain (Android, Software Engineering, etc.)
- teaching_style: Lecture / Project-based / Mixed

File location: data/universities.csv

---

## Tech Stack

- Python
- pandas
- matplotlib

---

## Analysis Performed

- Country-wise distribution of Kotlin courses
- Course level analysis
- Subject area distribution
- Teaching style trends

---

## Key Insights

- Kotlin is predominantly used in Android development courses
- Most courses are intermediate level
- Strong adoption is observed in India, USA, and Europe
- Project-based learning is widely used

---

## How to Run

1. Install dependencies:
   pip install pandas matplotlib

2. Run analysis:
   python scripts/analyze.py

---

## Project Structure

kotlin-education-landscape/
│
├── data/
│   └── universities.csv
│
├── scripts/
│   └── analyze.py
│
├── README.md

---

## Future Scope

- Expand dataset to 100+ universities
- Add automated data collection (web scraping)
- Compare Kotlin with other programming languages
- Build visualization dashboards
- Include educator survey data

---

## Motivation

Kotlin adoption in education is growing rapidly, but there is no centralized dataset or structured analysis available.

This project aims to bridge that gap by providing:
- A reusable dataset
- Actionable insights
- A foundation for further research

---

## Author

Avanish Kumar Jha  
GitHub: https://github.com/Kingjha13   
B.Tech Computer Science Engineering  
Parul University, India

---

## Contribution & Feedback

This is an evolving project. Suggestions and improvements are welcome.