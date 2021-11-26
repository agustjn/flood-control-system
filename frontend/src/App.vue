<template>
  <div id="app">
     <Navbar/>    
     <View/>
      <footer> 
        <div id="footer" class="container-fluid justify-content-center bg-dark" style="position:absolute; bottom:0">
          
          <span class="text-muted">
            @All rights reserved
          </span>
        </div>
    </footer>
  </div>
</template>

<script>
import Navbar from "./components/Navbar";
import View from "./components/View"

export default {
  name: "app",
  components: {
    Navbar,
    View
  }
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
