<!-- <template lang="pug">
.content
  .row
    .col-md-8
      .card
        .card-header(data-background-color='purple')
          h4.title Edit Profile
          p.category Complete your profile
        .card-content
          form
            .row
              .col-md-5
                md-fg-input(label='Company (disbaled)', :disabled='true', :labelFloating='true', v-model='user.company')
              .col-md-3
                md-fg-input(label='Username', :labelFloating='true', v-model='user.username')
              .col-md-4
                md-fg-input(type='email', label='Email address', :labelFloating='true', v-model='user.email')
            .row
              .col-md-6
                md-fg-input(label='First Name', :labelFloating='true', v-model='user.firstName')
              .col-md-6
                md-fg-input(label='Last Name', :labelFloating='true', v-model='user.lastName')
            .row
              .col-md-12
                md-fg-input(label='Adress', :labelFloating='true', v-model='user.address')
            .row
              .col-md-4
                md-fg-input(label='City', :labelFloating='true', v-model='user.city')
              .col-md-4
                md-fg-input(label='Country', :labelFloating='true', v-model='user.country')
              .col-md-4
                md-fg-input(label='Postal Code', :labelFloating='true', v-model='user.postalCode')
            .row
              .col-md-12
                md-fg-input(type='textarea', label='About Me', :labelFloating='true', :rows='5', v-model='user.aboutMe')
            md-button.btn.btn-primary.pull-right(@click.prevent='updateProfile') Update Profile
            .clearfix
    .col-md-4
      .card.card-profile
        .card-avatar
          a(href='#pablo')
            img.img(src='~images/faces/marc.jpg')
        .content
          h6.category.text-gray CEO / Co-Founder
          h4.card-title {{user.name}}
          p.card-content
            | {{user.aboutMe}}
          md-button.btn.btn-primary.btn-round(href='#/person') Follow
</template> -->
<template>
  <div class="content">
    <div class="row">
      <div class="col-md-8 col-sm-12 col-lg-9" v-if="showAdminAddUser">
        <div class="card">
          <div class="card-header" data-background-color="blue">
            <h4 class="title">Add Members</h4>
            <p class="category">You can add new members to your team here!</p>
          </div>


          <div class="card-content">
            <form v-on:submit.prevent = "addNewUser()" name="addNewUserForm" novalidate>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group label-floating is-empty">
                    <md-fg-input
                      type="text"
                      name="username" required
                      v-model="newUser.username"
                      label="Username"
                      :labelFloating=true></md-fg-input>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group label-floating is-empty">
                    <md-fg-input
                      type="email"
                      name="email" required
                      v-model="newUser.email"
                      label="Email"
                      :labelFloating=true></md-fg-input>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group label-floating is-empty">
                    <md-fg-input
                      type="password"
                      name="password" required
                      v-model="newUser.password"
                      label="Password"
                      :labelFloating=true></md-fg-input>
                  </div>
                </div>
                <div class="col-md-6">
                    <select
                      class="selectpicker"
                      required
                      v-model="newUser.sex"
                      data-style="btn btn-sm btn-round"
                      title="Choose Gender"
                      data-size="7">

                      <option disabled> Choose gender</option>
                      <option value="male">Male </option>
                      <option value="female">Female</option>
                    </select>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group label-floating is-empty">
                    <md-fg-input
                      type="phone"
                      name="phone" required
                      v-model="newUser.phone"
                      label="Phone"
                      :labelFloating=true></md-fg-input>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group label-floating is-empty">
                    <md-fg-input
                      type="zone"
                      name="zone" required
                      v-model="newUser.zone"
                      label="Zone"
                      :labelFloating=true></md-fg-input>
                  </div>
                </div>
              </div>
              <div class="row" v-show="newUser.error">
                <div class="col-md-12">
                  <div class="alert alert-danger">
                    <b>Error: </b><p v-model="newUser.error">{{newUser.error}}</p>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-12">
                  <div class="btn-group">
                    <button type="submit" class="btn btn-success">Add</button>
                  </div>
                </div>
              </div>
            </form>
            
          </div>
        </div>
      </div>
      <div :class="profileClasses">
        <div class="card card-profile">
          <div class="card-avatar">
            <a href="#"><img src="~images/faces/marc.jpg"></a>
          </div>
          <div class="content">
            <h6 class="category">{{ user.username }}</h6>
            <h4 class="title">{{ user.email }}</h4>
            <p class="card-content">Phone: {{user.phone}} | 
              Gender: {{user.sex}}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      showAdminAddUser: false,
      profileClasses: ["col-md-12","col-sm-12","col-lg-12"],
      user: {},
      newUser: {
        error:''
      }
    }
  },
  methods: {
    getUserFromLocalStorage() {
      this.user = JSON.parse(localStorage.getItem('user'))
      this.$authorize.isAuthorized(['admin'], ['view_admin']).then(function() {
        this.showAdminAddUser = true
        this.profileClasses = ["col-md-4","col-sm-12","col-lg-3"]
      }.bind(this)).catch(function() {
        this.showAdminAddUser = false
        this.profileClasses = ["col-md-12","col-sm-12","col-lg-12"]
      }.bind(this))

    },
    addNewUser() {
      console.log(this.newUser)
      this.$http.post('/signup', this.newUser).then(function onSuccess(response) {
        console.log(response)
        
        swal(
          'Member Added',
          "Added new user: " + this.newUser.username,
          'success',
          {
            button:{text:"Ok!",value:true,className:"btn btn-success"}
          }
        ).catch(swal.noop);

      }, function onError(response) {
        console.log(response)
        this.newUser.error = response.data.message;
      })
    }
  },
  created() {
    this.getUserFromLocalStorage();
  }
}
</script>