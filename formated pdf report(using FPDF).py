
#importing FPDF,Pandas and matplotlib

from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

#importing student name from the user

STUDENT_NAME=input("Enter the Student Name : ")

#student roll_number from the user

ROLL_NUMBER=input("Enter the Student Roll_Number : ")

#overall monthly attendance of the student in 2024

print(f"{STUDENT_NAME} Monthly Attendance Report 01/01/2024 To 31/12/2024 ")

# Initialising  data from the user

data = {
    "Months": ["January", "February", "March", "April","May","June","JUly","August","September","October","November","December"],
    "Attendance": [99.9,89.0,55.4,99.0,82.9,71.8,60.2,75.0,88.9,92.6,98.4,97.9]

}
df = pd.DataFrame(data)

# Generate a student attendance into a plot

#text style,color and size

f1={'family':'arial','color':'r','size':25}

plt.figure(figsize=(20,10))
plt.plot(df["Months"], df["Attendance"], marker='o', color='blue')
plt.title(f"{STUDENT_NAME} MONTHLY ATTENDANCE REPORT 01/01/2024 To 31/12/2024 ",fontdict=f1)
plt.xlabel("Months",fontdict=f1)
plt.ylabel("Attendance(%)",fontdict=f1)
plt.grid(True)
chart_path = "Attendance_chart.png"
plt.savefig(chart_path)
plt.close()

#generation pdf report

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, f"{STUDENT_NAME} MONTHLY ATTENDANCE REPORT-2024", border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def sales_table(self, dataframe):
        self.set_font("Arial", 'B', 12)
        self.cell(50, 10, "Month", 1, 0, 'C')
        self.cell(50, 10, "Sales ($)", 1, 1, 'C')

        self.set_font("Arial", '', 12)
        for i in range(len(dataframe)):
            self.cell(50, 10, dataframe["Months"][i], 1, 0, 'C')
            self.cell(50, 10, str(dataframe["Attendance"][i]), 1, 1, 'C')

    def insert_chart(self, image_path):
        self.image(image_path, x=30, y=self.get_y() + 10, w=150)
        self.ln(80)


# Creating pdf

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "This report contains the overall attendance  of the student.")
pdf.ln(5)

# Adding  table

pdf.sales_table(df)

# Adding  chart

pdf.insert_chart(chart_path)

# Saving PDF as
pdf.output("Attendance_report_fpdf.pdf")

print("PDF report generated: Attendance_report_fpdf.pdf")
