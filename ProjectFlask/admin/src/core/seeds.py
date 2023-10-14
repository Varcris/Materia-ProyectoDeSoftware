from src.core import auth
from src.core import board


def init_db():
    try:
        issue1 = board.create_issue(
            email="fede@gmail.com",
            title="Issue 1",
            description="Issue 1 description",
            status="open",
        )

        issue2 = board.create_issue(
            email="agus@gmail,com",
            title="Issue 2",
            description="Issue 2 description",
            status="open",
        )

        issue3 = board.create_issue(
            email="midu@gmail.com",
            title="Issue 3",
            description="Issue 3 description",
            status="open",
        )
        print("✅ Issues creados!")
    except Exception as e:
        print("❌ Error al crear los Issues")
        print(e)

    try:
        fede = auth.create_user(email="fede@gmail.com", password="123456")
        agus = auth.create_user(email="agus@gmail,com", password="536214")
        midu = auth.create_user(email="midu@gmail.com", password="784562")
        print("✅ Usuarios creados!")
    except Exception as e:
        print("❌ Error al crear los Usuarios")
        print(e)

    label1 = board.create_label(
        title="Urgente", description="issues que de deben resolver ya"
    )
    label2 = board.create_label(
        title="Importante", description="issues que de deben resolver pronto"
    )
    label3 = board.create_label(
        title="Soporte", description="issues relacionados con soporte"
    )
    label4 = board.create_label(
        title="Ventas", description="issues relacionados con ventas"
    )
    label5 = board.create_label(
        title="DEV", description="issues relacionados con desarrollo"
    )
    print("✅ Labels creadas!")

    board.assign_user(issue1, fede)
    board.assign_user(issue2, agus)
    board.assign_user(issue3, midu)
    print("✅ Issues asignados a usuarios!")

    board.assign_labels(issue1, [label1, label2, label3])
    board.assign_labels(issue2, [label4, label5])
    board.assign_labels(issue3, [label1, label4, label5])
    print("✅ Labels asignadas a issues!")
