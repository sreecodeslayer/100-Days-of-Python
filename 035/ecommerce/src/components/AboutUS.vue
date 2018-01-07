<template>
	<!-- START CONTENT -->
	<section id="content">
		<div id="breadcrumbs-wrapper">
			<div class="header-search-wrapper grey lighten-2 hide-on-large-only"></div>
			<div class="container">
				<div class="row">
					<div class="col s10 m6 l6">
						<h5 class="breadcrumbs-title">About Us</h5>
					</div>
				</div>
			</div>
		</div>
		<div class="container">
			<div class="section">
				<p class="caption">Want to know about us! You have come to the right place</p>
				<div class="divider"></div>
				<div id="about_us" class="card">
					<div class="card-image waves-effect waves-block waves-light">
						<img class="activator" src="http://via.placeholder.com/1920x600">
					</div>
					<div class="card-content">
						<h5 class="card-title activator grey-text text-darken-4">Ecommerce - Owner Name</h5>
						<p>
							<i class="material-icons">perm_phone_msg</i>+91-xxxxxxxxxx
						</p>
						<p>
							<i class="material-icons">email</i>contact@example.com
						</p>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>
<script>
	export default {
		name: 'AboutUS',
		data() {

			return {
				
				address: ""
			}
		}
	}
</script>