<template>
	<div id="app">
		<app-sidebar></app-sidebar>
		<router-view/>
	</div>
</template>

<script>
import SideBar from './components/Sidebar.vue'

export default {
	name: 'app',
	components:{
		'app-sidebar':SideBar
	}
}
</script>

<style>
/*#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}*/
</style>