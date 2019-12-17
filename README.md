# Проведение конкурсов в инстаграмм

 Учебный проект выполнен на Python3. Проект учит :
 * использовать api бота instabot для получения данных о постах в Instagramm
 * Используя API можно узнать сколько подписчиков у пользователя, на кого он подписался
 *  информацию о посте и кто прокоментировал пост ,кто поставил лайк ...
 * Приложение учит как выбирать победителей конкурса в типовом инстаграмм конкурсе
 
 
 

### Как установить


Файл `.env` должен содержать секретные данные ( вашего кабинета Instagramm ) :
* INTGRAM_LOGIN=<Ваш логин Инстаграмм>  
* INTGRAM_PASSWD=<Ваш логин Инстаграмм>
* 

###### Внимание без правильных данных в файле `.env` программа работать не будет
#### Проект написан на языке Python3 и состоит из файлов :

`main.py`            - содержит основной модуль программы


`requirements.txt`  стандартный файл зависимостей для установки  python окружения

`.env` Описывает среду выполнения.Обязателен для заполнения. Что надо усстановить в файле описано выше.


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`) для установки зависимостей:


    pip install -r requirements.txt


### Как запускать программу
	python.exe main.py <Ссылка на конкурс в инстарнрамме>
	


### Цель проекта

Код написан в образовательных целях на онлайн-курсе  для веб-разработчиков [dvmn.org](https://dvmn.org/).
Проект  учит обращаться из языка python к данным в Instagramm.
При прохождении  проекта осваиваются 
объекты и методы API доступа к инстаграмм-объектам, 
методы работы со списками и множествами,
доступ к аргументам командной строки и.т.д.


