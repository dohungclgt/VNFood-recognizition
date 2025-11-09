import hashlib, json, os

def get_cache_key(image_bytes: bytes):
    return hashlib.md5(image_bytes).hexdigest()

def load_cache(key: str):
    path = f"cache/{key}.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_cache(key: str, result):
    os.makedirs("cache", exist_ok=True)
    with open(f"cache/{key}.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
