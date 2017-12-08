var uuid_page_layout = `
<div class="jumbotron" id="uuid-page" v-cloak>
	<p>Current UUID : [[ current_uuid ]]</p>
</div>
`

var UuidPage =  {
	template: uuid_page_layout,
	delimiters:['[[',']]'],
	data: function(){
		return {

		current_uuid:""
		}
	},
	methods: {
		getUuid: function () {
			console.log("getUuid :: ")
			socketio.emit('uuid').on('uuid', (data) => { this.current_uuid = data.uuid })
		}
	},
	created: function(){
		this.getUuid()
	}
}

// new UuidPage().$mount('#uuid-page')
