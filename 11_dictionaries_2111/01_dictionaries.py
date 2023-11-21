phone = {
    "first_name": "John",
    "last_name": "Doe",
    "email": ['work@yahoo.com', 'johndoe@gmail.com'],
    "phone": {
        "private": "+15550100",
        "work": "+166630100",
    },
    "notes": {
        "birthday": "08/01/1990",
        "special": {
            "first_date": "12/08/2010",
            "Nickname": "JD_3000p",
        }
    }
}

# чтобы вывести имя:
print(phone["first_name"])
# чтобы вывести email, нужно правильно подобрать индекс, так как они находятся в списке
print(phone["email"][1])
# чтобы вывести рабочий телефон, обращаемся по двум ключам
print(phone["phone"]["work"])
# чтобы вывести никнейм, обращаемся по ключам, так как вся эта информация находится в словарях
print(phone["notes"]["special"]["Nickname"])
