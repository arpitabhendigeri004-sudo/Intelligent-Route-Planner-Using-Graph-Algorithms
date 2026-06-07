# 🗺️ Intelligent Route Planner Using Graph Algorithms

An interactive route optimization dashboard built using **Python, Streamlit, NetworkX, BFS, DFS, and Dijkstra's Algorithm**. The project simulates how navigation and logistics systems find the most efficient route between locations.

---

## 🚀 Features

✅ Graph-Based Road Network

✅ BFS Traversal

✅ DFS Traversal

✅ Dijkstra's Shortest Path Algorithm

✅ Traffic Simulation (Normal / Moderate / Heavy)

✅ Route Visualization

✅ Route History Tracking

✅ Analytics Dashboard

✅ Download Route Report

✅ Interactive Streamlit UI

---

## 📌 Problem Statement

Finding the shortest and most efficient route between locations is a common problem in:

- Google Maps
- Uber
- Ola
- Swiggy
- Zomato
- Logistics & Delivery Systems
- Smart Transportation Systems

This project models a city as a graph where:

- Locations → Nodes
- Roads → Edges
- Distance → Edge Weight

The system computes the optimal route using Dijkstra's Algorithm.

---

## 🧠 DSA Concepts Used

### Graph

Road network represented using an adjacency list.

### BFS (Breadth First Search)

Traverses locations level by level.

### DFS (Depth First Search)

Explores one branch completely before backtracking.

### Dijkstra's Algorithm

Computes the shortest path between source and destination.

### Priority Queue (Min Heap)

Used internally to optimize shortest path computation.

---

## 🏗️ Project Architecture

```text
User Input
     │
     ▼
Source & Destination
     │
     ▼
Graph Representation
(Adjacency List)
     │
     ▼
Dijkstra Algorithm
     │
     ▼
Shortest Route
     │
     ▼
Route Analytics & Visualization
```

---

## 📂 Folder Structure

```text
Intelligent-Route-Planner-Using-Graph-Algorithms/
│
├── data/
├── docs/
├── images/
├── outputs/
│
├── src/
│   ├── dashboard.py
│   ├── city_data.py
│   ├── dijkstra.py
│   ├── graph_visualizer.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Intelligent-Route-Planner-Using-Graph-Algorithms.git

cd Intelligent-Route-Planner-Using-Graph-Algorithms
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run src/dashboard.py
```

---

## 📍 Sample Route

### Input

```text
Source: Airport
Destination: University
Traffic: Normal
```

### Output

```text
Shortest Route:

Airport
   ↓
BusStation
   ↓
RailwayStation
   ↓
University

Distance: 11 km

ETA: 33 minutes
```

---

## 📊 Dashboard Modules

### 🏠 Home

- Project Overview
- Metrics
- Statistics

### 📍 Find Route

- Source Selection
- Destination Selection
- Traffic Simulation
- Route Calculation

### 🌐 Graph View

- Visual Road Network
- Connected Nodes
- Edge Weights

### 📊 Analytics

- Distance Analysis
- Traffic Distribution
- Route Dataset

### 📜 Route History

- Previously Calculated Routes
- Clear History Option

### 🔄 BFS Traversal

Traversal demonstration using BFS.

### 🧭 DFS Traversal

Traversal demonstration using DFS.

---

## 📸 Screenshots
<img width="960" height="540" alt="ss1" src="https://github.com/user-attachments/assets/c113cd95-aaa0-4312-b178-977d1d719187" />
<img width="960" height="540" alt="ss2" src="https://github.com/user-attachments/assets/33e14336-0e19-4fb7-a56e-f50b4f192779" />
<img width="960" height="540" alt="ss3" src="https://github.com/user-attachments/assets/63269b38-c652-41ab-8d76-93b08d7fba59" />
<img width="960" height="540" alt="ss4" src="https://github.com/user-attachments/assets/e37c3cf2-7879-48ce-a9c1-9b4a80c40f9c" />
<img width="960" height="540" alt="ss5" src="https://github.com/user-attachments/assets/91207be6-1d45-40d3-a5b7-317a649869ee" />
<img width="960" height="540" alt="ss6" src="https://github.com/user-attachments/assets/0fb98679-da5a-4552-8cf2-7b4ce7d046f7" />
<img width="960" height="540" alt="ss7" src="https://github.com/user-attachments/assets/9cd6d824-1e93-4628-95c0-a3c6d0a2b618" />
<img width="960" height="540" alt="ss8" src="https://github.com/user-attachments/assets/1e6e3207-6c68-4b57-a8d5-c7bf3fdcb58e" />
<img width="960" height="540" alt="ss9" src="https://github.com/user-attachments/assets/b39306e9-ff44-4255-9099-0bdc4b8d7ce8" />






## 🌍 Real World Applications

- Navigation Systems
- Ride Sharing Platforms
- Delivery Routing
- Logistics Optimization
- Smart Cities
- Public Transportation
- Campus Navigation


---

## 🎯 Learning Outcomes

Through this project, I learned:

- Graph Data Structures
- Adjacency Lists
- BFS and DFS Traversals
- Dijkstra's Algorithm
- Priority Queues
- Route Optimization
- Streamlit Dashboard Development
- Data Visualization
- Git & GitHub Workflow

---

## 💻 Tech Stack

- Python
- Streamlit
- NetworkX
- Matplotlib
- Pandas

---

## 👨‍💻 Author

**Arpita Bhendigeri**


If you found this project useful, consider giving it a ⭐ on GitHub.
