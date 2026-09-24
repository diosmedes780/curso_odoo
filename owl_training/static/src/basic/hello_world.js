/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class Helloworld extends Component {
    static template = "owl_training.HelloWorld";
    static props = ["name"];
}

registry.category("actions").add("owl_training.hello_world", Helloworld);