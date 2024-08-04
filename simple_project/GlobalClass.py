# Here we define global class for the project for structuration
from simple_project.settings import SECRET_KEY


class IResponse:
    def __init__(self, ok: bool, message: str, data=None):
        self.ok = ok
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            "ok": self.ok,
            "message": self.message,
            "data": self.data
        }



def print_info(variable_name: str, variable_value):
    print("============ Print of variable: " + variable_name + " ============")
    print(variable_value)


def is_request_valid(request):
    if "Authorization" not in request.headers or request.headers["Authorization"] is None or request.headers["Authorization"] != SECRET_KEY:
        return False, "Authorization header is missing or incorrect"
    return True, "OK"