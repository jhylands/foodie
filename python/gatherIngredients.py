from recipe_scrapers import BBCGoodFood
import os
import pickle

folders = ['bbcgoodfood','bbcgoodfoodnonum','bbcgoodfooduser']
files = []
for folder in folders:
    temp_files = os.listdir(folder)
    for temp_file in temp_files:
        files.append("%s/%s"%(folder,temp_file))
#files now contains all 20,800 recipes
recipes = []
for file_ in files:
    with open(file_,'r') as f:
        recipe = BBCGoodFood(f,True)
        print(recipe.title())
        recipes.append({'title':recipe.title(),'total_time':recipe.total_time(),'instructions':recipe.instructions(),'ingredients':recipe.ingredients()})

with open('recipe.pkl','wb') as f:
    pickle.dump(recipes,f)
print('fin')
    
