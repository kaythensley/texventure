print('It is dark. You may be eaten by a grue')
print('You are standing in a hallway. It stretches off into the distance in both directions.')
print('Options:')
print('1 - Left')
print('2 - Right')
input_value = input("Enter choice:")
if input_value == '1':
    print('You turn to the left.')
    print('After twenty paces you fall through a crack in the floor.')
    print('You are dead.')
elif input_value == '2':
    print('You turn to the right.')
    print('After twenty paces a painting falls off the wall and crushes you.')
    print('You are dead.')
print("Game under construction. Come back later")
