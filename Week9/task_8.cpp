#include <iostream>
#include <string>

using namespace std;

class Employee {  // Дополнительный класс - Работник

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
    string str1;
    string str2;
    string str3;

    // Ввод данных отдела
    cout << "Department name:" << endl;
    getline(cin, str1);
    dept.setDepartmentName(str1);

    cout << "Phone:" << endl;
    getline(cin, str1);
    dept.setPhone(str1);

    // Ввод данных работников (первая половина - методом 1)
    for (int i = 0; i < 3; i++) {
        cout << " Employee " << (i + 1) << ":" << endl;
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
        cout << " " << (i + 1) << ": " << emp.getName() 
             << ", " << emp.getPosition() 
             << ", hired: " << emp.getHireDate() << endl;
    }

    return 0;
}
