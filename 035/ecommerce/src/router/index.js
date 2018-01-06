import Vue from 'vue'
import Router from 'vue-router'
import ECommerceHome from '@/components/ECommerceHome'
import AllCategory from '@/components/AllCategory'
import Electronics from '@/components/Electronics'
import Fashion from '@/components/Fashion'
import HomeKitchen from '@/components/HomeKitchen'
import AboutUS from '@/components/AboutUS'
import ContactUs from '@/components/ContactUs'

Vue.use(Router)

export default new Router({
  routes: [
	{
		path: '/',
		name: 'ECommerceHome',
		component: ECommerceHome
	},
	{
		path: '/all_category',
		name: 'AllCategory',
		component: AllCategory
	},
	{
		path: '/electronics',
		name: 'Electronics',
		component: Electronics
	},
	{
		path: '/fashion',
		name: 'Fashion',
		component: Fashion
	},
	{
		path: '/home_kitchen',
		name: 'HomeKitchen',
		component: HomeKitchen
	},
	{
		path: '/about_us',
		name: 'AboutUS',
		component: AboutUS
	},
	{
		path: '/contact_us',
		name: 'ContactUs',
		component: ContactUs
	}
  ]
})
