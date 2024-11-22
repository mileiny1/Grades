def get_grade_category(grade):
    """Returns the grade category based on the input grade."""
    if grade >= 90:
        return "A", "Excellent!"
    elif grade >= 80:
        return "B", "Good job!"
    elif grade >= 70:
        return "C", "Satisfactory performance."
    elif grade >= 60:
        return "D", "Needs improvement."
    else:
        return "F", "Fail. Consider extra help."


def get_grade_input():
    """Handles the user input and ensures the grade is a valid number between 0 and 100."""
    while True:
        try:
            grade = float(input("Enter your grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Please enter a valid grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical grade.")


def main():
    """Main function to handle user interaction and display grade results."""
    print("Welcome to the Grading System!")

    # Option to input multiple grades
    while True:
        grade = get_grade_input()  # Get a valid grade from the user
        grade_letter, feedback = get_grade_category(grade)  # Determine the grade category and feedback

        # Print out the grade and feedback
        print(f"Your grade: {grade_letter}")
        print(f"Feedback: {feedback}")

        # Ask if the user wants to input another grade
        another = input("Do you want to enter another grade? (y/n): ").strip().lower()
        if another != 'y':
            print("Thank you for using the grading system!")
            break


# Run the program
main()

