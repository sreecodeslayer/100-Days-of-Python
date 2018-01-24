import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Dash from '@/components/Dash'
import UserProfile from '@/components/UserProfile'
import TableList from '@/components/TableList'
import Typography from '@/components/Typography'
import Icons from '@/components/Icons'
import Maps from '@/components/Maps'
import Notifications from '@/components/Notifications'

// GeneralViews
import NotFound from '@/components/GeneralViews/NotFound.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/dashboard',
      meta: {
        permissions:{
          roles:['user','admin'],
          permissions:['view_user','view_admin']
        }
      },
      name: 'CommonDash',
      component: Dash
    },
    {
      path: '/',
      meta: {
        permissions:{
          roles:['admin'],
          permissions:['view_admin'],
          redirectTo:'/dashboard'
        }
      },
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/person',
      meta: {
        permissions:{
          roles:['admin','user'],
          permissions:['view_admin','view_user'],
          redirectTo:'/'
        }
      },
      name: 'Person',
      component: UserProfile
    },
    {
      path: '/table',
      name: 'TableList',
      component: TableList
    },
    {
      path: '/typography',
      name: 'Typography',
      component: Typography
    },
    {
      path: '/icons',
      name: 'Icons',
      component: Icons
    },
    {
      path: '/maps',
      name: 'Maps',
      component: Maps
    },
    {
      path: '/notifications',
      name: 'Notifications',
      component: Notifications
    },
    { path: '*', component: NotFound }
  ],
  linkActiveClass: 'active'
})
