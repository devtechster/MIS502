import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('SchData2013.csv', low_memory=False)

# create a scatter plot of TotalSurgeryMin vs. PatientInRoomMin
df.plot(kind='scatter', x='TotalSurgeryMin', y='PatientInRoomMin', alpha=0.5)
plt.xlabel('Total Surgery Time (min)')
plt.ylabel('Patient In Room Time (min)')
plt.title('Relationship Between Total Surgery Time and Patient In Room Time')
plt.show()

# create a bar chart of PatientType counts
df['PatientType'].value_counts().plot(kind='bar')
plt.xlabel('Patient Type')
plt.ylabel('Count')
plt.title('Number of Patients by Type')
plt.show()

df2= df[(df.PatientAge >= 20) & (df.PatientAge <= 30)]
sns.boxplot(df2.PatientAge).set_title('Box Plot :Young Patient Operated')
plt.show()

# create a boxplot of ScheduledCaseDuration by SurgicalSpecialty and PatientType using Seaborn
sns.boxplot(x='SurgicalSpecialty', y='ScheduledCaseDuration', hue='PatientType', data=df)
plt.xlabel('Surgical Specialty')
plt.ylabel('Scheduled Case Duration (min)')
plt.title('Scheduled Case Duration by Surgical Specialty and Patient Type')
plt.show()


# create a line plot of TotalSurgeryMin over time
df.plot(kind='line', x='CaseStartDate_Time', y='TotalSurgeryMin')
plt.xlabel('Case Start Date')
plt.ylabel('Total Surgery Time (min)')
plt.title('Total Surgery Time Over Time')
plt.show()

# Create a series of the counts of each surgical specialty
specialty_counts = df['SurgicalSpecialty'].value_counts()

# Create a pie chart with labels
plt.pie(specialty_counts, labels=specialty_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Surgical Specialties')
plt.axis('equal')
plt.show()

# Create a figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Plot the histograms for each column
axs[0].hist(df["PatientAge"], bins=20, color="orange")
axs[0].set_title("Patient Age")
axs[0].set_xlabel("Age (years)")
axs[0].set_ylabel("Frequency")

axs[1].hist(df["ScheduledCaseDuration"], bins=20, color="purple")
axs[1].set_title("Scheduled Case Duration")
axs[1].set_xlabel("Duration (minutes)")
axs[1].set_ylabel("Frequency")

axs[2].hist(df["TotalSurgeryMin"], bins=20, color="green")
axs[2].set_title("Total Surgery Time")
axs[2].set_xlabel("Time (minutes)")
axs[2].set_ylabel("Frequency")

# Adjust the layout and spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()