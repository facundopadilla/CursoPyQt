from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('eventos.py')

modulo = open("modulo_2.txt", "w").write('\n'.join(finder.badmodules.keys()))