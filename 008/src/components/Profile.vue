<template>
    <div id="profile" class="jumbotron">
        <div class="row">
            <div class="col-lg-6">

                <div class="card mb-3">
                    <h3 class="card-header text-primary">{{ profile.name }}</h3>
                    <div class="card-body">
                        <h5 class="card-title">{{ profile.company }}</h5>
                        <h6 class="card-subtitle text-muted">{{ profile.designation }}</h6>
                    </div>
                    <img style="height: 25%; display: block; align: center" 
                    src="https://www.gorillacircuits.com/wp-content/uploads/2016/01/avatar_placeholder.png" alt="Card image">
                    <div class="card-body">
                        <p class="card-text">{{ profile.bio }}</p>
                    </div>
                    <div class="card-body">
                        <a href="#" class="card-link">Facebook</a>
                        <a href="#" class="card-link">Twitter</a>
                        <a href="#" class="card-link">Website</a>
                    </div>
                    <div class="card-footer text-muted">
                        Updated {{ profile.last_updated }} days ago
                    </div>
                </div>
            </div>
        </div>
        <router-view/>
    </div>
</template>

<script>
export default {
  name: 'profile',
  data () {
    return {
      profile: {}
}
},
methods:{
    getProfileData: function(){
        this.$http.get('/profile').then(
            function success(response){
                this.profile = response.profile
            },
            function error(response){
                this.profile = {}
                alert("Failed to fetch profile!")
            })
    }
},

created: function(){
    this.getProfileData()
    console.log(this.profile)
}
}
</script>