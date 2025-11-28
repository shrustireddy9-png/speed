import sys

def get_speed_info(distance, time):
    if time == 0:
        return "Error: Time cannot be zero."

    speed = distance / time

    return (
        f"Distance: {distance}\n"
        f"Time: {time}\n"
        f"Speed: {speed}"
    )


if _name_ == "_main_":
   
    if len(sys.argv) == 3:
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
    else:
        
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))

    print(get_speed_info(distance, time))
