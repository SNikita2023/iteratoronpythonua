
class Helper:
     def __init__(self, work):
       self.work = work
     def __call__(self, work): #Використовуєм метод __call__()
       return f"I will help you with your {self.work}. Afterwards I will help you with {work}"
#Тут в насвиводится дочірня функція яка має повертати результат, а батьківська робить за счет дочірньої функції
helper = Helper("homework")
print(helper("cleaning"))
#В нас з'явився об’єкт запам’ятав інформацію, що необхідна для його виклику . Так що функція наче «замикає» і «тримає в собі» аргументи для своєї роботи
