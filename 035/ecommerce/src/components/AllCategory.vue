<template>
	<!-- START CONTENT -->
	<section id="content">
		<div id="breadcrumbs-wrapper">
			<div class="header-search-wrapper grey lighten-2 hide-on-large-only"></div>
			<div class="container">
				<div class="row">
					<div class="col s10 m6 l6">
						<h5 class="breadcrumbs-title">Products - All Categories</h5>
					</div>
				</div>
			</div>
		</div>
		<div class="container">
			<div class="section">
				<div id="all_category" class="row" style="position: relative;" v-if="products">
					<div class="item-sizer"></div>
					<div class="col sm-12 md-2 lg-4" v-for="product in products">
						<div id="product" class="card">
							<div class="card-image waves-effect waves-block waves-light">
								<a href="#">
									<img src="http://via.placeholder.com/300x200"/>
								</a>
							</div>
							<ul class="card-action-buttons"></ul>
							<div class="card-content">
								<div class="row">
									<div class="col s12">
										<p class="card-title grey-text text-darken-4">{{ product }}</p>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div v-if="products.length <= 0">
					<p>No products</p>
				</div>
			</div>
		</div>
	</section>
</template>
<script>
	export default {
		name: 'AllCategory',
		// delimiters: ["[[","]]"],
		data() {
			return {
				products:[]
			}
		},
		methods: {
			loadProducts: function() {
				$http.get("")
			}
		}
	}
</script>
