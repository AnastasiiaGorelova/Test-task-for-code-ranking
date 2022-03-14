# Test task for code ranking

## Task 1.
#### Ответ
В двоичном коде /bin/grep встречается вызов функции malloc 21 раз.

#### Решение
Такой результат можно получить с помощью команды

``
objdump -d /bin/grep | grep -o malloc | wc -w
``

`Objdump -d` дизассемблирует файл, а затем утилитами `grep` и `wc` можно найти точное количество вызовов функции malloc.

## Task 2.
#### Решение
Находится в файле `task2.py`.

#### Запуск
``python3 task2.py Example.class ``

#### Пример использования
Для класс-файла Example.class программа выведет 

```
com/company/Example$Inner
java/lang/Integer
```
При этом вывод `javap -c Example.class` (дизассемблирует) будет следующим:
```commandline
Compiled from "Example.java"
public class com.company.Example {
  public com.company.Example();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public int innerSquare(com.company.Example$Inner);
    Code:
       0: aload_1
       1: invokevirtual #7                  // Method com/company/Example$Inner.getA:()Ljava/lang/Integer;
       4: invokevirtual #13                 // Method java/lang/Integer.intValue:()I
       7: aload_1
       8: invokevirtual #7                  // Method com/company/Example$Inner.getA:()Ljava/lang/Integer;
      11: invokevirtual #13                 // Method java/lang/Integer.intValue:()I
      14: imul
      15: ireturn
}
```
То есть действительно получили список классов, которые упоминаются во всех инструкциях invokevirtual.