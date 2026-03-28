# SDET_SimbirSoft_Task
<h2>Решение ТЗ для отбора на практикум SDET Python</h2>
<h2>Положительный тест-кейс №1</h2>
<h3>Заполнение всех полей формы</h3>
<strong>Предусловия:</strong> Открыта страница формы</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "Name"</li>
  <li>Заполнить поле "Password"</li>
  <li>Нажать на ячейку "Milk"</li>
  <li>Нажать на ячейку "Coffee"</li>
  <li>Нажать на радиокнопку "Yellow"</li>
  <li>Нажать на список с текстом "Do you like automation?"</li>
  <li>Нажать на любую ячейку из списка</li>
  <li>Заполнить поле "Email"</li>
  <li>Записать на поле "Message" количество пунктов и самый длинный текст из предложенных</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Появление окна сообщения Alert с текстом "Message received!"

<h2>Положительный тест-кейс №2</h2>
<h3>Заполнение только требующих полей</h3>
У нас на сайте только поле Name имеет свойство required - заполняем только его </br>
<strong>Предусловия:</strong> Открыта страница формы
</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "Name"</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Появление окна сообщения Alert с текстом "Message received!"

<h2>Положительный тест-кейс №3</h2>
<h3>Частичное заполнение полей формы</h3>
<strong>Предусловия:</strong> Открыта страница формы
</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "Name"</li>
  <li>Записать на поле "Message" количество пунктов и самый длинный текст из предложенных</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Появление окна сообщения Alert с текстом "Message received!"

<h2>Негативный тест-кейс №4</h2>
<h3>Заполнение всех полей формы кроме имени</h3>
<strong>Предусловия:</strong> Открыта страница формы</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "Password"</li>
  <li>Нажать на ячейку "Milk"</li>
  <li>Нажать на ячейку "Coffee"</li>
  <li>Нажать на радиокнопку "Yellow"</li>
  <li>Нажать на список с текстом "Do you like automation?"</li>
  <li>Нажать на любую ячейку из списка</li>
  <li>Заполнить поле "Email"</li>
  <li>Записать на поле "Message" количество пунктов и самый длинный текст из предложенных</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Окно сообщения Alert с текстом "Message received!" не появилось и сайт скроллит к полю "Name"

<h2>Негативный тест-кейс №5</h2>
<h3>Заполнение некоторых полей, где поле имени не входит</h3>
<strong>Предусловия:</strong> Открыта страница формы</br>
<strong>Шаги</strong>
<ul>
  <li>Нажать на ячейку "Milk"</li>
  <li>Нажать на ячейку "Coffee"</li>
  <li>Записать на поле "Message" самый длинный текст из предложенных</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Окно сообщения Alert с текстом "Message received!" не появилось и сайт скроллит к полю "Name"

<h2>Отчеты на Allure</h2>
<div align="center">
  <img src="https://raw.githubusercontent.com/MaximNguen/SDET_SimbirSoft_Task_New/main/screenshots/1.jpg" width="100%"><br>
  <img src="https://raw.githubusercontent.com/MaximNguen/SDET_SimbirSoft_Task_New/main/screenshots/2.jpg" width="100%">
</div>

<h2>Результаты запуска тестов</h2>
<code>tests/test_positive.py::TestPositiveResult::test_fill_form_full[test_data0]
tests/test_positive.py::TestPositiveResult::test_fill_form_full[test_data1]
tests/test_positive.py::TestPositiveResult::test_fill_form_full[test_data2]
tests/test_negative.py::TestNegativeResult::test_fill_form_without_name[test_data2]
tests/test_positive.py::TestPositiveResult::test_fill_only_required[test_data1]
tests/test_negative.py::TestNegativeResult::test_fill_form_without_name[test_data0]
tests/test_positive.py::TestPositiveResult::test_fill_only_required[test_data0]
tests/test_negative.py::TestNegativeResult::test_fill_form_optional_only[test_data0]
tests/test_negative.py::TestNegativeResult::test_fill_form_without_name[test_data1]
tests/test_positive.py::TestPositiveResult::test_fill_only_required[test_data2]
tests/test_positive.py::TestPositiveResult::test_fill_form_partial[test_data1]
tests/test_positive.py::TestPositiveResult::test_fill_form_partial[test_data0]
[gw7] [  7%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_only_required[test_data0]
[gw10] [ 15%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_form_partial[test_data0] 
[gw8] [ 23%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_only_required[test_data1]
[gw11] [ 30%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_form_partial[test_data1] 
[gw9] [ 38%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_only_required[test_data2] 
[gw3] [ 46%] PASSED tests/test_negative.py::TestNegativeResult::test_fill_form_optional_only[test_data0]
[gw5] [ 53%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_form_full[test_data1]
[gw1] [ 61%] PASSED tests/test_negative.py::TestNegativeResult::test_fill_form_without_name[test_data1] 
[gw2] [ 69%] PASSED tests/test_negative.py::TestNegativeResult::test_fill_form_without_name[test_data2] 
[gw0] [ 76%] PASSED tests/test_negative.py::TestNegativeResult::test_fill_form_without_name[test_data0] 
[gw6] [ 84%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_form_full[test_data2] 
[gw4] [ 92%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_form_full[test_data0] 
tests/test_positive.py::TestPositiveResult::test_fill_form_partial[test_data2] 
[gw0] [100%] PASSED tests/test_positive.py::TestPositiveResult::test_fill_form_partial[test_data2] 

======================================================================================= 13 passed in 73.45s (0:01:13) ======================================================================================= </code>

<h2>Установка и запуск</h2>
<ol>
    <li>Клонировать репозиторий</li>
    <li>Установить зависимости: <code>pip install -r requirements.txt</code></li>
    <li>Настроить переменные окружения в <code>.env</code></li>
    <li>Запустить тесты с нужными вам параметрами: <code>pytest -v -s</code> - это выдаст подробное описание тестов и все print</li>
    <li>Если вам нужен конректные тесты (Поиск элементов, Положительные или Негативные тесты), то запускайте так - <code>cd tests</code>, потом <code>pytest *Название файла*</code></li>
    <li>Если вам нужен тест какой-то из тест-кейса (функцию), то запускайте так - <code>cd tests</code>, потом <code>pytest *Название файла*::*Название функции*</code></li>
    <li>Если нужен отчет allure, можете локально запустить свой - <code>pytest --alluredir=allure-results</code></li>
    <li>Далее прописываете <code>allure serve allure-results</code></li>
    <li>Если нужно быстро пройтись по тестам, можно использовать несколько воркеров - <code>pytest -v -n auto</code></li>
</ol>
