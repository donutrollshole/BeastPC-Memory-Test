import tkinter as tk
import time

# Backbone algorithms for the latency test:

def latency_test():
    cycles = 2650  # This many cycles on M1 Macbook Air returns latency similar to AIDA

    # creating test list of length cycles
    test_list = []
    for i in range(cycles):
        test_list.append(str(i)) #random string
    
    # cycles1 and cycles2 are chosen for a balance of runtime and precision
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
def run_latency_test(iterations):
    total_time = 0
    for i in range(iterations):
        total_time += latency_test()
    avg_time = str(total_time/iterations)
    return avg_time


# GUI for the latency test:

root = tk.Tk()

# resizing window
canvas = tk.Canvas(root, width = 300, height = 300)
canvas.grid(columnspan = 4, rowspan = 4)

# title
title = tk.Label(root, text = "Memory Latency Test\n" + "Please allow 10 seconds for test to complete")
title.grid(columnspan=3, column=0, row=1)

# what to do when test starts
def start_test():
    #test_button_text.set("Testing...")
    result = run_latency_test(10)
    result = str(result) + 'ns'
    output_result = tk.Label(root, text = result)
    output_result.grid(column=1, row = 3)
    test_button_text.set("Test")


# create "Test" button
test_button_text = tk.StringVar()
test_button = tk.Button(root, command=lambda:start_test(), textvariable=test_button_text, height=2, width=15)
test_button_text.set("Test")
test_button.grid(column=1, row=2)

root.mainloop()