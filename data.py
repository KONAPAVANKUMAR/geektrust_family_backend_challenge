from models import Person

king = Person(
        name = "King Shan",
        gender = "male",
        wife = Person(
            name = "Queen Anga",
            gender= "female"
        ),
        children = [
            Person(
                name = "Chit",
                gender = "male",
                wife = Person("Amba","female"),
                children = [
                    Person(
                        name = "Dritha",
                        gender = "female",
                        husband = Person(
                            name = "Jaya",
                            gender = "male"
                        ),
                        children = [
                            Person(
                                name = "Yodhan",
                                gender = "male"
                            )
                        ],
                    ),
                    Person(
                        name = "Tritha",
                        gender = "female"
                    ),
                    Person(
                        name = "Vritha",
                        gender = "male"
                    )
                ]

            ),
            Person(
                name = "Ish",
                gender = "male",
            ),
            Person(
                name = "Vich",
                gender = "male",
                wife = Person("Lika","female"),
                children = [
                    Person("Vila","female"),
                    Person("Chika","female")
                ]
            ),
            Person(
                name = "Aras",
                gender = "male",
                wife = Person("Chitra","female"),
                children = [
                    Person("Ahit","male"),
                    Person(
                            "Jnki","female",
                            husband = Person("Arit","male"),
                            children = [
                                Person("Laki","male"),
                                Person("Lavnya","female")
                            ]
                        ),
                ]
            ),
            Person(
                name = "Satya",
                gender = "female",
                husband = Person("Vyan","male"),
                children = [
                    Person("Asva","male",
                        wife = Person("Satvy","female"),
                        children = [
                            Person("Vasa","male")
                        ]
                    ),
                    Person("Vyas","male",
                        wife = Person("Krpi","female"),
                        children = [
                            Person("Kriya","male"),
                            Person("Krithi","female")
                        ]
                    ),
                    Person("Atya","female"),
                ]
            )
        ]
    )




