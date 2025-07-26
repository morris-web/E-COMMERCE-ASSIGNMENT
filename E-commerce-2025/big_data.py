import os
import json
import sys

try:
    import meilisearch
except ImportError:
    print("meilisearch package not found. Please install it with 'pip install meilisearch'.")
    sys.exit(1)

DATASET_PATH = "dataset.json"
MEILI_URL = "http://localhost:7700"
MEILI_KEY = "_r0BYxHVyU7qvaNaedwC0fr9As-fFrgGFYv52hL8IFQ"
INDEX_NAME = "products"

# 1. Check if dataset.json exists
if not os.path.exists(DATASET_PATH):
    print(f"Error: {DATASET_PATH} not found in {os.getcwd()}")
    sys.exit(1)

# 2. Connect to MeiliSearch
try:
    client = meilisearch.Client(MEILI_URL, MEILI_KEY)
    index = client.index(INDEX_NAME)
except Exception as e:
    print(f"Error connecting to MeiliSearch: {e}")
    sys.exit(1)

# 3. Set searchable attributes
try:
    index.update_searchable_attributes(["product_category", "product_clicked", "country", "gender"])
except Exception as e:
    print(f"Error updating searchable attributes: {e}")

# 4. Load and add documents
try:
    with open(DATASET_PATH, encoding='utf-8') as f:
        products = json.load(f)
    print(f"Loaded {len(products)} records from {DATASET_PATH}")
except Exception as e:
    print(f"Error loading JSON: {e}")
    sys.exit(1)

try:
    response = index.add_documents(products)
    print("Documents added. Update ID:", response.status)
except Exception as e:
    print(f"Error adding documents to MeiliSearch: {e}")
    sys.exit(1)

# 5. Example multi-search
try:
    multi_query = [
        {"indexUid": INDEX_NAME, "q": "Electronics"},
        {"indexUid": INDEX_NAME, "q": "Beauty"}
    ]
    results = client.multi_search(multi_query)
    print("Sample multi-search results:")
    print(json.dumps(results, indent=2))
except Exception as e:
    print(f"Error performing multi-search: {e}")