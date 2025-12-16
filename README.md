# 🌍 Global Trade Analytics Suite

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tradesuite.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive analytics platform for visualizing international trade patterns, analyzing market trends, and forecasting future trade volumes using AI-driven predictive modeling.

### 🚀 **Live Demo:** [https://tradesuite.streamlit.app/](https://tradesuite.streamlit.app/)

---

## 📊 Key Features

*   **🌐 Interactive 3D Geospatial Intelligence**: 
    *   3D Orthographic globe visualization of trade flows.
    *   Detailed hover analytics for Import/Export volumes per country.
    *   Premium dark-themed UI for enhanced readability and aesthetics.

*   **📈 Temporal Market Analysis**:
    *   Historical trend analysis identifying seasonal patterns.
    *   Category-wise performance segmentation.
    *   Interactive time-series charts powered by Plotly.

*   **🤖 AI-Driven Forecasting Engine**:
    *   **Predictive Model**: Random Forest Regressor implementation.
    *   **High Accuracy**: Achieves ~88% R² score in trade volume prediction.
    *   **Real-time Validation**: On-demand model training and performance metrics (MAE, R²).

## 🛠️ Tech Stack

*   **Frontend/Dashboard**: [Streamlit](https://streamlit.io/)
*   **Data Analysis**: Pandas, NumPy
*   **Visualization**: Plotly Express (Interactive 3D Maps & Charts)
*   **Machine Learning**: Scikit-learn (Random Forest Regressor)

## 📂 Project Structure

```bash
Global-Trade-Analytics-Suite/
├── app.py                # Main Streamlit Application
├── requirements.txt      # Project Dependencies
├── README.md             # Project Documentation
├── src/
│   ├── analysis.py       # Data Aggregation & Logic
│   ├── config.py         # App Configuration & Constants
│   ├── generate_data.py  # Synthetic Data Generator
│   └── model.py          # Machine Learning Model
└── data/                 # Data Storage (Generated CSVs)
```

## 🚀 Getting Started

### Prerequisites
*   Python 3.8 or higher
*   Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/mohansree14/Global-Trade-Analytics-Suite.git
    cd Global-Trade-Analytics-Suite
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    streamlit run app.py
    ```
    The application will automatically generate synthetic training data on the first run.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
