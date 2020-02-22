def collision(speed, pos):
    particles = len(speed)
    crash = 0

    for i in range(pos):
        if speed[i] > speed[pos]:
            crash += 1

    for i in range(pos+1, particles):
        if speed[i] < speed[pos]:
            crash += 1
    
    return crash