
import json
import os
from datetime import date


# File to store job applications
FILE_NAME = "applications.json"


# Load applications from file
def load_applications():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            applications = json.load(file)

        return applications

    return []


# Save applications to file
def save_applications(applications):

    with open(FILE_NAME, "w") as file:

        json.dump(applications, file, indent=4)

    print("Applications saved successfully!")


# Add a new application
def add_application(applications):

    print("\n--- Add Job Application ---")

    company = input("Enter company name: ")
    role = input("Enter job role: ")
    location = input("Enter job location: ")
    job_link = input("Enter job link: ")

    application = {

        "company": company,
        "role": role,
        "location": location,
        "job_link": job_link,
        "date": str(date.today()),
        "status": "Applied"

    }

    applications.append(application)

    save_applications(applications)

    print("Job application added successfully!")


# View all applications
def view_applications(applications):

    print("\n--- All Job Applications ---")

    if len(applications) == 0:

        print("No applications found.")

        return

    for i, application in enumerate(applications, start=1):

        print("\nApplication Number:", i)

        print("Company:", application["company"])
        print("Role:", application["role"])
        print("Location:", application["location"])
        print("Date:", application["date"])
        print("Status:", application["status"])
        print("Job Link:", application["job_link"])


# Search applications
def search_application(applications):

    print("\n--- Search Application ---")

    company_name = input("Enter company name: ")

    found = False

    for application in applications:

        if company_name.lower() in application["company"].lower():

            print("\nCompany:", application["company"])
            print("Role:", application["role"])
            print("Status:", application["status"])
            print("Date:", application["date"])

            found = True

    if not found:

        print("No matching application found.")


# Update application status
def update_application(applications):

    print("\n--- Update Application Status ---")

    view_applications(applications)

    if len(applications) == 0:

        return

    try:

        number = int(input("\nEnter application number: "))

        if number < 1 or number > len(applications):

            print("Invalid application number.")

            return

        print("\nChoose new status:")

        print("1. Applied")
        print("2. Interview")
        print("3. Selected")
        print("4. Rejected")

        choice = input("Enter choice: ")

        statuses = {

            "1": "Applied",
            "2": "Interview",
            "3": "Selected",
            "4": "Rejected"

        }

        if choice in statuses:

            applications[number - 1]["status"] = statuses[choice]

            save_applications(applications)

            print("Status updated successfully!")

        else:

            print("Invalid status choice.")

    except ValueError:

        print("Please enter a valid number.")


# Delete application
def delete_application(applications):

    print("\n--- Delete Application ---")

    view_applications(applications)

    if len(applications) == 0:

        return

    try:

        number = int(input("\nEnter application number: "))

        if number < 1 or number > len(applications):

            print("Invalid application number.")

            return

        removed = applications.pop(number - 1)

        save_applications(applications)

        print("Deleted application:", removed["company"])

    except ValueError:

        print("Please enter a valid number.")


# Show statistics
def show_statistics(applications):

    print("\n--- Application Statistics ---")

    total = len(applications)

    applied = 0
    interview = 0
    selected = 0
    rejected = 0

    for application in applications:

        status = application["status"]

        if status == "Applied":

            applied += 1

        elif status == "Interview":

            interview += 1

        elif status == "Selected":

            selected += 1

        elif status == "Rejected":

            rejected += 1

    print("Total Applications:", total)
    print("Applied:", applied)
    print("Interviews:", interview)
    print("Selected:", selected)
    print("Rejected:", rejected)


# Main program
def main():

    applications = load_applications()

    while True:

        print("\n========== JOBTRACK ==========")

        print("1. Add Application")
        print("2. View Applications")
        print("3. Search Application")
        print("4. Update Status")
        print("5. Delete Application")
        print("6. Show Statistics")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            add_application(applications)

        elif choice == "2":

            view_applications(applications)

        elif choice == "3":

            search_application(applications)

        elif choice == "4":

            update_application(applications)

        elif choice == "5":

            delete_application(applications)

        elif choice == "6":

            show_statistics(applications)

        elif choice == "7":

            print("Thank you for using JobTrack!")

            break

        else:

            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":

    main()
