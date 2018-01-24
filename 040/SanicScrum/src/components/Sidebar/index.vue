<template lang="pug">
.sidebar(data-color='blue')
  .logo
    a.simple-text(href='http://www.creative-tim.com')
      | Creative Tim
  .sidebar-wrapper
    navbar-search(v-if='open')
    navbar-right(v-if='open', :mobile='true')
    ul.nav
      item(title='Admin Dashboard', v-if="isAdmin" v-cloak icon='dashboard', href='/')
      item(title='Your Dashboard', v-if="!isAdmin" v-cloak icon='dashboard', href='/dashboard')
      item(title='User Profile', icon='person', href='person')
      item(title='Table List', icon='content_paste', href='table')
      item(title='Typography', icon='library_books', href='typography')
      item(title='Icons', icon='bubble_chart', href='icons')
      item(title='Maps', icon='location_on', href='maps')
      item(title='Notifications', icon='notifications', href='notifications')
      li(:class='{ "active-pro" : !open }')
        a(href='upgrade.html')
          i.material-icons unarchive
          p Upgrade to PRO
  .sidebar-background
</template>
<script>
import Item from './item'
import NavbarSearch from '@/components/Navigation/navbar-search'
import NavbarRight from '@/components/Navigation/navbar-right'

export default {
  props: {
    open: Boolean,
  },
  components: {
    Item,
    NavbarSearch,
    NavbarRight
  },
  data() {

    return {

      isAdmin:""
    }
  },
  mounted() {
    this.$authorize.isAuthorized(['admin'], ['view_admin']).then(function() {
      this.isAdmin = true
    }.bind(this)).catch(function() {
      this.isAdmin = false
    }.bind(this))
    console.log(this.isAdmin)
  }
}
</script>

<style lang="scss">
.sidebar-background {
  background-image: url('~images/sidebar-2.jpg')
}
</style>

