import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a DataFrame
file_path = r"C:\Users\DIMPLE K B\Downloads\folder\sam_prac\hackathon_project\engineering_branch_data - Sheet1 (1).csv"
df = pd.read_csv(file_path)

# 1. **Which branch has the highest risk for students?**  
def highest_risk_branch(df):
    return df.loc[df["Dropout Rates (%)"].idxmax(), "Branch Name"]



# 2. **Which branch has the best mix of gender diversity and career stability?**
def best_gender_career_mix(df):
    best_mix = df.loc[(df['Gender Diversity'].apply(lambda x: int(x.split("%")[0].strip()) >= 30)) & 
                      (df['Job Market Stability'] == 'Stable')]
    return best_mix[['Branch Name', 'Gender Diversity', 'Job Market Stability', 'Placements (%)']]

# 3. **Which branch is struggling despite strong industry collaboration?**
def struggling_branch(df):
    struggling = df.loc[(df['Industry Collaboration'] == 'Strong') & 
                        (df['Current Demand'].isin(['Low', 'Very Low'])) & 
                        (df['Placements (%)'] < 75)]
    return struggling[['Branch Name', 'Industry Collaboration', 'Current Demand', 'Placements (%)']]

# Results
highest_risk = highest_risk_branch(df)
best_mix = best_gender_career_mix(df)
struggling = struggling_branch(df)

# Visualizations

# 1. Visualization for Highest Risk Branch

colors = ['red' if branch == highest_risk else 'gray' for branch in df["Branch Name"]]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 5))

# Dropout Rates Bar Chart
ax.bar(df["Branch Name"], df["Dropout Rates (%)"], color=colors, alpha=0.7)
ax.set_title("Dropout Rates Across Branches")
ax.set_xticks(range(len(df["Branch Name"])))  # Ensuring correct x-tick placement
ax.set_xticklabels(df["Branch Name"], rotation=45, ha="right")
ax.set_ylabel("Dropout Rate (%)")

# Show the plot
plt.tight_layout()
plt.show()


# 2. Visualization for Best Gender Diversity and Career Stability
plt.figure(figsize=(10, 6))
sns.barplot(x='Branch Name', y='Placements (%)', data=best_mix, palette='muted')
plt.title("Placements by Branch with Gender Diversity >= 30% and Career Stability")
plt.xlabel("Branch Name")
plt.ylabel("Placements (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Visualization for Struggling Branch Despite Strong Industry Collaboration
plt.figure(figsize=(10, 6))
sns.barplot(x='Branch Name', y='Placements (%)', data=struggling, palette='rocket')
plt.title("Placements of Branches Struggling Despite Industry Collaboration")
plt.xlabel("Branch Name")
plt.ylabel("Placements (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Output the results for reference
print("1. Branch with Highest Risk for Students:")
print(highest_risk, "\n")

print("2. Branch with Best Mix of Gender Diversity and Career Stability:")
print(best_mix, "\n")

print("3. Branch Struggling Despite Strong Industry Collaboration:")
print(struggling)
