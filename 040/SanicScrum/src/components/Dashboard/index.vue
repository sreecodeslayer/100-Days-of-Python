<!-- <template lang="pug">
.content
  .container-fluid
    .row
      .col-lg-3.col-md-6.col-sm-6
        md-stats-widget(faIcon='fa-user', backgroundColor='orange', title='Total Users')
          div(slot='content')
            | 49/50
            small GB
          div(slot='footer')
            i.material-icons.text-danger warning
            router-link(to='Dashboard') Get More Space...
      .col-lg-3.col-md-6.col-sm-6
        md-stats-widget(icon='warning', backgroundColor='green', title='Revenue')
          div(slot='content') $34,245
          div(slot='footer')
            i.material-icons date_range
            |  Last 24 Hours
      .col-lg-3.col-md-6.col-sm-6
        md-stats-widget(icon='info_outline', backgroundColor='red', title='Fixed Issues')
          div(slot='content') 75
          div(slot='footer')
            i.material-icons local_offer
            |  Tracked from Github
      .col-lg-3.col-md-6.col-sm-6
        md-stats-widget(faIcon='fa-twitter', backgroundColor='blue', title='Followers')
          div(slot='content') +245
          div(slot='footer')
            i.material-icons update
            |  Just Updated
    .row
      .col-md-4
        md-chart-widget(type='Line', 
                        backgroundColor='green', 
                        title='Daily Sales', 
                        id='dailySalesChart',
                        :options='dailySalesChart.options',
                        :data='dailySalesChart.data')
          div(slot='subTitle')
            span.text-success
              i.fa.fa-long-arrow-up
              |  55%
            |  increase in today sales.
          div(slot='footer')
            i.material-icons access_time
            |  updated 4 minutes ago
      .col-md-4
        md-chart-widget(type='Bar', 
                        backgroundColor='orange', 
                        title='Email Subscriptions', 
                        id='emailsSubscriptionChart',
                        :options='emailsSubscriptionChart.options',
                        :data='emailsSubscriptionChart.data')
          div(slot='subTitle')
            | Last Campaign Performance
          div(slot='footer')
            i.material-icons access_time
            |  campaign sent 2 days ago
      .col-md-4
        md-chart-widget(type='Line', 
                        backgroundColor='red', 
                        title='Completed Tasks', 
                        id='completedTasksChart',
                        :options='completedTasksChart.options',
                        :data='completedTasksChart.data')
          div(slot='subTitle')
            | Last Campaign Performance
          div(slot='footer')
            i.material-icons access_time
            |  campaign sent 2 days ago
    .row
      .col-lg-6.col-md-12
        md-card.card-nav-tabs(backgroundColor='purple')
          .nav-tabs-navigation(slot='header')
            .nav-tabs-wrapper
              span.nav-tabs-title Tasks:
              md-nav-tabs(:tabs='tabs', @onTabClick='onTabClick')
          md-tab(:tab='tabs')
            md-tab-content(:tab='tabs[0]', slot='content')
              table.table
                tbody
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes', checked='')
                    td Sign contract for "What are conference organizers afraid of?"
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes')
                    td Lines From Great Russian Literature? Or E-mails From My Boss?
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes')
                    td
                      | Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes', checked='')
                    td Create 4 Invisible User Experiences you Never Knew About
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
            md-tab-content(:tab='tabs[1]', slot='content')
              table.table
                tbody
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes', checked='')
                    td
                      | Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes')
                    td Sign contract for "What are conference organizers afraid of?"
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
            md-tab-content(:tab='tabs[2]', slot='content')
              table.table
                tbody
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes')
                    td Lines From Great Russian Literature? Or E-mails From My Boss?
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes', checked='')
                    td
                      | Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
                  tr
                    td
                      .checkbox
                        label
                          input(type='checkbox', name='optionsCheckboxes')
                    td Sign contract for "What are conference organizers afraid of?"
                    td.td-actions.text-right
                      button.btn.btn-primary.btn-simple.btn-xs(type='button', rel='tooltip', title='Edit Task')
                        i.material-icons edit
                      button.btn.btn-danger.btn-simple.btn-xs(type='button', rel='tooltip', title='Remove')
                        i.material-icons close
      .col-lg-6.col-md-12
        md-card(title='Employees Stats', category='New Employees on 15th September, 2016', backgroundColor='orange')
          table.table.table-hover
            thead.text-warning
              th ID
              th Name
              th Salary
              th Country
            tbody
              tr
                td 1
                td Dakota Rice
                td $36,738
                td Niger
              tr
                td 2
                td Minerva Hooper
                td $23,789
                td Curaçao
              tr
                td 3
                td Sage Rodriguez
                td $56,142
                td Netherlands
              tr
                td 4
                td Philip Chaney
                td $38,735
                td Korea, South
</template> -->
<template>

<div class="content">
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-3 col-md-6 col-sm-6">
        <div class="card card-stats">
          <div class="card-header" data-background-color="purple">
            <i class="fa fa-copy"></i>
          </div>
          <div class="card-content">
            <p class="category">Total Users</p>
            <h3 class="title">{{ users.length }}</h3>
          </div>
          <div class="card-footer">
            <div class="stats">
              <i class="material-icons">update</i> Just Updated!
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-10 col-md-12">
        <div class="card">
          <div class="card-header" data-background-color="orange">
            <h4 class="title">Users stats</h4>            
          </div>
          <div class="card-content table-responsive">
            <table class="table table-hover">
              <thead class="text-warning">
                <tr>
                  <th>ID</th>
                  <th>Userame</th>
                  <th>Email</th>
                  <th>Sex</th>
                  <th>Zone</th>
                  <th>Phone</th>
                  <th>Joined on</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in users">
                  <td>{{ user.id }}</td>
                  <td>{{ user.username }}</td>
                  <td>{{ user.email }}</td>
                  <td>{{ user.sex }}</td>
                  <td>{{ user.zone }}</td>
                  <td>{{ user.phone }}</td>
                  <td>{{ user.create_datetime }}</td>
                  <td>
                    <button class="btn btn-danger btn-fab btn-fab-mini" v-on:click="deleteUser(user.email)">
                      <i class="fa fa-trash-o"></i>
                      <div class="ripple-container"></div>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</template>
<script>
import MdNavTabs from '@/core/components/mdTab/nav-tabs'
import MdTabContent from '@/core/components/mdTab/tab-content'

export default {
  name: 'dashboard',
  components: {
    MdTabContent,
    MdNavTabs
  },

  data() {
    const lineSmooth = this.$Chartist.Interpolation.cardinal({ tension: 0 })
    return {
      users: [],
    }
  },

  methods: {
    onTabClick(tab) {
      console.log(`onTabClick: `, tab)
      // console.log(`tabs: `, this.tabs)
    },

    getUsers() {
      this.$http.get('/users').then(function onSuccess(resp) {
        this.users = resp.data.users;
      }, function onError(resp) {
        console.log("Error.... ")
      })
    },
     deleteUser(email) {
      this.$http.delete('/user', {body:{'email':email}}).then(
        function onSuccess(response) {
          this.$router.go(this.$router.currentRoute);
        }, function onError(response) {})
     }
  },
  mounted() {
    this.getUsers();
  }
}
</script>

<style lang="scss" scoped>

</style>
