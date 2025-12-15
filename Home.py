import streamlit as st

st.set_page_config(
    page_title="Discrete Math Project",
    layout="wide"
)

st.title("👋 Welcome to Our Project! ✨")
st.markdown("""
This application visualizes network graphs.

* **Graph Visualization:** Generate a simple graph with defined nodes and edges, and view its properties (degree and adjacency matrix).
* **Map Visualization:** Visualize a network of cities in Java Island and calculate the shortest path (Dijkstra's algorithm) between any two cities.
""")
# --- Add this code section to the end of your Home.py file ---

st.markdown("---")
st.header("📖 Application User Guide")

st.subheader("1. 'Profile' Page")
st.markdown("* This page contains static information about the team or members involved in this project.")

st.subheader("2. 'Graph Visualization' Page")
st.markdown("""
* **Function**: Demonstrates core concepts of Graph Theory.
* **How to Use**: Enter the desired number of **Nodes** and **Edges**.
* **Output**: The application generates a random graph and displays the **Degree** of each node and the corresponding **Adjacency Matrix**.
""")

st.subheader("3. 'Map Visualization' Page")
st.markdown("""
* **Main Function**: Visualization of the transportation network across cities/regencies in Java Island and calculation of the shortest path.
* **Data Source**: Location data (Nodes) and connections (Edges) are currently hardcoded within the application's source code.
* **Shortest Path Feature**: Utilizes **Dijkstra's algorithm** (implemented via the NetworkX library) to find the path with the minimum travel distance (weight) between the selected Start City and End City. The distance calculation uses the Haversine formula.
* **Output**: An interactive map highlights the shortest route found in red, along with the total distance in Kilometers (KM).
""")

st.markdown("---")
st.caption("Discrete Mathematics Course Project")