<!-- <template lang="pug">
ul.nav(:class='navClasses')
  li
    router-link.dropdown-toggle(to='/', data-toggle='dropdown')
      i.material-icons dashboard
      p.hidden-lg.hidden-md Dashboard
  li.dropdown(:class='{ open : isDropdownOpened }', v-click-outside='closeDropdown')
    a.dropdown-toggle(href='#', data-toggle='dropdown', @click.prevent='openDropdown')
      i.material-icons notifications
      span.notification 5
      p.hidden-lg.hidden-md Notifications
    ul.dropdown-menu
      li
        a(href='#') Mike John responded to your email
      li
        a(href='#') You have 5 new tasks
      li
        a(href='#') You're now friend with Andrew
      li
        a(href='#') Another Notification
      li
        a(href='#') Another One
  li
    a.dropdown-toggle(href='#', data-toggle='dropdown')
      i.material-icons person
      p.hidden-lg.hidden-md Profile    
</template> -->
<template>
  <ul :class="navClasses" class="nav">
    <li>
      <a href="#" data-toggle='dropdown' class="dropdown-toggle" v-on:click="logoutUser()">
        <i class="fa fa-sign-out"></i>
        <p class="hidden-lg hidden-md">Logout</p>
        <div class="ripple-container"></div>
      </a>
    </li>
  </ul>
</template>
<script>
export default {
  name: 'navbar-right',
  props: {
    mobile: Boolean
  },
  data() {
    return {
      isDropdownOpened: false
    }
  },
  computed: {
    navClasses() {
      return this.mobile ? ['nav-mobile-menu'] : ['navbar-nav', 'navbar-right']
    }
  },
  methods: {
    openDropdown() {
      this.isDropdownOpened = !this.isDropdownOpened
    },
    closeDropdown() {
      if (this.isDropdownOpened) {
        this.isDropdownOpened = false
      }
    },
    logoutUser() {
      localStorage.removeItem('user')
      this.$http.get('/logout')
    }
  }
}
</script>

