<template>
  <div class="container-fluid bg-secondary bg-success" style="height:50px">
      <div class="container bg-success">
          <div class="content">
              <ReportsView/>
          </div>
      

      </div>

  </div>
</template>

<script>
import ReportsView from './reports/ReportsView.vue'
export default {
    name:'view',
    components:ReportsView
}
</script>

<style>

</style>