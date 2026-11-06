"""
Day 01 - Interactive Menu for AapleSeva
Provides a while-loop console menu to learn about AapleSeva,
view sample citizen queries, test domain eligibility rules (if/elif),
and cleanly exit.
"""

def show_about():
    print("\n" + "=" * 60)
    print("           ABOUT AAPLESEVA (AAPLE SARKAR)           ")
    print("=" * 60)
    print("• Overview:")
    print("  Aaple Sarkar (AapleSeva) is the flagship citizen service portal")
    print("  by the Government of Maharashtra (https://aaplesarkar.mahaonline.gov.in).")
    print("\n• Statutory Backing:")
    print("  Enacted under the Maharashtra Right to Public Services Act (RTS Act, 2015),")
    print("  it guarantees time-bound, transparent, and hassle-free public services.")
    print("\n• Key Departments & Services:")
    print("  1. Revenue Department: Income, Domicile, Caste, Non-Creamy Layer Certificates.")
    print("  2. Food & Civil Supplies: New Ration Cards, Member Addition/Deletion.")
    print("  3. Rural Development & Urban Local Bodies: Birth/Death/Marriage Certificates.")
    print("  4. Home Department: Police Character Verification, Event Permissions.")
    print("\n• Key Benefits:")
    print("  - 100% online application, fee payment, and digital certificate download.")
    print("  - Eliminates unauthorized intermediaries and ensures fixed SLA delivery.")
    print("=" * 60 + "\n")


def show_sample_questions():
    print("\n" + "=" * 60)
    print("            FREQUENTLY ASKED CITIZEN QUESTIONS             ")
    print("=" * 60)
    questions = [
        "1. What documents are mandatory for an Income Certificate (उत्पन्नाचा दाखला)?",
        "2. What is the statutory RTS delivery timeline for a Domicile Certificate?",
        "3. How is eligibility determined for a Non-Creamy Layer (NCL) Certificate?",
        "4. Which pre-1961/1967 proofs are acceptable for Caste Certificate verification?",
        "5. How can I appeal if my application is delayed beyond the RTS time limit?",
        "6. Can I download a digitally signed certificate directly from the portal?",
    ]
    for q in questions:
        print(f"  {q}")
    print("=" * 60 + "\n")


def check_eligibility_rule():
    print("\n" + "=" * 60)
    print("    AAPLESEVA DOMAIN RULE: NON-CREAMY LAYER (NCL) CHECKER   ")
    print("=" * 60)
    print("This rule checks Non-Creamy Layer / Certificate eligibility based on")
    print("Maharashtra Government Revenue Dept criteria (Income & Category).\n")

    category = input("Enter Category (OBC / VJNT / SBC / SC / ST / OPEN): ").strip().upper()

    try:
        income_input = input("Enter Gross Annual Family Income in INR (e.g., 450000): ").strip()
        income = float(income_input)
    except ValueError:
        print("\nError: Please enter a valid numerical value for annual income.\n")
        return

    # Domain Rule Check using if / elif / else
    print("\n--- Assessment Result ---")
    if income < 0:
        print("Invalid Input: Annual income cannot be negative.")
    elif category in ["SC", "ST"]:
        print(f"Category: {category}")
        print("Status: Non-Creamy Layer (NCL) certificate is NOT required.")
        print("SC/ST beneficiaries are entitled to reservation benefits using their")
        print("Caste Certificate and Caste Validity Certificate alone.")
    elif category in ["OBC", "VJNT", "SBC"]:
        if income <= 800000:
            print(f"Category: {category} | Annual Income: INR {income:,.2f}")
            print("Status: ELIGIBLE for Non-Creamy Layer (NCL) Certificate.")
            print("Details: Income is within the statutory INR 8,00,000 threshold.")
            print("Benefits: Reservation in government jobs, admissions, and fee concessions.")
            print("Required Documents: 3-year ITR / Form 16 / Talathi Income Report,")
            print("                    Caste Certificate, Ration Card, School Leaving Certificate.")
        else:
            print(f"Category: {category} | Annual Income: INR {income:,.2f}")
            print("Status: INELIGIBLE for Non-Creamy Layer (NCL) Certificate.")
            print("Details: Income exceeds the statutory INR 8,00,000 ceiling (Creamy Layer).")
            print("Note: You may still apply for a standard Income Certificate for general purposes.")
    elif category == "OPEN":
        if income <= 800000:
            print(f"Category: OPEN | Annual Income: INR {income:,.2f}")
            print("Status: Eligible for Economically Weaker Section (EWS) Certificate.")
            print("Details: Income is <= INR 8 Lakhs. You may apply for 10% EWS quota")
            print("         provided family land holding is < 5 acres and flat is < 1,000 sq ft.")
        else:
            print(f"Category: OPEN | Annual Income: INR {income:,.2f}")
            print("Status: Standard General Category.")
            print("Details: Eligible for general statutory services and General Income Certificate.")
    else:
        print(f"Unrecognized Category '{category}'. Please choose OBC, VJNT, SBC, SC, ST, or OPEN.")
    print("=" * 60 + "\n")


def main():
    while True:
        print("=" * 45)
        print("       AAPLESEVA CITIZEN PORTAL MENU         ")
        print("=" * 45)
        print("  1. About AapleSeva")
        print("  2. Sample Questions")
        print("  3. Domain Rule Check (NCL Eligibility)")
        print("  0. Exit")
        print("=" * 45)

        choice = input("Enter your choice (0-3): ").strip()

        if choice == "1":
            show_about()
        elif choice == "2":
            show_sample_questions()
        elif choice == "3":
            check_eligibility_rule()
        elif choice == "0":
            print("\nThank you for using AapleSeva Assistant. Jai Hind, Jai Maharashtra!")
            break
        else:
            print(f"\nInvalid choice '{choice}'. Please select an option between 0 and 3.\n")


if __name__ == "__main__":
    main()
