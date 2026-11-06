# AapleSeva Citizen Services Assistant

## Project Card

### 1. Product
**AapleSeva Citizen Services Assistant** is an intelligent digital guidance and eligibility verification tool designed to simplify access to Maharashtra Government public services under the **Maharashtra Right to Public Services Act (RTS Act, 2015)** and the **Aaple Sarkar Portal** (`https://aaplesarkar.mahaonline.gov.in`). The system guides citizens through service workflows, identifies required documents, checks eligibility criteria, and displays statutory delivery timelines.

---

### 2. User (Target Audience)
- **Citizens of Maharashtra:** Residents seeking key G2C (Government-to-Citizen) certificates such as Income, Caste, Domicile, and Non-Creamy Layer (NCL).
- **Students & Job Aspirants:** Candidates requiring time-sensitive documentation for educational admissions (MHT-CET, CAP rounds) and government recruitments (MPSC, Saral Seva).
- **Rural & Urban Beneficiaries:** Farmers applying for agriculturist certificates, families updating ration cards, and senior citizens applying for welfare cards.
- **Maha e-Seva / CSC Center Operators:** Village-level entrepreneurs assisting local citizens with error-free application submissions.

---

### 3. Problem Statement
Navigating government services often presents severe hurdles for common citizens:
- **Complex Documentation:** Ambiguity about exact acceptable documents (e.g., grandfather's 1961/1967 proof for caste certificates, 3-year income proofs for NCL).
- **Application Rejections:** High rejection rates due to missing proofs, wrong affidavit formats, or exceeding eligibility thresholds.
- **Middlemen & Exploitation:** Citizens falling prey to unauthorized agents and paying exorbitant fees for free or subsidized statutory services.
- **Lack of Transparency:** Limited awareness of statutory timelines guaranteed under the RTS Act and the proper appellate hierarchy.

---

### 4. Data Source
- **Primary Source:** Official Aaple Sarkar Portal (`https://aaplesarkar.mahaonline.gov.in`)
- **Statutory Framework:** Maharashtra Right to Public Services Act (RTS Act, 2015) Citizen Charters and Gazette Notifications
- **Departmental Charters:** Revenue and Forest Department, Rural Development & Panchayat Raj Department, and Food, Civil Supplies & Consumer Protection Department, Government of Maharashtra

---

## Repository Contents
- **`README.md`**: Project overview and AapleSeva project card.
- **`day01_intro.py`**: Introductory script that defines project card details using variables, prints them with clean f-strings, and takes user input for their name and inquiry.
- **`day01_menu.py`**: Interactive CLI menu offering portal details, sample citizen questions, an if/elif eligibility rule checker for the Non-Creamy Layer (NCL) certificate, and an exit option.

---

## How to Run
```bash
# Run Day 01 Intro
python day01_intro.py

# Run Day 01 Interactive Menu
python day01_menu.py
```
