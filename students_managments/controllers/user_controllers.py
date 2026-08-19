from odoo.http import Controller, request, route
import json


class UserController(Controller):

    @route("/students", auth="user", type="http")
    def students(self):

        return request.make_response(
            json.dumps(
                {
                    "name": "Jose",
                }
            )
        )

    @route("/new/students", auth="public", type="http", method=["POST"], csrf=False)
    def new_students(self, **kwargs):

        name = kwargs.get("name")

        if name:

            new_contact = request.env["res.partner"].sudo().create(
                {
                    "name": name,
                }
            )

            new_students = request.env["students.info"].sudo().create({
                "student_id": int(new_contact.id)
            })

            return request.make_response(
                json.dumps(
                    {
                        "name": name,
                        "parent_id": new_contact.id,
                        "student_id": new_students.id

                    }
                )
            )

        return request.make_response(
            json.dumps(
                {
                    "status": "The name is required.",
                }
            )
        )

    @route("/student/web", type="http", auth="public", csrf=False, website=True)
    def students_web(self):

        return request.render("students_managments.view_students_web")

    @route("/view/calification", type="http", auth="public", csrf=False, website=True)
    def view_calification(self):

        userNow = request.env.user

        userInfo = {
            "userName": userNow.partner_id.name
        }

        return request.render("students_managments.students_template_students",userInfo)
