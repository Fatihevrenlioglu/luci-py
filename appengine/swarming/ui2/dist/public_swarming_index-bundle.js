!function(e){var t={};function s(i){if(t[i])return t[i].exports;var n=t[i]={i:i,l:!1,exports:{}};return e[i].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=e,s.c=t,s.d=function(e,t,i){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:i})},s.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var i=Object.create(null);if(s.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)s.d(i,n,function(t){return e[t]}.bind(null,n));return i},s.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/newres/",s(s.s=4)}([function(e,t,s){"use strict";function i(e,t){if(e.hasOwnProperty(t)){let s=e[t];delete e[t],e[t]=s}}s.d(t,"a",function(){return i})},function(e,t,s){"use strict";const i=new Map;class n{constructor(e,t,s,i=w){this.strings=e,this.values=t,this.type=s,this.partCallback=i}getHTML(){const e=this.strings.length-1;let t="",s=!0;for(let i=0;i<e;i++){const e=this.strings[i];t+=e;const n=c(e);t+=(s=n>-1?n<e.length:s)?a:o}return t+this.strings[e]}getTemplateElement(){const e=document.createElement("template");return e.innerHTML=this.getHTML(),e}}function r(e,t,s=function(e){let t=i.get(e.type);void 0===t&&(t=new Map,i.set(e.type,t));let s=t.get(e.strings);return void 0===s&&(s=new _(e,e.getTemplateElement()),t.set(e.strings,s)),s}){const n=s(e);let r=t.__templateInstance;if(void 0!==r&&r.template===n&&r._partCallback===e.partCallback)return void r.update(e.values);r=new k(n,e.partCallback,s),t.__templateInstance=r;const o=r._clone();r.update(e.values),x(t,t.firstChild),t.appendChild(o)}const o=`{{lit-${String(Math.random()).slice(2)}}}`,a=`\x3c!--${o}--\x3e`,l=new RegExp(`${o}|${a}`),h=/[ \x09\x0a\x0c\x0d]([^\0-\x1F\x7F-\x9F \x09\x0a\x0c\x0d"'>=/]+)[ \x09\x0a\x0c\x0d]*=[ \x09\x0a\x0c\x0d]*(?:[^ \x09\x0a\x0c\x0d"'`<>=]*|"[^"]*|'[^']*)$/;function c(e){const t=e.lastIndexOf(">");return e.indexOf("<",t+1)>-1?e.length:t}class u{constructor(e,t,s,i,n){this.type=e,this.index=t,this.name=s,this.rawName=i,this.strings=n}}const d=e=>-1!==e.index;class _{constructor(e,t){this.parts=[],this.element=t;const s=this.element.content,i=document.createTreeWalker(s,133,null,!1);let n=-1,r=0;const a=[];let c,d;for(;i.nextNode();){n++,c=d;const t=d=i.currentNode;if(1===t.nodeType){if(!t.hasAttributes())continue;const s=t.attributes;let i=0;for(let e=0;e<s.length;e++)s[e].value.indexOf(o)>=0&&i++;for(;i-- >0;){const i=e.strings[r],o=h.exec(i)[1],a=s.getNamedItem(o),c=a.value.split(l);this.parts.push(new u("attribute",n,a.name,o,c)),t.removeAttribute(a.name),r+=c.length-1}}else if(3===t.nodeType){const e=t.nodeValue;if(e.indexOf(o)<0)continue;const s=t.parentNode,i=e.split(l),h=i.length-1;r+=h;for(let e=0;e<h;e++)s.insertBefore(""===i[e]?document.createComment(""):document.createTextNode(i[e]),t),this.parts.push(new u("node",n++));s.insertBefore(""===i[h]?document.createComment(""):document.createTextNode(i[h]),t),a.push(t)}else if(8===t.nodeType&&t.nodeValue===o){const e=t.parentNode,s=t.previousSibling;null===s||s!==c||s.nodeType!==Node.TEXT_NODE?e.insertBefore(document.createComment(""),t):n--,this.parts.push(new u("node",n++)),a.push(t),null===t.nextSibling?e.insertBefore(document.createComment(""),t):n--,d=c,r++}}for(const e of a)e.parentNode.removeChild(e)}}const p=(e,t)=>f(t)?(t=t(e),g):null===t?void 0:t,f=e=>"function"==typeof e&&!0===e.__litDirective,g={},m=e=>null===e||!("object"==typeof e||"function"==typeof e);class b{constructor(e,t,s,i){this.instance=e,this.element=t,this.name=s,this.strings=i,this.size=i.length-1,this._previousValues=[]}_interpolate(e,t){const s=this.strings,i=s.length-1;let n="";for(let r=0;r<i;r++){n+=s[r];const i=p(this,e[t+r]);if(i&&i!==g&&(Array.isArray(i)||"string"!=typeof i&&i[Symbol.iterator]))for(const e of i)n+=e;else n+=i}return n+s[i]}_equalToPreviousValues(e,t){for(let s=t;s<t+this.size;s++)if(this._previousValues[s]!==e[s]||!m(e[s]))return!1;return!0}setValue(e,t){if(this._equalToPreviousValues(e,t))return;const s=this.strings;let i;2===s.length&&""===s[0]&&""===s[1]?(i=p(this,e[t]),Array.isArray(i)&&(i=i.join(""))):i=this._interpolate(e,t),i!==g&&this.element.setAttribute(this.name,i),this._previousValues=e}}class v{constructor(e,t,s){this.instance=e,this.startNode=t,this.endNode=s,this._previousValue=void 0}setValue(e){if((e=p(this,e))!==g)if(m(e)){if(e===this._previousValue)return;this._setText(e)}else e instanceof n?this._setTemplateResult(e):Array.isArray(e)||e[Symbol.iterator]?this._setIterable(e):e instanceof Node?this._setNode(e):void 0!==e.then?this._setPromise(e):this._setText(e)}_insert(e){this.endNode.parentNode.insertBefore(e,this.endNode)}_setNode(e){this._previousValue!==e&&(this.clear(),this._insert(e),this._previousValue=e)}_setText(e){const t=this.startNode.nextSibling;e=void 0===e?"":e,t===this.endNode.previousSibling&&t.nodeType===Node.TEXT_NODE?t.textContent=e:this._setNode(document.createTextNode(e)),this._previousValue=e}_setTemplateResult(e){const t=this.instance._getTemplate(e);let s;this._previousValue&&this._previousValue.template===t?s=this._previousValue:(s=new k(t,this.instance._partCallback,this.instance._getTemplate),this._setNode(s._clone()),this._previousValue=s),s.update(e.values)}_setIterable(e){Array.isArray(this._previousValue)||(this.clear(),this._previousValue=[]);const t=this._previousValue;let s=0;for(const i of e){let e=t[s];if(void 0===e){let i=this.startNode;s>0&&(i=t[s-1].endNode=document.createTextNode(""),this._insert(i)),e=new v(this.instance,i,this.endNode),t.push(e)}e.setValue(i),s++}if(0===s)this.clear(),this._previousValue=void 0;else if(s<t.length){const e=t[s-1];t.length=s,this.clear(e.endNode.previousSibling),e.endNode=this.endNode}}_setPromise(e){this._previousValue=e,e.then(t=>{this._previousValue===e&&this.setValue(t)})}clear(e=this.startNode){x(this.startNode.parentNode,e.nextSibling,this.endNode)}}const w=(e,t,s)=>{if("attribute"===t.type)return new b(e,s,t.name,t.strings);if("node"===t.type)return new v(e,s,s.nextSibling);throw new Error(`Unknown part type ${t.type}`)};class k{constructor(e,t,s){this._parts=[],this.template=e,this._partCallback=t,this._getTemplate=s}update(e){let t=0;for(const s of this._parts)s?void 0===s.size?(s.setValue(e[t]),t++):(s.setValue(e,t),t+=s.size):t++}_clone(){const e=this.template.element.content.cloneNode(!0),t=this.template.parts;if(t.length>0){const s=document.createTreeWalker(e,133,null,!1);let i=-1;for(let e=0;e<t.length;e++){const n=t[e],r=d(n);if(r)for(;i<n.index;)i++,s.nextNode();this._parts.push(r?this._partCallback(this,n,s.currentNode):void 0)}}return e}}const x=(e,t,s=null)=>{let i=t;for(;i!==s;){const t=i.nextSibling;e.removeChild(i),i=t}};s.d(t,"a",function(){return y}),s.d(t,"b",function(){return r});const y=(e,...t)=>new n(e,t,"html",T),T=(e,t,s)=>{if("attribute"===t.type){if("on-"===t.rawName.substr(0,3)){return new class{constructor(e,t,s){this.instance=e,this.element=t,this.eventName=s}setValue(e){const t=p(this,e);t!==this._listener&&(null==t?this.element.removeEventListener(this.eventName,this):null==this._listener&&this.element.addEventListener(this.eventName,this),this._listener=t)}handleEvent(e){"function"==typeof this._listener?this._listener.call(this.element,e):"function"==typeof this._listener.handleEvent&&this._listener.handleEvent(e)}}(e,s,t.rawName.slice(3))}const i=t.name.substr(t.name.length-1);if("$"===i){const i=t.name.slice(0,-1);return new b(e,s,i,t.strings)}if("?"===i){return new class extends b{setValue(e,t){const s=this.strings;if(2!==s.length||""!==s[0]||""!==s[1])throw new Error("boolean attributes can only contain a single expression");{const s=p(this,e[t]);if(s===g)return;s?this.element.setAttribute(this.name,""):this.element.removeAttribute(this.name)}}}(e,s,t.name.slice(0,-1),t.strings)}return new class extends b{setValue(e,t){const s=this.strings;let i;this._equalToPreviousValues(e,t)||((i=2===s.length&&""===s[0]&&""===s[1]?p(this,e[t]):this._interpolate(e,t))!==g&&(this.element[this.name]=i),this._previousValues=e)}}(e,s,t.rawName,t.strings)}return w(e,t,s)}},function(e,t,s){"use strict";function i(e,t=1e4){"object"==typeof e&&(e=e.message||JSON.stringify(e));var s={message:e,duration:t};document.dispatchEvent(new CustomEvent("error-sk",{detail:s,bubbles:!0}))}s.d(t,"a",function(){return i})},function(e,t,s){"use strict";var i=s(1),n=s(0);s(15);const r=document.createElement("template");window.customElements.define("menu-icon-sk",class extends class extends HTMLElement{constructor(){super(),r.innerHTML=`<svg class="icon-sk-svg" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">${this.constructor._svg}</svg>`}connectedCallback(){let e=r.content.cloneNode(!0);this.appendChild(e)}}{static get _svg(){return'<path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>'}}),window.customElements.define("spinner-sk",class extends HTMLElement{connectedCallback(){Object(n.a)(this,"active")}get active(){return this.hasAttribute("active")}set active(e){e?this.setAttribute("active",""):this.removeAttribute("active")}});s(13),s(12);var o=s(2);window.customElements.define("oauth-login",class extends HTMLElement{connectedCallback(){Object(n.a)(this,"client_id"),Object(n.a)(this,"testing_offline"),this._auth_header="",this.testing_offline?this._profile={email:"missing@chromium.org",imageURL:"http://storage.googleapis.com/gd-wagtail-prod-assets/original_images/logo_google_fonts_color_2x_web_64dp.png"}:(this._profile=null,document.addEventListener("oauth-lib-loaded",()=>{gapi.auth2.init({client_id:this.client_id}).then(()=>{this._maybeFireLoginEvent(),this._render()},e=>{console.error(e),Object(o.a)(`Error initializing oauth: ${JSON.stringify(e)}`,1e4)})})),this._render()}static get observedAttributes(){return["client_id","testing_offline"]}get auth_header(){return this._auth_header}get client_id(){return this.getAttribute("client_id")}set client_id(e){return this.setAttribute("client_id",e)}get testing_offline(){return this.getAttribute("testing_offline")}set testing_offline(e){e&&"false"!==e?this.setAttribute("testing_offline",!0):this.removeAttribute("testing_offline")}_maybeFireLoginEvent(){let e=gapi.auth2.getAuthInstance().currentUser.get();if(e.isSignedIn()){let t=e.getBasicProfile();this._profile={email:t.getEmail(),imageURL:t.getImageUrl()};let s=e.getAuthResponse(!0),i=`${s.token_type} ${s.access_token}`;return this.dispatchEvent(new CustomEvent("log-in",{detail:{auth_header:i},bubbles:!0})),this._auth_header=i,!0}return this._profile=null,this._auth_header="",!1}_logIn(){if(this.testing_offline)this._auth_header="Bearer 12345678910-boomshakalaka",this.dispatchEvent(new CustomEvent("log-in",{detail:{auth_header:this._auth_header},bubbles:!0})),this._render();else{let e=gapi.auth2.getAuthInstance();e&&e.signIn({scope:"email",prompt:"select_account"}).then(()=>{this._maybeFireLoginEvent()||console.warn("login was not successful; maybe user canceled"),this._render()})}}_logOut(){if(this.testing_offline)this._auth_header="",this._render(),window.location.reload();else{let e=gapi.auth2.getAuthInstance();e&&e.signOut().then(()=>{this._auth_header="",this._profile=null,window.location.reload()})}}_render(){Object(i.b)((e=>e.auth_header?i["a"]` <div> <img class=center id=avatar src="${e._profile.imageURL}" width=30 height=30> <span class=center>${e._profile.email}</span> <span class=center>|</span> <a class=center on-click=${()=>e._logOut()} href="#">Sign out</a> </div>`:i["a"]` <div> <a on-click=${()=>e._logIn()} href="#">Sign in</a> </div>`)(this),this)}attributeChangedCallback(e,t,s){this._render()}});const a=document.createElement("template");a.innerHTML="\n<button class=toggle-button>\n  <menu-icon-sk>\n  </menu-icon-sk>\n</button>\n";const l=document.createElement("template");l.innerHTML="\n<div class=spinner-spacer>\n  <spinner-sk></spinner-sk>\n</div>\n";window.customElements.define("swarming-app",class extends HTMLElement{connectedCallback(){Object(n.a)(this,"client_id"),Object(n.a)(this,"testing_offline"),this._busyTaskCount=0,this._spinner=null,this._loginEle=null,this._addHTML(),this._render()}static get observedAttributes(){return["client_id","testing_offline"]}get busy(){return!!this._busyTaskCount}get client_id(){return this.getAttribute("client_id")}set client_id(e){return this.setAttribute("client_id",e)}get testing_offline(){return this.getAttribute("testing_offline")}set testing_offline(e){e&&"false"!==e?this.setAttribute("testing_offline",!0):this.removeAttribute("testing_offline")}addBusyTasks(e){this._busyTaskCount+=e,this._spinner&&this._busyTaskCount>0&&(this._spinner.active=!0)}finishedTask(){this._busyTaskCount--,this._busyTaskCount<=0&&(this._busyTaskCount=0,this._spinner&&(this._spinner.active=!1),this.dispatchEvent(new CustomEvent("busy-end",{bubbles:!0})))}_addHTML(){let e=this.querySelector("header"),t=e&&e.querySelector("aside");if(!(e&&t&&t.classList.contains("hideable")))return;let s=a.content.cloneNode(!0);e.insertBefore(s,e.firstElementChild),(s=e.firstElementChild).addEventListener("click",e=>this._toggleMenu(e,t));let i=l.content.cloneNode(!0);e.insertBefore(i,t),this._spinner=e.querySelector("spinner-sk");let n=document.createElement("span");n.classList.add("grow"),e.appendChild(n),this._loginEle=document.createElement("div"),e.appendChild(this._loginEle)}_toggleMenu(e,t){t.classList.toggle("shown")}_render(){this._loginEle&&Object(i.b)((e=>i["a"]` <oauth-login client_id=${e.client_id} testing_offline=${e.testing_offline}></oauth-login> `)(this),this._loginEle)}attributeChangedCallback(e,t,s){this._render()}});s(11)},function(e,t,s){"use strict";s.r(t);var i=s(1),n=s(0);function r(e){if(e.ok)return e.json();throw{message:`Bad network response: ${e.statusText}`,resp:e,status:e.status}}var o=s(2);window.customElements.define("toast-sk",class extends HTMLElement{constructor(){super(),this._timer=null}connectedCallback(){this.hasAttribute("duration")||(this.duration=5e3),Object(n.a)(this,"duration")}get duration(){return+this.getAttribute("duration")}set duration(e){this.setAttribute("duration",e)}show(){this.setAttribute("shown",""),this.duration>0&&!this._timer&&(this._timer=window.setTimeout(()=>{this._timer=null,this.hide()},this.duration))}hide(){this.removeAttribute("shown"),this._timer&&(window.clearTimeout(this._timer),this._timer=null)}});s(10);window.customElements.define("error-toast-sk",class extends HTMLElement{connectedCallback(){this.innerHTML="<toast-sk></toast-sk>",this._toast=this.firstElementChild,document.addEventListener("error-sk",this)}disconnectedCallback(){document.removeEventListener("error-sk",this)}handleEvent(e){e.detail.duration&&(this._toast.duration=e.detail.duration),this._toast.textContent=e.detail.message,this._toast.show()}});s(3);const a=e=>i["a"]` <swarming-app id=swapp client_id="${e.client_id}" testing_offline="${e.testing_offline}"> <header> <div class=title>Swarming Server</div> <aside class=hideable> <a href=/>Home</a> <a href=/botlist>Bot List</a> <a href=/tasklist>Task List</a> </aside> </header> <main> <h2>Service Status</h2> <div>Server Version: <span class=server_version>${e._server_details.server_version}</span></div> <div>Bot Version: ${e._server_details.bot_version} </div> <ul> <li>  <a href=/stats>Usage statistics</a> </li> <li> <a href=/restricted/mapreduce/status>Map Reduce Jobs</a> </li> <li> <a href=${(e=>"https://console.cloud.google.com/appengine/instances"+`project=${e._project_id}&versionId=${e._server_details.server_version}`)(e)}>View version's instances on Cloud Console</a> </li> <li> <a><a href=${(e=>`https://console.cloud.google.com/errors?project=${e}`)(e._project_id)}>View server errors on Cloud Console</a></a> </li> <li> <a><a href=${(e=>`https://console.cloud.google.com/logs/viewer?filters=status:500..599&project=${e}`)(e._project_id)}>View logs for HTTP 5xx on Cloud Console</a></a> </li> </ul> <h2>Configuration</h2> <ul>  <li> <a href="/restricted/config">View server config</a> </li> <li> <a href="/restricted/upload/bootstrap">View/upload bootstrap.py</a> </li> <li> <a href="/restricted/upload/bot_config">View/upload bot_config.py</a> </li> <li> <a href="/auth/groups">View/edit user groups</a> </li> </ul> ${e._permissions.get_bootstrap_token?(e=>i["a"]` <div> <h2>Bootstrapping a bot</h2> To bootstrap a bot, run one of these (all links are valid for 1 hour): <ol> <li> <strong> TL;DR; </strong> <pre class=command>python -c "import urllib; exec urllib.urlopen('${e._host_url}/bootstrap?tok=${e._bootstrap_token}').read()"</pre> </li> <li> Escaped version to pass as a ssh argument: <pre class=command>'python -c "import urllib; exec urllib.urlopen('"'${e._host_url}/bootstrap?tok=${e._bootstrap_token}'"').read()"'</pre> </li> <li> Manually: <pre class=command>mkdir bot; cd bot
rm -f swarming_bot.zip; curl -sSLOJ ${e._host_url}/bot_code?tok=${e._bootstrap_token}
python swarming_bot.zip</pre> </li> </ol> </div> `)(e):""} </main> <footer><error-toast-sk></error-toast-sk></footer> </swarming-app>`;window.customElements.define("swarming-index",class extends class extends HTMLElement{constructor(e){super(),this._template=e}connectedCallback(){Object(n.a)(this,"client_id"),Object(n.a)(this,"testing_offline")}static get observedAttributes(){return["client_id","testing_offline"]}get client_id(){return this.getAttribute("client_id")}set client_id(e){return this.setAttribute("client_id",e)}get testing_offline(){return this.getAttribute("testing_offline")}set testing_offline(e){e&&"false"!==e?this.setAttribute("testing_offline",!0):this.removeAttribute("testing_offline")}render(){Object(i.b)(this._template(this),this)}attributeChangedCallback(e,t,s){this.render()}}{constructor(){super(a),this._server_details={server_version:"You must log in to see more details",bot_version:""},this._permissions={},this._bootstrap_token="...";let e=location.hostname.indexOf(".appspot.com");this._project_id=location.hostname.substring(0,e)||"not_found",this._host_url=location.origin,this._auth_header=""}connectedCallback(){super.connectedCallback(),this.addEventListener("log-in",e=>{this._auth_header=e.detail.auth_header,this._update()}),this.render()}_fetchToken(){let e={headers:{authorization:this._auth_header},method:"POST"},t=this.firstElementChild;t.addBusyTasks(1),fetch("/_ah/api/swarming/v1/server/token",e).then(r).then(e=>{this._bootstrap_token=e.bootstrap_token,this.render(),t.finishedTask()}).catch(e=>{console.error(e),Object(o.a)(`Error loading token: ${e.body}`,5e3),t.finishedTask()})}_update(){if(!this._auth_header)return;this._server_details={server_version:"<loading>",bot_version:"<loading>"};let e={headers:{authorization:this._auth_header}},t=this.firstElementChild;t.addBusyTasks(2),fetch("/_ah/api/swarming/v1/server/details",e).then(r).then(e=>{this._server_details=e,this.render(),t.finishedTask()}).catch(e=>{403===e.status?(this._server_details={server_version:"User unauthorized - try logging in with a different account",bot_version:""},this.render()):(console.error(e),Object(o.a)(`Unexpected error loading details: ${e.body}`,5e3)),t.finishedTask()}),fetch("/_ah/api/swarming/v1/server/permissions",e).then(r).then(e=>{this._permissions=e,this._permissions.get_bootstrap_token&&this._fetchToken(),this.render(),t.finishedTask()}).catch(e=>{403!==e.status&&(console.error(e),Object(o.a)(`Unexpected error loading permissions: ${e.body}`,5e3)),t.finishedTask()})}});s(9)},,,,,function(e,t){},function(e,t){},function(e,t){},function(e,t){},function(e,t){},,function(e,t){}]);