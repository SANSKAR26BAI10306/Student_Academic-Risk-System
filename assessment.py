def evaluate_performance(attendance, marks):
    if attendance < 75:
        return "High Risk", "Attendance is low. Must attend classes regularly."
    if marks < 50:
        return "High Risk", "Marks are low. Needs revision and practice."
    if marks < 60:
        return "Medium Risk", "Improve marks through more practice."
    return "Low Risk", "Good performance. Keep it up."