var hex_page_layout = `
<div class="jumbotron">
	<p>Current HEX : [[ current_hex ]]</p>
</div>
`

var HexPage =  {
	template: hex_page_layout,
	delimiters:['[[',']]'],
	data: function(){
		return {

		current_hex:""
		}
	},
	methods: {
		getHex: function () {
			console.log("getHex :: ")
			socketio.emit('hex')
		}
	},
	created: function(){
		this.getHex()
		socketio.on('hex', (data) => { this.current_hex = data.hex })
	}
}