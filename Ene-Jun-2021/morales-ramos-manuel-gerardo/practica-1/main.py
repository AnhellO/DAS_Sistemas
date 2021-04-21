from vehicle import Vehicle
from bus import Bus

def fare(vehicle):
    final_amount = (vehicle.get_capacity() * 100)
    
    if isinstance(vehicle, Bus):
        return final_amount + (final_amount * 0.1)
    else:
        return final_amount

def main():
    list = [
        Vehicle(100, 200000, 4),
        Bus(90, 350000, 45),
        Vehicle(200, 300000, 8),
        Bus(100, 300000, 40),
        Vehicle(150, 250000, 2),
        Bus(95, 400000, 35),
    ]

    for x in list:
        if not isinstance(x, Bus):
            continue

        print(f"{ x }\nFare: { fare(x) } $", end="\n\n")

if __name__ == "__main__":
    main()