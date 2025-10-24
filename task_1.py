

#Лабораторная №1:Первичная инициализация
#Курс :Основы теории систем 
#Студент :[Хайров Салават Шавкятович] 

def get_system_info():
  """
  Эта функция должна вернуть словарь с информацией о вашей "системе".
  """
  # TODO:Заполните словарь вашими реальными данными 
  system_info = {
  "student_name" : "Хайров Салават Шавкятович",
  "academic_group": "ВТАСбз-21",
  "github_link":"https://github.com/shine919",
  }
  return system_info 

if __name__ == "__main__":
  info = get_system_info()
  print("Информация о системе:")
  for k,v in info.items():
    print(f"- {key}: {value}")
