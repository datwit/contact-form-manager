import { Controller } from "stimulus"
import notifier from 'codex-notifier'
import {guid} from "../utiles.js"

const axios = require('axios').default;

// ejemplo en html
// <div class="..."
//     data-controller="component"
//     data-component-remote="url-remota"
//     data-component-ajax="false|true"
//     id="algun-id">
//   <div class="spinner-border" role="status">
//     <span class="sr-only">Loading...</span>
//   </div>
// </div>


export default class ComponentController extends Controller {

  initialize() {
    // crear id del componente si no se nos da
    if( !this.element.hasAttribute("id") ){
      const cid = guid();
      this.element.id = cid;
      this.componentId = cid;
    } else {
      this.componentId = this.element.id;
    }

    // uri del contenido remoto
    this.remote = this.data.get("remote")
    console.log(this.remote);
  }

  connect() {
    const isPreview = document.documentElement.hasAttribute(
        "data-turbolinks-preview");
    const ajaxload = this.data.get("ajax") == "true";

    if ( !isPreview && ajaxload ) {
      // cargar desde remoto si no es una vista previa y se pide
      // cargar con ajax
      this.loadRemote(this.remote, this.element);
    }

    // Now, if you can get a reference to the DOM element your controller
    // is defined on, you can easily access the internal scope of that
    // controller from jQuery plugins, the browser console and other
    // Stimulus controllers.
    this.element['controller'] = this

    // instalar handler para enlaces dentro del componente
    this.element.addEventListener(
        "click", (e) => { this.handleLink(e) }, false
      );
    // manejar form submit dentro del componte
    this.element.addEventListener(
        "submit", (e) => { this.handleSubmit(e) }, false);
  }

  reload() {
    // recargar componente desde ubicacion original
    this.loadRemote(this.data.get("remote"), this.element);
  }

  disconnect() {
    // limpiar handlers para los eventos internos
    this.element.removeEventListener(
        "click", (e) => { this.handleLink(e) }, false
      );
    this.element.removeEventListener(
        "submit", (e) => { this.handleSubmit(e) }, false);
  }

  processHeaders(headers) {
    // procesar headers despues de una llamada ajax
    // var command = headers['web2py-component-command'];
    // var flash = headers['web2py-component-flash'];
    var flash = false; // buscar forma de hacerlo en flask
    // if (command !== null) {
    //     console.log(decodeURIComponent(command));
    //     eval(decodeURIComponent(command));
    // }
    if (flash) {
        notifier.show({
          message: decodeURIComponent(flash),
          style: 'error',
          time: 5000
        })
    }
  }

  handleSubmit(e) {
    // atrapar submits de formularios
    var target = e.target;
    e.preventDefault();
    e.stopPropagation();

    var formData = new FormData(target);

    axios({
      method: 'post',
      url: this.remote,
      data: formData,
      headers: {
        // my custom headers
        'X-Component-Location': document.location.href,
        'X-Component-Element': this.componentId,
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'multipart/form-data'
      }
    }).then((response) => {
      this.processHeaders(response.headers);
      this.updateContent(response.data, this.element);
    }).catch((error) => {
      // handle error
      notifier.show({
        message: error,
        style: 'error',
        time: 5000
      });
      console.log(error);
    });
  }

  handleLink(e){
    var target = e.target;

    while (target && (target.dataset && !('componentId' in target.dataset))) {
      // buscas elemento inmediato superior con el attributo que quiero
      target = target.parentNode;
    }

    if (target && (target != document)) {
      // si lo encontramos entonces hacemos algo
      if(target.dataset.componentId == this.componentId) {
        // si es para este componente en particular, sino no hacemos nada ...
        // hasta que se encuentre con un componente que si quiera hacerse cargo
        // del evento.
        e.preventDefault();
        e.stopPropagation();
        if ('targetComponent' in target.dataset) {
          var loadin = document.getElementById(target.dataset.targetComponent);
          this.loadRemote(target.getAttribute('href'), loadin);
        } else {
          this.loadRemote(target.getAttribute('href'), this.element);
        }
      }
    }
  }

  updateContent(html, target) {
    target.innerHTML = html;
    // do things to the loaded html
    // hidde hpot
    var el = document.getElementById('ctcfields');
    if (el) {
      el.style.display = 'none';
    }
  }

  loadRemote(url_to_load, target) {
    // cargar contenido remoto con ajax
    axios({
      method: 'get',
      url: url_to_load,
      headers: {
        // my custom headers
        'X-Component-Location': document.location.href,
        'X-Component-Element': this.componentId,
        'X-Requested-With': 'XMLHttpRequest'
      }
    }).then((response) => {
      this.processHeaders(response.headers);
      this.remote = url_to_load;
      this.updateContent(response.data, target)
    }).catch((error) => {
      // handle error
      notifier.show({
        message: "Unexpected error, reload the page",
        style: 'error',
        time: 5000
      });
      console.log(error);
    });
  }


  set componentId(cid) {
    this._componentId = cid;
  }

  get componentId() {
    return this._componentId;
  }
}
