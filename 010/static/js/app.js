Vue.options.root = '/'

app = new Vue({
	el:"#app",
	delimiters:['[[', ']]'],
	data: function(){
		return {
			starts_with : '',
			means : '',
			gender : '',
			names : []
		}
	},
	methods: {
		getNames: function(){

			payload = {'starts_with':this.starts_with, 'gender':this.gender, 'means':this.means}
			console.log(payload)
			this.$http.get('/name', {params: payload}).then(
				function(res) {
					this.names = res.data.result;
					console.log(this.names)
				}, function(res) {
					console.log("Err: ", res.data)

				})
		}
	}
})