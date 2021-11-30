<template>

    <div>
    <h1>Reportes:</h1>
    <ul v-if="reports && reports.length">
      <li v-for="(report, index) in reports" :key="index">
        <p>
            {{report.description}}
        </p>
      </li>/
    </ul>

    <ul v-if="errors && errors.length">
      <li v-for="(error, index) in errors" :key="index">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'


export default {
      data() {
    return {
      reports: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created() {
    axios.get('https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/report/all')
          .then(response => {
          // JSON responses are automatically parsed.
          this.reports = response.data;
          console.log(this.reports)
          })
          .catch(e => {
            this.errors.push(e)
          })
  }
}
</script>
<style>

</style>