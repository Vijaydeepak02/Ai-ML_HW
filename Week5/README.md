
# Student Pass/Fail Prediction

## 1. Problem Statement
Predict whether a student will pass or fail based on study hours and attendance.

## 2. Dataset Summary
- Records: 10
- Features: Hours, Attendance
- Target: Pass (0 = Fail, 1 = Pass)

## 3. Preprocessing
- Created a Pandas DataFrame.
- Separated features (X) and target (y).
- Split data into 70% training and 30% testing.
- Used stratified splitting to preserve class proportions.

## 4. Models Used
- Decision Tree Classifier
- Random Forest Classifier

## 5. Evaluation Metric
Accuracy was used to compare the models.

## 6. Conclusion
The model with the higher test accuracy was selected.
The small dataset is for learning purposes and is not
sufficient to establish real-world model performance.
