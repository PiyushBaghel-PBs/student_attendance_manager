

import json
import os

FILENAME = "attendance.txt"


def load_data():
  """Load data from the file at start."""
  if not os.path.exists(FILENAME):
    return []
  try:
    with open(FILENAME, "r") as f:
      return json.load(f)
  except Exception:
    return []


def save_data(students):
  """Save data to the file after every change."""
  with open(FILENAME, "w") as f:
    json.dump(students, f, indent=4)


def add_student(students):
  """Menu option 1: Add a student with unique roll number."""
  roll_input = input("Roll: ").strip()
  try:
    roll = int(roll_input)
  except ValueError:
    print("Invalid roll number format.")
    return students

  # Check for unique roll number
  for s in students:
    if s["roll"] == roll:
      print(f"Roll number {roll} already exists.")
      return students

  name = input("Name: ").strip()

  # Create student dictionary
  new_student = {"roll": roll, "name": name, "held": 0, "attended": 0}
  students.append(new_student)
  save_data(students)

  print(
      f"Student added: {roll} | {name} | Held: {new_student['held']} | Attended:"
      f" {new_student['attended']}"
  )
  return students


def mark_attendance(students):
  """Menu option 2: Mark daily attendance as present (P) or absent (A)."""
  roll_input = input("Roll: ").strip()
  try:
    roll = int(roll_input)
  except ValueError:
    print("Invalid roll number format.")
    return students

  # Find student
  student = None
  for s in students:
    if s["roll"] == roll:
      student = s
      break

  if student is None:
    print(f"Roll number {roll} not found.")
    return students

  status = input("Status (P/A): ").strip().upper()
  if status not in ["P", "A"]:
    print("Invalid status. Enter P or A.")
    return students

  student["held"] += 1
  if status == "P":
    student["attended"] += 1

  save_data(students)
  print(f"Attendance marked for {student['name']}: {status}")
  return students


def show_percentage(students):
  """Menu option 3: View each student's attendance percentage."""
  roll_input = input("Roll: ").strip()
  try:
    roll = int(roll_input)
  except ValueError:
    print("Invalid roll number format.")
    return

  student = None
  for s in students:
    if s["roll"] == roll:
      student = s
      break

  if student is None:
    print(f"Roll number {roll} not found.")
    return

  # Avoid dividing by zero when no classes are held
  if student["held"] == 0:
    print(f"{student['name']}: Attendance 0.00% (no classes held yet)")
  else:
    percentage = (student["attended"] / student["held"]) * 100
    print(f"{student['name']}: Attendance {percentage:.2f}%")


def show_shortage_list(students):
  """Menu option 4: List students below the 75% requirement."""
  if not students:
    print("No student records found.")
    return

  for s in students:
    if s["held"] == 0:
      percentage = 0.0
    else:
      percentage = (s["attended"] / s["held"]) * 100

    if percentage < 75.0:
      print(f"Below 75%: {s['roll']} | {s['name']} | {percentage:.2f}%")
    else:
      print(f"{s['name']} ({percentage:.2f}%) meets the requirement.")


def main():
  students = load_data()

  while True:
    print("\n--- Student Attendance Manager Menu ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Show Percentage")
    print("4. Show Shortage List")
    print("5. Exit")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
      students = add_student(students)
    elif choice == "2":
      students = mark_attendance(students)
    elif choice == "3":
      show_percentage(students)
    elif choice == "4":
      show_shortage_list(students)
    elif choice == "5":
      print("Exiting application. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
  main()
