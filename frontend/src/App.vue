<template>
  <Navbar/>
  <View/>
  <ReportsView/>
  <!-- <Footer/> -->
</template>

<script>
import Navbar from "./components/Navbar";
import View from "./components/View"
import ReportsView from "./components/reports/ReportsView.vue"

export default {
  name: "App",
  components: {
    Navbar,
    View,
    ReportsView
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50
}
</style>
