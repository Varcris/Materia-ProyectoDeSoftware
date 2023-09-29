from src.core import board


def run():
    issue1 = board.create_issue(
        email="user1@gmail.com",
        title="Issue 1",
        description="Issue 1 description",
        status="open",
    )

    issue2 = board.create_issue(
        email="user2@gmail.com",
        title="Issue 2",
        description="Issue 2 description",
        status="open",
    )

    issue3 = board.create_issue(
        email="user2@gmail.com",
        title="Issue 3",
        description="Issue 3 description",
        status="open",
    )
