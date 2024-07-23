import time

def my_function():
    time.sleep(2)
start_time = time.time()
my_function()             
end_time = time.time()    
execution_time = end_time - start_time 

print(f"Execution time: {execution_time}")