candidates = []

while True:
    print("\n--- Recruitment Tracker ---")
    print("1. Add Candidate")
    print("2. View Candidates")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter candidate name: ")
        status = input("Enter status (Applied / Interview / Offer / Rejected): ")

        candidate = {
            "name": name,
            "status": status
        }

        candidates.append(candidate)
        print("Candidate added successfully!")

    elif choice == "2":
        if not candidates:
            print("No candidates yet.")
        else:
            print("\nCurrent Candidates:")
            for i, c in enumerate(candidates, start=1):
                print(f"{i}. {c['name']} - {c['status']}")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
