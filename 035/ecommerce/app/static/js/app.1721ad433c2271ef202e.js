webpackJsonp([1],{"2dtk":function(t,s,a){"use strict";var e={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("aside",{staticClass:"nav-expanded nav-lock nav-collapsible",attrs:{id:"left-sidebar-nav"}},[s("div",{staticClass:"brand-sidebar"},[s("h1",{staticClass:"logo-wrapper"},[s("a",{staticClass:"brand-logo darken-2",attrs:{href:"#"}},[s("img",{attrs:{src:"http://www.freepngimg.com/download/cart/8-2-cart-picture.png"}}),this._v(" "),s("span",{staticClass:"logo-text"},[this._v("ECommerce")])]),this._v(" "),s("a",{staticClass:"navbar-toggler",attrs:{href:"#"}},[s("i",{staticClass:"material-icons"},[this._v("radio_button_checked")])])])]),this._v(" "),s("ul",{staticClass:"side-nav fixed leftside-navigation",attrs:{id:"slide-out"}},[s("li",{staticClass:"no-padding bold"},[s("a",{staticClass:"waves-effect waves-cyan",attrs:{href:"#/all_category"}},[s("i",{staticClass:"material-icons"},[this._v("apps")]),this._v(" "),s("span",[this._v("All Categories")])])]),this._v(" "),s("li",{staticClass:"no-padding bold"},[s("a",{staticClass:"waves-effect waves-cyan",attrs:{href:"#/electronics"}},[s("i",{staticClass:"material-icons"},[this._v("developer_board")]),this._v(" "),s("span",[this._v("Electronics")])])]),this._v(" "),s("li",{staticClass:"no-padding bold"},[s("a",{staticClass:"waves-effect waves-cyan",attrs:{href:"#/home_kitchen"}},[s("i",{staticClass:"material-icons"},[this._v("home")]),this._v(" "),s("span",[this._v("Home and Kitchen")])])]),this._v(" "),s("li",{staticClass:"no-padding bold"},[s("a",{staticClass:"waves-effect waves-cyan",attrs:{href:"#/fashion"}},[s("i",{staticClass:"material-icons"},[this._v("wc")]),this._v(" "),s("span",[this._v("Fashion")])])]),this._v(" "),s("li",{staticClass:"no-padding bold"},[s("a",{staticClass:"waves-effect waves-cyan",attrs:{href:"#/contact_us"}},[s("i",{staticClass:"material-icons"},[this._v("contact_mail")]),this._v(" "),s("span",[this._v("Contact US")])])]),this._v(" "),s("li",{staticClass:"no-padding bold"},[s("a",{staticClass:"waves-effect waves-cyan",attrs:{href:"#/about_us"}},[s("i",{staticClass:"material-icons"},[this._v("info_outline")]),this._v(" "),s("span",[this._v("About US")])])])])])}]};s.a=e},MQyw:function(t,s){},NHnr:function(t,s,a){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var e=a("7+uW"),i={name:"app",components:{"app-sidebar":a("lZ5c").default}},n={render:function(){var t=this.$createElement,s=this._self._c||t;return s("div",{attrs:{id:"app"}},[s("app-sidebar"),this._v(" "),s("router-view")],1)},staticRenderFns:[]};var l=a("VU/8")(i,n,!1,function(t){a("MQyw")},null,null).exports,c=a("/ocq"),r=a("w/U7"),o={render:function(){var t=this.$createElement;return(this._self._c||t)("div")},staticRenderFns:[]},d=a("VU/8")({name:"ECommerce",data:function(){return{msg:"Welcome to Your Vue.js App"}}},o,!1,null,null,null).exports,v={name:"AllCategory",data:function(){return{products:[]}},methods:{loadProducts:function(){$http.get("")}}},h={render:function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("section",{attrs:{id:"content"}},[t._m(0),t._v(" "),a("div",{staticClass:"container"},[a("div",{staticClass:"section"},[t.products?a("div",{staticClass:"row",staticStyle:{position:"relative"},attrs:{id:"all_category"}},[a("div",{staticClass:"item-sizer"}),t._v(" "),t._l(t.products,function(s){return a("div",{staticClass:"col sm-12 md-2 lg-4"},[a("div",{staticClass:"card",attrs:{id:"product"}},[t._m(1,!0),t._v(" "),a("ul",{staticClass:"card-action-buttons"}),t._v(" "),a("div",{staticClass:"card-content"},[a("div",{staticClass:"row"},[a("div",{staticClass:"col s12"},[a("p",{staticClass:"card-title grey-text text-darken-4"},[t._v(t._s(s))])])])])])])})],2):t._e(),t._v(" "),t.products.length<=0?a("div",[a("p",[t._v("No products")])]):t._e()])])])},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("div",{attrs:{id:"breadcrumbs-wrapper"}},[s("div",{staticClass:"header-search-wrapper grey lighten-2 hide-on-large-only"}),this._v(" "),s("div",{staticClass:"container"},[s("div",{staticClass:"row"},[s("div",{staticClass:"col s10 m6 l6"},[s("h5",{staticClass:"breadcrumbs-title"},[this._v("Products - All Categories")])])])])])},function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"card-image waves-effect waves-block waves-light"},[s("a",{attrs:{href:"#"}},[s("img",{attrs:{src:"http://via.placeholder.com/300x200"}})])])}]},u=a("VU/8")(v,h,!1,null,null,null).exports,p=a("VU/8")(null,null,!1,null,null,null).exports,_=a("VU/8")(null,null,!1,null,null,null).exports,m=a("VU/8")(null,null,!1,null,null,null).exports,C={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("section",{attrs:{id:"content"}},[s("div",{attrs:{id:"breadcrumbs-wrapper"}},[s("div",{staticClass:"header-search-wrapper grey lighten-2 hide-on-large-only"}),this._v(" "),s("div",{staticClass:"container"},[s("div",{staticClass:"row"},[s("div",{staticClass:"col s10 m6 l6"},[s("h5",{staticClass:"breadcrumbs-title"},[this._v("About Us")])])])])]),this._v(" "),s("div",{staticClass:"container"},[s("div",{staticClass:"section"},[s("p",{staticClass:"caption"},[this._v("Want to know about us! You have come to the right place")]),this._v(" "),s("div",{staticClass:"divider"}),this._v(" "),s("div",{staticClass:"card",attrs:{id:"about_us"}},[s("div",{staticClass:"card-image waves-effect waves-block waves-light"},[s("img",{staticClass:"activator",attrs:{src:"http://via.placeholder.com/1920x600"}})]),this._v(" "),s("div",{staticClass:"card-content"},[s("h5",{staticClass:"card-title activator grey-text text-darken-4"},[this._v("Ecommerce - Owner Name")]),this._v(" "),s("p",[s("i",{staticClass:"material-icons"},[this._v("perm_phone_msg")]),this._v("+91-xxxxxxxxxx\n\t\t\t\t\t")]),this._v(" "),s("p",[s("i",{staticClass:"material-icons"},[this._v("email")]),this._v("contact@example.com\n\t\t\t\t\t")])])])])])])}]},f=a("VU/8")({name:"AboutUS",data:function(){return{address:""}}},C,!1,null,null,null).exports,g=a("VU/8")(null,null,!1,null,null,null).exports;e.a.use(c.a),e.a.use(r.a);var w=new c.a({routes:[{path:"/",name:"ECommerceHome",component:d},{path:"/all_category",name:"AllCategory",component:u},{path:"/electronics",name:"Electronics",component:p},{path:"/fashion",name:"Fashion",component:_},{path:"/home_kitchen",name:"HomeKitchen",component:m},{path:"/about_us",name:"AboutUS",component:f},{path:"/contact_us",name:"ContactUs",component:g}]});e.a.config.productionTip=!1,e.a.options.delimiters=["[[","]]"],new e.a({el:"#app",router:w,template:"<App/>",components:{App:l}})},f3NK:function(t,s){},lZ5c:function(t,s,a){"use strict";var e=a("f3NK"),i=a.n(e),n=a("2dtk"),l=a("VU/8")(i.a,n.a,!1,null,null,null);s.default=l.exports}},["NHnr"]);
//# sourceMappingURL=app.1721ad433c2271ef202e.js.map