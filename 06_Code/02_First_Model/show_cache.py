from huggingface_hub import scan_cache_dir

cache = scan_cache_dir()

print(cache)