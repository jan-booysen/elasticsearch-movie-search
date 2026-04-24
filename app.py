from fastapi import FastAPI
from elasticsearch import Elasticsearch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Correct connection for ES 8+/9+
es = Elasticsearch(
    "http://localhost:9200",
    verify_certs=False,
    request_timeout=30
)


@app.get("/")
def root():
    return {"message": "Movie Search API running"}


@app.get("/test")
def test():
    try:
        res = es.info()
        return res.body
    except Exception as e:
        return {"error": str(e)}


@app.get("/search")
def search_movies(q: str, page: int = 1, size: int = 10):
    from_ = (page - 1) * size

    try:
        res = es.search(
            index="movies",
            from_=from_,
            size=size,
            query={
                "match": {
                    "title": {
                        "query": q,
                        "fuzziness": "AUTO"
                    }
                }
            }
        )

        return {
            "total": res.body["hits"]["total"]["value"],
            "results": [hit["_source"] for hit in res.body["hits"]["hits"]]
        }

    except Exception as e:
        return {"error": str(e)}