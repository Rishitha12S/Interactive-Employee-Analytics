import pandas as pd
import streamlit as st
import plotly.express as px

# Page Title
st.title("Employee Performance Dashboard")

# Load Data
df = pd.read_csv("data/employee_performance_data.csv")

# Sidebar Filter
st.sidebar.header("Dashboard Filters")

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(df["Department"].unique())
)

# Apply Filter
if department != "All":
    filtered_df = df[df["Department"] == department]
else:
    filtered_df = df

# KPI Metrics
total_tasks = filtered_df["Tasks_Completed"].sum()
avg_attendance = filtered_df["Attendance"].mean()
avg_score = filtered_df["Performance_Score"].mean()

# Display KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Tasks", total_tasks)
col2.metric("Average Attendance", f"{avg_attendance:.2f}%")
col3.metric("Average Performance", f"{avg_score:.2f}")

# Tasks Trend
st.subheader("Monthly Task Completion Trend")

task_chart = px.line(
    filtered_df,
    x="Month",
    y="Tasks_Completed",
    color="Department",
    markers=True,
    title="Tasks Completed Over Time"
)

st.plotly_chart(task_chart)

# Attendance Chart
st.subheader("Attendance Analysis")

attendance_chart = px.bar(
    filtered_df,
    x="Department",
    y="Attendance",
    color="Department",
    title="Department Attendance"
)

st.plotly_chart(attendance_chart)

# Performance Score Pie Chart
st.subheader("Performance Distribution")

performance_chart = px.pie(
    filtered_df,
    names="Department",
    values="Performance_Score",
    title="Performance Score Share"
)

st.plotly_chart(performance_chart)

# Employee Table
st.subheader("Employee Performance Data")
st.dataframe(filtered_df)