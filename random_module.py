import random 

#floating Value between 0 and 1 
value = random.random()

#floating value between given range
value = random.uniform(1,10)

#integers value between given range
value = random.randint(1,6) 
print(value)


#random choicing 
greetings = ["helo","konichiwa","hola amigo"]
value = random.choice(greetings)
print(value+"!! from abhinav ")

#many random choices for a list 
value = random.choices(greetings,k=10)#choices method repeat values 

#adding weighs or probability of getting selected 
value = random.choices(greetings,weights=[18,18,2])
print(value)

#selectring from a range of numbers and also shuffling it 
deck = range(1,53)
deck = list(range(1,53))
random.shuffle(deck) 
value = random.choice(deck)
print(value)

#slectring unique elements from the deck
value = random.sample(deck,k=10)
print(value)