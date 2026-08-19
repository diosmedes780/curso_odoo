/**@odoo-module **/

import {Component} from "@odoo/owl";
import {registry} from "@web/core/registry";


export class StudentsComponent extends Component{

        static template = "students_managments.students_view_calification_student";
        static props = {
            userName: String
        }

    setup(){

        console.log("Se cargo el componente")

    }
}

registry.category("public_components").add("students_managments.students_components",StudentsComponent)