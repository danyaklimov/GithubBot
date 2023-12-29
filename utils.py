import requests


def leave_comment(url: str) -> None:
    comment = "Github commented"
    json = {
        "body": comment
    }

    requests.patch(url=url, json=json)


if __name__ == '__main__':
    leave_comment()
