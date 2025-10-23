# ✈️ Flight Data Analytics Dashboard  

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Built%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> An interactive **Streamlit dashboard** connected to a **MySQL database** that lets users explore flight data — visualize routes, airline frequency, and date-wise trends with rich charts and tables.  

---

## 🚀 Features  

- 🧭 **Dynamic Dropdown Selection** – Choose **source** and **destination** airports interactively.  
- 📊 **Flight Results Display** – View all available flights in a **dataframe** after selection.  
- 🛫 **Airline Analytics** –  
  - Retrieve airline names with frequency counts.  
  - Visualized using a **Pie Chart**.  
- 🏙️ **Airport Insights** –  
  - Fetch city-wise airport data and flight counts.  
  - Displayed in a **Bar Chart**.  
- 📅 **Date-Wise Analysis** –  
  - Fetch daily flight frequencies.  
  - Shown in a **Line Chart** to observe trends.  
- 🔐 **Secure Database Connection** –  
  - Credentials stored in **environment variables**.  
  - Managed via a **Database Helper Class** for clean architecture.  

---

## 🧠 Tech Stack  

| Layer | Technology |
|:------|:------------|
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **Backend** | Python |
| **Database** | MySQL |
| **Visualization** | Plotly / Matplotlib |
| **Data Handling** | Pandas |
| **Security** | Environment Variables (`os`, `dotenv`) |

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/<your-username>/flight-analytics-dashboard.git
cd flight-analytics-dashboard
