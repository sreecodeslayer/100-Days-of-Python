var time_page_layout = `
<div class="jumbotron" id="time-page">
	<p>Current Time : [[ current_time ]]</p>
</div>
`
var TimePage = {
	template: time_page_layout,
	delimiters:['[[',']]'],
	data: function(){
		return{
			current_time: '',
		}
	},
	methods:{
	},
	created: function(){
		socketio.on('time', (data) => {
			this.current_time = data.time
		})
	}
}