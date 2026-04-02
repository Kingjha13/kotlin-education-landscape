import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/universities.csv")

df.columns = df.columns.str.strip()

print("Total courses:", len(df))

print("\nTop countries:")
print(df["country"].value_counts())

print("\nCourse levels:")
print(df["course_level"].value_counts())

print("\nSubject areas:")
print(df["subject_area"].value_counts())

print("\nTeaching styles:")
print(df["teaching_style"].value_counts())

df["country"].value_counts().plot(kind="bar")
plt.title("Kotlin Courses by Country")
plt.show()

df["subject_area"].value_counts().plot(kind="bar")
plt.title("Kotlin Subject Areas")
plt.show()