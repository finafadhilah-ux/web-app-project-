import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 

# Set page configuration
st.set_page_config(layout="wide")

def display_graph_properties(G):
    """Displays graph properties: Degree and Adjacency Matrix."""
    
    st.subheader("📊 Graph Properties")

    # 1. Degree
    st.markdown("#### Degree of Each Node")
    degrees = dict(G.degree())
    degree_df = pd.DataFrame(degrees.items(), columns=['Node', 'Degree'])
    st.dataframe(degree_df, use_container_width=True)

    # 2. Adjacency Matrix
    st.markdown("#### Adjacency Matrix")
    
    # Fix for previous 'todense' error: using .toarray() and pd.DataFrame
    try:
        # Convert NetworkX Sparse Matrix to a NumPy array, then to a Pandas DataFrame
        adj_matrix_np = nx.adjacency_matrix(G).toarray()
        adj_matrix = pd.DataFrame(
            adj_matrix_np, 
            index=list(G.nodes()), 
            columns=list(G.nodes())
        )
        st.dataframe(adj_matrix, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error calculating Adjacency Matrix: {e}")


def draw_graph(G):
    """Draws the graph using Matplotlib and standard NetworkX function."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Define the visual layout of the graph
    pos = nx.spring_layout(G, seed=42)
    
    # FIX for 'draw_nodes' error: Use nx.draw_networkx() which is more stable
    # This single function handles nodes, edges, and labels
    nx.draw_networkx(
        G, 
        pos, 
        node_size=3000, 
        node_color="#ADD8E6", 
        edgecolors="black", 
        linewidths=1.5, 
        width=2, 
        alpha=0.6, 
        edge_color="gray", 
        with_labels=True, # Display node labels
        font_size=12, 
        font_weight="bold", 
        ax=ax
    )
    
    ax.set_title("Random Graph Visualization")
    st.pyplot(fig) 

# --- MAIN STREAMLIT APP ---

st.header("✨ Graph Visualization (Discrete Mathematics)")
st.markdown("This application demonstrates simple graph visualization and its basic properties.")
st.markdown("---")

# User input for Node and Edge count
col1, col2 = st.columns(2)

with col1:
    num_nodes = st.number_input(
        "Enter Number of Nodes (Vertices):", 
        min_value=2, 
        max_value=15, 
        value=5, 
        step=1
    )

with col2:
    max_edges = int(num_nodes * (num_nodes - 1) / 2)
    num_edges = st.number_input(
        "Enter Number of Edges (Sides):", 
        min_value=0, 
        max_value=max_edges, 
        value=min(6, max_edges),
        step=1
    )

if st.button("Generate Graph"):
    if num_edges > max_edges:
        st.error(f"The number of edges exceeds the maximum limit ({max_edges}) for {num_nodes} nodes.")
    else:
        # 1. Create Graph
        try:
            # Use nx.gnm_random_graph(n, m) to create a random graph with n nodes and m edges
            G = nx.gnm_random_graph(num_nodes, num_edges, seed=42)
            
            st.success("Graph created successfully!")
            
            # 2. Draw Graph
            draw_graph(G)
            
            # 3. Display Properties
            display_graph_properties(G)
            
        except Exception as e:
            st.error(f"An error occurred while creating the graph: {e}")

st.markdown("---")
st.caption("Using NetworkX and Streamlit for Graph Theory demonstration.")