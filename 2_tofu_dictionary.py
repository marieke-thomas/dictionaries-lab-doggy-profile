# CRUD: Create
cutedoggy32 = {
  "first_name":"Tofu",
  "last_name":"Thomas", 
  "age":7, 
  "fur color":"brown", 
  "breed":"terrier", 
  "favorite toy":"squeaky carrot", 
  "weight":19, 
  "favorite activity":"long walks in the park"
}

# Read a dictionary
print(cutedoggy32["age"])

# Update a dictionary
cutedoggy32["age"] = 8
print(cutedoggy32)
# Happy birthday Tofu


# Delete
cutedoggy32.pop("favorite activity")
print(cutedoggy32)