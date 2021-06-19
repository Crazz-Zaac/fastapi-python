from collections import namedtuple

Item = namedtuple("Item", "name,value")

running_max = None

def counter(items):
    global running_max
    total = 0

    for i in items:
        total += i.value

    if not running_max or total > running_max:
        running_max = total

    return total

def main():
    print("Creating some items")

    dinner_items = [Item('Pizza', 20), Item('Beer', 9), Item('Chips', 5)]
    breakfast_items = [Item('Pancakes', 11), Item('Beacon', 4), Item('Coffee', 3), Item('Coffee', 10), Item('Apples', 3)]

    diner_total = counter(dinner_items)
    print(f"Dinner was ${diner_total:,.02f}")

    breakfast_total = counter(breakfast_items)
    print(f"Breakfast was ${breakfast_total:,.02f}")

    print(f"Today your most expensive meal costs ${running_max:,.02f}")

if __name__ == '__main__':
    main()
