{
    "name": "Students Management",
    "category": "students",
    "author": "Diomedes Yeguez",
    "version": "19.0.0.0",
    "depends": [
        "web",
        "website"
    ],
    "data": [
        "views/students_info.xml",
        "views/courses_students.xml",
        "views/school_subjects.xml",
        "views/qualification_students.xml",
        "views/res_partner.xml",
        "views/students_view_web.xml",
        "views/view_students_template.xml",
        "wizard/qualification_wizard_views.xml",
        "security/students_security.xml",
        "security/ir.model.access.csv",
    ],
    "assets": {
        "web.assets_frontend": [
            "/students_managments/static/src/xml/**/*.xml",
            "/students_managments/static/src/css/**/*.css",
            "/students_managments/static/src/js/**/*.js"
        ]
    },
    "application": True,
}