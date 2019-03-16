<template>
  <button @click="submitForm">Foo</button>
</template>

<script>
import store from '../store'
export default {
  data: function () {
    return {
      isMobile: /Mobile/.test(navigator.userAgent)
    }
  },
  methods: {
    changelanguage: function (lang) {
      store.commit('UPDATE_LANG', lang)
    }
  },
  computed: {
    language: function () {
      return store.state.lang
    }
  },
    submitForm: function (e) {
      this.$validator.validateAll().then(response => {
        if (response && this.api_response.allow_send) {
          this.clear_only_solution()
          let data = {
            numbers: this.inputs.numbers,
            target: this.inputs.target,
            id: this.me
          }
          this.$http.post('/numbers_async', data).then((response) => {
            this.api_response.response = response.data
            this.api_response.allow_send = false
            if (this.numbers_solution.solution.length === 0 && !this.me) {
              this.manual_fetching_data() // only call if we don't have one solution yet
            }
          }).catch((error) => {
            console.log(error)
            this.api_response.has_errors = true
          })
        }
      })
    }
}
</script>
