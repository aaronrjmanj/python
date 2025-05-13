def get_temp(): #returns float
    # Implementation needed
    pass
def set_temp(target_temp): #takes target temp as parameter, returns float
    # Implementation needed
    pass

def run_test(time_sec): #input string
    # Implementation needed
    pass

import time

test = {100:"12.2", 20:"20.5"} #temp:time to run the test in that temp

current_temp = get_temp()
current_temp = 30.8 # setting the temp manually for the ease of coding

for target_temp, test_time in test.items():
    print(f"Target temperature: {target_temp}°C, Test time: {test_time} seconds")
    
    if target_temp != current_temp:
        print(f"Setting temperature to {target_temp}°C")
        set_temp(target_temp)
        current_temp = target_temp ## again adding this line for the coding flow
        # Wait for temperature to reach target
        while abs(current_temp - target_temp) > 0.5:  # 0.5°C tolerance
            print(f"\nCurrent temperature: {current_temp}°C, waiting to reach {target_temp}°C...")
            time.sleep(5)  # Check every 5 seconds
            current_temp = get_temp()  # Get updated temperature
    
    print(f"\n\nTemperature reached {target_temp}°C. Running test for {test_time} seconds...")
    run_test(test_time)
    print(f"Test completed at {target_temp}°C")
