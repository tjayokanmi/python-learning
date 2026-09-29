# The function should return a new profile with an extra tag. 
# The original profile and its tags must stay unchanged. 
# The profile has only a string name and a list of string tags; both keys always exist.
def add_tag(profile, tag):
    updated = profile[:]
    updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])

QGQSRF