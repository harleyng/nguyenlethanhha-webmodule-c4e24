# Update, Delete 
# Atomic 

import mlab 
from models.character import Character

mlab.connect ()

character = Character.objects().with_id("5c34aa66df3edc1a45c0ad9c")

# 1. Update
# 1.1 Read document 
# 1.2 Update document 

# character.update(set__rate=2, set__name="Super superman") #set__ inc__ dec__
# character.reload()
# print(character.rate)

# 2. Delete
# 2.1 Read document 
# 2.2 Delete document 

character.delete()