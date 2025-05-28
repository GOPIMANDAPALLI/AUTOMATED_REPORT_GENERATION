# AUTOMATED_REPORT_GENERATION


*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : MANDAPALLI GOPI

*INTERN ID* : CT04DN1772

*DURATION* : 4-WEEKS

*MENTOR* : NEELA SANTOSH

*DESCRIPTION FOR AUTOMATED REPORT GENERATION USING (FPDF LIBRARY) FOR THE TASK* :

The given Python program is a comprehensive script designed to generate a detailed student attendance report for the year 2024 in both visual and PDF formats. It leverages three major Python libraries: FPDF, Pandas, and Matplotlib. The purpose of the program is to take a student's name and roll number as input, process and visualize their monthly attendance data, and generate a professional looking PDF report containing both a tabular representation and a line chart of the attendance.

The process begins by importing the required libraries. FPDF is used for creating the PDF report, pandas is utilized for organizing and handling tabular data, and matplotlib.pyplot is used for plotting the attendance data as a graph. The script first prompts the user to enter the student’s name and roll number. These details are essential not only for personalization but also for proper identification in the generated report.

Once the student’s details are obtained, the script defines a dictionary containing the months of the year and the corresponding attendance percentages. This dictionary is converted into a pandas DataFrame for easy data handling and manipulation. This DataFrame consists of two columns: "Months" and "Attendance". The attendance values are hard-coded, assuming they have been pre-collected for the entire year.

The next step in the program is to create a visual representation of the attendance data using Matplotlib. A line chart is generated where the x-axis represents the months and the y-axis shows the attendance percentages. The chart is styled using a red-colored, Arial font with a size of 25 to ensure readability. The plot includes grid lines for better clarity and is saved as an image file named "Attendance_chart.png". This chart visually summarizes the attendance trend throughout the year.

After the chart is created, the script proceeds to the core part: generating a PDF report. A custom class PDF is defined that inherits from FPDF. This class includes methods for adding a header and footer to each page, inserting a table that displays the monthly attendance, and embedding the previously created attendance chart. The header of the PDF includes the student’s name and the title of the report, centered at the top of the page. The footer includes page numbering.

The sales_table() method within the class is responsible for adding a table to the PDF. This table lists each month along with the corresponding attendance percentage. Although the method name refers to "sales", it has been repurposed to suit attendance data, which might be a small naming oversight. The table has two columns: one for the month and one for the attendance percentage. The insert_chart() method adds the saved attendance chart image into the PDF document at a suitable position with defined width and spacing.

Finally, the script creates an instance of the PDF class, adds a page, and inserts the introductory text, table, and chart into the report. The final PDF is saved as “Attendance_report_fpdf.pdf” in the working directory. A confirmation message is printed to notify the user of the successful generation of the report. This script is a well-rounded example of how to combine data processing, visualization, and PDF report generation in Python, making it highly useful for educational institutions and academic purposes.



*OUTPUT VIDEO FOR AUTOMATED REPORT GENERATION* :


*OUTPUT PHOTOS FOR AUTOMATED REPORT GENERATION* :


PHOTO-1 :
![Image](https://github.com/user-attachments/assets/689f4e63-41a7-4390-94a7-2cb411cf6641)
PHOTO-2 :
![Image](https://github.com/user-attachments/assets/28d236dd-5729-40f2-8d0e-d8d14f6dced2)
PHOTO-3 :
![Image](https://github.com/user-attachments/assets/baf52794-a419-4a32-bdba-92e457ee3e78)
PHOTO-4 :
![Image](https://github.com/user-attachments/assets/082ff16d-0ba0-41bd-9f12-147920f63128)


