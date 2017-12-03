// Vue.use(VueSocketio, 'http://127.0.0.1:8000')
var app = new Vue({
	el: '#vue-app',
	delimiters:['[[',']]'],
	data: {
		greeting: 'Welcome to Vue.js Sanic app!',
		album:[],
		toggleAlbum:"Show",
		groceryList: [
			{ id: 0, text: 'Vegetables' },
			{ id: 1, text: 'Cheese' },
			{ id: 2, text: 'Whatever else humans are supposed to eat' }
		]
	},
	sockets:{
		connect: function(){
			console.log("connect!!")
		}
	},
	methods: {
		sendSocket: function() {
			this.socket = new WebSocket('ws://127.0.0.1:8000/getRandomAlbum')

			this.socket.onmessage = response => {
				this.album = JSON.parse(response.data).album
				console.log(this.album)
			}
		},

		showAlbum: function() {
			if (this.toggleAlbum == "Show")
				this.toggleAlbum = "Hide"
			else
				this.toggleAlbum =  "Show"
		}
	},
	created: function () {
		this.sendSocket()
		
	}
})
