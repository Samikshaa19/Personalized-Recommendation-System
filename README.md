# **AMIGOS - Personalized Event Recommendation System** 🎉  

A powerful recommendation system that suggests events based on user web browsing history and intra-website browsing patterns.  

## 🚀 **Key Features**  

- 🔥 **Trending Events**: Displays trending events and trending events by category.  
- 🏷 **Keyword Extraction**: Uses the **TF-IDF algorithm** to extract keywords from event titles and descriptions.  
- 🔗 **Event Similarity Calculation**: Computes event similarities to enhance recommendations.  
- 📌 **Personalized Event Recommendations**:  
  - Based on past intra-website searches.  
  - Based on intra-website browsing patterns.  
  - Matches user web history with events for personalized suggestions.  
- 🌍 **Local Event Recommendations**: Suggests events based on user location.  

---

## 🛠 **Technology Stack**  


<img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/> <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/> <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/> <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/> <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/> <img alt="SASS" src="https://img.shields.io/badge/SASS-hotpink.svg?style=for-the-badge&logo=SASS&logoColor=white"/> 

---

## 🏢 **Project Setup & Installation**  

### 1⃣ Clone the Repository  
```sh
git clone https://github.com/Samikshaa19/Personalized-Recommendation-System.git
cd Personalized-Recommendation-System
```

### 2⃣ Set Up Virtual Environment (Recommended)  
```sh
python -m venv myenv
source myenv/bin/activate  # (Linux/macOS)
myenv\Scripts\activate      # (Windows)
```

### 3⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```
Or install them manually:  
```sh
pip install pandas scikit-learn geopandas geopy folium
```

### 4⃣ Run Migrations  
Once all the dependencies are installed, ensure the database is in the correct state by running:  
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5⃣ Populate Database with Event Data  
The GitHub repository contains **pre-calculated event similarities and extracted keywords**.  
If using a **new dataset (CSV)**, run the scripts below **before** executing the project:  

```sh
python add_events_data_to_models_from_csv.py
python add_categories_to_events.py 
python add_keywords_to_events.py
python add_similarity_to_events.py
```

### 6⃣ Start the Development Server  
Run the following command:  
```sh
python manage.py runserver <port-number>
```
- `<port-number>` is optional, but the **default port (8000) is recommended**.  
- The **History Extractor Extension** is configured to work on port **8000**. If you change the port, update the extension settings accordingly.  

---

## 🔍 **Personalized Recommendations via Chrome Extension**  

To enable personalized recommendations, install the **History Extractor Extension** in Google Chrome:  

1. Open **Google Chrome** and go to **Settings**.  
2. Navigate to **Extensions** from the left-hand menu.  
3. Enable **Developer Mode** (top-right corner).  
4. Click **Load Unpacked**.  
5. Select the `history_extractor_extension` folder from the project directory.  

🎉 **The browser extension is now installed and ready to enhance recommendations!**  

---

## ✅ **The Project is Now Ready to Run!** 🚀  
