
"""
//Write a factorial that generates moves of n
"""
all_plays = [['rock'], ['paper'], ['scissors']]

  
  

def rock_paper_scissors(n):
  last_game = []
  new_ar = []
  def recursion(ar,num):
    if num == 0:
      last_game.append(ar)
      return
    for i in all_plays:
      recursion(ar+[i],num-1)
    recursion(new_ar,n)
    return last_game
  

    

   






# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')