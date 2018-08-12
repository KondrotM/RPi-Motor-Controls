from inputs import get_gamepad

def button_input():
    events = get_gamepad()
    for event in events:
        return [event.code, event.state]

def main():
    while True:
        button = button_input()
        if button[0] == "BTN_TR":
            if button[1] == 1:
                print("Motor start")
            if button[1] == 0:
                print("Motor stop")
        if button[0] == "BTN_TL":
            if button[1] == 1:
                print("Reverse start")
            if button[1] == 0:
                print("Reverse stop")
                
main()