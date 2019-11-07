#!/usr/bin/python

# import math




# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
def recipe_batches(recipe, ingredients):
    batch_count = 0
    l = []
    for i in recipe:
        print("key: ", i)
        if i in ingredients:
            needed = recipe[i]
            have = ingredients[i]
            batches = 0
            if needed <= have:
                while needed <= have:
                    have -= needed
                    batches += 1
                    print("we have =>", have)
                    print("batches =>", batches)
            else:
                break

            l.append(batches)
        else:
            l.append(0)
    print(l)
    batch_count = min(l)

    return batch_count

    



        
        








  # print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))