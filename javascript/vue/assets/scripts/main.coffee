Vue = require 'vue'


vm = new Vue
  el: '#sample'
  data:
    firstName: 'H'
    lastName: 'Moka'
  methods:
    fullName: -> "#{this.firstName} #{this.lastName}"
