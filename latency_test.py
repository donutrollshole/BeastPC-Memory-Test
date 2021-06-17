def latency_test():
    import time

    cycles = 2650  # This many cycles on M1 Macbook Air returns latency similar to AIDA

    # creating test list of length cycles
    test_list = []
    for i in range(cycles):
        test_list.append(str(i)) #random string
    
    # testing total latency time by finding average over cycles1 tries
    totallatencytime = 0
    cycles1 = 3000
    for i in range(cycles1):
        initial = time.process_time_ns()
        for i in range(cycles):
            test_list[i]
        final = time.process_time_ns()
        alltime = final - initial
        totallatencytime += alltime
    alltime = totallatencytime/cycles1

    #finding the time spent processing iterations, by finding average over cycles2 tries
    totaliterationtime = 0
    cycles2 = 3000
    for i in range(cycles1):
        iterationinitial = time.process_time_ns()
        for i in range(cycles):
            pass
        iterationfinal = time.process_time_ns()
        iterationtime = iterationfinal - iterationinitial
        totaliterationtime += iterationtime
    iterationtime = totaliterationtime/cycles1

    #creating output: total time minus time spent iterating
    output = alltime - iterationtime
    output = int(output/1000)
    return(output)

#perform the latency test iterations times and find the average
total_time = 0
iterations = 10
for i in range(iterations):
    total_time += latency_test()
avg_time = str(total_time/iterations)

print(avg_time + 'ns')