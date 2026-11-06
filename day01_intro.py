"""
Day 01 - Introduction to AapleSeva Project
Prints the AapleSeva Project Card using variables and f-strings,
and collects user information through standard input.
"""

def main():
    # Project Card Variables
    project_title = "AapleSeva Citizen Services Assistant"
    product_description = (
        "An intelligent guidance and eligibility verification tool for Maharashtra "
        "Government public services delivered under the RTS Act 2015 via Aaple Sarkar."
    )
    target_users = (
        "Citizens of Maharashtra, students applying for admissions/scholarships, "
        "job aspirants (MPSC/Govt exams), rural residents, and CSC/Maha e-Seva operators."
    )
    problem_statement = (
        "Citizens struggle to understand exact document requirements, face high rejection "
        "rates due to missing proofs, lack awareness of statutory delivery timelines, "
        "and often fall prey to unauthorized middlemen."
    )
    data_sources = (
        "Official Aaple Sarkar Portal (aaplesarkar.mahaonline.gov.in), "
        "Maharashtra Right to Public Services Act (RTS Act, 2015) Citizen Charters, "
        "and Revenue & Forest Department Government Resolutions (GRs)."
    )

    # Print Project Card using f-strings
    print("=" * 70)
    print(f"{project_title.center(70)}")
    print("=" * 70)
    print(f"PRODUCT:\n  {product_description}\n")
    print(f"TARGET USERS:\n  {target_users}\n")
    print(f"PROBLEM STATEMENT:\n  {problem_statement}\n")
    print(f"DATA SOURCES:\n  {data_sources}")
    print("=" * 70)
    print()

    # User Interaction
    print("--- Citizen Inquiry Desk ---")
    user_name = input("Enter your full name: ").strip()
    user_question = input("What question do you have about AapleSeva services? ").strip()

    print()
    print("-" * 70)
    print(f"Namaskar, {user_name}!")
    print(f"Thank you for reaching out to the AapleSeva Helpdesk.")
    print(f"Your inquiry: \"{user_question}\"")
    print("Our automated assistant is ready to help guide you through the process.")
    print("-" * 70)


if __name__ == "__main__":
    main()
