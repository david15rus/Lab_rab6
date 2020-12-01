#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys
# Условние задания
# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название товара? ")
            coast = int(input("Его стоимость? "))
            shop = input("Название магазина? ")

            product = {
                'name': name,
                'coast': сoast,
                'shop': shop
            }

            products.append(product)
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                ' | {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Наименование товара",
                    "Стоимость",
                    "Название магазина"
                )
            )
            print(line)

            for idx, product in enumerate(products, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('coast', 0),
                        worker.get('shop', '')
                    )
                )

            print(line)

        elif command.startswith('select '):
            name_user = input("Введите название интересующего магазина ")

            count = 0
            for product in products:
                if name_user == product.key(shop):
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, product.get('coast', ''))
                    )
            if count == 0:
                print("Магазин с таким названием не найден")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товары;")
            print("list - вывести список товаров;")
            print("select <магазин> - запросить товары в выбранном магазине")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)