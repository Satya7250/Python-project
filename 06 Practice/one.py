# cse college details methods
def cse_college_details():
    # Static data for college details
    college_info = {
        "College Name": "Katihar College of Engineering",
        "Location": "Katihar, Bihar"
    }

    # Print college details
    print("\nCollege Details")
    print(f"{'College Name':<20}: {college_info['College Name']}")
    print(f"{'Location':<20}: {college_info['Location']}")


def cse_faculty_details():
    # Static data for faculty
    faculty_info = {
        "Dr. Smith": "Computer Science",
        "Dr. Johnson": "Mathematics",
        "Dr. Williams": "Physics",
        "Dr. Brown": "Chemistry",
        "Dr. Jones": "Biology"
    }

    # Print faculty details
    print("\nFaculty Details")
    print(f"{'Faculty Name':<20} {'Department':<20}")
    print("-" * 40)  # Separator line
    
    # Print each faculty name and department
    for name, department in faculty_info.items():
        print(f"{name:<20} {department:<20}")
