// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueResource from 'vue-resource'
import VueSweetAlert from 'vue-sweetalert'
import VueAuthenticate from 'vue-authenticate'
import VueAuthorize from 'vue-authorize'

import router from './router'


// Libraries
import 'bootstrap/dist/css/bootstrap.css'
import './assets/sass/material-dashboard.scss'
import 'es6-promise/auto'
import Chartist from 'chartist'
import CoreComponents from '@/core/components'
import NotificationPlugin from '@/core/components/mdNotifications/install'
import vClickOutside from 'v-click-outside'

Vue.config.productionTip = false

// global library setup
Object.defineProperty(Vue.prototype, '$Chartist', {
  get() {
    return this.$root.Chartist
  }
})

// Use Core Components
Vue.use(CoreComponents)
Vue.use(NotificationPlugin)
Vue.use(vClickOutside)
Vue.use(VueResource)
Vue.use(VueSweetAlert)
Vue.use(VueAuthenticate,
  {
    baseUrl: 'http://localhost:8080',
    bindRequestInterceptor: function () {},
    bindResponseInterceptor: function () {}
})
 
Vue.use(VueAuthorize, {
  roles: {
    admin: {
      handler: function() {
        var user = JSON.parse(localStorage.getItem('user'))

        console.log("admin role check: ",user.role)

        if (user.role === "admin") {
          // console.log("enter here first for role ")
          return true
        }
        else {
          return false
        }
      },
      permissions: ['view_admin']
    },
    user: {
      handler: function() {
        var user = JSON.parse(localStorage.getItem('user'))

        console.log("user role check: ",user.role)

        if (user.role === "user" || user.role === "admin") {
          // console.log("enter here first for role ")
          return true
        }
        else {
          return false
        }
      },
      permissions: ['view_user']
    }
  },
  permissions: {
    view_admin: function() {
      var user = JSON.parse(localStorage.getItem('user'))

      if (user.role == "admin") {
        // console.log("then here for permissions")
        return true
      }

      return false
    },

    view_user: function() {
      var user = JSON.parse(localStorage.getItem('user'))

      if (user.role == "user") {
        // console.log("then here for permissions")
        return true
      }

      return false
    }
  }
})


router.beforeEach(function (to, from, next) {
  if (to.meta && to.meta.permissions) {
    let roles = to.meta.permissions.roles
    let permissions = to.meta.permissions.permissions

    router.app.$authorize.isAuthorized(roles, permissions).then(function () {
      next()
    }).catch(function () {
      next(to.meta.permissions.redirectTo || '/unathorized')
    })
  }
  else {
    next()
  }
})


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App },
  data: {
    Chartist
  }
})
