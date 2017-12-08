
Vue.http.options.root = '/';

var url = location.protocol+"//"+location.host
console.log(url)
var socketio = io(url+'/vue')

// templates
const TimePageComponent = TimePage
const UUIDPageComponent = UuidPage
const HexPageComponent = HexPage

const routes = [
	{
		path: '/',
		component: TimePageComponent,
	},
	{
		path: '/uuid',
		component: UUIDPageComponent,
	},
	{ 
		path: '/hex',
		component: HexPageComponent
	}
]

const router = new VueRouter({ routes })

var App = new Vue({
	router,
	el:'#app',
	delimiters:['[[',']]'],
	data:{
	}
})