# Student Performance Assessment System
# A simple console-based program for first-year beginners

from assessment import evaluate_performance
from report import print_report


def main():
    print("==============================================")
    print("     STUDENT PERFORMANCE ASSESSMENT SYSTEM    ")
    print("==============================================")
    print()

    name = input("Enter Student Name            : ")
    attendance = float(input("Enter Attendance Percentage (%): "))
    marks = float(input("Enter Average Marks (%)       : "))

    risk_level, recommendation = evaluate_performance(attendance, marks)
    print_report(name, attendance, marks, risk_level, recommendation)


if __name__ == "__main__":
    main()
