import ClassBuilder

character = ClassBuilder.Character()

print(character.Stats)
print(character.check())

gui = ClassBuilder.Interface()

gui.menu.mainloop()
