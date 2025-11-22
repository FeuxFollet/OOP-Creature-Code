class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"


# ===============================
# FlyingCreature Branch
# ===============================

class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.altitude = 0

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} swoops down from altitude {self.altitude}!")
        self.altitude = 0

        print(f"{self.name} performs an aerial attack on {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power


# ===============================
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, target_depth):
        self.depth = target_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for 7 damage!")
        target.hp -= self.attack_power


# ===============================
# FireCreature Branch
# ===============================

class FireCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.fire_level = 0

    def emit_fire(self, target_level):
        if target_level <= 100:
            self.fire_level = target_level
            print(f"{self.name} emits fire to level {self.fire_level}.")
        else:
            print("Emit failed, fire level limit is 100.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} incorporate fire on {target.name} for {self.attack_power} physical damage + {self.fire_level} fire damage!")
        target.hp -= (self.attack_power + self.fire_level)


if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    print("=== FlyingCreature Tests ===\n")
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    hawk.fly_to(120)
    print(f"Altitude should be 120 → Actual: {hawk.altitude}")

    dummy = Creature("Practice Dummy", 40, 0)
    hawk.attack(dummy)
    print(f"Dummy HP should be 32 → Actual: {dummy.hp}")
    dummy.attack(hawk)
    print()    
    print("=== Tests Completed ===")
    print()

    print("=== SwimmingCreature Tests ===\n")
    serpent = SwimmingCreature("Aqua Serpent", 60, 7)
    serpent.dive_to(30)
    print(f"Depth should be 30 → Actual: {serpent.depth}")

    dummy = Creature("Practice Dummy", 40, 0)
    serpent.attack(dummy)
    print(f"Dummy HP should be 33 → Actual: {dummy.hp}")
    print()    
    print("=== Tests Completed ===")
    print()

    print("=== FireCreature Tests ===\n")
    pheonix = FireCreature("Pheonix", 65, 8)
    pheonix.emit_fire(30)
    print(f"Fire Level should be 30 → Actual: {pheonix.fire_level}")

    dummy = Creature("Practice Dummy", 40, 0)
    pheonix.attack(dummy)
    print(f"Dummy HP should be 2 → Actual: {dummy.hp}")
    print()
    print("=== Tests Completed ===")
    print()