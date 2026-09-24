/**@odoo-module **/

import {Component, useState, onWillStart, onWillRender, onMounted, useRef} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";


export class StudentsComponent extends Component{

        static template = "students_managments.students_view_calification_student";
        static props = {
            userName: String,
            student_id: Number
        }

    setup(){

        this.ui = useService("ui");
        this.notification = useService("notification")
        this.state = useState({number: 0, edad: 0, calificaciones: []})
        this.orm = useService("orm");
        this.input_edad = useRef("input_edad");

        onWillStart(async()=>{
            // this.state.number += 10;
            console.log("Prueba")

            const student = await this.orm.searchRead(
                "students.info",
                [["id", "=", this.props.student_id]],
                ["age"]
            );

            if(!student){
                this.notification.add("No se encontro el estudiante", {type: "danger"})
                return;
            }

            console.log(student);
            this.state.edad = student[0].age

            const califications = await this.orm.searchRead(
                "qualification.students",
                [["students_id", "=", this.props.student_id]],
                ["id","school_subject_id", "state_subject", "qualification"]
            )

            this.state.calificaciones = califications;

            console.log(califications)
        })

        onWillRender(()=>{
            this.notification.add("cambio", {type: "success"})
        })

        onMounted(()=>{
            console.log("onMounted")
        })

    }

    openAlert(){
            this.ui.block();

            setTimeout(() => {
                this.ui.unblock();
            }, 5000);
    }

    viewInput(ev){
            console.log(ev.target.value);
    }

    viewNotification(){
            this.notification.add("Mostrando alerta", {type: "success"})
    }

    changeNumber(){
            this.state.number++;
    }

    validarEdad(){
            const valueAge = parseInt(this.input_edad.el.value);

            if (valueAge < 18 ||  !valueAge){
                this.notification.add("La edad no cumple los requisitos", {type: "danger"});
                return;
            }

            this.notification.add("La edad es correccta eres apto");
    }
}

registry.category("public_components").add("students_managments.students_components",StudentsComponent)