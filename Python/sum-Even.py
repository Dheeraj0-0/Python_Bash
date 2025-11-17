#Write a function sum_even(numbers) that returns the sum of all even numbers in a list



def sum_even(listt):
  sum = 0
  for i in listt:
    if i % 2 == 0:
      sum += i

  return sum
listt = [1,2,3,4,5,6,7,8]
print(sum_even(listt))