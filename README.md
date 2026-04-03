
# 🎬 Movie Backend API (FastAPI)

A lightweight backend API built with FastAPI that fetches movie data using the OMDb API.  
This API powers a full-stack movie search application.

---

## 🚀 Features

- 🔍 Search movies by name
- 🎬 Get detailed movie information by IMDb ID
- ⚡ FastAPI for high performance APIs
- 🌐 Deployed on Render
- 🔐 Environment-based API key handling

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn
- Requests
- Python-dotenv
- OMDb API

---

## 📦 API Endpoints

### 🔹 Home  
**GET /**  
Returns API status

**Response:**
```json
{
  "message": "Movie Backend API is running 🚀"
}
````

---

### 🔹 Search Movies

**GET /search?query=movie_name**

**Example:**

```
/search?query=avengers
```

**Response:**

```json
{
  "Search": [
    {
      "Title": "The Avengers",
      "Year": "2012",
      "imdbID": "tt0848228",
      "Type": "movie",
      "Poster": "URL"
    }
  ]
}
```

---

### 🔹 Movie Details

**GET /movie/{movie_id}**

**Example:**

```
/movie/tt0848228
```

**Response:**

```json
{
  "Title": "The Avengers",
  "Year": "2012",
  "Genre": "Action, Sci-Fi",
  "Director": "Joss Whedon",
  "Actors": "Robert Downey Jr., Chris Evans",
  "Plot": "Earth's mightiest heroes must come together...",
  "imdbRating": "8.0"
}
```

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/moningi-nidhi25/movie-backend.git
cd movie-backend
```

---

### 2️⃣ Create Virtual Environment (using uv)

```bash
uv venv
```

Activate it:

* Windows:

```bash
.venv\Scripts\activate
```

* Mac/Linux:

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
uv pip install fastapi uvicorn requests python-dotenv
```

---

### 4️⃣ Add Environment Variables

Create a `.env` file in the root directory:

```
OMDB_API_KEY=your_api_key_here
```

👉 Get API key from: [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx)

---

### 5️⃣ Run the Server

```bash
uv run uvicorn main:app --reload
```

---

### 6️⃣ Open in Browser

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌍 Live API

👉 [https://movie-backend-xew0.onrender.com](https://movie-backend-xew0.onrender.com)

---

## ⚠️ Notes

* ⏳ Render free tier may take ~30–50 seconds to wake up (cold start)
* ❗ Ensure API key is valid to avoid errors

---

## 💡 Future Improvements

* 🔐 Authentication (JWT)
* ⚡ Caching (Redis)
* 📊 Logging & monitoring
* 🚫 Rate limiting
* 📄 Pagination support

---

