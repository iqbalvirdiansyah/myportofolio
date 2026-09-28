from django.urls import path
from main.views import (
    register,
    login_user,
    logout_user,
    show_main,
    show_experience,
    get_experience_json,
    create_experience,
    update_experience,
    delete_experience,
    show_projects,
    show_project_detail,
    create_project,
    get_projects_json,
    delete_project,
    toggle_star,
    toggle_star_experience
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    # Experience
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("api/experiences/", get_experience_json, name="get_experience_json"),
    # Projects
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:id>/", show_project_detail, name="show_project_detail"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    # Auth
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
