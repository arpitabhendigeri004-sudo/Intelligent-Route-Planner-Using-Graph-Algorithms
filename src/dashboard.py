import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from city_data import graph
from dijkstra import dijkstra, shortest_path
from graph_visualizer import draw_graph

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Intelligent Route Planner",
    page_icon="🗺️",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    text-align:center;
}

[data-testid="stMetric"]{
    border:1px solid #333;
    border-radius:12px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE
# ==================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🗺️ Route Planner")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📍 Find Route",
        "🌐 Graph View",
        "📊 Analytics",
        "📜 Route History",
        "🔄 BFS Traversal",
        "🧭 DFS Traversal"
    ]
)

# ==================================================
# TITLE
# ==================================================

st.title("🗺️ Intelligent Route Planner")

# ==================================================
# HOME PAGE
# ==================================================

if page == "🏠 Home":

    total_roads = sum(
        len(v)
        for v in graph.values()
    ) // 2

    st.markdown("""
    ## 🚦 Route Intelligence Center

    Find optimized routes using Graph Algorithms and Dijkstra's Algorithm.
    """)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📍 Locations",
            len(graph)
        )

    with c2:
        st.metric(
            "🛣️ Roads",
            total_roads
        )

    with c3:
        st.metric(
            "⚡ Algorithm",
            "Dijkstra"
        )

    with c4:
        st.metric(
            "📈 Routes",
            len(st.session_state.history)
        )

    st.info(
        "Navigate to '📍 Find Route' to calculate the shortest path."
    )

# ==================================================
# FIND ROUTE PAGE
# ==================================================

elif page == "📍 Find Route":

    st.header("📍 Smart Route Finder")

    locations = list(graph.keys())

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox(
            "Source Location",
            locations
        )

    with col2:
        destination = st.selectbox(
            "Destination Location",
            locations
        )

    traffic = st.selectbox(
        "🚦 Traffic Condition",
        [
            "Normal",
            "Moderate",
            "Heavy"
        ]
    )

    if st.button("🚀 Find Shortest Route"):

        if source == destination:

            st.warning(
                "Source and Destination cannot be the same."
            )

        else:

            distances, previous = dijkstra(
                graph,
                source
            )

            path = shortest_path(
                previous,
                source,
                destination
            )

            if path:

                distance = distances[destination]

                if traffic == "Normal":
                    eta = distance * 3
                elif traffic == "Moderate":
                    eta = distance * 5
                else:
                    eta = distance * 8

                m1, m2, m3 = st.columns(3)

                with m1:
                    st.metric(
                        "📏 Distance",
                        f"{distance} km"
                    )

                with m2:
                    st.metric(
                        "⏱️ ETA",
                        f"{eta} min"
                    )

                with m3:
                    st.metric(
                        "📍 Stops",
                        len(path)
                    )

                st.success(
                    "Optimal Route Found"
                )

                st.markdown(
                    "### 🛣️ Route Path"
                )

                st.code(
                    " ➜ ".join(path)
                )

                # Save history

                st.session_state.history.append(
                    {
                        "Source": source,
                        "Destination": destination,
                        "Distance": distance,
                        "ETA": eta,
                        "Traffic": traffic
                    }
                )

                # Download report

                report = f"""
INTELLIGENT ROUTE PLANNER

Source: {source}

Destination: {destination}

Route:
{' ➜ '.join(path)}

Distance:
{distance} km

ETA:
{eta} min

Traffic:
{traffic}
"""

                st.download_button(
                    label="📥 Download Route Report",
                    data=report,
                    file_name="route_report.txt",
                    mime="text/plain"
                )

                st.markdown(
                    "### 🌐 Route Visualization"
                )

                fig = draw_graph(
                    graph,
                    path
                )

                st.pyplot(fig)

            else:

                st.error(
                    "No route found."
                )

# ==================================================
# GRAPH VIEW
# ==================================================

elif page == "🌐 Graph View":

    st.header(
        "🌐 Complete Road Network"
    )

    fig = draw_graph(graph)

    st.pyplot(fig)

# ==================================================
# ANALYTICS
# ==================================================

elif page == "📊 Analytics":

    st.header(
        "📊 Route Analytics"
    )

    if len(st.session_state.history) > 0:

        df = pd.DataFrame(
            st.session_state.history
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Distance Analysis"
            )

            fig, ax = plt.subplots()

            ax.bar(
                df["Destination"],
                df["Distance"]
            )

            ax.set_ylabel(
                "Distance (km)"
            )

            st.pyplot(fig)

        with col2:

            st.subheader(
                "Traffic Distribution"
            )

            traffic_count = (
                df["Traffic"]
                .value_counts()
            )

            fig2, ax2 = plt.subplots()

            ax2.pie(
                traffic_count,
                labels=traffic_count.index,
                autopct="%1.1f%%"
            )

            st.pyplot(fig2)

        st.subheader(
            "Route Dataset"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No route data available."
        )

# ==================================================
# ROUTE HISTORY
# ==================================================

elif page == "📜 Route History":

    st.header(
        "📜 Route History"
    )

    if len(st.session_state.history) > 0:

        df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        if st.button(
            "🗑️ Clear History"
        ):
            st.session_state.history = []
            st.rerun()

    else:

        st.info(
            "No routes calculated yet."
        )

# ==================================================
# BFS PAGE
# ==================================================

elif page == "🔄 BFS Traversal":

    st.header(
        "🔄 BFS Traversal"
    )

    st.code(
        "Airport ➜ BusStation ➜ Mall ➜ RailwayStation ➜ University"
    )

    st.info(
        "Breadth First Search explores nodes level by level."
    )

# ==================================================
# DFS PAGE
# ==================================================

elif page == "🧭 DFS Traversal":

    st.header(
        "🧭 DFS Traversal"
    )

    st.code(
        "Airport ➜ BusStation ➜ RailwayStation ➜ Mall ➜ University"
    )

    st.info(
        "Depth First Search explores one branch before backtracking."
    )

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.caption(
    "Built using Python • Streamlit • Graph Algorithms • Dijkstra"
)