# 🎬 Elasticsearch Movie Search

A full-stack movie search application built with Elasticsearch, FastAPI, and a lightweight frontend.

## 🚀 Features

* 🔍 Fuzzy search (handles typos like "interstelar" → "Interstellar")
* 📄 Pagination (using from + size)
* ⚡ Fast search powered by Elasticsearch
* 🎥 Real dataset (~87k movies from MovieLens)
* 🌐 Simple frontend UI

## 🧱 Tech Stack

* Backend: FastAPI (Python)
* Search Engine: Elasticsearch
* Frontend: HTML, CSS, JavaScript
* Data: MovieLens dataset

## 🏗️ Architecture

Browser → FastAPI → Elasticsearch → Results → UI

## ▶️ How to Run

### 1. Start Elasticsearch (Docker)

```bash
docker run -d --name elasticsearch -p 9200:9200 \
-e "discovery.type=single-node" \
-e "xpack.security.enabled=false" \
docker.elastic.co/elasticsearch/elasticsearch:8.13.4
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run API

```bash
uvicorn app:app --reload
```

### 4. Open frontend

Open:

frontend/index.html

## 🔎 Example

Search:

```
interstelar
```

Result:

```
Interstellar (2014)
```

## 📌 Notes

* Uses fuzzy matching (Levenshtein distance)
* Designed as a simple demo of real-world search functionality

## 💡 Future Improvements

* Autocomplete (search-as-you-type)
* Movie posters (OMDb/TMDb integration)
* Filters (genre, year)
* Deployment (public demo)

## 👤 Author

Jan
