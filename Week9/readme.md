# Лабораторная работа на неделю 9
## **Тема**: Объектно-ориентированное программирование на С++ 
### Студента группы ПИЖ-б-о-23-1(1) Джабраилова Бекхана Магомедовича <br><br>
**Репозиторий Git:** https://github.com/haneex22/pizh2311_Dzhabrailov
**Вариант: 8**  
**Практическая работа:**  

*Задание:*  

Тема проекта: приложение «Отдел кадров».  
В приложении должно быть реализовано 2 класса: Отдел и Работник. Класс Отдел содержит название, телефон. Класс Работник содержит имя, должность, дату приема.  

*Ответ:*  
```cpp
#include <iostream>
#include <string>

using namespace std;

class Employee {  // Дополнительный класс - Работник
private:
    string name;
    string position;
    string hireDate;

public:
    // Методы доступа
    string getName() {
        return name;
    }
    void setName(string name) {
        this->name = name;
    }

    string getPosition() {
        return position;
    }
    void setPosition(string position) {
        this->position = position;
    }

    string getHireDate() {
        return hireDate;
    }
    void setHireDate(string hireDate) {
        this->hireDate = hireDate;
    }

    // Перегруженные методы
    void setProperties() {
        string str;
        cout << " Employee name:" << endl;
        getline(cin, str);
        this->setName(str);
        
        cout << " Position:" << endl;
        getline(cin, str);
        this->setPosition(str);
        
        cout << " Hire date:" << endl;
        getline(cin, str);
        this->setHireDate(str);
    }

    void setProperties(string name, string position, string hireDate) {
        this->setName(name);
        this->setPosition(position);
        this->setHireDate(hireDate);
    }
};

class Department {  // Основной класс - Отдел
private:
    string departmentName;
    string phone;
    Employee employees[10];  // Массив объектов дополнительного класса

public:
    // Методы доступа
    string getDepartmentName() {
        return departmentName;
    }
    void setDepartmentName(string name) {
        this->departmentName = name;
    }

    string getPhone() {
        return phone;
    }
    void setPhone(string phone) {
        this->phone = phone;
    }

    // Метод для добавления работника в массив
    void addEmployee(Employee emp, int index) {
        employees[index] = emp;
    }

    // Метод для получения работника из массива
    Employee getEmployee(int index) {
        return employees[index];
    }
};

int main() {
    Department dept;  // Создание объекта основного класса
    string str1, str2, str3;

    // Ввод данных отдела
    cout << "Department name:" << endl;
    getline(cin, str1);
    dept.setDepartmentName(str1);

    cout << "Phone:" << endl;
    getline(cin, str1);
    dept.setPhone(str1);

    // Ввод данных работников (первая половина - методом 1)
    for (int i = 0; i < 3; i++) {
        cout << " Employee " << (i+1) << ":" << endl;
        Employee emp;
        emp.setProperties();  // Заполнение методом 1
        dept.addEmployee(emp, i);
    }

    // Вывод данных
    cout << endl << "Department information:" << endl;
    cout << "Name: " << dept.getDepartmentName() << endl;
    cout << "Phone: " << dept.getPhone() << endl;
    cout << "Employees:" << endl;

    for (int i = 0; i < 3; i++) {
        Employee emp = dept.getEmployee(i);
        cout << " " << (i+1) << ": " << emp.getName() 
             << ", " << emp.getPosition() 
             << ", hired: " << emp.getHireDate() << endl;
    }

    return 0;
}

```  

Вывод программы: 

Department name:  
Cisco  
Phone:  
89998886633  
 Employee 1:  
 Employee name:  
Max  
 Position:  
manager  
 Hire date:  
12.12.2012  
 Employee 2:  
 Employee name:  
Devon  
 Position:  
team leader  
 Hire date:  
15.08.2018  
 Employee 3:  
 Employee name:  
John  
 Position:  
programmer  
 Hire date:  
21.02.2021  

Department information:  
Name: Cisco  
Phone: 89998886633  
Employees:  
 1: Max, manager, hired: 12.12.2012  
 2: Devon, team leader, hired: 15.08.2018  
 3: John, programmer, hired: 21.02.2021  
