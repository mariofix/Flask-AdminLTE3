import typing
from dataclasses import dataclass
from functools import partial
from flask_admin.theme import Theme


@dataclass
class AdminLTETheme(Theme):
    folder: typing.Literal["adminlte"]
    base_template: str = "admin/base.html"


AdminLTETheme = partial(AdminLTETheme, folder="adminlte")